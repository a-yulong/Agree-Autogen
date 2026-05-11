"""Minimal AADL Inspector wrapper used by tests and documentation examples."""

import os
from pathlib import Path
from typing import Optional

from .diagnostics import ValidationResult


class AADLInspectorWrapper:
    """Check AADL Inspector configuration without requiring the tool in tests."""

    def __init__(self, executable: Optional[str] = None):
        self.executable = executable or os.environ.get("AADL_INSPECTOR_PATH", "")

    def validate(self, aadl_path: str) -> ValidationResult:
        if not self.executable:
            return ValidationResult(status="not_configured", message="AADL_INSPECTOR_PATH is not configured.")
        if not Path(self.executable).exists():
            return ValidationResult(status="not_configured", message=f"AADL Inspector not found: {self.executable}")
        if not Path(aadl_path).exists():
            return ValidationResult(status="input_missing", errors=[f"AADL file not found: {aadl_path}"])
        return ValidationResult(status="configured", message="AADL Inspector is configured; full execution is handled by the main pipeline.")

