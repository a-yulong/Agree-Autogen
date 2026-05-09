"""Shared validation diagnostic data structures."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class ValidationResult:
    """Result returned by lightweight validator wrappers."""

    status: str
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    message: str = ""

    @property
    def configured(self) -> bool:
        return self.status != "not_configured"

    @property
    def success(self) -> bool:
        return self.status == "ok" and not self.errors

