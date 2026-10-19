"""Rebuild source requirements around AGREE-generatable interface contracts.

This script does not try to preserve the old LLM-generated requirements.  It
uses each case's existing AADL model and target component, extracts visible
type-scope symbols, and writes a cleaner requirement only when a simple,
explicit AGREE relation can be formed over those visible symbols.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any


DEFAULT_SOURCE_ROOT = Path(r"C:\Users\25780\Desktop\Exp_Data\Sources")
DEFAULT_REPORT_ROOT = Path(r"C:\Users\25780\Desktop\Exp_Data\SourceReq_Rebuild")


@dataclass(frozen=True)
class Feature:
    name: str
    direction: str
    category: str
    aadl_type: str
    scalar: str


@dataclass(frozen=True)
class CaseCandidate:
    case_num: int
    letter: str
    label: str
    source_type: str
    target: str
    req_path: str
    base_path: str
    selected: bool
    requirement_class: str
    expected_output_type: str
    reason: str
    trace_refs: list[str]
    quality_checks: dict[str, bool]
    visible_symbols: list[dict[str, str]]
    natural_requirement: str = ""
    expected_agree: str = ""


def main() -> int:
    parser = argparse.ArgumentParser(description="Rebuild AGREE-oriented source requirements.")
    parser.add_argument("--source-root", default=str(DEFAULT_SOURCE_ROOT))
    parser.add_argument("--report-root", default=str(DEFAULT_REPORT_ROOT))
    parser.add_argument("--min-case", type=int, default=110)
    parser.add_argument("--max-case", type=int, default=9999)
    parser.add_argument("--letters", default="A,B")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--write", action="store_true", help="Overwrite selected CaseXX_Req.txt files after backup.")
    parser.add_argument(
        "--curated-root",
        default="",
        help="Optional output source root containing only selected cases with rebuilt requirements.",
    )
    args = parser.parse_args()

    source_root = Path(args.source_root)
    stamp = time.strftime("%Y%m%d_%H%M%S")
    run_root = Path(args.report_root) / f"req_rebuild_{stamp}"
    run_root.mkdir(parents=True, exist_ok=True)
    backup_root = source_root / f"_req_backup_before_rebuild_{stamp}"
    if args.write:
        backup_root.mkdir(parents=True, exist_ok=True)

    source_map = load_source_map(source_root / "Case_Source_Map.csv")
    letters = {part.strip().upper() for part in args.letters.split(",") if part.strip()}
    candidates: list[CaseCandidate] = []
    for row in source_map:
        case_num = int(row["Case"])
        if case_num < args.min_case or case_num > args.max_case:
            continue
        for letter in sorted(letters):
            label = f"Case{case_num:02d}_{letter}"
            case_dir = source_root / label
            case_label = f"Case{case_num:02d}"
            req_path = case_dir / f"{case_label}_Req.txt"
            base_path = case_dir / f"{case_label}_Base.aadl"
            if not base_path.exists():
                base_path = case_dir / f"{case_label}_Base.txt"
            if not req_path.exists() or not base_path.exists():
                continue
            aadl_text = base_path.read_text(encoding="utf-8", errors="replace")
            candidate = build_candidate(case_num, letter, row.get("Target", ""), req_path, base_path, aadl_text)
            candidates.append(candidate)
            if args.limit and len(candidates) >= args.limit:
                break
        if args.limit and len(candidates) >= args.limit:
            break

    manifest_path = run_root / "manifest.json"
    manifest_path.write_text(
        json.dumps([asdict(item) for item in candidates], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    write_csv(run_root / "manifest.csv", candidates)

    if args.write:
        for item in candidates:
            if not item.selected:
                continue
            req_path = Path(item.req_path)
            rel_dir = req_path.parent.relative_to(source_root)
            backup_dir = backup_root / rel_dir
            backup_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(req_path, backup_dir / req_path.name)
            req_path.write_text(item.natural_requirement.strip() + "\n", encoding="utf-8")

    curated_root = Path(args.curated_root) if args.curated_root else None
    if curated_root:
        create_curated_source_root(source_root, curated_root, candidates)

    write_summary(run_root, candidates, args.write, backup_root if args.write else None, curated_root)
    print(f"Cases considered: {len(candidates)}")
    print(f"Selected clean AGREE-generatable requirements: {sum(1 for item in candidates if item.selected)}")
    print(f"Run root: {run_root}")
    print(f"Summary: {run_root / 'summary.md'}")
    if curated_root:
        print(f"Curated source root: {curated_root}")
    return 0


def load_source_map(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row.get("Case", "").isdigit()]
    rows.sort(key=lambda row: int(row["Case"]))
    return rows


def build_candidate(
    case_num: int,
    letter: str,
    target: str,
    req_path: Path,
    base_path: Path,
    aadl_text: str,
) -> CaseCandidate:
    component = target.split(".", 1)[0].strip()
    features = extract_features(aadl_text, component)
    selected, reason, natural, expected, trace_refs = synthesize_requirement(component, features)
    quality_checks = build_quality_checks(selected, natural, trace_refs)
    return CaseCandidate(
        case_num=case_num,
        letter=letter,
        label=f"Case{case_num:02d}_{letter}",
        source_type="aadl_synthetic",
        target=target,
        req_path=str(req_path),
        base_path=str(base_path),
        selected=selected,
        requirement_class="generatable" if selected else "not_selected",
        expected_output_type="agree_annex" if selected else "no_agree_with_reason",
        reason=reason,
        trace_refs=trace_refs,
        quality_checks=quality_checks,
        visible_symbols=[asdict(feature) for feature in features],
        natural_requirement=natural,
        expected_agree=expected,
    )


def extract_features(aadl_text: str, component: str) -> list[Feature]:
    block = extract_component_type_block(aadl_text, component)
    if not block:
        return []
    feature_section = extract_section(block, "features")
    if not feature_section:
        return []
    pattern = re.compile(
        r"(?im)^\s*([A-Za-z_][A-Za-z0-9_]*)\s*:\s*"
        r"(?:(in|out|in\s+out)\s+)?"
        r"(?:(event\s+data|event|data)\s+)?port\s*([^;{]*)\s*;"
    )
    features: list[Feature] = []
    for match in pattern.finditer(feature_section):
        name = match.group(1)
        direction = re.sub(r"\s+", " ", (match.group(2) or "")).strip() or "in out"
        category = re.sub(r"\s+", " ", (match.group(3) or "data")).strip()
        aadl_type = re.sub(r"\s+", " ", (match.group(4) or "")).strip()
        features.append(
            Feature(
                name=name,
                direction=direction,
                category=category,
                aadl_type=aadl_type,
                scalar=infer_scalar(aadl_type, category),
            )
        )
    return features


def extract_component_type_block(aadl_text: str, component: str) -> str:
    if not component:
        return ""
    kind = r"(?:system|process|thread|device|abstract|subprogram|data|bus|memory|processor)"
    start_re = re.compile(rf"(?im)^\s*{kind}\s+{re.escape(component)}\b.*$")
    match = start_re.search(aadl_text)
    if not match:
        return ""
    end_re = re.compile(rf"(?im)^\s*end\s+{re.escape(component)}\s*;")
    end = end_re.search(aadl_text, match.end())
    if not end:
        return ""
    return aadl_text[match.start() : end.end()]


def extract_section(block: str, section_name: str) -> str:
    section_re = re.compile(
        rf"(?ims)^\s*{re.escape(section_name)}\s*$"
        r"(.*?)(?=^\s*(?:features|subcomponents|connections|flows|properties|modes|calls|annex|end\b)\s*)"
    )
    match = section_re.search(block)
    return match.group(1) if match else ""


def infer_scalar(aadl_type: str, category: str) -> str:
    text = f"{aadl_type} {category}".lower()
    if "boolean" in text or re.search(r"\bbool\b", text):
        return "bool"
    if any(token in text for token in ["integer", "int", "float", "real", "double", "base_types::integer", "base_types::float"]):
        return "numeric"
    if "event" in category.lower() and not aadl_type:
        return "event"
    return "opaque"


def synthesize_requirement(component: str, features: list[Feature]) -> tuple[bool, str, str, str, list[str]]:
    runtime_features = [feature for feature in features if feature.category.lower() == "data"]
    event_features = [feature for feature in features if "event" in feature.category.lower()]
    inputs = [feature for feature in runtime_features if feature.direction.startswith("in")]
    outputs = [feature for feature in runtime_features if feature.direction.startswith("out")]
    bool_inputs = [feature for feature in inputs if feature.scalar == "bool"]
    bool_outputs = [feature for feature in outputs if feature.scalar == "bool"]
    numeric_inputs = [feature for feature in inputs if feature.scalar == "numeric"]
    numeric_outputs = [feature for feature in outputs if feature.scalar == "numeric"]

    if bool_inputs and bool_outputs:
        source = bool_inputs[0]
        target = bool_outputs[0]
        requirement = (
            f"For component {component}, whenever input {source.name} is true, "
            f"output {target.name} shall be true."
        )
        agree = f'guarantee "{target.name} follows {source.name}": {source.name} => {target.name};'
        trace_refs = [component, source.name, target.name]
        return True, "bool input to bool output implication over visible symbols", requirement, agree, trace_refs

    if numeric_inputs and numeric_outputs:
        source = numeric_inputs[0]
        target = numeric_outputs[0]
        requirement = f"For component {component}, output {target.name} shall equal input {source.name}."
        agree = f'guarantee "{target.name} equals {source.name}": {target.name} = {source.name};'
        trace_refs = [component, source.name, target.name]
        return True, "numeric input to numeric output equality over visible symbols", requirement, agree, trace_refs

    if len(numeric_inputs) >= 2 and numeric_outputs:
        left, right = numeric_inputs[0], numeric_inputs[1]
        target = numeric_outputs[0]
        requirement = f"For component {component}, output {target.name} shall equal the sum of inputs {left.name} and {right.name}."
        agree = f'guarantee "{target.name} sums inputs": {target.name} = {left.name} + {right.name};'
        trace_refs = [component, left.name, right.name, target.name]
        return True, "numeric sum relation over visible symbols", requirement, agree, trace_refs

    if numeric_inputs and bool_outputs:
        source = numeric_inputs[0]
        target = bool_outputs[0]
        requirement = (
            f"For component {component}, output {target.name} shall be true "
            f"whenever input {source.name} is greater than zero."
        )
        agree = f'guarantee "{target.name} follows positive {source.name}": {source.name} > 0 => {target.name};'
        trace_refs = [component, source.name, target.name]
        return True, "numeric threshold to bool output implication over visible symbols", requirement, agree, trace_refs

    reason = "no clear visible bool/numeric input-output relation could be formed"
    if not outputs:
        reason = "target type exposes no visible output port"
    elif not inputs:
        reason = "target type exposes output ports but no visible input ports"
    elif event_features and not runtime_features:
        reason = "visible ports are event/event-data only; avoid treating event ports as AGREE values"
    elif all(feature.scalar in {"opaque", "event"} for feature in runtime_features):
        reason = "visible ports are opaque/event-only; avoid type-validity or connection pseudo-contracts"
    return False, reason, "", "", [component] if component else []


def build_quality_checks(selected: bool, requirement: str, trace_refs: list[str]) -> dict[str, bool]:
    text = requirement.lower()
    vague_terms = [
        "valid",
        "correct",
        "appropriate",
        "normal operation",
        "legal boundary",
        "robust",
        "safe",
        "consistent",
    ]
    return {
        "atomic": not selected or requirement.count(".") <= 1,
        "uses_shall": not selected or " shall " in f" {text} ",
        "traceable": bool(trace_refs),
        "scope_bounded": not selected or all(ref and "::" not in ref for ref in trace_refs[1:]),
        "unambiguous": not selected or not any(term in text for term in vague_terms),
        "verifiable": selected,
        "old_requirement_used": False,
    }


def write_csv(path: Path, candidates: list[CaseCandidate]) -> None:
    fields = [
        "case_num",
        "letter",
        "label",
        "target",
        "selected",
        "source_type",
        "requirement_class",
        "expected_output_type",
        "reason",
        "trace_refs",
        "natural_requirement",
        "expected_agree",
        "req_path",
    ]
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for item in candidates:
            row = asdict(item)
            clean_row = {field: row.get(field, "") for field in fields}
            clean_row["trace_refs"] = json.dumps(row.get("trace_refs", []), ensure_ascii=False)
            writer.writerow(clean_row)


def create_curated_source_root(source_root: Path, curated_root: Path, candidates: list[CaseCandidate]) -> None:
    curated_root.mkdir(parents=True, exist_ok=True)
    selected = [item for item in candidates if item.selected]
    selected_labels = {item.label for item in selected}
    for item in selected:
        src_dir = source_root / item.label
        dst_dir = curated_root / item.label
        if dst_dir.exists():
            shutil.rmtree(dst_dir)
        shutil.copytree(src_dir, dst_dir)
        req_path = dst_dir / Path(item.req_path).name
        req_path.write_text(item.natural_requirement.strip() + "\n", encoding="utf-8")
        sidecar = dst_dir / f"{Path(item.req_path).stem}_Expected_AGREE.json"
        sidecar.write_text(
            json.dumps(
                {
                    "source_type": item.source_type,
                    "requirement_class": item.requirement_class,
                    "expected_output_type": item.expected_output_type,
                    "natural_requirement": item.natural_requirement,
                    "expected_agree": item.expected_agree,
                    "trace_refs": item.trace_refs,
                    "visible_symbols": item.visible_symbols,
                    "quality_checks": item.quality_checks,
                    "selection_reason": item.reason,
                    "old_requirement_used": False,
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
    source_map = source_root / "Case_Source_Map.csv"
    if source_map.exists():
        rows = load_source_map(source_map)
        with (curated_root / "Case_Source_Map.csv").open("w", encoding="utf-8-sig", newline="") as handle:
            if rows:
                writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
                writer.writeheader()
                for row in rows:
                    case_num = int(row["Case"])
                    if f"Case{case_num:02d}_A" in selected_labels or f"Case{case_num:02d}_B" in selected_labels:
                        writer.writerow(row)
    dataset_readme = [
        "# Curated AGREE-Oriented Source Requirements",
        "",
        "This source root contains only selected AADL cases whose natural-language",
        "requirements were rebuilt from the AADL architecture rather than copied or",
        "edited from the previous generated requirements.",
        "",
        "## Construction Principles",
        "",
        "- AADL models are unchanged.",
        "- Requirements are architecture-grounded synthetic requirements.",
        "- Each selected requirement is atomic, traceable, scope-bounded, and AGREE-generatable.",
        "- Event/event-data-only ports, opaque type-validity claims, connection consistency claims, and AADL property claims are excluded from this main generatable subset.",
        "- Each case includes a `*_Expected_AGREE.json` sidecar with trace refs, expected AGREE, and quality checks.",
        "",
        "## Intended Use",
        "",
        "Use this subset to evaluate NL-to-AGREE generation on requirements that are",
        "explicitly expressible over visible target-interface runtime symbols.",
    ]
    (curated_root / "DATASET_README.md").write_text("\n".join(dataset_readme) + "\n", encoding="utf-8")


def write_summary(
    run_root: Path,
    candidates: list[CaseCandidate],
    write_mode: bool,
    backup_root: Path | None,
    curated_root: Path | None,
) -> None:
    selected = [item for item in candidates if item.selected]
    skipped = [item for item in candidates if not item.selected]
    reason_counts: dict[str, int] = {}
    for item in skipped:
        reason_counts[item.reason] = reason_counts.get(item.reason, 0) + 1
    lines = [
        "# AGREE-Oriented Source Requirement Rebuild",
        "",
        f"- Considered: {len(candidates)}",
        f"- Selected generatable: {len(selected)}",
        f"- Not selected: {len(skipped)}",
        f"- Write mode: {write_mode}",
    ]
    if backup_root is not None:
        lines.append(f"- Backup root: {backup_root}")
    if curated_root is not None:
        lines.append(f"- Curated source root: {curated_root}")
    lines.extend(["", "## Selection Policy", ""])
    lines.extend(
        [
            "- Keep AADL models unchanged.",
            "- Ignore old requirement wording when generating clean requirements.",
            "- Treat the selected subset as architecture-grounded synthetic requirements, not industrial requirements.",
            "- Require trace_refs and an expected_output_type for every selected item.",
            "- Select only requirements expressible over visible bool/numeric target-interface symbols.",
            "- Do not generate requirements from opaque type-validity, connection consistency, or AADL properties.",
            "- Exclude event/event-data-only ports from the main AGREE-generatable subset.",
            "- Do not force the final dataset size to match the old 800+ cases.",
        ]
    )
    lines.extend(["", "## Not Selected Reasons", ""])
    for reason, count in sorted(reason_counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- {count}: {reason}")
    lines.extend(["", "## Selected Cases", ""])
    for item in selected[:200]:
        lines.append(f"- {item.label} target={item.target}: {item.natural_requirement}")
    if len(selected) > 200:
        lines.append(f"- ... {len(selected) - 200} more selected cases omitted from summary.")
    (run_root / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
