"""
Experiment recording utilities for Agree-Autogen.

The recorder persists first-pass generated code, repaired code, validator
diagnostics, repair statistics, and a compact Markdown report for each case.
"""

import difflib
import json
import os
import re
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ErrorClassification:
    """Counts for the T1-T5 error taxonomy."""

    T1: int = 0  # Lexical and basic syntax
    T2: int = 0  # External references and context
    T3: int = 0  # Architecture and component-structure violations
    T4: int = 0  # Declarations and identifier conflicts
    T5: int = 0  # Type and numeric-logic issues

    def to_dict(self) -> Dict[str, int]:
        return {"T1": self.T1, "T2": self.T2, "T3": self.T3, "T4": self.T4, "T5": self.T5}

    def has_any_error(self) -> bool:
        return any(value > 0 for value in self.to_dict().values())


class ErrorClassifier:
    """Rule-based fallback classifier for validation diagnostics."""

    @classmethod
    def classify_error(cls, error_text: str) -> List[str]:
        text = error_text.lower()
        categories: List[str] = []
        if any(key in text for key in ["syntax", "missing eof", "mismatched", "extraneous", "token", "parse"]):
            categories.append("T1")
        if any(key in text for key in ["couldn't resolve", "not found", "with clause", "reference", "package", "property set"]):
            categories.append("T2")
        if any(key in text for key in ["subcomponent", "connection", "feature", "implementation", "classifier"]):
            categories.append("T3")
        if any(key in text for key in ["duplicate", "already defined", "identifier", "declaration", "name"]):
            categories.append("T4")
        if any(key in text for key in ["type", "int", "real", "bool", "numeric", "left and right"]):
            categories.append("T5")
        return categories or ["T1"]

    @classmethod
    def classify_errors(cls, errors: List[str], aadl_code: Optional[str] = None) -> ErrorClassification:
        result = ErrorClassification()
        for error in errors:
            for category in cls.classify_error(error):
                setattr(result, category, getattr(result, category) + 1)
        return result


class CodeChangeAnalyzer:
    """Analyze line-level changes between first-pass and final code."""

    @classmethod
    def count_changed_lines(cls, original_code: str, fixed_code: str) -> int:
        if not original_code and not fixed_code:
            return 0
        original_lines = original_code.splitlines()
        fixed_lines = fixed_code.splitlines()
        matcher = difflib.SequenceMatcher(None, original_lines, fixed_lines)
        changed = 0
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag == "equal":
                continue
            changed += max(i2 - i1, j2 - j1)
        return changed

    @classmethod
    def get_line_changes(cls, original_code: str, fixed_code: str) -> List[Dict[str, Any]]:
        original_lines = original_code.splitlines()
        fixed_lines = fixed_code.splitlines()
        matcher = difflib.SequenceMatcher(None, original_lines, fixed_lines)
        changes: List[Dict[str, Any]] = []
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag == "equal":
                continue
            changes.append(
                {
                    "type": tag,
                    "original_start": i1 + 1,
                    "original_end": i2,
                    "fixed_start": j1 + 1,
                    "fixed_end": j2,
                    "original_lines": original_lines[i1:i2],
                    "fixed_lines": fixed_lines[j1:j2],
                }
            )
        return changes


class ExperimentRecorder:
    """Manage per-case experiment artifacts and reports."""

    def __init__(self, base_dir: str = None):
        if base_dir is None:
            base_dir = os.environ.get("AGREE_DATA_ROOT", os.path.abspath("data"))
        self.base_dir = base_dir
        self.result_dir = os.environ.get("AGREE_RESULT_ROOT", os.path.join(base_dir, "Result"))

    def get_case_dir(self, case_num: str, case_letter: str) -> str:
        return os.path.join(self.result_dir, f"Case{case_num}_{case_letter}")

    def get_report_dir(self, case_num: str, case_letter: str) -> str:
        return os.path.join(self.get_case_dir(case_num, case_letter), "Report")

    def ensure_report_dir(self, case_num: str, case_letter: str) -> str:
        report_dir = self.get_report_dir(case_num, case_letter)
        os.makedirs(report_dir, exist_ok=True)
        return report_dir

    def _stage_display_name(self, stage: str) -> str:
        mapping = {
            "aadl_model_analysis": "AADL model analysis",
            "requirement_analysis": "Requirement analysis",
            "agree_generation": "AGREE generation",
            "pipeline_exception": "Pipeline exception",
            "aadl_merge": "AADL merge",
            "validation": "Validation",
        }
        return mapping.get(stage, stage.replace("_", " ").title())

    def _extract_error_items(self, report_dir: str, limit: int = 8) -> List[str]:
        candidates = [
            os.path.join(report_dir, "initial_errors.json"),
            os.path.join(report_dir, "Case_errors.json"),
        ]
        for path in candidates:
            if not os.path.exists(path):
                continue
            try:
                with open(path, "r", encoding="utf-8") as file:
                    data = json.load(file)
                items = data.get("aadl_errors", []) + data.get("agree_errors", [])
                return [str(item) for item in items[:limit]]
            except Exception:
                continue
        return []

    def _infer_failure_summary(self, stage: str, error_message: str, report_dir: str) -> Dict[str, Any]:
        lowered = (error_message or "").lower()
        direct_cause = error_message or "Unknown failure"
        likely_category = "pipeline"
        interpretation = "The run stopped before a successful final validation report could be produced."

        if "report file" in lowered and "not found" in lowered:
            likely_category = "validator_output_missing"
            interpretation = "The external validator did not produce the expected report artifact."
        elif "couldn't resolve" in lowered or "not found" in lowered or "with clause" in lowered:
            likely_category = "dependency_or_reference"
            interpretation = "The generated model likely references a missing package, property set, or model unit."
        elif "empty response" in lowered:
            likely_category = "llm_empty_response"
            interpretation = "The LLM provider returned an empty response, which the pipeline rejected."
        elif "timeout" in lowered:
            likely_category = "external_timeout"
            interpretation = "An external validator or model call timed out."

        examples = self._extract_error_items(report_dir)
        return {
            "stage": stage,
            "stage_display": self._stage_display_name(stage),
            "direct_cause": direct_cause,
            "likely_category": likely_category,
            "interpretation": interpretation,
            "examples": examples,
        }

    def save_initial_code(self, case_num: str, case_letter: str, code: str) -> str:
        report_dir = self.ensure_report_dir(case_num, case_letter)
        path = os.path.join(report_dir, f"Case{case_num}_initial.txt")
        with open(path, "w", encoding="utf-8") as file:
            file.write(code or "")
        first_path = os.path.join(report_dir, f"Case{case_num}_first.txt")
        with open(first_path, "w", encoding="utf-8") as file:
            file.write(code or "")
        return path

    def save_fixed_code(self, case_num: str, case_letter: str, code: str) -> str:
        report_dir = self.ensure_report_dir(case_num, case_letter)
        path = os.path.join(report_dir, f"Case{case_num}_fixed.txt")
        with open(path, "w", encoding="utf-8") as file:
            file.write(code or "")
        return path

    def save_errors(
        self,
        case_num: str,
        case_letter: str,
        aadl_errors: List[str],
        agree_errors: List[str],
    ) -> str:
        report_dir = self.ensure_report_dir(case_num, case_letter)
        path = os.path.join(report_dir, "initial_errors.json")
        payload = {
            "aadl_errors": aadl_errors or [],
            "agree_errors": agree_errors or [],
            "total_errors": len(aadl_errors or []) + len(agree_errors or []),
        }
        with open(path, "w", encoding="utf-8") as file:
            json.dump(payload, file, indent=2, ensure_ascii=True)
        return path

    def generate_report(
        self,
        case_num: str,
        case_letter: str,
        initial_code: str,
        fixed_code: str,
        aadl_errors: List[str],
        agree_errors: List[str],
        token_stats: Dict[str, Any],
        runtime: float,
        success: bool,
        repair_count: int = 0,
    ) -> Dict[str, Any]:
        report_dir = self.ensure_report_dir(case_num, case_letter)
        all_errors = (aadl_errors or []) + (agree_errors or [])
        classification = ErrorClassifier.classify_errors(all_errors, initial_code)
        changed_lines = CodeChangeAnalyzer.count_changed_lines(initial_code or "", fixed_code or "")

        report_data = {
            "case_num": case_num,
            "case_letter": case_letter,
            "success": success,
            "repair_count": repair_count,
            "token_stats": token_stats or {},
            "runtime": runtime,
            "changed_lines": changed_lines,
            "error_classification": classification.to_dict(),
            "initial_error_count": len(all_errors),
        }

        json_path = os.path.join(report_dir, f"Case{case_num}_report.json")
        with open(json_path, "w", encoding="utf-8") as file:
            json.dump(report_data, file, indent=2, ensure_ascii=True)

        md_path = os.path.join(report_dir, f"Case{case_num}_report.md")
        with open(md_path, "w", encoding="utf-8") as file:
            file.write(f"# Case{case_num}_{case_letter} Experiment Report\n\n")
            file.write("## Summary\n\n")
            file.write(f"- Final status: {'Success' if success else 'Fail'}\n")
            file.write(f"- Repair rounds: {repair_count}\n")
            file.write(f"- Runtime seconds: {runtime:.2f}\n")
            file.write(f"- Changed lines: {changed_lines}\n")
            file.write(f"- Initial validation errors: {len(all_errors)}\n\n")
            file.write("## Token Usage\n\n")
            file.write(f"- Prompt tokens: {(token_stats or {}).get('prompt_tokens', 0)}\n")
            file.write(f"- Completion tokens: {(token_stats or {}).get('completion_tokens', 0)}\n")
            file.write(f"- Total tokens: {(token_stats or {}).get('total_tokens', 0)}\n\n")
            file.write("## Error Classification\n\n")
            for key, value in classification.to_dict().items():
                file.write(f"- {key}: {value}\n")
            if all_errors:
                file.write("\n## Initial Diagnostics\n\n")
                for index, error in enumerate(all_errors, 1):
                    file.write(f"{index}. {error}\n")

        report_data["report_path"] = md_path
        return report_data

    def generate_failure_report(
        self,
        case_num: str,
        case_letter: str,
        stage: str,
        error_message: str,
        token_stats: Dict[str, Any],
        runtime: float,
        initial_code: str = "",
        fixed_code: str = "",
    ) -> Dict[str, Any]:
        report_dir = self.ensure_report_dir(case_num, case_letter)
        summary = self._infer_failure_summary(stage, error_message, report_dir)
        changed_lines = CodeChangeAnalyzer.count_changed_lines(initial_code or "", fixed_code or "")
        report_data = {
            "case_num": case_num,
            "case_letter": case_letter,
            "success": False,
            "stage": stage,
            "error": error_message,
            "failure_summary": summary,
            "token_stats": token_stats or {},
            "runtime": runtime,
            "changed_lines": changed_lines,
        }

        json_path = os.path.join(report_dir, f"Case{case_num}_report.json")
        with open(json_path, "w", encoding="utf-8") as file:
            json.dump(report_data, file, indent=2, ensure_ascii=True)

        md_path = os.path.join(report_dir, f"Case{case_num}_report.md")
        with open(md_path, "w", encoding="utf-8") as file:
            file.write(f"# Case{case_num}_{case_letter} Failure Report\n\n")
            file.write("## Failure Summary\n\n")
            file.write(f"- Stage: {summary['stage_display']}\n")
            file.write(f"- Category: {summary['likely_category']}\n")
            file.write(f"- Runtime seconds: {runtime:.2f}\n")
            file.write(f"- Changed lines: {changed_lines}\n")
            file.write(f"- Direct cause: {summary['direct_cause']}\n")
            file.write(f"- Interpretation: {summary['interpretation']}\n\n")
            if summary["examples"]:
                file.write("## Diagnostic Examples\n\n")
                for item in summary["examples"]:
                    file.write(f"- {item}\n")

        report_data["report_path"] = md_path
        return report_data


def create_recorder() -> ExperimentRecorder:
    return ExperimentRecorder()
