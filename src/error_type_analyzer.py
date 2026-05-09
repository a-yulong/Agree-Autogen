"""Standalone T1-T5 error type analyzer for AADL/AGREE diagnostics."""

import argparse
import json
import os
import re
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from openai import OpenAI

LLM_BASE_URL = os.environ.get(
    "AGREE_ERROR_ANALYZER_BASE_URL",
    os.environ.get("AGREE_MODEL_BASE_URL", "https://api.openai.com/v1"),
)
LLM_API_KEY = os.environ.get("AGREE_ERROR_ANALYZER_API_KEY", os.environ.get("AGREE_MODEL_API_KEY", ""))
LLM_MODEL_NAME = os.environ.get("AGREE_ERROR_ANALYZER_MODEL", os.environ.get("AGREE_MODEL_NAME", "gpt-4o-mini"))


@dataclass
class ErrorClassification:
    """Counts for the T1-T5 taxonomy."""

    T1: int = 0
    T2: int = 0
    T3: int = 0
    T4: int = 0
    T5: int = 0

    def to_dict(self) -> Dict[str, int]:
        return {"T1": self.T1, "T2": self.T2, "T3": self.T3, "T4": self.T4, "T5": self.T5}


class LLMErrorAnalyzer:
    """Classify validation errors with an OpenAI-compatible LLM."""

    taxonomy = """
T1: Lexical and basic syntax errors, including malformed annex syntax, missing EOF, punctuation, or keyword misuse.
T2: External references and context errors, including unresolved packages, property sets, model units, with clauses, or library dependencies.
T3: Architecture and component-structure violations, including invalid component declarations, features, subcomponents, connections, implementations, or classifier usage.
T4: Declaration and identifier conflicts, including duplicate definitions, naming conflicts, undeclared variables, or illegal redeclarations.
T5: Type and numeric-logic errors, including Boolean/integer/real mismatches, invalid comparisons, invalid assignments, or expression typing issues.
"""

    def __init__(self, base_url: str = LLM_BASE_URL, api_key: str = LLM_API_KEY, model_name: str = LLM_MODEL_NAME):
        self.client = OpenAI(base_url=base_url, api_key=api_key)
        self.model_name = model_name

    def analyze_single_error(self, error_text: str, aadl_code: Optional[str] = None) -> str:
        system_prompt = (
            "You are an AADL and AGREE validation-error classifier. "
            "Return exactly one label: T1, T2, T3, T4, or T5.\n\n"
            f"{self.taxonomy}"
        )
        user_prompt = f"Error:\n{error_text}\n"
        if aadl_code:
            user_prompt += f"\nRelevant AADL/AGREE code:\n```aadl\n{aadl_code[:6000]}\n```"

        completion = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.0,
            max_tokens=16,
        )
        content = (completion.choices[0].message.content or "").strip().upper()
        match = re.search(r"\bT[1-5]\b", content)
        return match.group(0) if match else rule_based_classify(error_text)[0]

    def analyze_errors(self, errors: List[str], aadl_code: Optional[str] = None) -> ErrorClassification:
        result = ErrorClassification()
        for error in errors:
            label = self.analyze_single_error(error, aadl_code)
            setattr(result, label, getattr(result, label) + 1)
        return result


def rule_based_classify(error_text: str) -> List[str]:
    text = error_text.lower()
    categories: List[str] = []
    if any(key in text for key in ["syntax", "missing eof", "mismatched", "extraneous", "token", "parse"]):
        categories.append("T1")
    if any(key in text for key in ["couldn't resolve", "not found", "with clause", "reference", "package", "property set"]):
        categories.append("T2")
    if any(key in text for key in ["subcomponent", "connection", "feature", "implementation", "classifier"]):
        categories.append("T3")
    if any(key in text for key in ["duplicate", "already defined", "identifier", "declaration", "name"]):
        categories.append("T4")
    if any(key in text for key in ["type", "int", "real", "bool", "numeric", "left and right"]):
        categories.append("T5")
    return categories or ["T1"]


def extract_errors_from_report(report_content: str) -> List[str]:
    errors: List[str] = []
    try:
        data = json.loads(report_content)
        if isinstance(data, dict):
            for issue in data.get("issues", []):
                if isinstance(issue, dict) and issue.get("severity") == "error":
                    errors.append(str(issue.get("issue", "")))
    except Exception:
        pass

    if not errors:
        for line in report_content.splitlines():
            if re.search(r"\berror\b", line, re.IGNORECASE):
                errors.append(line.strip())
    return [error for error in errors if error]


def analyze_case_report(
    case_num: str,
    case_letter: str,
    base_dir: str,
    use_llm: bool = True,
) -> Dict[str, Any]:
    report_dir = os.path.join(base_dir, f"Case{case_num}_{case_letter}", "Report")
    report_path = os.path.join(report_dir, f"Case{case_num}_report.txt")
    if not os.path.exists(report_path):
        report_path = os.path.join(report_dir, f"Case{case_num}_report.md")
    if not os.path.exists(report_path):
        return {"success": False, "error": f"Report file not found: {report_path}"}

    with open(report_path, "r", encoding="utf-8") as file:
        report_content = file.read()
    errors = extract_errors_from_report(report_content)

    aadl_code = None
    initial_path = os.path.join(report_dir, f"Case{case_num}_initial.txt")
    if os.path.exists(initial_path):
        with open(initial_path, "r", encoding="utf-8") as file:
            aadl_code = file.read()

    if use_llm and LLM_API_KEY:
        try:
            classification = LLMErrorAnalyzer().analyze_errors(errors, aadl_code)
        except Exception:
            classification = ErrorClassification()
            for error in errors:
                for label in rule_based_classify(error):
                    setattr(classification, label, getattr(classification, label) + 1)
    else:
        classification = ErrorClassification()
        for error in errors:
            for label in rule_based_classify(error):
                setattr(classification, label, getattr(classification, label) + 1)

    result = {
        "success": True,
        "case_num": case_num,
        "case_letter": case_letter,
        "total_errors": len(errors),
        "classification": classification.to_dict(),
        "errors": errors,
    }

    output_path = os.path.join(report_dir, f"Case{case_num}_error_analysis.json")
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(result, file, indent=2, ensure_ascii=True)
    result["output_path"] = output_path
    return result


def print_summary(result: Dict[str, Any]):
    if not result.get("success"):
        print(f"Analysis failed: {result.get('error')}")
        return
    print("Error type summary")
    print("==================")
    print(f"Case: Case{result['case_num']}_{result['case_letter']}")
    print(f"Total errors: {result['total_errors']}")
    for key, value in result["classification"].items():
        print(f"{key}: {value}")


def main():
    parser = argparse.ArgumentParser(description="Analyze AADL/AGREE validation error types.")
    parser.add_argument("case_num", nargs="?", help="Case number, for example 01")
    parser.add_argument("case_letter", nargs="?", default="A", help="Case letter, for example A")
    parser.add_argument("--base-dir", default=os.environ.get("AGREE_RESULT_ROOT", os.path.abspath("results")))
    parser.add_argument("--report", help="Analyze a specific report file")
    parser.add_argument("--no-llm", action="store_true", help="Use rule-based classification only")
    args = parser.parse_args()

    if args.report:
        if not os.path.exists(args.report):
            print(f"Report file not found: {args.report}")
            return
        with open(args.report, "r", encoding="utf-8") as file:
            content = file.read()
        errors = extract_errors_from_report(content)
        classification = ErrorClassification()
        for error in errors:
            for label in rule_based_classify(error):
                setattr(classification, label, getattr(classification, label) + 1)
        result = {"success": True, "case_num": "manual", "case_letter": "", "total_errors": len(errors), "classification": classification.to_dict()}
        print_summary(result)
        return

    if not args.case_num:
        parser.error("case_num is required unless --report is provided")
    result = analyze_case_report(args.case_num, args.case_letter, args.base_dir, use_llm=not args.no_llm)
    print_summary(result)


if __name__ == "__main__":
    main()
