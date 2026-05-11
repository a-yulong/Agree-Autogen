import subprocess
import sys
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
KB_ROOT = REPO_ROOT / "knowledge_base"
BUILD_RAG_INDEX = REPO_ROOT / "scripts" / "build_rag_index.py"


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def test_source_inventory_files_parse():
    sources = load_yaml(KB_ROOT / "sources.yaml")
    local_example = load_yaml(KB_ROOT / "local_sources.example.yaml")
    assert sources["sources"]
    assert local_example["local_sources"]


def test_real_curated_sources_exist():
    assert (KB_ROOT / "curated" / "kdef" / "attention_zh.md").exists()
    assert (KB_ROOT / "curated" / "kdef" / "defensive_rules.jsonl").exists()
    assert (KB_ROOT / "curated" / "kexp" / "agree_code_knowledge_dataset.txt").exists()
    assert (KB_ROOT / "curated" / "kexp" / "agree_examples.jsonl").exists()
    assert (KB_ROOT / "curated" / "ksyn" / "agree_syntax_notes.md").exists()
    assert (KB_ROOT / "curated" / "ksyn" / "aadl_scope_notes.md").exists()


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
    assert "--knowledge-base" in result.stdout
