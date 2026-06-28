"""Run AGREE-AutoGen from direct requirement and AADL file inputs.

The existing research pipeline uses a CaseXX_A benchmark layout. This script
provides a user-facing file-based entry point and internally prepares a
temporary compatible case directory when a real pipeline run is requested.
"""

import argparse
import json
import os
import shutil
import sys
import tempfile
import time
from pathlib import Path
from typing import Any, Dict, Optional


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = REPO_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from agree_autogen.validators import AADLInspectorWrapper, AgreeValidatorWrapper


def _write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True), encoding="utf-8")


def _copy_inputs(requirement: Path, aadl: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(requirement, output_dir / "requirement.txt")
    shutil.copyfile(aadl, output_dir / "input.aadl")


def _check_inputs(requirement: Path, aadl: Path, config: Optional[Path], output_dir: Path) -> Dict[str, Any]:
    errors = []
    if not requirement.exists():
        errors.append(f"Requirement file not found: {requirement}")
    if not aadl.exists():
        errors.append(f"AADL file not found: {aadl}")
    if config is not None and not config.exists():
        errors.append(f"Config file not found: {config}")
    if not errors:
        output_dir.mkdir(parents=True, exist_ok=True)
    return {"ok": not errors, "errors": errors}


def _validator_status(aadl: Path, skip_validation: bool) -> Dict[str, Any]:
    if skip_validation:
        return {"validation_skipped": True, "validation_status": "skipped"}
    aadl_result = AADLInspectorWrapper().validate(str(aadl))
    agree_result = AgreeValidatorWrapper().validate(str(aadl))
    if aadl_result.status == "not_configured" or agree_result.status == "not_configured":
        status = "not_configured"
    elif aadl_result.status == "configured" and agree_result.status == "configured":
        status = "configured"
    else:
        status = "unknown"
    return {
        "validation_skipped": False,
        "validation_status": status,
        "aadl_inspector": aadl_result.__dict__,
        "agree_validator": agree_result.__dict__,
    }


def _dry_run(args) -> int:
    requirement = Path(args.requirement)
    aadl = Path(args.aadl)
    output_dir = Path(args.output_dir)
    config = Path(args.config) if args.config else None
    check = _check_inputs(requirement, aadl, config, output_dir)
    report = {
        "mode": "dry_run",
        "success": check["ok"],
        "errors": check["errors"],
        "requirement": str(requirement),
        "aadl": str(aadl),
        "output_dir": str(output_dir),
        "config": str(config) if config else None,
        "rag_enabled": not args.disable_rag,
        "repair_enabled": not args.disable_repair,
        "llm_called": False,
        "external_validators_called": False,
        "knowledge_base_status": _knowledge_base_status(args.disable_rag),
        **_validator_status(aadl, args.skip_validation),
    }
    if check["ok"]:
        _copy_inputs(requirement, aadl, output_dir)
    _write_json(output_dir / "dry_run_report.json", report)
    if not check["ok"]:
        print("; ".join(check["errors"]))
        return 2
    print(f"Dry run completed: {output_dir / 'dry_run_report.json'}")
    return 0


def _knowledge_base_status(disable_rag: bool) -> Dict[str, Any]:
    if disable_rag:
        return {"rag_enabled": False, "status": "disabled"}
    candidates = [Path(os.environ.get("AGREE_DOCS_DIR", "")), REPO_ROOT / "knowledge_base"]
    existing = [str(path) for path in candidates if str(path) and path.exists()]
    return {"rag_enabled": True, "status": "available" if existing else "not_configured", "paths": existing}


def _missing_model_config() -> Optional[str]:
    if not os.environ.get("AGREE_MODEL_API_KEY"):
        return "AGREE_MODEL_API_KEY is not configured. Set it or use --dry-run."
    if not os.environ.get("AGREE_MODEL_BASE_URL"):
        return "AGREE_MODEL_BASE_URL is not configured. Set it or use --dry-run."
    if not os.environ.get("AGREE_MODEL_NAME"):
        return "AGREE_MODEL_NAME is not configured. Set it or use --dry-run."
    return None


def _prepare_temp_case(temp_root: Path, requirement: Path, aadl: Path) -> Path:
    case_dir = temp_root / "Case01"
    case_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(aadl, case_dir / "Case01_Base.txt")
    shutil.copyfile(requirement, case_dir / "Case01_Req.txt")
    return case_dir


def _run_pipeline(args) -> int:
    requirement = Path(args.requirement)
    aadl = Path(args.aadl)
    output_dir = Path(args.output_dir)
    config = Path(args.config) if args.config else None
    check = _check_inputs(requirement, aadl, config, output_dir)
    if not check["ok"]:
        report = {"success": False, "errors": check["errors"], "stage": "input_validation"}
        _write_json(output_dir / "report.json", report)
        print("; ".join(check["errors"]))
        return 2

    missing = _missing_model_config()
    if missing:
        _copy_inputs(requirement, aadl, output_dir)
        report = {
            "success": False,
            "stage": "configuration",
            "error": missing,
            "llm_called": False,
            **_validator_status(aadl, args.skip_validation),
        }
        _write_json(output_dir / "report.json", report)
        print(missing)
        return 2

    _copy_inputs(requirement, aadl, output_dir)

    from agree_autogen.case_runner import collect_aadl_models, extract_target_component
    from agree_autogen.refactor.config import EXPERIMENTS, RuntimeConfig
    from agree_autogen.refactor.orchestrator import RefactoredAgreeAutogenPipeline

    start_time = time.time()
    original_env = {key: os.environ.get(key) for key in ["AGREE_SOURCE_ROOT", "AGREE_RESULT_ROOT", "AGREE_WORK_MODEL"]}
    try:
        with tempfile.TemporaryDirectory(prefix="agree_autogen_files_") as temp_dir:
            temp_root = Path(temp_dir)
            _prepare_temp_case(temp_root, requirement, aadl)
            os.environ["AGREE_SOURCE_ROOT"] = str(temp_root)
            os.environ["AGREE_RESULT_ROOT"] = str(output_dir)
            setting = args.setting.upper()
            config = RuntimeConfig.from_env(
                result_root=str(output_dir),
                docs_dir=os.environ.get("AGREE_DOCS_DIR", str(REPO_ROOT / "knowledge_base")),
            )
            if args.disable_repair and setting != "E1":
                setting = "E4"
            if args.disable_rag and setting == "E2":
                setting = "E3"
            if args.skip_validation:
                print("Warning: --skip-validation is not supported by the refactored full runner; validators remain part of the experiment contract.")

            aadl_model = aadl.read_text(encoding="utf-8", errors="replace")
            requirement_text = requirement.read_text(encoding="utf-8", errors="replace").strip()
            models = collect_aadl_models(str(temp_root / "Case01" / "Case01_Base.aadl"))
            target_component = extract_target_component(requirement_text, aadl_model)
            pipeline = RefactoredAgreeAutogenPipeline(config)
            result = pipeline.run_case(
                setting=setting,
                case_num="01",
                case_letter="",
                aadl_model=aadl_model,
                requirement_text=requirement_text,
                target_component=target_component,
                references=models.get("references", []),
            )
            final_model = result.get("artifacts", {}).get("Case01_final.aadl", "")
            if final_model:
                final_path = Path(final_model)
                if final_path.exists():
                    shutil.copyfile(final_path, output_dir / "final_output.aadl")
            report = {
                "success": bool(result.get("success")),
                "stage": "pipeline",
                "runtime": time.time() - start_time,
                "case_result": result,
                "setting": setting,
                "rag_enabled": EXPERIMENTS[setting].rag,
                "repair_enabled": EXPERIMENTS[setting].repair,
                **_validator_status(aadl, args.skip_validation),
            }
            _write_json(output_dir / "report.json", report)
            print(f"Run completed. Report: {output_dir / 'report.json'}")
            return 0 if report["success"] else 1
    except Exception as exc:
        report = {
            "success": False,
            "stage": "pipeline_exception",
            "error": str(exc),
            "runtime": time.time() - start_time,
            "rag_enabled": not args.disable_rag,
            "repair_enabled": not args.disable_repair,
            **_validator_status(aadl, args.skip_validation),
        }
        _write_json(output_dir / "report.json", report)
        print(f"Pipeline failed: {exc}")
        return 1
    finally:
        for key, value in original_env.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run AGREE-AutoGen from a natural-language requirement and an AADL architecture file."
    )
    parser.add_argument("--requirement", required=True, help="Requirement text file.")
    parser.add_argument("--aadl", required=True, help="Input AADL architecture file.")
    parser.add_argument("--output-dir", required=True, help="Directory for copied inputs, generated artifacts, and reports.")
    parser.add_argument("--config", default="configs/experiments.yaml", help="Experiment config file.")
    parser.add_argument("--disable-rag", action="store_true", help="Run without retrieval augmentation or a knowledge-base index.")
    parser.add_argument("--disable-repair", action="store_true", help="Do not run iterative repair when runtime support is available.")
    parser.add_argument("--setting", default="E2", choices=["E1", "E2", "E3", "E4", "E5", "E6", "E7"], help="Experiment setting for the refactored runner.")
    parser.add_argument("--skip-validation", action="store_true", help="Do not call external AADL/AGREE validators.")
    parser.add_argument("--dry-run", action="store_true", help="Check paths and configuration without calling LLMs or validators.")
    args = parser.parse_args()

    if args.dry_run:
        return _dry_run(args)
    return _run_pipeline(args)


if __name__ == "__main__":
    raise SystemExit(main())
