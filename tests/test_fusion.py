from pathlib import Path


def test_released_case_contains_model_and_requirement():
    case_dir = Path("data/benchmark/cases/Case01")
    model = (case_dir / "Case01_Base.aadl").read_text(encoding="utf-8")
    requirement = (case_dir / "Case01_Req.txt").read_text(encoding="utf-8")
    assert "system" in model
    assert "TCAS_singleton" in requirement
    assert (case_dir / "Case01_Req_Expected.json").exists()

