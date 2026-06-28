"""Run a released AGREE-AutoGen experiment setting over the benchmark cases."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
RUN_EXISTING_BATCH = REPO_ROOT / "scripts" / "run_existing_batch.py"
DEFAULT_SETTINGS = Path(__file__).resolve().parent / "settings.yaml"
DEFAULT_BENCHMARK = REPO_ROOT / "data" / "benchmark" / "cases"


def load_settings(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file) or {}


def main() -> int:
    parser = argparse.ArgumentParser(description="Run an AGREE-AutoGen experiment setting.")
    parser.add_argument("--setting", required=True, help="Experiment setting, for example E2.")
    parser.add_argument("--benchmark", default=str(DEFAULT_BENCHMARK), help="Benchmark case root.")
    parser.add_argument("--output-dir", default="outputs/experiment", help="Experiment output directory.")
    parser.add_argument("--config", default=str(DEFAULT_SETTINGS), help="Experiment settings YAML.")
    parser.add_argument("--start", type=int, default=1, help="First case number.")
    parser.add_argument("--end", type=int, default=459, help="Last case number.")
    parser.add_argument("--limit", type=int, default=None, help="Optional maximum number of discovered cases to run.")
    parser.add_argument("--max-repair-rounds", type=int, default=5)
    parser.add_argument("--llm-base-url", default=None)
    parser.add_argument("--llm-api-key", default=None)
    parser.add_argument("--llm-model-name", default=None)
    parser.add_argument("--python", default=sys.executable)
    args = parser.parse_args()

    settings = load_settings(Path(args.config)).get("settings", {})
    if args.setting not in settings:
        print(f"unknown setting: {args.setting}")
        return 2

    env = os.environ.copy()
    env["AGREE_SOURCE_ROOT"] = str(Path(args.benchmark))
    env["AGREE_RESULT_ROOT"] = str(Path(args.output_dir))
    env.setdefault("PYTHONIOENCODING", "utf-8")
    env.setdefault("PYTHONUTF8", "1")

    cmd = [
        args.python,
        str(RUN_EXISTING_BATCH),
        "--source-root",
        str(Path(args.benchmark)),
        "--case-from",
        str(args.start),
        "--case-to",
        str(args.end),
        "--canonical-one-per-number",
        "--setting",
        args.setting,
        "--max-repair-rounds",
        str(args.max_repair_rounds),
        "--result-root",
        args.output_dir,
    ]
    if args.limit is not None:
        cmd.extend(["--limit", str(args.limit)])
    if args.llm_base_url:
        cmd.extend(["--llm-base-url", args.llm_base_url])
    if args.llm_api_key:
        cmd.extend(["--llm-api-key", args.llm_api_key])
    if args.llm_model_name:
        cmd.extend(["--llm-model-name", args.llm_model_name])

    return subprocess.run(cmd, check=False, env=env).returncode


if __name__ == "__main__":
    raise SystemExit(main())
