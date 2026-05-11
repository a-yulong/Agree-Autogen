"""Run E2 Full Framework using the existing case-based batch runner."""

import argparse
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
RUN_BATCH = REPO_ROOT / "scripts" / "run_batch.py"
DEFAULT_CONFIG = Path(__file__).resolve().parent / "configs" / "e2_full_framework.yaml"


def main() -> int:
    parser = argparse.ArgumentParser(description="Run E2 Full Framework.")
    parser.add_argument("--start", type=int, required=True)
    parser.add_argument("--end", type=int, required=True)
    parser.add_argument("--letters", nargs="+", default=["A"])
    parser.add_argument("--result-root", default="./results")
    parser.add_argument("--python", default=sys.executable)
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    args = parser.parse_args()

    print(f"Using experiment config: {args.config}")
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
    return subprocess.run(cmd, check=False).returncode


if __name__ == "__main__":
    sys.exit(main())
