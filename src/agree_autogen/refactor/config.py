"""Experiment and runtime configuration for the refactored pipeline."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List


@dataclass(frozen=True)
class ExperimentConfig:
    """Module switches for one E1-E7 experiment condition."""

    name: str
    rag: bool
    repair: bool
    requirement_analyst: bool
    model_analyst: bool
    agree_generator: str | bool
    model_fusion: bool


EXPERIMENTS: Dict[str, ExperimentConfig] = {
    "E1": ExperimentConfig("Bare Model", False, False, False, False, "direct", False),
    "E2": ExperimentConfig("Full AGREE-AutoGen", True, True, True, True, True, True),
    "E3": ExperimentConfig("NoRAG", False, True, True, True, True, True),
    "E4": ExperimentConfig("NoRepair", True, False, True, True, True, True),
    "E5": ExperimentConfig("No Model Analyst", True, True, True, False, True, True),
    "E6": ExperimentConfig("No Requirement Analyst", True, True, False, True, True, True),
    "E7": ExperimentConfig("No Dual Analysts", True, True, False, False, True, True),
}


@dataclass
class RuntimeConfig:
    """Runtime knobs shared by all experiment settings."""

    model_base_url: str
    model_api_key: str
    model_name: str
    source_root: Path
    result_root: Path
    knowledge_base: Path
    temperature: float = 0.2
    max_tokens: int | None = None
    max_repair_rounds: int = 5
    aadl_inspector_path: str = ""
    agree_validator_root: Path = Path("tools/agree-validator")
    java_home: str = ""
    osate_home: str = ""
    aadl_library_dirs: List[Path] | None = None

    @classmethod
    def from_env(
        cls,
        result_root: str | None = None,
        docs_dir: str | None = None,
        max_repair_rounds: int | None = None,
    ) -> "RuntimeConfig":
        repo_root = Path(__file__).resolve().parents[3]
        source_root = Path(os.environ.get("AGREE_SOURCE_ROOT", repo_root / "data" / "Sources"))
        validator_root = Path(os.environ.get("AGREE_VALIDATOR_ROOT", repo_root / "tools" / "agree-validator"))
        library_dirs = cls._aadl_library_dirs_from_env(repo_root, source_root, validator_root)
        return cls(
            model_base_url=os.environ.get("AGREE_MODEL_BASE_URL", "https://api.openai.com/v1"),
            model_api_key=os.environ.get("AGREE_MODEL_API_KEY", ""),
            model_name=os.environ.get("AGREE_MODEL_NAME", "gpt-4o-mini"),
            source_root=source_root,
            result_root=Path(result_root or os.environ.get("AGREE_RESULT_ROOT", repo_root / "results")),
            knowledge_base=Path(docs_dir or os.environ.get("AGREE_DOCS_DIR", repo_root / "knowledge_base")),
            temperature=float(os.environ.get("AGREE_TEMPERATURE", "0.2")),
            max_tokens=cls._optional_int_from_env("AGREE_MAX_TOKENS"),
            max_repair_rounds=max_repair_rounds or int(os.environ.get("AGREE_MAX_REPAIR_ROUNDS", "5")),
            aadl_inspector_path=os.environ.get("AADL_INSPECTOR_PATH", ""),
            agree_validator_root=validator_root,
            java_home=os.environ.get("JAVA_HOME", ""),
            osate_home=os.environ.get("OSATE_HOME", ""),
            aadl_library_dirs=library_dirs,
        )

    @staticmethod
    def _aadl_library_dirs_from_env(repo_root: Path, source_root: Path, validator_root: Path) -> List[Path]:
        """Collect configured AADL library roots used to resolve transitive with dependencies."""
        dirs: List[Path] = []
        configured = os.environ.get("AGREE_AADL_LIB_DIRS", "")
        for item in configured.split(os.pathsep):
            item = item.strip().strip('"')
            if item:
                dirs.append(Path(item))
        workspace_roots = os.environ.get("AGREE_AADL_LIB_WORKSPACE", "")
        for item in workspace_roots.split(os.pathsep):
            item = item.strip().strip('"')
            if item:
                dirs.append(Path(item))
        default_workspace = Path(r"D:\AADL_Lib_workspace")
        if default_workspace.exists():
            dirs.append(default_workspace)

        candidates = [
            validator_root / "static-libs",
            source_root,
            repo_root / "data",
        ]
        for candidate in candidates:
            if candidate not in dirs:
                dirs.append(candidate)

        seen = set()
        existing: List[Path] = []
        for directory in dirs:
            normalized = directory.expanduser().resolve() if directory.exists() else directory.expanduser()
            key = str(normalized).lower()
            if key in seen or not normalized.exists() or not normalized.is_dir():
                continue
            seen.add(key)
            existing.append(normalized)
        return existing

    @staticmethod
    def _optional_int_from_env(name: str) -> int | None:
        value = os.environ.get(name, "").strip()
        if not value:
            return None
        return int(value)


RAG_QUERIES: Dict[str, Dict[str, str]] = {
    "model_analyst": {
        "Ksyn": "AADL component type implementation feature port connection AGREE annex scope",
        "Kexp": "AADL architecture AGREE component example ports features",
        "Kdef": "scope naming structural binding identifier reference",
    },
    "requirement_analyst": {
        "Ksyn": "requirement formalization assumption guarantee condition response",
        "Kexp": "RequirementNL LogicProp CodeAGREE semantic triplet assume guarantee",
        "Kdef": "",
    },
    "agree_generator": {
        "Ksyn": "AGREE syntax assume guarantee eq const assign expression temporal operator pre arrow",
        "Kexp": "RequirementNL LogicProp CodeAGREE verified contract implication guarantee assume",
        "Kdef": "syntax prohibitions scope naming structural binding",
    },
    "model_fusion": {
        "Ksyn": "AGREE annex placement component type implementation assign guarantee eq const",
        "Kexp": "AADL AGREE integrated model component type implementation annex example",
        "Kdef": "structural binding scope naming syntax prohibitions",
    },
    "validation_repair": {
        "Ksyn": "AGREE validation error syntax type unresolved reference AADL annex",
        "Kexp": "verified AGREE contract repair pattern syntax example",
        "Kdef": "syntax prohibitions unresolved reference scope naming structural binding",
    },
}
