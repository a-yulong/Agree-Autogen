"""Run ablation experiment templates for E3-E7.

Implemented directly:
- E3 NoRAG maps to the current batch runner with --no-rag.

Template-only in this public entry point:
- E4 NoRepair
- E5 No Model Analyst
- E6 No Requirement Analyst
- E7 No Dual Analysts
"""

import argparse
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
RUN_BATCH = REPO_ROOT / "scripts" / "run_batch.py"
CONFIGS = {
    "E3": Path(__file__).resolve().parent / "configs" / "e3_no_rag.yaml",
    "E4": Path(__file__).resolve().parent / "configs" / "e4_no_repair.yaml",
    "E5": Path(__file__).resolve().parent / "configs" / "e5_no_model_analyst.yaml",
    "E6": Path(__file__).resolve().parent / "configs" / "e6_no_requirement_analyst.yaml",
    "E7": Path(__file__).resolve().parent / "configs" / "e7_no_dual_analysts.yaml",
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Run AGREE-AutoGen ablation settings.")
    parser.add_argument("--setting", choices=["E3", "E4", "E5", "E6", "E7"], required=True)
    parser.add_argument("--start", type=int, required=True)
    parser.add_argument("--end", type=int, required=True)
    parser.add_argument("--letters", nargs="+", default=["A"])
    parser.add_argument("--result-root", default="./results")
    parser.add_argument("--python", default=sys.executable)
    parser.add_argument("--config", default=None)
    args = parser.parse_args()

    config_path = args.config or str(CONFIGS[args.setting])
    print(f"Using experiment config: {config_path}")

    if args.setting != "E3":
        print(f"{args.setting} is currently provided as a template.")
        print("Additional runtime switches are needed before this ablation can be executed.")
        print("No benchmark results were generated.")
        return 2

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
        "--no-rag",
    ]
    return subprocess.run(cmd, check=False).returncode


if __name__ == "__main__":
    sys.exit(main())
