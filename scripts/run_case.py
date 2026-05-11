import argparse
import os

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = REPO_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from agree_autogen import runtime
from agree_autogen.pipeline import AGREEVerificationPipeline
from agree_autogen.case_runner import run_single_case


def main():
    """Single-case entry point for the Agree-Autogen pipeline."""
    parser = argparse.ArgumentParser(description="Run the Agree-Autogen pipeline for one case.")
    parser.add_argument("--case-num", type=int, default=1, help="Case number, e.g. 58")
    parser.add_argument("--case-letter", default="A", help="Case letter, e.g. A or B")
    parser.add_argument("--use-rag", dest="use_rag", action="store_true", default=True)
    parser.add_argument("--no-rag", dest="use_rag", action="store_false")
    parser.add_argument("--llm-base-url", default=None, help="Override LLM base URL")
    parser.add_argument("--llm-api-key", default=None, help="Override LLM API key")
    parser.add_argument("--llm-model-name", default=None, help="Override LLM model name")
    parser.add_argument("--result-root", default=None, help="Override output result root")
    parser.add_argument("--docs-dir", default=os.environ.get("AGREE_DOCS_DIR", "docs/AGREE_Users_Guide"))
    args, unknown_args = parser.parse_known_args()
    if unknown_args:
        print(f"Ignoring extra startup args: {unknown_args}")

    runtime.update_runtime_model_config(
        model_base_url=args.llm_base_url,
        model_api_key=args.llm_api_key,
        model_name=args.llm_model_name,
        result_root=args.result_root,
    )

    os.makedirs(runtime.RESULT_ROOT, exist_ok=True)
    pipeline = AGREEVerificationPipeline(args.docs_dir, use_rag=args.use_rag)

    print(f"Pipeline initialized. RAG: {'on' if args.use_rag else 'off'}")
    print(f"Model: {runtime.MODEL_NAME}")
    print(f"Base URL: {runtime.MODEL_BASE_URL}")
    print(f"Result root: {runtime.RESULT_ROOT}")
    print("\n" + "=" * 80)
    print(f"Starting Case{args.case_num:02d}_{args.case_letter}")
    print("=" * 80)

    case_result = run_single_case(pipeline, args.case_num, args.case_letter)
    result = case_result["result"]
    if result.get("success"):
        print(f"\nCase{args.case_num:02d}_{args.case_letter} completed")
    else:
        print(f"\nCase{args.case_num:02d}_{args.case_letter} failed: {result.get('error')}")


if __name__ == "__main__":
    main()
