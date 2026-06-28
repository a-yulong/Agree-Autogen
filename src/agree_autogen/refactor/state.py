"""Explicit pipeline state and structured results."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List


DISABLED = "DISABLED"


@dataclass
class TokenStats:
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0

    def add(self, usage: Dict[str, Any]) -> None:
        self.prompt_tokens += int(usage.get("prompt_tokens", 0) or 0)
        self.completion_tokens += int(usage.get("completion_tokens", 0) or 0)
        self.total_tokens += int(usage.get("total_tokens", 0) or 0)

    def to_dict(self) -> Dict[str, int]:
        return {
            "prompt_tokens": self.prompt_tokens,
            "completion_tokens": self.completion_tokens,
            "total_tokens": self.total_tokens,
        }


@dataclass
class ValidationOutcome:
    aadl_executed: bool = False
    agree_executed: bool = False
    aadl_errors: List[str] = field(default_factory=list)
    agree_errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    aadl_report_path: str = ""
    agree_report_path: str = ""
    raw: Dict[str, Any] = field(default_factory=dict)

    @property
    def success(self) -> bool:
        return not self.aadl_errors and not self.agree_errors

    def to_dict(self) -> Dict[str, Any]:
        return {
            "success": self.success,
            "aadl_executed": self.aadl_executed,
            "agree_executed": self.agree_executed,
            "aadl_errors": self.aadl_errors,
            "agree_errors": self.agree_errors,
            "warnings": self.warnings,
            "aadl_report_path": self.aadl_report_path,
            "agree_report_path": self.agree_report_path,
            "raw": self.raw,
        }


@dataclass
class PipelineState:
    case_num: str
    case_letter: str
    setting: str
    target_component: str
    raw_requirement: str
    raw_aadl: str
    references: List[Dict[str, str]] = field(default_factory=list)
    model_analysis_full: Any = DISABLED
    model_analysis: Any = DISABLED
    requirement_analysis: Any = DISABLED
    agree_generation_output: str = ""
    fused_aadl: str = ""
    final_aadl: str = ""
    validation_initial: ValidationOutcome | None = None
    validation_final: ValidationOutcome | None = None
    generation_valid: bool = True
    generation_failure_reason: str = ""
    repair_history: List[Dict[str, Any]] = field(default_factory=list)
    rag_bundles: Dict[str, Any] = field(default_factory=dict)
    recovery_actions: List[Dict[str, Any]] = field(default_factory=list)
    artifacts: Dict[str, str] = field(default_factory=dict)
    token_stats: TokenStats = field(default_factory=TokenStats)

    @property
    def case_id(self) -> str:
        if not self.case_letter:
            return f"Case{self.case_num}"
        return f"Case{self.case_num}_{self.case_letter}"

    def report_dir(self, result_root: Path) -> Path:
        return result_root / self.case_id / "Report"
