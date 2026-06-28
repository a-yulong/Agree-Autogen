import argparse
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = REPO_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from agree_autogen.case_runner import collect_aadl_models, extract_target_component
from agree_autogen.refactor.config import EXPERIMENTS, RuntimeConfig
from agree_autogen.refactor.orchestrator import RefactoredAgreeAutogenPipeline
from agree_autogen.runtime import configure_utf8_stdio


PROVIDER_STOP_MARKERS = (
    "insufficient",
    "quota",
    "credit",
    "credits",
    "balance",
    "payment",
    "billing",
    "rate limit",
    "rate_limit",
    "too many requests",
    "429",
    "402",
)


def _should_stop_for_provider_error(report: dict) -> bool:
    if report.get("success"):
        return False
    text = " ".join(
        str(report.get(key, ""))
        for key in ("stage_error", "error", "message")
    ).lower()
    return any(marker in text for marker in PROVIDER_STOP_MARKERS)


def _case_layout(source_root: Path, case_num: int, case_letter: str):
    case_str = f"Case{case_num:02d}"
    candidates = []
    if case_letter:
        candidates.append(source_root / f"{case_str}_{case_letter}")
    candidates.append(source_root / case_str)
    for case_dir in candidates:
        base_txt = case_dir / f"{case_str}_Base.txt"
        req_txt = case_dir / f"{case_str}_Req.txt"
        base_aadl = case_dir / f"{case_str}_Base.aadl"
        if base_txt.exists() and req_txt.exists():
            return case_str, case_dir, base_txt, req_txt, base_aadl
    case_labels = ", ".join(str(path) for path in candidates)
    raise FileNotFoundError(f"No source case with Base/Req files found for {case_str}: {case_labels}")


def _read_case(source_root: Path, case_num: int, case_letter: str):
    case_str, case_dir, base_txt, req_txt, base_aadl = _case_layout(source_root, case_num, case_letter)
    aadl_model = base_txt.read_text(encoding="utf-8", errors="replace")
    requirement = req_txt.read_text(encoding="utf-8", errors="replace").strip()
    base_aadl.write_text(aadl_model, encoding="utf-8", errors="replace")
    models = collect_aadl_models(str(base_aadl))
    target = extract_target_component(requirement, aadl_model)
    return case_str.removeprefix("Case"), aadl_model, requirement, target, models.get("references", [])


def main() -> int:
    configure_utf8_stdio()
    parser = argparse.ArgumentParser(description="Run one AGREE-AutoGen case with the refactored pipeline.")
    parser.add_argument("--case-num", type=int, default=1)
    parser.add_argument("--case-letter", default="")
    parser.add_argument("--setting", default="E2", choices=sorted(EXPERIMENTS))
    parser.add_argument("--llm-base-url", default=None)
    parser.add_argument("--llm-api-key", default=None)
    parser.add_argument("--llm-model-name", default=None)
    parser.add_argument("--result-root", default=None)
    parser.add_argument("--docs-dir", default=os.environ.get("AGREE_DOCS_DIR", str(REPO_ROOT / "knowledge_base")))
    parser.add_argument("--max-repair-rounds", type=int, default=int(os.environ.get("AGREE_MAX_REPAIR_ROUNDS", "5")))
    parser.add_argument("--use-rag", action="store_true", default=True, help="Accepted for compatibility; E settings decide whether RAG is active.")
    parser.add_argument("--no-rag", action="store_false", dest="use_rag", help="Accepted for compatibility; E settings decide whether RAG is active.")
    args, unknown = parser.parse_known_args()
    if unknown:
        print(f"Ignoring extra startup args: {unknown}")

    if args.llm_base_url:
        os.environ["AGREE_MODEL_BASE_URL"] = args.llm_base_url
    if args.llm_api_key is not None:
        os.environ["AGREE_MODEL_API_KEY"] = args.llm_api_key
    if args.llm_model_name:
        os.environ["AGREE_MODEL_NAME"] = args.llm_model_name
    if args.result_root:
        os.environ["AGREE_RESULT_ROOT"] = args.result_root
    os.environ["AGREE_MAX_REPAIR_ROUNDS"] = str(args.max_repair_rounds)

    config = RuntimeConfig.from_env(
        result_root=args.result_root,
        docs_dir=args.docs_dir,
        max_repair_rounds=args.max_repair_rounds,
    )
    config.result_root.mkdir(parents=True, exist_ok=True)
    case_num, aadl_model, requirement, target, references = _read_case(config.source_root, args.case_num, args.case_letter)

    print("=" * 80)
    print("AGREE-AutoGen refactored runner")
    case_display = f"Case{case_num}_{args.case_letter}" if args.case_letter else f"Case{case_num}"
    print(f"Case: {case_display}")
    print(f"Setting: {args.setting} ({EXPERIMENTS[args.setting].name})")
    print(f"Model: {config.model_name}")
    print(f"RAG active by setting: {EXPERIMENTS[args.setting].rag}")
    print(f"Result root: {config.result_root}")
    print("=" * 80)

    pipeline = RefactoredAgreeAutogenPipeline(config)
    report = pipeline.run_case(
        setting=args.setting,
        case_num=case_num,
        case_letter=args.case_letter,
        aadl_model=aadl_model,
        requirement_text=requirement,
        target_component=target,
        references=references,
    )
    print(f"Report success: {report.get('success')}")
    report_case_dir = f"Case{case_num}_{args.case_letter}" if args.case_letter else f"Case{case_num}"
    print(f"Report path: {config.result_root / report_case_dir / 'Report' / f'Case{case_num}_report.json'}")
    if _should_stop_for_provider_error(report):
        print("Provider quota/rate/billing-like error detected; stopping this run.", flush=True)
        return 75
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
