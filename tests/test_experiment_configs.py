import subprocess
import sys
from pathlib import Path

import yaml

from experiments.compute_metrics import compute_metrics, load_reports


REPO_ROOT = Path(__file__).resolve().parents[1]
SETTINGS = REPO_ROOT / "experiments" / "settings.yaml"
RUN_EXPERIMENT = REPO_ROOT / "experiments" / "run_experiment.py"


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def test_e1_to_e7_settings_exist_and_parse():
    data = load_yaml(SETTINGS)
    settings = data["settings"]
    assert set(settings) == {"E1", "E2", "E3", "E4", "E5", "E6", "E7"}
    for item in settings.values():
        assert "enable_rag" in item
        assert "enable_repair" in item
        assert "enable_model_analyst" in item
        assert "enable_requirement_analyst" in item
        assert "enable_fusion" in item
        assert "public_runner_status" in item
        assert "required_runtime_support" in item


def test_run_experiment_help_returns_success():
    result = subprocess.run(
        [sys.executable, str(RUN_EXPERIMENT), "--help"],
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    assert result.returncode == 0
    assert "--setting" in result.stdout


def test_sample_results_are_readable_by_metrics_loader():
    reports = load_reports(REPO_ROOT / "experiments" / "sample_results")
    assert len(reports) == 2
    metrics = compute_metrics(reports)
    assert metrics["cases"] == 2.0
    assert metrics["FVSR"] == 0.5
    assert metrics["IEC"] == 1.5
