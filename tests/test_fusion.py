from pathlib import Path


def test_gf_monitor_expected_output_contains_agree_annex():
    output = Path("data/examples/gf_monitor/expected_output.aadl").read_text(encoding="utf-8")
    assert "annex agree {**" in output
    assert "guarantee" in output
    assert "GF_Monitor" in output

