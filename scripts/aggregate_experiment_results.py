"""Aggregate AGREE-AutoGen reports by model and setting."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


T_LABELS = ("T1", "T2", "T3", "T4", "T5")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Aggregate AGREE-AutoGen experiment reports.")
    parser.add_argument("--result-root", required=True)
    parser.add_argument("--out-csv", default=None)
    parser.add_argument("--out-json", default=None)
    return parser.parse_args()


def iter_reports(root: Path):
    reports = set(root.glob("*/*/Case*_*/Report/Case*_report.json"))
    reports.update(root.glob("*/*/Case*/Report/Case*_report.json"))
    for report in sorted(reports):
        try:
            rel = report.relative_to(root).parts
            model_slug, setting_slug = rel[0], rel[1]
            yield model_slug, setting_slug, report
        except Exception:
            continue


def safe_load(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {"success": False, "stage_error": f"report_parse_error: {exc}"}


def main() -> int:
    args = parse_args()
    root = Path(args.result_root)
    rows: dict[tuple[str, str], dict[str, Any]] = {}
    stage_errors: dict[tuple[str, str], Counter] = defaultdict(Counter)

    for model_slug, setting_slug, report in iter_reports(root):
        key = (model_slug, setting_slug)
        row = rows.setdefault(
            key,
            {
                "model": model_slug,
                "setting": setting_slug,
                "cases": 0,
                "success": 0,
                "fail": 0,
                "validator_success": 0,
                "generation_valid": 0,
                "stage_error_cases": 0,
                "initial_errors": 0,
                "final_errors": 0,
                "repair_count": 0,
                "runtime_seconds": 0.0,
                **{label: 0 for label in T_LABELS},
            },
        )
        payload = safe_load(report)
        row["cases"] += 1
        row["success"] += 1 if payload.get("success") else 0
        row["fail"] += 0 if payload.get("success") else 1
        row["validator_success"] += 1 if payload.get("validator_success") else 0
        row["generation_valid"] += 1 if payload.get("generation_valid") else 0
        row["stage_error_cases"] += 1 if payload.get("stage_error") else 0
        row["initial_errors"] += int(payload.get("initial_error_count") or 0)
        row["final_errors"] += int(payload.get("final_error_count") or 0)
        row["repair_count"] += int(payload.get("repair_count") or 0)
        row["runtime_seconds"] += float(payload.get("runtime") or 0.0)
        for label, value in (payload.get("error_classification") or {}).items():
            if label in T_LABELS:
                row[label] += int(value or 0)
        if payload.get("stage_error"):
            stage_errors[key][str(payload.get("stage_error"))[:160]] += 1

    output_rows = []
    for key, row in sorted(rows.items()):
        cases = row["cases"] or 1
        row = dict(row)
        row["success_rate"] = row["success"] / cases
        row["avg_runtime_seconds"] = row["runtime_seconds"] / cases
        row["top_stage_errors"] = " | ".join(f"{count}x {text}" for text, count in stage_errors[key].most_common(5))
        output_rows.append(row)

    out_csv = Path(args.out_csv) if args.out_csv else root / "_aggregate_summary.csv"
    out_json = Path(args.out_json) if args.out_json else root / "_aggregate_summary.json"
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "model",
        "setting",
        "cases",
        "success",
        "fail",
        "success_rate",
        "validator_success",
        "generation_valid",
        "stage_error_cases",
        "initial_errors",
        "final_errors",
        "repair_count",
        "runtime_seconds",
        "avg_runtime_seconds",
        *T_LABELS,
        "top_stage_errors",
    ]
    with out_csv.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(output_rows)
    out_json.write_text(json.dumps(output_rows, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {out_csv}")
    print(f"Wrote {out_json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
