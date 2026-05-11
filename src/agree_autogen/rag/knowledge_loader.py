"""Knowledge-base loading helpers."""

from pathlib import Path
from typing import List


def list_knowledge_files(root: str) -> List[Path]:
    base = Path(root)
    if not base.exists():
        return []
    return sorted(path for path in base.rglob("*") if path.is_file() and path.suffix.lower() in {".txt", ".md", ".csv"})

