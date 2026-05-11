import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
RUN_FILES = REPO_ROOT / "scripts" / "run_files.py"
REQ = REPO_ROOT / "data" / "examples" / "gf_monitor" / "requirement.txt"
AADL = REPO_ROOT / "data" / "examples" / "gf_monitor" / "input.aadl"
CONFIG = REPO_ROOT / "configs" / "experiments.yaml"


def run_cli(args):
    return subprocess.run(
        [sys.executable, str(RUN_FILES), *args],
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def test_dry_run_with_gf_monitor_succeeds(tmp_path):
    out = tmp_path / "gf_monitor"
    result = run_cli([
        "--requirement", str(REQ),
        "--aadl", str(AADL),
        "--output-dir", str(out),
        "--config", str(CONFIG),
        "--disable-rag",
        "--skip-validation",
        "--dry-run",
    ])
    assert result.returncode == 0, result.stderr
    report = json.loads((out / "dry_run_report.json").read_text(encoding="utf-8"))
    assert report["success"] is True
    assert report["llm_called"] is False
    assert report["external_validators_called"] is False
    assert report["validation_skipped"] is True


def test_missing_requirement_file_returns_clear_failure(tmp_path):
    out = tmp_path / "missing_req"
    result = run_cli([
        "--requirement", str(tmp_path / "missing.txt"),
        "--aadl", str(AADL),
        "--output-dir", str(out),
        "--config", str(CONFIG),
        "--dry-run",
    ])
    assert result.returncode == 2
    assert "Requirement file not found" in result.stdout
    report = json.loads((out / "dry_run_report.json").read_text(encoding="utf-8"))
    assert report["success"] is False


def test_missing_aadl_file_returns_clear_failure(tmp_path):
    out = tmp_path / "missing_aadl"
    result = run_cli([
        "--requirement", str(REQ),
        "--aadl", str(tmp_path / "missing.aadl"),
        "--output-dir", str(out),
        "--config", str(CONFIG),
        "--dry-run",
    ])
    assert result.returncode == 2
    assert "AADL file not found" in result.stdout
    report = json.loads((out / "dry_run_report.json").read_text(encoding="utf-8"))
    assert report["success"] is False


def test_skip_validation_does_not_require_external_validator(tmp_path):
    out = tmp_path / "skip_validation"
    result = run_cli([
        "--requirement", str(REQ),
        "--aadl", str(AADL),
        "--output-dir", str(out),
        "--config", str(CONFIG),
        "--disable-rag",
        "--skip-validation",
        "--dry-run",
    ])
    assert result.returncode == 0
    report = json.loads((out / "dry_run_report.json").read_text(encoding="utf-8"))
    assert report["validation_status"] == "skipped"


def test_disable_rag_does_not_require_knowledge_base_index(tmp_path):
    out = tmp_path / "disable_rag"
    result = run_cli([
        "--requirement", str(REQ),
        "--aadl", str(AADL),
        "--output-dir", str(out),
        "--config", str(CONFIG),
        "--disable-rag",
        "--skip-validation",
        "--dry-run",
    ])
    assert result.returncode == 0
    report = json.loads((out / "dry_run_report.json").read_text(encoding="utf-8"))
    assert report["knowledge_base_status"]["status"] == "disabled"


def test_help_returns_success():
    result = run_cli(["--help"])
    assert result.returncode == 0
    assert "--requirement" in result.stdout
    assert "--dry-run" in result.stdout
