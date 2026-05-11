"""Compute aggregate metrics from AGREE-AutoGen report JSON files."""

import argparse
import csv
import json
from pathlib import Path
from typing import Dict, Iterable, List


def load_reports(results_dir: Path) -> List[Dict]:
    reports: List[Dict] = []
    for path in results_dir.rglob("*_report.json"):
        with path.open("r", encoding="utf-8") as file:
            item = json.load(file)
        item["_path"] = str(path)
        reports.append(item)
    return reports


def compute_metrics(reports: Iterable[Dict]) -> Dict[str, float]:
    items = list(reports)
    total = len(items)
    if total == 0:
        return {
            "cases": 0,
            "FVSR": 0.0,
            "ZRR": 0.0,
            "IEC": 0.0,
            "ARR": 0.0,
            "RRR": 0.0,
            "MFR": 0.0,
            "ART": 0.0,
            "ATC": 0.0,
        }

    successes = [item for item in items if item.get("success")]
    zero_repair = [item for item in successes if int(item.get("repair_count", 0) or 0) == 0]
    rescued = [
        item
        for item in successes
        if int(item.get("initial_error_count", 0) or 0) > 0 and int(item.get("repair_count", 0) or 0) > 0
    ]
    initially_failing = [item for item in items if int(item.get("initial_error_count", 0) or 0) > 0]
    multi_round_failures = [
        item
        for item in items
        if not item.get("success") and int(item.get("repair_count", 0) or 0) > 1
    ]

    def avg(values: List[float]) -> float:
        return sum(values) / len(values) if values else 0.0

    return {
        "cases": float(total),
        "FVSR": len(successes) / total,
        "ZRR": len(zero_repair) / total,
        "IEC": avg([float(item.get("initial_error_count", 0) or 0) for item in items]),
        "ARR": avg([float(item.get("repair_count", 0) or 0) for item in items]),
        "RRR": len(rescued) / len(initially_failing) if initially_failing else 0.0,
        "MFR": len(multi_round_failures) / total,
        "ART": avg([float(item.get("runtime", 0) or 0) for item in items]),
        "ATC": avg([float((item.get("token_stats") or {}).get("total_tokens", 0) or 0) for item in items]),
    }


def write_metrics(metrics: Dict[str, float], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(metrics.keys()))
        writer.writeheader()
        writer.writerow(metrics)


def main() -> int:
    parser = argparse.ArgumentParser(description="Compute aggregate metrics from result JSON files.")
    parser.add_argument("--results-dir", default="./results")
    parser.add_argument("--output", default="./results/metrics/metrics.csv")
    args = parser.parse_args()

    reports = load_reports(Path(args.results_dir))
    metrics = compute_metrics(reports)
    write_metrics(metrics, Path(args.output))
    print(f"Loaded {int(metrics['cases'])} report(s)")
    print(f"Wrote metrics to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

