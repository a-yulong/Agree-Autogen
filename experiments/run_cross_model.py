"""Run the existing batch runner for one configured model endpoint."""

import argparse
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
RUN_BATCH = REPO_ROOT / "scripts" / "run_batch.py"


def main() -> int:
    parser = argparse.ArgumentParser(description="Run cross-model experiments with environment-configured model settings.")
    parser.add_argument("--start", type=int, required=True)
    parser.add_argument("--end", type=int, required=True)
    parser.add_argument("--letters", nargs="+", default=["A", "B"])
    parser.add_argument("--result-root", required=True)
    parser.add_argument("--no-rag", action="store_true")
    parser.add_argument("--python", default=sys.executable)
    args = parser.parse_args()

    cmd = [
        args.python,
        str(RUN_BATCH),
        "--start",
        str(args.start),
        "--end",
        str(args.end),
        "--letters",
        *args.letters,
        "--result-root",
        args.result_root,
    ]
    if args.no_rag:
        cmd.append("--no-rag")
    return subprocess.run(cmd, check=False).returncode


if __name__ == "__main__":
    sys.exit(main())

