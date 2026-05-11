"""Evaluation metrics for validation-centered experiments."""

from typing import Dict, Iterable


def _avg(values):
    values = list(values)
    return sum(values) / len(values) if values else 0.0


def compute_aggregate_metrics(reports: Iterable[Dict]) -> Dict[str, float]:
    items = list(reports)
    total = len(items)
    if total == 0:
        return {"cases": 0.0, "FVSR": 0.0, "ZRR": 0.0, "IEC": 0.0, "ARR": 0.0, "RRR": 0.0, "MFR": 0.0, "ART": 0.0, "ATC": 0.0}

    successes = [item for item in items if item.get("success")]
    zero_repair = [item for item in successes if int(item.get("repair_count", 0) or 0) == 0]
    initially_failing = [item for item in items if int(item.get("initial_error_count", 0) or 0) > 0]
    rescued = [
        item
        for item in successes
        if int(item.get("initial_error_count", 0) or 0) > 0 and int(item.get("repair_count", 0) or 0) > 0
    ]
    multi_round_failures = [item for item in items if not item.get("success") and int(item.get("repair_count", 0) or 0) > 1]

    return {
        "cases": float(total),
        "FVSR": len(successes) / total,
        "ZRR": len(zero_repair) / total,
        "IEC": _avg(float(item.get("initial_error_count", 0) or 0) for item in items),
        "ARR": _avg(float(item.get("repair_count", 0) or 0) for item in items),
        "RRR": len(rescued) / len(initially_failing) if initially_failing else 0.0,
        "MFR": len(multi_round_failures) / total,
        "ART": _avg(float(item.get("runtime", 0) or 0) for item in items),
        "ATC": _avg(float((item.get("token_stats") or {}).get("total_tokens", 0) or 0) for item in items),
    }

