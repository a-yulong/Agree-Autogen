"""Unified experiment entry point for AGREE-AutoGen."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
RUN_BATCH = REPO_ROOT / "scripts" / "run_batch.py"
DEFAULT_SETTINGS = Path(__file__).resolve().parent / "settings.yaml"


def load_settings(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file) or {}


def main() -> int:
    parser = argparse.ArgumentParser(description="Run an AGREE-AutoGen experiment setting.")
    parser.add_argument("--setting", required=True, help="Experiment setting, e.g. E2 or E3.")
    parser.add_argument("--benchmark", default="data/Sources", help="Case-layout benchmark root.")
    parser.add_argument("--output-dir", default="outputs/experiment", help="Experiment output directory.")
    parser.add_argument("--config", default=str(DEFAULT_SETTINGS), help="Experiment settings YAML.")
    parser.add_argument("--start", type=int, default=1, help="First case number.")
    parser.add_argument("--end", type=int, default=1, help="Last case number.")
    parser.add_argument("--letters", nargs="+", default=["A"], help="Case letters to run.")
    parser.add_argument("--python", default=sys.executable)
    args = parser.parse_args()

    settings = load_settings(Path(args.config)).get("settings", {})
    setting = settings.get(args.setting)
    if not setting:
        print(f"unknown setting: {args.setting}")
        return 2

    if setting.get("public_runner_status") != "executable":
        print("unsupported_in_public_runner")
        print(f"setting: {args.setting} {setting.get('name')}")
        print("required_runtime_support: " + ", ".join(setting.get("required_runtime_support", [])))
        return 2

    env = os.environ.copy()
    env["AGREE_SOURCE_ROOT"] = str(Path(args.benchmark))
    env["AGREE_RESULT_ROOT"] = str(Path(args.output_dir))

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
        args.output_dir,
    ]
    if not setting.get("enable_rag", True):
        cmd.append("--no-rag")

    return subprocess.run(cmd, check=False, env=env).returncode


if __name__ == "__main__":
    raise SystemExit(main())
