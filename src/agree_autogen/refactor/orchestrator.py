"""Refactored AGREE-AutoGen orchestration."""

from __future__ import annotations

import time
import re
from pathlib import Path
from typing import Any, Dict, List

from .agents import (
    AgentRuntime,
    AgreeGeneratorAgent,
    BareDirectAgent,
    ModelAnalystAgent,
    ModelFusionAgent,
    RequirementAnalystAgent,
    ValidationRepairAgent,
)
from .config import EXPERIMENTS, RuntimeConfig
from .reporting import RefactoredReportWriter
from .state import DISABLED, PipelineState
from .validation import ValidationRunner
from experiment_recorder import ErrorClassifier


class RefactoredAgreeAutogenPipeline:
    """New experiment-controlled pipeline for E1-E7."""

    def __init__(self, config: RuntimeConfig):
        self.config = config
        self.runtime = AgentRuntime(config)
        self.reporter = RefactoredReportWriter(config)
        self.validator = ValidationRunner(config)
        self.model_analyst = ModelAnalystAgent(self.runtime)
        self.requirement_analyst = RequirementAnalystAgent(self.runtime)
        self.agree_generator = AgreeGeneratorAgent(self.runtime)
        self.model_fusion = ModelFusionAgent(self.runtime)
        self.validation_repair = ValidationRepairAgent(self.runtime)
        self.bare_direct = BareDirectAgent(self.runtime)

    def run_case(
        self,
        setting: str,
        case_num: str,
        case_letter: str,
        aadl_model: str,
        requirement_text: str,
        target_component: str,
        references: List[Dict[str, str]],
    ) -> Dict[str, Any]:
        start = time.time()
        exp = EXPERIMENTS[setting.upper()]
        state = PipelineState(
            case_num=case_num,
            case_letter=case_letter,
            setting=setting.upper(),
            target_component=target_component,
            raw_requirement=requirement_text,
            raw_aadl=aadl_model,
            references=references,
        )
        report_dir = self.reporter.ensure_dirs(state)
        self._stage_references(state)
        self.reporter.write_artifact(state, f"Case{case_num}_input.aadl", aadl_model)
        self.reporter.write_artifact(state, f"Case{case_num}_requirement.txt", requirement_text)

        try:
            if setting.upper() == "E1":
                state.final_aadl = self.bare_direct.run(state)
                state.fused_aadl = state.final_aadl
                artifact = self.reporter.write_artifact(state, f"Case{case_num}_initial.txt", state.final_aadl)
                self.reporter.write_artifact(state, f"Case{case_num}_fixed.txt", state.final_aadl)
                state.validation_initial = self.validator.validate(state, artifact)
                state.validation_final = state.validation_initial
                return self.reporter.write_final_report(state, exp, time.time() - start)

            if exp.model_analyst:
                state.model_analysis_full = self.model_analyst.run(state, exp.rag)
                self.reporter.write_json_artifact(state, "model_analysis_full.json", state.model_analysis_full)
                state.model_analysis = state.model_analysis_full
                self.reporter.write_json_artifact(state, "model_analysis.json", state.model_analysis)
            else:
                state.model_analysis_full = DISABLED
                state.model_analysis = DISABLED

            if exp.requirement_analyst:
                state.requirement_analysis = self.requirement_analyst.run(state, exp.rag)
                self.reporter.write_json_artifact(state, "requirement_analysis.json", state.requirement_analysis)
            else:
                state.requirement_analysis = DISABLED

            state.agree_generation_output = self.agree_generator.run(state, exp.rag)
            self.reporter.write_artifact(state, "agree_generator_output.txt", state.agree_generation_output)

            if exp.model_fusion:
                state.fused_aadl = self.model_fusion.run(state, exp.rag)
            else:
                state.fused_aadl = state.agree_generation_output
            state.final_aadl = state.fused_aadl
            artifact = self.reporter.write_artifact(state, f"Case{case_num}_initial.txt", state.final_aadl)

            state.validation_initial = self.validator.validate(state, artifact)
            state.validation_final = state.validation_initial
            if exp.repair and not state.validation_initial.success:
                self._repair_loop(state, exp.rag)

            self.reporter.write_artifact(state, f"Case{case_num}_fixed.txt", state.final_aadl)
            final_artifact = self.reporter.write_artifact(state, f"Case{case_num}_final.aadl", state.final_aadl)
            if state.validation_final is None or str(final_artifact) != state.validation_final.raw.get("artifact_path"):
                state.validation_final = self.validator.validate(state, final_artifact)
            return self.reporter.write_final_report(state, exp, time.time() - start)
        except Exception as exc:
            state.final_aadl = state.final_aadl or state.fused_aadl
            self.reporter.write_artifact(state, f"Case{case_num}_failure_partial.txt", state.final_aadl)
            payload = {
                "case_num": case_num,
                "case_letter": case_letter,
                "setting": setting.upper(),
                "success": False,
                "stage_error": str(exc),
                "error_classification": ErrorClassifier.classify_errors([str(exc)], state.final_aadl or "").to_dict(),
                "token_stats": state.token_stats.to_dict(),
                "rag_bundles": state.rag_bundles,
                "artifacts": state.artifacts,
                "runtime": time.time() - start,
            }
            (report_dir / f"Case{case_num}_report.json").write_text(__import__("json").dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
            (report_dir / f"Case{case_num}_report.md").write_text(f"# Case{case_num}_{case_letter} Failure\n\n- Stage error: {exc}\n", encoding="utf-8")
            return payload

    def _has_nonempty_agree_annex(self, aadl: str) -> bool:
        for match in re.finditer(r"annex\s+agree\s*\{\*\*(.*?)\*\*\}\s*;", aadl or "", flags=re.IGNORECASE | re.DOTALL):
            body = match.group(1)
            if re.search(r"(?im)^\s*(assume|guarantee|eq|const|assign|assert)\b", body):
                return True
        return False

    def _stage_references(self, state: PipelineState) -> None:
        ref_dir = state.report_dir(self.config.result_root) / "references"
        ref_dir.mkdir(parents=True, exist_ok=True)
        for index, ref in enumerate(state.references, 1):
            name = Path(ref.get("path", f"reference_{index}.aadl")).name
            target = ref_dir / name
            target.write_text(ref.get("content", ""), encoding="utf-8", errors="replace")
            ref["runtime_path"] = str(target)

    def _repair_loop(self, state: PipelineState, rag_enabled: bool) -> None:
        current_validation = state.validation_initial
        for round_index in range(1, self.config.max_repair_rounds + 1):
            if current_validation is None or current_validation.success:
                break
            try:
                repair = self.validation_repair.run(
                    state,
                    aadl_diagnostics=current_validation.aadl_errors,
                    agree_diagnostics=current_validation.agree_errors,
                    rag_enabled=rag_enabled,
                )
            except Exception as exc:
                state.repair_history.append(
                    {
                        "round": round_index,
                        "repair_failed": True,
                        "error": str(exc),
                        "success_after_round": False,
                        "aadl_errors": len(current_validation.aadl_errors),
                        "agree_errors": len(current_validation.agree_errors),
                    }
                )
                state.validation_final = current_validation
                continue
            state.final_aadl = repair["repaired_aadl"]
            artifact = self.reporter.write_artifact(state, f"repair_round_{round_index}.aadl", state.final_aadl)
            next_validation = self.validator.validate(state, artifact)
            state.repair_history.append(
                {
                    "round": round_index,
                    "diagnosis": repair["diagnosis"],
                    "repair_plan": repair["repair_plan"],
                    "success_after_round": next_validation.success,
                    "aadl_errors": len(next_validation.aadl_errors),
                    "agree_errors": len(next_validation.agree_errors),
                }
            )
            current_validation = next_validation
            state.validation_final = next_validation
            if next_validation.success:
                break
