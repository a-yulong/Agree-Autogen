import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
RUN_CASE = REPO_ROOT / "scripts" / "run_case.py"


def main():
    parser = argparse.ArgumentParser(description="Run Agree-Autogen over a range of cases.")
    parser.add_argument("--start", type=int, required=True)
    parser.add_argument("--end", type=int, required=True)
    parser.add_argument("--letters", nargs="+", default=["A"])
    parser.add_argument("--result-root", default=os.environ.get("AGREE_RESULT_ROOT", str(REPO_ROOT / "results")))
    parser.add_argument("--no-rag", action="store_true")
    parser.add_argument("--setting", default="E2", choices=["E1", "E2", "E3", "E4", "E5", "E6", "E7"])
    parser.add_argument("--max-repair-rounds", type=int, default=int(os.environ.get("AGREE_MAX_REPAIR_ROUNDS", "5")))
    parser.add_argument("--llm-base-url", default=None)
    parser.add_argument("--llm-api-key", default=None)
    parser.add_argument("--llm-model-name", default=None)
    parser.add_argument("--python", default=sys.executable)
    parser.add_argument("--exclude-file", default=str(REPO_ROOT / "configs" / "excluded_cases_large_model.json"))
    parser.add_argument("--max-base-kb", type=float, default=None)
    args = parser.parse_args()
    excluded = _load_excluded_cases(Path(args.exclude_file)) if args.exclude_file else set()

    for case_num in range(args.start, args.end + 1):
        for letter in args.letters:
            label = f"Case{case_num:02d}_{letter}"
            if case_num in excluded:
                print(f"Skipping {label}: listed in exclude file {args.exclude_file}", flush=True)
                continue
            if args.max_base_kb is not None and _base_model_kb(case_num, letter) > args.max_base_kb:
                print(f"Skipping {label}: base model exceeds {args.max_base_kb:.1f} KB", flush=True)
                continue
            print("\n" + "=" * 80, flush=True)
            print(f"Running {label}", flush=True)
            print("=" * 80, flush=True)
            cmd = [
                args.python,
                str(RUN_CASE),
                "--case-num", str(case_num),
                "--case-letter", letter,
                "--setting", args.setting,
                "--max-repair-rounds", str(args.max_repair_rounds),
                "--result-root", args.result_root,
            ]
            if args.llm_base_url:
                cmd.extend(["--llm-base-url", args.llm_base_url])
            if args.llm_api_key:
                cmd.extend(["--llm-api-key", args.llm_api_key])
            if args.llm_model_name:
                cmd.extend(["--llm-model-name", args.llm_model_name])
            if args.no_rag or args.setting.upper() in {"E1", "E3"}:
                cmd.append("--no-rag")
            else:
                cmd.append("--use-rag")
            env = os.environ.copy()
            env.setdefault("PYTHONIOENCODING", "utf-8")
            env.setdefault("PYTHONUTF8", "1")
            completed = subprocess.run(cmd, check=False, env=env)
            if completed.returncode == 75:
                print("Stopping batch because provider quota/rate/billing-like error was detected.", flush=True)
                return 75
            completed.check_returncode()


def _load_excluded_cases(path: Path) -> set[int]:
    if not path.exists():
        return set()
    payload = json.loads(path.read_text(encoding="utf-8"))
    values = payload.get("case_nums", payload if isinstance(payload, list) else [])
    return {int(value) for value in values}


def _base_model_kb(case_num: int, letter: str) -> float:
    source_root = Path(os.environ.get("AGREE_SOURCE_ROOT", REPO_ROOT / "data" / "Sources"))
    case_str = f"Case{case_num:02d}"
    base = source_root / f"{case_str}_{letter}" / f"{case_str}_Base.txt"
    if not base.exists():
        return 0.0
    return base.stat().st_size / 1024.0


if __name__ == "__main__":
    raise SystemExit(main())
