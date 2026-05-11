import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
BUILD_RAG_INDEX = REPO_ROOT / "scripts" / "build_rag_index.py"


def test_build_rag_index_help_returns_success():
    result = subprocess.run(
        [sys.executable, str(BUILD_RAG_INDEX), "--help"],
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    assert result.returncode == 0
    assert "--dry-run" in result.stdout
    assert "--include-local-sources" in result.stdout
