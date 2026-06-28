import argparse
import json
import os
import random
import subprocess
import sys
import time
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
RUN_CASE = REPO_ROOT / "scripts" / "run_case.py"


def main() -> int:
    parser = argparse.ArgumentParser(description="Supervise random AGREE-AutoGen batches.")
    parser.add_argument("--count", type=int, default=50)
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int, default=910)
    parser.add_argument("--letter", default="A")
    parser.add_argument("--setting", default="E2")
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--source-root", default=os.environ.get("AGREE_SOURCE_ROOT", r"C:\Users\25780\Desktop\Exp_Data\Sources"))
    parser.add_argument("--result-root", required=True)
    parser.add_argument("--desktop-report", required=True)
    parser.add_argument("--exclude-file", default=str(REPO_ROOT / "configs" / "excluded_cases_large_model.json"))
    parser.add_argument("--max-base-kb", type=float, default=64.0)
    parser.add_argument("--max-repair-rounds", type=int, default=5)
    args = parser.parse_args()

    source_root = Path(args.source_root)
    result_root = Path(args.result_root)
    result_root.mkdir(parents=True, exist_ok=True)
    desktop_report = Path(args.desktop_report)
    excluded = load_excluded(Path(args.exclude_file))
    seed = args.seed if args.seed is not None else int(time.time())
    selected = select_cases(source_root, args.start, args.end, args.letter, args.count, excluded, args.max_base_kb, seed)
    progress_path = result_root / "supervision_progress.json"
    report_path = result_root / "supervision_report.md"

    rows = []
    write_reports(progress_path, report_path, desktop_report, selected, rows, seed, status="running")
    for index, case_num in enumerate(selected, 1):
        label = f"Case{case_num:02d}_{args.letter}"
        started = time.time()
        cmd = [
            sys.executable,
            str(RUN_CASE),
            "--case-num",
            str(case_num),
            "--case-letter",
            args.letter,
            "--setting",
            args.setting,
            "--max-repair-rounds",
            str(args.max_repair_rounds),
            "--result-root",
            str(result_root),
        ]
        env = os.environ.copy()
        env["AGREE_SOURCE_ROOT"] = str(source_root)
        env.setdefault("PYTHONIOENCODING", "utf-8")
        env.setdefault("PYTHONUTF8", "1")
        env["PYTHONPATH"] = str(REPO_ROOT / "src")
        row = {
            "index": index,
            "case": label,
            "case_num": case_num,
            "returncode": None,
            "success": False,
            "validator_success": False,
            "repair_count": None,
            "final_error_count": None,
            "initial_error_count": None,
            "runtime_seconds": None,
            "stage_error": "",
            "report": "",
        }
        try:
            completed = subprocess.run(cmd, cwd=REPO_ROOT, env=env, text=True, encoding="utf-8", errors="replace")
            row["returncode"] = completed.returncode
            row["runtime_seconds"] = round(time.time() - started, 2)
            report_file = result_root / label / "Report" / f"Case{case_num:02d}_report.json"
            if report_file.exists():
                payload = json.loads(report_file.read_text(encoding="utf-8", errors="replace"))
                row["success"] = bool(payload.get("success"))
                row["validator_success"] = bool(payload.get("validator_success"))
                row["repair_count"] = payload.get("repair_count")
                row["final_error_count"] = payload.get("final_error_count")
                row["initial_error_count"] = payload.get("initial_error_count")
                row["stage_error"] = str(payload.get("stage_error") or payload.get("error") or "")
                row["report"] = str(report_file)
            if completed.returncode == 75:
                row["stage_error"] = row["stage_error"] or "Provider quota/rate/billing-like stop marker."
                rows.append(row)
                write_reports(progress_path, report_path, desktop_report, selected, rows, seed, status="provider_stop")
                return 75
        except Exception as exc:
            row["runtime_seconds"] = round(time.time() - started, 2)
            row["stage_error"] = f"{type(exc).__name__}: {exc}"
        rows.append(row)
        write_reports(progress_path, report_path, desktop_report, selected, rows, seed, status="running")
    write_reports(progress_path, report_path, desktop_report, selected, rows, seed, status="completed")
    return 0


def load_excluded(path: Path) -> set[int]:
    if not path.exists():
        return set()
    payload = json.loads(path.read_text(encoding="utf-8", errors="replace"))
    values = payload.get("case_nums", payload if isinstance(payload, list) else [])
    return {int(value) for value in values}


def select_cases(source_root: Path, start: int, end: int, letter: str, count: int, excluded: set[int], max_base_kb: float, seed: int) -> list[int]:
    candidates = []
    for case_num in range(start, end + 1):
        if case_num in excluded:
            continue
        case = f"Case{case_num:02d}"
        base = source_root / f"{case}_{letter}" / f"{case}_Base.txt"
        req = source_root / f"{case}_{letter}" / f"{case}_Req.txt"
        if not base.exists() or not req.exists():
            continue
        if max_base_kb and base.stat().st_size / 1024.0 > max_base_kb:
            continue
        candidates.append(case_num)
    rng = random.Random(seed)
    rng.shuffle(candidates)
    return candidates[:count]


def score(rows: list[dict]) -> float:
    if not rows:
        return 0.0
    success_rate = sum(1 for row in rows if row.get("success")) / len(rows)
    avg_final_errors = sum(int(row.get("final_error_count") or 0) for row in rows) / len(rows)
    error_penalty = min(2.0, avg_final_errors / 10.0)
    return max(0.0, min(10.0, round(success_rate * 10.0 - error_penalty, 2)))


def write_reports(progress_path: Path, report_path: Path, desktop_report: Path, selected: list[int], rows: list[dict], seed: int, status: str) -> None:
    completed = len(rows)
    successes = sum(1 for row in rows if row.get("success"))
    payload = {
        "status": status,
        "seed": seed,
        "selected": selected,
        "completed": completed,
        "total": len(selected),
        "successes": successes,
        "success_rate": round(successes / completed, 4) if completed else 0.0,
        "score": score(rows),
        "rows": rows,
    }
    progress_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8", errors="replace")
    failing = [row for row in rows if not row.get("success")]
    lines = [
        "# AGREE-AutoGen Supervised Random Batch",
        "",
        f"- Status: {status}",
        f"- Seed: {seed}",
        f"- Completed: {completed}/{len(selected)}",
        f"- Successes: {successes}",
        f"- Current score: {payload['score']}/10",
        f"- Selected cases: {', '.join(str(x) for x in selected)}",
        "",
        "## Failures / Abnormal Cases",
    ]
    if failing:
        for row in failing[-20:]:
            lines.append(
                f"- {row.get('case')}: return={row.get('returncode')}, final_errors={row.get('final_error_count')}, repair={row.get('repair_count')}, error={row.get('stage_error')}"
            )
    else:
        lines.append("- None so far.")
    lines.append("")
    lines.append("## Completed Rows")
    for row in rows:
        lines.append(
            f"- {row.get('index'):02d}. {row.get('case')}: success={row.get('success')}, final_errors={row.get('final_error_count')}, runtime={row.get('runtime_seconds')}s"
        )
    text = "\n".join(lines) + "\n"
    report_path.write_text(text, encoding="utf-8", errors="replace")
    desktop_report.write_text(text, encoding="utf-8", errors="replace")


if __name__ == "__main__":
    raise SystemExit(main())
