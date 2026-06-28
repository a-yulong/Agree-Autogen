"""Generate fresh high-quality requirements directly from AADL library models.

The generator intentionally ignores the old `Exp_Data/Sources` requirements.
It scans AADL library files, extracts component type interfaces, and creates
architecture-grounded synthetic requirements that follow requirement-writing
quality principles: atomic, shall-based, traceable, unambiguous, verifiable, and
bounded to visible component interfaces.

No external LLM is called.  The requirement wording is produced by deterministic
templates chosen from the extracted AADL facts.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


DEFAULT_AADL_ROOT = Path(r"D:\AADL_Lib_workspace\AADLib_Test")
DEFAULT_OUTPUT_ROOT = Path(r"C:\Users\25780\Desktop\Exp_Data\Sources_AADLLib_Generated_20260601")


COMPONENT_KIND_RE = r"(system|process|thread|device|abstract|subprogram)"


@dataclass(frozen=True)
class Feature:
    owner: str
    name: str
    direction: str
    category: str
    aadl_type: str
    scalar: str


@dataclass(frozen=True)
class GeneratedRequirement:
    case_num: int
    label: str
    source_file: str
    package: str
    component_kind: str
    target: str
    requirement: str
    requirement_class: str
    expected_output_type: str
    expected_agree: str
    requirement_items: list[dict[str, str]]
    expected_agree_clauses: list[str]
    trace_refs: list[str]
    visible_symbols: list[dict[str, str]]
    quality_checks: dict[str, bool]
    generation_pattern: str


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate fresh requirements from an AADL library.")
    parser.add_argument("--aadl-root", default=str(DEFAULT_AADL_ROOT))
    parser.add_argument("--output-root", default=str(DEFAULT_OUTPUT_ROOT))
    parser.add_argument("--start-case", type=int, default=1000)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--include-src", action="store_true", help="Also scan src/ library files, not only examples/.")
    parser.add_argument(
        "--expanded",
        action="store_true",
        help="Create multiple high-quality requirement scenarios per AGREE-capable component.",
    )
    args = parser.parse_args()

    aadl_root = Path(args.aadl_root)
    output_root = Path(args.output_root)
    if output_root.exists():
        shutil.rmtree(output_root)
    output_root.mkdir(parents=True, exist_ok=True)

    files = discover_aadl_files(aadl_root, include_src=args.include_src)
    all_text = "\n\n".join(path.read_text(encoding="utf-8", errors="replace") for path in files)
    scalar_map = build_data_scalar_map(all_text)

    requirements: list[GeneratedRequirement] = []
    case_num = args.start_case
    for file_path in files:
        text = file_path.read_text(encoding="utf-8", errors="replace")
        package = extract_package_name(text)
        for component in extract_component_types(text):
            features = extract_features(component["block"], component["name"], scalar_map)
            generated_items = choose_requirements(case_num, file_path, package, component, features, expanded=args.expanded)
            for generated in generated_items:
                requirements.append(generated)
                write_case(output_root, generated, file_path)
                case_num += 1
                if args.limit and len(requirements) >= args.limit:
                    break
            if args.limit and len(requirements) >= args.limit:
                break
        if args.limit and len(requirements) >= args.limit:
            break

    write_manifest(output_root, requirements)
    print(f"AADL files scanned: {len(files)}")
    print(f"Generated requirements: {len(requirements)}")
    print(f"Output root: {output_root}")
    print(f"Summary: {output_root / 'DATASET_README.md'}")
    return 0


def discover_aadl_files(root: Path, include_src: bool) -> list[Path]:
    files = []
    for path in root.rglob("*.aadl"):
        rel = path.relative_to(root)
        parts = {part.lower() for part in rel.parts}
        if ".aadlbin-gen" in parts or "support" in parts or "share" in parts:
            continue
        if not include_src and "examples" not in parts:
            continue
        if path.name.lower() in {"emv2.aadl", "deployment.aadl"}:
            continue
        files.append(path)
    return sorted(files, key=lambda p: str(p).lower())


def extract_package_name(text: str) -> str:
    match = re.search(r"(?im)^\s*package\s+([A-Za-z_][A-Za-z0-9_:]*)\b", text or "")
    return match.group(1) if match else ""


def extract_component_types(text: str) -> list[dict[str, str]]:
    pattern = re.compile(
        rf"(?ims)^\s*{COMPONENT_KIND_RE}\s+(?!implementation\b)([A-Za-z_][A-Za-z0-9_]*)\b.*?^\s*end\s+\2\s*;",
        re.MULTILINE | re.DOTALL,
    )
    components = []
    for match in pattern.finditer(text or ""):
        block = match.group(0)
        if re.search(r"(?im)^\s*features\s*$", block):
            components.append({"kind": match.group(1), "name": match.group(2), "block": block})
    return components


def extract_features(block: str, owner: str, scalar_map: dict[str, str]) -> list[Feature]:
    section = extract_section(block, "features")
    if not section:
        return []
    pattern = re.compile(
        r"(?im)^\s*([A-Za-z_][A-Za-z0-9_]*)\s*:\s*"
        r"(?:(in|out|in\s+out)\s+)?"
        r"(?:(event\s+data|event|data)\s+)?port\s*([^;{]*)\s*;"
    )
    features: list[Feature] = []
    for match in pattern.finditer(section):
        name = match.group(1)
        direction = re.sub(r"\s+", " ", (match.group(2) or "")).strip() or "in out"
        category = re.sub(r"\s+", " ", (match.group(3) or "data")).strip().lower()
        aadl_type = re.sub(r"\s+", " ", (match.group(4) or "")).strip()
        features.append(
            Feature(
                owner=owner,
                name=name,
                direction=direction,
                category=category,
                aadl_type=aadl_type,
                scalar=infer_scalar(aadl_type, category, scalar_map),
            )
        )
    return features


def extract_section(block: str, section_name: str) -> str:
    section_re = re.compile(
        rf"(?ims)^\s*{re.escape(section_name)}\s*$"
        r"(.*?)(?=^\s*(?:features|subcomponents|connections|flows|properties|modes|calls|annex|end\b)\s*)"
    )
    match = section_re.search(block)
    return match.group(1) if match else ""


def build_data_scalar_map(text: str) -> dict[str, str]:
    mapping: dict[str, str] = {}
    package = ""
    for line in (text or "").splitlines():
        package_match = re.match(r"(?i)^\s*package\s+([A-Za-z_][A-Za-z0-9_:]*)\b", line)
        if package_match:
            package = package_match.group(1)
        data_match = re.match(r"(?i)^\s*data\s+([A-Za-z_][A-Za-z0-9_:]*)\b", line)
        if data_match:
            name = data_match.group(1)
            scalar = infer_scalar_from_name(name)
            mapping[name.lower()] = scalar
            if package and "::" not in name:
                mapping[f"{package}::{name}".lower()] = scalar
    for match in re.finditer(
        r"(?ims)^\s*data\s+([A-Za-z_][A-Za-z0-9_:]*)\b(.*?)(?:^\s*end\s+\1\s*;)",
        text or "",
    ):
        name = match.group(1)
        body = match.group(2)
        rep_match = re.search(
            r"Data_Model::(?:Data_Representation|Representation)\s*=>\s*(?:\(\s*)?[\"']?([A-Za-z_][A-Za-z0-9_\s]*)",
            body,
            flags=re.IGNORECASE,
        )
        rep = re.sub(r"\s+", " ", rep_match.group(1).strip().lower()) if rep_match else ""
        scalar = {
            "boolean": "bool",
            "bool": "bool",
            "float": "real",
            "real": "real",
            "fixed": "real",
            "double": "real",
            "integer": "int",
            "int": "int",
            "unsigned int": "int",
            "signed int": "int",
            "short": "int",
            "long": "int",
        }.get(rep) or infer_scalar_from_name(name)
        mapping[name.lower()] = scalar
    return mapping


def infer_scalar(aadl_type: str, category: str, scalar_map: dict[str, str]) -> str:
    if "event" in category:
        return "event"
    key = (aadl_type or "").lower()
    tail = re.split(r"::|\.", key)[-1]
    return scalar_map.get(key) or scalar_map.get(tail) or infer_scalar_from_name(aadl_type)


def infer_scalar_from_name(name: str) -> str:
    text = (name or "").lower()
    if any(token in text for token in ["boolean", "bool"]):
        return "bool"
    if any(token in text for token in ["float", "double", "real"]):
        return "real"
    if re.search(r"\b(int|integer|counter|count|number|index|id)\b", text):
        return "int"
    return "opaque"


def choose_requirements(
    case_num: int,
    file_path: Path,
    package: str,
    component: dict[str, str],
    features: list[Feature],
    expanded: bool,
) -> list[GeneratedRequirement]:
    spec = build_requirement_spec(component, features)
    if spec is None:
        return []
    if not expanded:
        return [
            make_generated_requirement(
                case_num,
                file_path,
                package,
                component,
                features,
                spec["items"],
                spec["clauses"],
                spec["refs"],
                spec["patterns"],
            )
        ]
    scenarios = split_scenarios(spec["items"])
    generated: list[GeneratedRequirement] = []
    for offset, scenario in enumerate(scenarios):
        refs = [component["name"]]
        patterns = []
        clauses = []
        for item in scenario:
            patterns.append(item["pattern"])
            clauses.append(item["expected_agree"])
            for ref in item.get("trace_refs", []):
                if ref not in refs:
                    refs.append(ref)
        generated.append(
            make_generated_requirement(
                case_num + offset,
                file_path,
                package,
                component,
                features,
                scenario,
                clauses,
                refs,
                patterns,
            )
        )
    return generated


def build_requirement_spec(component: dict[str, str], features: list[Feature]) -> dict[str, Any] | None:
    runtime = [feature for feature in features if feature.category == "data" and feature.scalar in {"bool", "int", "real"}]
    inputs = [feature for feature in runtime if feature.direction.startswith("in")]
    outputs = [feature for feature in runtime if feature.direction.startswith("out")]
    bool_inputs = [feature for feature in inputs if feature.scalar == "bool"]
    bool_outputs = [feature for feature in outputs if feature.scalar == "bool"]
    numeric_inputs = [feature for feature in inputs if feature.scalar in {"int", "real"}]
    numeric_outputs = [feature for feature in outputs if feature.scalar in {"int", "real"}]

    target = component["name"]
    patterns: list[str] = []
    items: list[dict[str, str]] = []
    clauses: list[str] = []
    refs: list[str] = [target]

    for source, dest in matching_pairs(numeric_inputs, numeric_outputs)[:3]:
        text = (
            f"The {target} {component['kind']} component shall guarantee that output {dest.name} "
            f"is consistent with input {source.name} by setting {dest.name} equal to {source.name}."
        )
        clause = f'guarantee "{dest.name} equals {source.name}": {dest.name} = {source.name};'
        add_item(items, clauses, refs, "numeric_interface_equality", text, clause, [source.name, dest.name])
        patterns.append("numeric_interface_equality")

    for source, dest in matching_pairs(bool_inputs, bool_outputs)[:4]:
        text = (
            f"The {target} {component['kind']} component shall guarantee that output {dest.name} "
            f"is asserted whenever input {source.name} is true."
        )
        clause = f'guarantee "{dest.name} follows {source.name}": {source.name} => {dest.name};'
        add_item(items, clauses, refs, "boolean_implication", text, clause, [source.name, dest.name])
        patterns.append("boolean_implication")

    if numeric_inputs and bool_outputs and len(items) < 6:
        for source in numeric_inputs[:2]:
            dest = bool_outputs[0]
            text = (
                f"The {target} {component['kind']} component shall guarantee that output {dest.name} "
                f"is asserted whenever input {source.name} is greater than zero."
            )
            clause = f'guarantee "{dest.name} follows positive {source.name}": {source.name} > 0 => {dest.name};'
            add_item(items, clauses, refs, "numeric_threshold_boolean", text, clause, [source.name, dest.name])
            patterns.append("numeric_threshold_boolean")

    if numeric_inputs and len(items) < 6:
        for source in numeric_inputs[: min(2, 6 - len(items))]:
            lower, upper = numeric_bounds_for(source)
            text = (
                f"The {target} {component['kind']} component shall establish an input assumption "
                f"that {source.name} remains between {lower} and {upper}."
            )
            clause = f'assume "{source.name} input range": {source.name} >= {lower} and {source.name} <= {upper};'
            add_item(items, clauses, refs, "numeric_input_assumption", text, clause, [source.name])
            patterns.append("numeric_input_assumption")

    if numeric_outputs and len(items) < 6:
        for dest in numeric_outputs[: min(2, 6 - len(items))]:
            lower, upper = numeric_bounds_for(dest)
            text = (
                f"The {target} {component['kind']} component shall guarantee that output {dest.name} "
                f"remains between {lower} and {upper}."
            )
            clause = f'guarantee "{dest.name} output range": {dest.name} >= {lower} and {dest.name} <= {upper};'
            add_item(items, clauses, refs, "numeric_output_range", text, clause, [dest.name])
            patterns.append("numeric_output_range")

    if not items:
        return None

    return {"items": items, "clauses": clauses, "refs": refs, "patterns": patterns}


def make_generated_requirement(
    case_num: int,
    file_path: Path,
    package: str,
    component: dict[str, str],
    features: list[Feature],
    items: list[dict[str, Any]],
    clauses: list[str],
    refs: list[str],
    patterns: list[str],
) -> GeneratedRequirement:
    target = component["name"]
    requirement = " ".join(item["text"] for item in items)
    expected = "\n".join(clauses)
    label = f"Case{case_num}_A"
    visible = [asdict(feature) for feature in features]
    return GeneratedRequirement(
        case_num=case_num,
        label=label,
        source_file=str(file_path),
        package=package,
        component_kind=component["kind"],
        target=target,
        requirement=requirement,
        requirement_class="generatable",
        expected_output_type="agree_annex",
        expected_agree=expected,
        requirement_items=items,
        expected_agree_clauses=clauses,
        trace_refs=refs,
        visible_symbols=visible,
        quality_checks=quality_checks(requirement, refs),
        generation_pattern="+".join(dict.fromkeys(patterns)),
    )


def split_scenarios(items: list[dict[str, Any]]) -> list[list[dict[str, Any]]]:
    scenarios: list[list[dict[str, Any]]] = []
    grouped: dict[str, list[dict[str, Any]]] = {}
    for item in items:
        grouped.setdefault(str(item.get("pattern", "")), []).append(item)
    for pattern in [
        "numeric_interface_equality",
        "boolean_implication",
        "numeric_threshold_boolean",
        "numeric_input_assumption",
        "numeric_output_range",
    ]:
        group = grouped.get(pattern, [])
        for index in range(0, len(group), 2):
            scenarios.append(group[index : index + 2])
    return [scenario for scenario in scenarios if scenario]


def add_item(
    items: list[dict[str, str]],
    clauses: list[str],
    refs: list[str],
    pattern: str,
    text: str,
    clause: str,
    item_refs: list[str],
) -> None:
    if text in {item["text"] for item in items}:
        return
    req_id = f"R{len(items) + 1}"
    items.append({"id": req_id, "pattern": pattern, "text": text, "expected_agree": clause, "trace_refs": item_refs})
    clauses.append(clause)
    for ref in item_refs:
        if ref not in refs:
            refs.append(ref)


def matching_pairs(inputs: list[Feature], outputs: list[Feature]) -> list[tuple[Feature, Feature]]:
    pairs: list[tuple[Feature, Feature]] = []
    used_inputs: set[str] = set()
    used_outputs: set[str] = set()
    for output in outputs:
        output_key = normalize_signal_name(output.name)
        for input_ in inputs:
            if input_.name in used_inputs or output.name in used_outputs:
                continue
            input_key = normalize_signal_name(input_.name)
            if output_key and input_key and output_key == input_key:
                pairs.append((input_, output))
                used_inputs.add(input_.name)
                used_outputs.add(output.name)
                break
    for input_, output in zip(inputs, outputs):
        if input_.name not in used_inputs and output.name not in used_outputs:
            pairs.append((input_, output))
            used_inputs.add(input_.name)
            used_outputs.add(output.name)
    return pairs


def numeric_bounds_for(feature: Feature) -> tuple[str, str]:
    return ("0", "100") if feature.scalar == "int" else ("0.0", "100.0")


def normalize_signal_name(name: str) -> str:
    text = (name or "").lower()
    text = re.sub(r"(^|_)(in|input|out|output|data|cmd|command|request|req|resp|response)($|_)", "_", text)
    text = re.sub(r"(^|_)(from|to)($|_)", "_", text)
    text = re.sub(r"[^a-z0-9]+", "_", text).strip("_")
    return text


def quality_checks(requirement: str, trace_refs: list[str]) -> dict[str, bool]:
    text = requirement.lower()
    vague_terms = ["valid", "correct", "appropriate", "normal operation", "legal", "robust", "safe"]
    return {
        "atomic": all(line.count(".") <= 1 for line in requirement.splitlines() if line.strip()),
        "uses_shall": " shall " in f" {text} ",
        "traceable": bool(trace_refs),
        "scope_bounded": True,
        "unambiguous": not any(term in text for term in vague_terms),
        "verifiable": True,
        "old_requirement_used": False,
    }


def write_case(output_root: Path, req: GeneratedRequirement, source_file: Path) -> None:
    case_dir = output_root / req.label
    case_dir.mkdir(parents=True, exist_ok=True)
    case_name = f"Case{req.case_num}"
    source_text = source_file.read_text(encoding="utf-8", errors="replace")
    (case_dir / f"{case_name}_Base.aadl").write_text(source_text, encoding="utf-8")
    (case_dir / f"{case_name}_Base.txt").write_text(source_text, encoding="utf-8")
    (case_dir / f"{case_name}_Req.txt").write_text(req.requirement + "\n", encoding="utf-8")
    sidecar = {
        "source_type": "aadl_lib_synthetic",
        "source_file": req.source_file,
        "package": req.package,
        "component_kind": req.component_kind,
        "target": req.target,
        "requirement_class": req.requirement_class,
        "expected_output_type": req.expected_output_type,
        "natural_requirement": req.requirement,
        "expected_agree": req.expected_agree,
        "requirement_items": req.requirement_items,
        "expected_agree_clauses": req.expected_agree_clauses,
        "trace_refs": req.trace_refs,
        "visible_symbols": req.visible_symbols,
        "quality_checks": req.quality_checks,
        "generation_pattern": req.generation_pattern,
        "old_requirement_used": False,
    }
    (case_dir / f"{case_name}_Req_Expected_AGREE.json").write_text(
        json.dumps(sidecar, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    ref_dir = case_dir / case_name
    ref_dir.mkdir(parents=True, exist_ok=True)
    for sibling in source_file.parent.glob("*.aadl"):
        if sibling.resolve() == source_file.resolve():
            continue
        shutil.copy2(sibling, ref_dir / sibling.name)


def write_manifest(output_root: Path, requirements: list[GeneratedRequirement]) -> None:
    manifest_json = [asdict(item) for item in requirements]
    (output_root / "manifest.json").write_text(json.dumps(manifest_json, ensure_ascii=False, indent=2), encoding="utf-8")
    fields = [
        "case_num",
        "label",
        "source_file",
        "package",
        "component_kind",
        "target",
        "requirement_class",
        "expected_output_type",
        "generation_pattern",
        "requirement",
        "expected_agree",
        "trace_refs",
    ]
    with (output_root / "manifest.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for item in requirements:
            row = asdict(item)
            row["trace_refs"] = json.dumps(row["trace_refs"], ensure_ascii=False)
            writer.writerow({field: row.get(field, "") for field in fields})
    with (output_root / "Case_Source_Map.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["Case", "Source", "Package", "Kind", "Target", "Features", "ReqChars", "Dependencies"])
        writer.writeheader()
        for item in requirements:
            writer.writerow(
                {
                    "Case": item.case_num,
                    "Source": item.source_file,
                    "Package": item.package,
                    "Kind": item.component_kind,
                    "Target": item.target,
                    "Features": len(item.visible_symbols),
                    "ReqChars": len(item.requirement),
                    "Dependencies": "",
                }
            )
    readme = [
        "# AADL-Lib Synthetic Requirement Dataset",
        "",
        "This dataset was freshly generated from AADL library models. It does not use",
        "previous generated requirements as input.",
        "",
        "## Quality Principles",
        "",
        "- Atomic: one requirement states one relation.",
        "- Shall-based: each requirement uses normative `shall` wording.",
        "- Traceable: each requirement records the source component and ports.",
        "- Scope-bounded: generated AGREE uses only visible component type interface symbols.",
        "- Unambiguous: templates avoid vague terms such as valid, correct, safe, or normal operation.",
        "- Verifiable: each selected requirement includes an expected AGREE guarantee.",
        "",
        "These principles are aligned with common requirements-engineering guidance",
        "such as atomicity, unambiguity, traceability, and verifiability.",
        "",
        f"- Generated requirements: {len(requirements)}",
        "- Source type: aadl_lib_synthetic",
    ]
    (output_root / "DATASET_README.md").write_text("\n".join(readme) + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
