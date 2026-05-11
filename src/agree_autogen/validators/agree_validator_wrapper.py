"""Minimal standalone AGREE validator wrapper."""

import os
from pathlib import Path
from typing import Optional

from .diagnostics import ValidationResult


class AgreeValidatorWrapper:
    """Check standalone AGREE validator configuration without invoking Java."""

    def __init__(self, validator_root: Optional[str] = None, java_home: Optional[str] = None, osate_home: Optional[str] = None):
        self.validator_root = validator_root or os.environ.get("AGREE_VALIDATOR_ROOT", "./tools/agree-validator")
        self.java_home = java_home or os.environ.get("JAVA_HOME", "")
        self.osate_home = osate_home or os.environ.get("OSATE_HOME", "")

    def validate(self, aadl_path: str) -> ValidationResult:
        missing = []
        if not self.java_home:
            missing.append("JAVA_HOME")
        if not self.osate_home:
            missing.append("OSATE_HOME")
        if not self.validator_root or not Path(self.validator_root).exists():
            missing.append("AGREE_VALIDATOR_ROOT")
        if missing:
            return ValidationResult(status="not_configured", message="Missing configuration: " + ", ".join(missing))
        if not Path(aadl_path).exists():
            return ValidationResult(status="input_missing", errors=[f"AADL file not found: {aadl_path}"])
        return ValidationResult(status="configured", message="Standalone AGREE validator is configured; full execution is handled by the main pipeline.")

