"""Run AGREE-AutoGen over existing CaseXX_A/B source directories.

This runner enumerates the source root instead of assuming every case number
has both A and B variants. It is intended for regenerated benchmark layouts
where labels are authoritative.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
RUN_CASE = REPO_ROOT / "scripts" / "run_case.py"
CASE_RE = re.compile(r"^Case(\d+)(?:_([AB]))?$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run existing AGREE-AutoGen cases.")
    parser.add_argument("--source-root", default=os.environ.get("AGREE_SOURCE_ROOT", str(REPO_ROOT / "data" / "benchmark" / "cases")))
    parser.add_argument("--result-root", required=True)
    parser.add_argument("--setting", default="E2", choices=["E1", "E2", "E3", "E4", "E5", "E6", "E7"])
    parser.add_argument("--case-from", type=int, default=1)
    parser.add_argument("--case-to", type=int, default=10**9)
    parser.add_argument("--letters", nargs="+", default=["A", "B"])
    parser.add_argument("--canonical-one-per-number", action="store_true")
    parser.add_argument("--preferred-letter", default="A", choices=["A", "B"])
    parser.add_argument("--max-repair-rounds", type=int, default=int(os.environ.get("AGREE_MAX_REPAIR_ROUNDS", "5")))
    parser.add_argument("--llm-base-url", default=None)
    parser.add_argument("--llm-api-key", default=None)
    parser.add_argument("--llm-model-name", default=None)
    parser.add_argument("--python", default=sys.executable)
    parser.add_argument("--resume", action="store_true", default=True)
    parser.add_argument("--no-resume", action="store_false", dest="resume")
    parser.add_argument("--limit", type=int, default=None)
    return parser.parse_args()


def discover_cases(
    source_root: Path,
    case_from: int,
    case_to: int,
    letters: set[str],
    canonical_one_per_number: bool,
    preferred_letter: str,
) -> list[tuple[int, str, str]]:
    found: dict[int, dict[str, str]] = {}
    for path in source_root.iterdir():
        if not path.is_dir():
            continue
        match = CASE_RE.match(path.name)
        if not match:
            continue
        num = int(match.group(1))
        letter = match.group(2) or ""
        if case_from <= num <= case_to and (not letter or letter in letters):
            base = path / f"Case{num:02d}_Base.txt"
            req = path / f"Case{num:02d}_Req.txt"
            if base.exists() and req.exists():
                found.setdefault(num, {})[letter] = path.name
    cases: list[tuple[int, str, str]] = []
    if canonical_one_per_number:
        fallback = "B" if preferred_letter == "A" else "A"
        for num, variants in found.items():
            if "" in variants:
                letter = ""
            else:
                letter = preferred_letter if preferred_letter in variants else fallback
            if letter in variants:
                cases.append((num, letter, variants[letter]))
    else:
        for num, variants in found.items():
            for letter, label in variants.items():
                cases.append((num, letter, label))
    return sorted(cases, key=lambda item: (item[0], item[1]))


def report_path(result_root: Path, case_num: int, letter: str) -> Path:
    label = f"Case{case_num:02d}_{letter}" if letter else f"Case{case_num:02d}"
    return result_root / label / "Report" / f"Case{case_num:02d}_report.json"


def main() -> int:
    args = parse_args()
    source_root = Path(args.source_root)
    result_root = Path(args.result_root)
    result_root.mkdir(parents=True, exist_ok=True)
    os.environ["AGREE_SOURCE_ROOT"] = str(source_root)

    cases = discover_cases(
        source_root,
        args.case_from,
        args.case_to,
        {item.upper() for item in args.letters},
        args.canonical_one_per_number,
        args.preferred_letter.upper(),
    )
    if args.limit is not None:
        cases = cases[: args.limit]
    print(f"Existing-case batch runner")
    print(f"Source root: {source_root}")
    print(f"Result root: {result_root}")
    print(f"Setting: {args.setting}")
    print(f"Cases: {len(cases)}")
    print(f"Canonical one per number: {args.canonical_one_per_number}, preferred={args.preferred_letter.upper()}")
    print(f"Model: {args.llm_model_name or os.environ.get('AGREE_MODEL_NAME', '')}")

    completed_count = 0
    for index, (case_num, letter, label) in enumerate(cases, start=1):
        report = report_path(result_root, case_num, letter)
        if args.resume and report.exists():
            print(f"[{index}/{len(cases)}] Skip existing {label}")
            continue
        print("\n" + "=" * 80, flush=True)
        print(f"[{index}/{len(cases)}] Running {label}", flush=True)
        print("=" * 80, flush=True)
        cmd = [
            args.python,
            str(RUN_CASE),
            "--case-num",
            str(case_num),
            "--case-letter",
            letter,
            "--setting",
            args.setting,
            "--max-repair-rounds",
            str(args.max_repair_rounds),
            "--result-root",
            str(result_root),
        ]
        if args.llm_base_url:
            cmd.extend(["--llm-base-url", args.llm_base_url])
        if args.llm_api_key:
            cmd.extend(["--llm-api-key", args.llm_api_key])
        if args.llm_model_name:
            cmd.extend(["--llm-model-name", args.llm_model_name])
        env = os.environ.copy()
        env.setdefault("PYTHONIOENCODING", "utf-8")
        env.setdefault("PYTHONUTF8", "1")
        completed = subprocess.run(cmd, check=False, env=env)
        if completed.returncode == 75:
            print("Stopping batch because provider quota/rate/billing-like error was detected.", flush=True)
            return 75
        if completed.returncode != 0:
            print(f"Case process returned non-zero exit {completed.returncode}; continuing with next case.", flush=True)
        completed_count += 1

    summary_path = result_root / "_batch_completed.json"
    summary_path.write_text(
        json.dumps({"source_root": str(source_root), "setting": args.setting, "case_count": len(cases), "executed": completed_count}, indent=2),
        encoding="utf-8",
    )
    print(f"Batch finished. Summary: {summary_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
