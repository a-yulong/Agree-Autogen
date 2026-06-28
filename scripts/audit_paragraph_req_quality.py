"""Audit paragraph-style requirements against AADL and expected trace metadata."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


DEFAULT_ROOT = Path(r"C:\Users\25780\Desktop\Exp_Data\Sources_Curated_ParagraphStyle_20260603")
DEFAULT_REPORT = Path(r"C:\Users\25780\Desktop\Exp_Data\SourceReq_Quality_Audit")


AGREE_BEHAVIOR_WORDS = [
    "guarantee",
    "assume",
    "if ",
    "when ",
    "whenever ",
    "equal",
    "greater than",
    "less than",
    "between",
    "true",
    "false",
    "previous",
    "current",
    "pre(",
]

UNSUPPORTED_VAGUE_WORDS = [
    "normal operation",
    "legal",
    "correct",
    "appropriate",
    "environmental conditions",
    "valid values",
    "data type constraints",
    "within the valid",
    "legitimate action",
]

STRUCTURAL_WORDS = [
    "route",
    "routing",
    "through connection",
    "data flow",
    "control signal",
    "signal flow",
    "event flow",
]

PROPERTY_WORDS = [
    "dispatch protocol",
    "period",
    "deadline",
    "compute execution",
    "priority",
    "bandwidth",
    "mass",
    "power consumption",
    "latency",
    "bind",
    "binding",
    "entrypoint",
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit paragraph-style source requirements.")
    parser.add_argument("--root", default=str(DEFAULT_ROOT))
    parser.add_argument("--report-root", default=str(DEFAULT_REPORT))
    args = parser.parse_args()

    root = Path(args.root)
    report_root = Path(args.report_root)
    report_root.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, Any]] = []
    issue_examples: dict[str, list[dict[str, str]]] = defaultdict(list)

    for case_dir in sorted(iter_case_dirs(root), key=lambda p: natural_key(p.name)):
        row = audit_case(case_dir)
        rows.append(row)
        for issue in row["issues"]:
            if len(issue_examples[issue]) < 12:
                issue_examples[issue].append(
                    {
                        "label": row["label"],
                        "req": row["req_text"][:400],
                        "detail": row["issue_details"].get(issue, ""),
                    }
                )

    write_csv(report_root / "paragraph_req_quality_audit.csv", rows)
    write_summary(report_root / "paragraph_req_quality_audit.md", rows, issue_examples)
    print(f"Audited labels: {len(rows)}")
    print(f"Report: {report_root / 'paragraph_req_quality_audit.md'}")
    return 0


def iter_case_dirs(root: Path) -> list[Path]:
    return [p for p in root.iterdir() if p.is_dir() and re.fullmatch(r"Case\d+_[A-Z]", p.name)]


def natural_key(text: str) -> list[Any]:
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", text)]


def audit_case(case_dir: Path) -> dict[str, Any]:
    match = re.fullmatch(r"Case(\d+)_([A-Z])", case_dir.name)
    assert match
    case_label = f"Case{int(match.group(1)):02d}"
    req_path = case_dir / f"{case_label}_Req.txt"
    sidecar_path = case_dir / f"{case_label}_Req_Expected.json"
    aadl_path = case_dir / f"{case_label}_Base.aadl"
    if not aadl_path.exists():
        aadl_path = case_dir / f"{case_label}_Base.txt"

    req = req_path.read_text(encoding="utf-8", errors="replace").strip()
    sidecar = json.loads(sidecar_path.read_text(encoding="utf-8", errors="replace"))
    aadl = aadl_path.read_text(encoding="utf-8", errors="replace") if aadl_path.exists() else ""
    items = sidecar.get("requirement_items", [])
    classes = Counter(item.get("requirement_class", "") for item in items)
    action = sidecar.get("action", "")
    expected_route = infer_expected_route(req, classes, action)
    issues: list[str] = []
    details: dict[str, str] = {}

    trace_missing = []
    for item in items:
        check = item.get("expected_check") or {}
        missing = missing_trace_terms(check, aadl)
        if missing:
            trace_missing.append(f"{check.get('kind')}:{','.join(missing[:4])}")
    if trace_missing:
        issues.append("trace_not_found_in_aadl")
        details["trace_not_found_in_aadl"] = "; ".join(trace_missing[:8])

    lower = req.lower()
    vague_hits = [word for word in UNSUPPORTED_VAGUE_WORDS if word in lower]
    if vague_hits:
        issues.append("unsupported_vague_wording")
        details["unsupported_vague_wording"] = ", ".join(vague_hits)

    has_behavior_word = any(word in lower for word in AGREE_BEHAVIOR_WORDS)
    has_struct_or_prop = bool(classes.get("structural_check") or classes.get("property_check"))
    if expected_route != "agree_generation" and has_behavior_word and not action == "kept_existing_high_quality":
        issues.append("may_induce_agree_generation")
        details["may_induce_agree_generation"] = "contains behavior-like wording in structural/property req"

    if action == "kept_existing_high_quality" and not classes.get("kept_existing_precise"):
        issues.append("kept_action_without_precise_class")

    if has_struct_or_prop and "kept_existing_precise" not in classes and len(req) > 850:
        issues.append("long_structural_property_paragraph")
        details["long_structural_property_paragraph"] = f"chars={len(req)}"

    if not items:
        issues.append("missing_requirement_items")

    simulated = simulate_downstream(req, classes, action)
    if simulated["risk"] != "low":
        issues.append(f"simulation_{simulated['risk']}_risk")
        details[f"simulation_{simulated['risk']}_risk"] = simulated["reason"]

    return {
        "label": case_dir.name,
        "action": action,
        "classes": dict(classes),
        "expected_route": expected_route,
        "simulated_outcome": simulated["outcome"],
        "simulation_risk": simulated["risk"],
        "issues": issues,
        "issue_details": details,
        "req_chars": len(req),
        "item_count": len(items),
        "req_text": req,
    }


def infer_expected_route(req: str, classes: Counter, action: str) -> str:
    if classes.get("kept_existing_precise") or action == "kept_existing_high_quality":
        return "agree_generation"
    if classes.get("structural_check") and classes.get("property_check"):
        return "aadl_structural_property_validation"
    if classes.get("structural_check"):
        return "aadl_structural_validation"
    if classes.get("property_check"):
        return "aadl_property_validation"
    return "unknown"


def missing_trace_terms(check: dict[str, Any], aadl: str) -> list[str]:
    if not check:
        return []
    terms: list[str] = []
    kind = check.get("kind", "")
    if kind == "connection":
        terms.extend([check.get("connection", ""), check.get("source", ""), check.get("destination", "")])
    elif kind == "property":
        terms.extend([check.get("property", ""), check.get("value", "")])
        if check.get("element"):
            terms.append(check.get("element", ""))
    missing = []
    aadl_lower = aadl.lower()
    for term in terms:
        term = str(term).strip()
        if not term:
            continue
        if term.lower() not in aadl_lower:
            compact = re.sub(r"\s+", "", term.lower())
            aadl_compact = re.sub(r"\s+", "", aadl_lower)
            if compact not in aadl_compact:
                missing.append(term)
    return missing


def simulate_downstream(req: str, classes: Counter, action: str) -> dict[str, str]:
    lower = req.lower()
    if classes.get("kept_existing_precise") or action == "kept_existing_high_quality":
        vague_hits = [word for word in UNSUPPORTED_VAGUE_WORDS if word in lower]
        if vague_hits:
            return {
                "outcome": "LLM may try to generate AGREE from unsupported vague natural-language semantics.",
                "risk": "high",
                "reason": f"behavior subset contains unsupported terms: {', '.join(vague_hits)}",
            }
        return {
            "outcome": "LLM should attempt AGREE assume/guarantee generation using visible variables and relations.",
            "risk": "low",
            "reason": "kept behavior requirement",
        }
    if classes.get("structural_check") or classes.get("property_check"):
        structural = any(word in lower for word in STRUCTURAL_WORDS)
        prop = any(word in lower for word in PROPERTY_WORDS)
        if structural or prop:
            return {
                "outcome": "LLM should classify as AADL structural/property requirement and avoid forcing AGREE clauses.",
                "risk": "low",
                "reason": "clear structural/property wording",
            }
        return {
            "outcome": "LLM may not recognize validation target without sidecar metadata.",
            "risk": "medium",
            "reason": "structural/property classes but weak natural-language cue",
        }
    return {"outcome": "Unknown downstream path.", "risk": "medium", "reason": "unknown classes"}


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = [
        "label",
        "action",
        "expected_route",
        "simulated_outcome",
        "simulation_risk",
        "req_chars",
        "item_count",
        "classes",
        "issues",
        "issue_details",
    ]
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    field: json.dumps(row[field], ensure_ascii=False) if isinstance(row.get(field), (dict, list)) else row.get(field, "")
                    for field in fields
                }
            )


def write_summary(path: Path, rows: list[dict[str, Any]], issue_examples: dict[str, list[dict[str, str]]]) -> None:
    risk_counts = Counter(row["simulation_risk"] for row in rows)
    route_counts = Counter(row["expected_route"] for row in rows)
    issue_counts = Counter(issue for row in rows for issue in row["issues"])
    lines = [
        "# Paragraph REQ Quality Audit",
        "",
        f"- Audited A/B labels: {len(rows)}",
        f"- Expected routes: `{json.dumps(dict(route_counts), ensure_ascii=False)}`",
        f"- Simulation risks: `{json.dumps(dict(risk_counts), ensure_ascii=False)}`",
        "",
        "## Issue Counts",
        "",
    ]
    if issue_counts:
        for issue, count in issue_counts.most_common():
            lines.append(f"- {count}: {issue}")
    else:
        lines.append("- No issues found.")
    lines.extend(["", "## Issue Examples", ""])
    for issue, examples in issue_examples.items():
        lines.append(f"### {issue}")
        for example in examples:
            lines.append(f"- `{example['label']}` {example['detail']}: {example['req']}")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
