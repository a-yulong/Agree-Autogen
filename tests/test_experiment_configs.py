from pathlib import Path

import yaml

from experiments.compute_metrics import compute_metrics, load_reports


CONFIG_DIR = Path("experiments/configs")


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def test_e1_to_e7_configs_exist_and_parse():
    expected = {
        "e1_bare_model.yaml",
        "e2_full_framework.yaml",
        "e3_no_rag.yaml",
        "e4_no_repair.yaml",
        "e5_no_model_analyst.yaml",
        "e6_no_requirement_analyst.yaml",
        "e7_no_dual_analysts.yaml",
    }
    actual = {path.name for path in CONFIG_DIR.glob("*.yaml")}
    assert expected <= actual
    for path in CONFIG_DIR.glob("*.yaml"):
        data = load_yaml(path)
        assert data["experiment_id"].startswith("E")
        assert "settings" in data
        assert "supported_in_public_release" in data


def test_sample_results_are_readable_by_metrics_loader():
    reports = load_reports(Path("experiments/sample_results"))
    assert len(reports) == 2
    metrics = compute_metrics(reports)
    assert metrics["cases"] == 2.0
    assert metrics["FVSR"] == 0.5
    assert metrics["IEC"] == 1.5
