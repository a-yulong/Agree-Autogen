from agree_autogen.metrics.evaluation_metrics import compute_aggregate_metrics


def test_compute_aggregate_metrics():
    reports = [
        {"success": True, "repair_count": 0, "initial_error_count": 0, "runtime": 10, "token_stats": {"total_tokens": 100}},
        {"success": True, "repair_count": 2, "initial_error_count": 5, "runtime": 20, "token_stats": {"total_tokens": 300}},
        {"success": False, "repair_count": 3, "initial_error_count": 4, "runtime": 30, "token_stats": {"total_tokens": 500}},
    ]
    metrics = compute_aggregate_metrics(reports)
    assert metrics["cases"] == 3.0
    assert round(metrics["FVSR"], 4) == 0.6667
    assert round(metrics["ZRR"], 4) == 0.3333
    assert metrics["IEC"] == 3.0
    assert round(metrics["ARR"], 4) == 1.6667
    assert metrics["ART"] == 20.0
    assert metrics["ATC"] == 300.0

