"""Artifact and report writing for the refactored pipeline."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

from experiment_recorder import ErrorClassifier, CodeChangeAnalyzer

from .config import ExperimentConfig, RuntimeConfig
from .state import PipelineState, ValidationOutcome


class RefactoredReportWriter:
    def __init__(self, config: RuntimeConfig):
        self.config = config

    def ensure_dirs(self, state: PipelineState) -> Path:
        report_dir = state.report_dir(self.config.result_root)
        report_dir.mkdir(parents=True, exist_ok=True)
        return report_dir

    def write_artifact(self, state: PipelineState, name: str, content: str) -> Path:
        report_dir = self.ensure_dirs(state)
        path = report_dir / name
        path.write_text(content or "", encoding="utf-8", errors="replace")
        state.artifacts[name] = str(path)
        return path

    def write_json_artifact(self, state: PipelineState, name: str, payload: Any) -> Path:
        return self.write_artifact(state, name, json.dumps(payload, indent=2, ensure_ascii=False))

    def write_final_report(self, state: PipelineState, exp: ExperimentConfig, runtime_seconds: float) -> Dict[str, Any]:
        report_dir = self.ensure_dirs(state)
        initial = state.fused_aadl or state.final_aadl
        final = state.final_aadl or initial
        validation = state.validation_final or state.validation_initial or ValidationOutcome()
        all_errors = validation.aadl_errors + validation.agree_errors
        generation_errors = []
        if not state.generation_valid:
            generation_errors.append(state.generation_failure_reason or "No valid AGREE contract was generated.")
        pipeline_success = validation.success and state.generation_valid
        payload: Dict[str, Any] = {
            "case_num": state.case_num,
            "case_letter": state.case_letter,
            "setting": state.setting,
            "setting_name": exp.name,
            "success": pipeline_success,
            "validator_success": validation.success,
            "generation_valid": state.generation_valid,
            "generation_failure_reason": state.generation_failure_reason,
            "repair_count": len(state.repair_history),
            "runtime": runtime_seconds,
            "changed_lines": CodeChangeAnalyzer.count_changed_lines(initial or "", final or ""),
            "initial_error_count": len((state.validation_initial or validation).aadl_errors + (state.validation_initial or validation).agree_errors),
            "final_error_count": len(all_errors) + len(generation_errors),
            "error_classification": ErrorClassifier.classify_errors(all_errors + generation_errors, final).to_dict(),
            "token_stats": state.token_stats.to_dict(),
            "modules": {
                "rag": exp.rag,
                "repair": exp.repair,
                "requirement_analyst": exp.requirement_analyst,
                "model_analyst": exp.model_analyst,
                "agree_generator": exp.agree_generator,
                "model_fusion": exp.model_fusion,
            },
            "validation_summary": {
                "aadl_inspector_executed": validation.aadl_executed,
                "agree_validator_executed": validation.agree_executed,
                "aadl_errors_count": len(validation.aadl_errors),
                "agree_errors_count": len(validation.agree_errors),
                "generation_errors_count": len(generation_errors),
                "warnings_count": len(validation.warnings),
                "aadl_report_path": validation.aadl_report_path,
                "agree_report_path": validation.agree_report_path,
            },
            "rag_bundles": state.rag_bundles,
            "recovery_actions": state.recovery_actions,
            "artifacts": state.artifacts,
            "repair_history": state.repair_history,
        }
        (report_dir / f"Case{state.case_num}_report.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        self._write_markdown(report_dir / f"Case{state.case_num}_report.md", payload, validation)
        return payload

    def _write_markdown(self, path: Path, payload: Dict[str, Any], validation: ValidationOutcome) -> None:
        case_label = f"Case{payload['case_num']}_{payload['case_letter']}" if payload.get("case_letter") else f"Case{payload['case_num']}"
        lines: List[str] = [
            f"# {case_label} Refactored Experiment Report",
            "",
            "## Summary",
            "",
            f"- Setting: {payload['setting']} ({payload['setting_name']})",
            f"- Final status: {'Success' if payload['success'] else 'Fail'}",
            f"- Repair rounds: {payload['repair_count']}",
            f"- Runtime seconds: {payload['runtime']:.2f}",
            f"- Initial validation errors: {payload['initial_error_count']}",
            f"- Final validation errors: {payload['final_error_count']}",
            "",
            "## Validation",
            "",
            f"- AADL Inspector executed: {payload['validation_summary']['aadl_inspector_executed']}",
            f"- AGREE validator executed: {payload['validation_summary']['agree_validator_executed']}",
            f"- AADL errors: {payload['validation_summary']['aadl_errors_count']}",
            f"- AGREE errors: {payload['validation_summary']['agree_errors_count']}",
            f"- Warnings: {payload['validation_summary']['warnings_count']}",
            "",
            "## Modules",
            "",
        ]
        for key, value in payload["modules"].items():
            lines.append(f"- {key}: {value}")
        lines.extend(["", "## Token Usage", ""])
        for key, value in payload["token_stats"].items():
            lines.append(f"- {key}: {value}")
        if payload.get("recovery_actions"):
            lines.extend(["", "## Output Recovery", ""])
            for index, item in enumerate(payload["recovery_actions"], 1):
                lines.append(f"{index}. [{item.get('stage')}] {item.get('action')} - {item.get('detail', '')}")
        generation_errors = []
        if not payload.get("generation_valid", True):
            generation_errors.append(payload.get("generation_failure_reason") or "No valid AGREE contract was generated.")
        if generation_errors:
            lines.extend(["", "## Generation Failure", ""])
            for index, error in enumerate(generation_errors, 1):
                lines.append(f"{index}. {error}")
        if validation.aadl_errors or validation.agree_errors:
            lines.extend(["", "## Final Diagnostics", ""])
            for index, error in enumerate(validation.aadl_errors + validation.agree_errors, 1):
                lines.append(f"{index}. {error}")
        path.write_text("\n".join(lines) + "\n", encoding="utf-8", errors="replace")
