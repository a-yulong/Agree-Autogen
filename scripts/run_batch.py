import argparse
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
    parser.add_argument("--python", default=sys.executable)
    args = parser.parse_args()

    for case_num in range(args.start, args.end + 1):
        for letter in args.letters:
            label = f"Case{case_num:02d}_{letter}"
            print("\n" + "=" * 80, flush=True)
            print(f"Running {label}", flush=True)
            print("=" * 80, flush=True)
            cmd = [
                args.python,
                str(RUN_CASE),
                "--case-num", str(case_num),
                "--case-letter", letter,
                "--result-root", args.result_root,
            ]
            cmd.append("--no-rag" if args.no_rag else "--use-rag")
            subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
