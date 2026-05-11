import json
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


def iter_jsonl(path: Path):
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            text = line.strip()
            if text:
                yield json.loads(text)


def test_source_inventory_and_raw_files_exist():
    data = load_yaml(KB_ROOT / "sources.yaml")
    assert data["sources"]
    assert (KB_ROOT / "raw" / "kdef" / "Attention.txt").exists()
    assert (KB_ROOT / "raw" / "kexp" / "AGREE_code_knowledge_dataset.txt").exists()
    assert (KB_ROOT / "raw" / "ksyn" / "AGREE_knowledge_dataset_en.pdf").exists()
    assert (KB_ROOT / "raw" / "ksyn" / "AGREE_Users_Guide.pdf").exists()
    assert (KB_ROOT / "raw" / "ksyn" / "AADL_AS5506C.local_source.md").exists()


def test_local_sources_example_uses_placeholders():
    data = load_yaml(KB_ROOT / "local_sources.example.yaml")
    assert "sources" in data
    assert data["sources"]["aadl_as5506c_pdf"].startswith("<LOCAL_AADL_STANDARD>")


def test_processed_kdef_files_parse():
    assert (KB_ROOT / "processed" / "kdef" / "attention_zh.md").exists()
    records = list(iter_jsonl(KB_ROOT / "processed" / "kdef" / "defensive_rules.jsonl"))
    assert records
    assert records[0]["role"] == "kdef"
    assert records[0]["source_file"] == "raw/kdef/Attention.txt"


def test_processed_kexp_files_parse():
    assert (KB_ROOT / "processed" / "kexp" / "agree_code_knowledge_dataset.txt").exists()
    records = list(iter_jsonl(KB_ROOT / "processed" / "kexp" / "agree_examples.jsonl"))
    assert records
    assert records[0]["role"] == "kexp"
    assert records[0]["source_file"] == "raw/kexp/AGREE_code_knowledge_dataset.txt"


def test_build_rag_index_dry_run_returns_success():
    result = subprocess.run(
        [sys.executable, str(BUILD_RAG_INDEX), "--dry-run"],
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    assert result.returncode == 0
    assert "raw/kdef" in result.stdout or "raw\\kdef" in result.stdout
    assert "raw/kexp" in result.stdout or "raw\\kexp" in result.stdout
    assert "raw/ksyn" in result.stdout or "raw\\ksyn" in result.stdout
