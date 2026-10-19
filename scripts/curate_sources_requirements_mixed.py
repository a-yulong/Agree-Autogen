"""Curate old Sources requirements into clear, verifiable requirements.

This script starts from the existing Exp_Data/Sources directory, keeps old
requirements that are already precise, and rebuilds vague requirements from the
case AADL model when a clear verification target can be identified.

The output is a new Sources-like root. AADL files are copied unchanged.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


DEFAULT_SOURCE_ROOT = Path(r"C:\Users\25780\Desktop\Exp_Data\Sources")
DEFAULT_OUTPUT_ROOT = Path(r"C:\Users\25780\Desktop\Exp_Data\Sources_Curated_Mixed_20260601")
DEFAULT_REPORT_ROOT = Path(r"C:\Users\25780\Desktop\Exp_Data\SourceReq_Curated_Mixed")


VAGUE_TERMS = [
    "valid",
    "correct",
    "appropriate",
    "normal operation",
    "legal operational",
    "legal boundary",
    "legal boundaries",
    "assumed environmental",
    "environmental conditions",
    "input constraints",
    "communication envelope",
    "consistency",
    "consistent",
    "robust",
    "integrity",
    "safe",
    "proper",
    "suitable",
]


@dataclass(frozen=True)
class Feature:
    owner: str
    name: str
    direction: str
    category: str
    aadl_type: str
    scalar: str


@dataclass(frozen=True)
class Connection:
    owner: str
    name: str
    kind: str
    source: str
    destination: str
    properties: list[dict[str, str]]


@dataclass(frozen=True)
class PropertyAssignment:
    owner: str
    owner_kind: str
    name: str
    value: str
    element: str = ""


@dataclass(frozen=True)
class RequirementItem:
    text: str
    requirement_class: str
    expected_output_type: str
    trace_refs: list[str]
    expected_agree: str = ""
    expected_check: dict[str, Any] | None = None
    origin: str = "rebuilt"


@dataclass(frozen=True)
class CaseResult:
    case_num: int
    letter: str
    label: str
    target: str
    selected: bool
    action: str
    reason: str
    old_quality: str
    old_req_path: str
    base_path: str
    output_dir: str
    requirement_count: int
    classes: dict[str, int]
    items: list[RequirementItem]


def main() -> int:
    parser = argparse.ArgumentParser(description="Curate Sources into clear mixed-verification requirements.")
    parser.add_argument("--source-root", default=str(DEFAULT_SOURCE_ROOT))
    parser.add_argument("--output-root", default=str(DEFAULT_OUTPUT_ROOT))
    parser.add_argument("--report-root", default=str(DEFAULT_REPORT_ROOT))
    parser.add_argument("--cases", default="", help="Comma-separated case numbers or ranges.")
    parser.add_argument("--letters", default="A,B")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--max-items-per-case", type=int, default=6)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    source_root = Path(args.source_root)
    output_root = Path(args.output_root)
    report_root = Path(args.report_root) / f"curate_mixed_{time.strftime('%Y%m%d_%H%M%S')}"
    report_root.mkdir(parents=True, exist_ok=True)
    if output_root.exists():
        if not args.force:
            raise RuntimeError(f"Output root already exists: {output_root}. Use --force to replace it.")
        shutil.rmtree(output_root)
    output_root.mkdir(parents=True, exist_ok=True)

    source_map_by_case = load_source_map(source_root / "Case_Source_Map.csv")
    cases = discover_cases(source_root, parse_cases(args.cases), parse_letters(args.letters))
    if args.limit:
        cases = cases[: args.limit]

    results: list[CaseResult] = []
    for index, case in enumerate(cases, 1):
        label, case_num, letter, req_path, base_path = case
        print(f"[{index}/{len(cases)}] {label}", flush=True)
        old_req = req_path.read_text(encoding="utf-8", errors="replace").strip()
        aadl_text = base_path.read_text(encoding="utf-8", errors="replace")
        map_row = source_map_by_case.get(case_num, {})
        target = map_row.get("Target", "").strip() or infer_target_from_requirement(old_req, aadl_text)
        result = curate_case(
            source_root=source_root,
            output_root=output_root,
            label=label,
            case_num=case_num,
            letter=letter,
            req_path=req_path,
            base_path=base_path,
            old_req=old_req,
            aadl_text=aadl_text,
            target=target,
            max_items=args.max_items_per_case,
        )
        results.append(result)

    write_root_metadata(source_root, output_root, results, source_map_by_case)
    write_report(report_root, output_root, results)
    print(f"Considered: {len(results)}")
    print(f"Selected: {sum(1 for item in results if item.selected)}")
    print(f"Output root: {output_root}")
    print(f"Report: {report_root / 'summary.md'}")
    return 0


def parse_cases(text: str) -> set[int] | None:
    text = (text or "").strip()
    if not text:
        return None
    values: set[int] = set()
    for part in text.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start, end = part.split("-", 1)
            values.update(range(int(start), int(end) + 1))
        else:
            values.add(int(part))
    return values


def parse_letters(text: str) -> set[str]:
    return {part.strip().upper() for part in text.split(",") if part.strip()} or {"A", "B"}


def natural_key(text: str) -> list[Any]:
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", text)]


def discover_cases(
    source_root: Path,
    case_filter: set[int] | None,
    letters: set[str],
) -> list[tuple[str, int, str, Path, Path]]:
    cases: list[tuple[str, int, str, Path, Path]] = []
    for case_dir in sorted(source_root.iterdir(), key=lambda p: natural_key(p.name)):
        if not case_dir.is_dir():
            continue
        match = re.fullmatch(r"Case(\d+)_([A-Z])", case_dir.name, flags=re.IGNORECASE)
        if not match:
            continue
        case_num = int(match.group(1))
        letter = match.group(2).upper()
        if case_filter is not None and case_num not in case_filter:
            continue
        if letter not in letters:
            continue
        case_label = f"Case{case_num:02d}"
        req_path = case_dir / f"{case_label}_Req.txt"
        base_path = case_dir / f"{case_label}_Base.aadl"
        if not base_path.exists():
            base_path = case_dir / f"{case_label}_Base.txt"
        if req_path.exists() and base_path.exists():
            cases.append((case_dir.name, case_num, letter, req_path, base_path))
    return cases


def load_source_map(path: Path) -> dict[int, dict[str, str]]:
    if not path.exists():
        return {}
    rows: dict[int, dict[str, str]] = {}
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            if row.get("Case", "").isdigit():
                rows[int(row["Case"])] = row
    return rows


def infer_target_from_requirement(old_req: str, aadl_text: str) -> str:
    patterns = [
        r"\b(?:component|system|process|thread|device)\s+([A-Za-z_][A-Za-z0-9_.]*)\b",
        r"\bthe\s+([A-Za-z_][A-Za-z0-9_.]*)\s+component\b",
        r"\bFor\s+component\s+([A-Za-z_][A-Za-z0-9_.]*)\b",
        r"\bWhen\s+the\s+([A-Za-z_][A-Za-z0-9_.]*)\s+component\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, old_req, flags=re.IGNORECASE)
        if match and extract_component_type_block(aadl_text, strip_punct(match.group(1))):
            return strip_punct(match.group(1))
    candidates = []
    for block_match in re.finditer(
        r"(?ims)^\s*(system|process|thread|device|abstract|subprogram)\s+([A-Za-z_][A-Za-z0-9_]*)\b(.*?)^\s*end\s+\2\s*;",
        aadl_text,
    ):
        name = block_match.group(2)
        features = extract_features_from_block(name, block_match.group(0))
        candidates.append((len(features), name))
    candidates.sort(reverse=True)
    return candidates[0][1] if candidates else ""


def strip_punct(text: str) -> str:
    return text.strip().strip(".,:;")


def curate_case(
    source_root: Path,
    output_root: Path,
    label: str,
    case_num: int,
    letter: str,
    req_path: Path,
    base_path: Path,
    old_req: str,
    aadl_text: str,
    target: str,
    max_items: int,
) -> CaseResult:
    component = target.split(".", 1)[0].strip()
    features = extract_features(aadl_text, component)
    implementation = target if "." in target else find_implementation_name(aadl_text, component)
    connections = extract_connections(aadl_text, implementation) if implementation else []
    properties = extract_properties(aadl_text, implementation, connections) if implementation else []
    old_quality = classify_old_requirement(old_req, features)

    if old_quality == "high_quality":
        items = [
            RequirementItem(
                text=old_req,
                requirement_class="kept_existing_precise",
                expected_output_type="mixed_or_agree",
                trace_refs=[component] + mentioned_feature_names(old_req, features),
                expected_check={"note": "Existing requirement kept because it is explicit and non-vague."},
                origin="kept_existing_high_quality",
            )
        ]
        action = "kept_existing_high_quality"
        reason = "existing requirement is explicit enough"
    else:
        items = build_rebuilt_items(component, implementation, features, connections, properties, max_items=max_items)
        action = "rebuilt_from_aadl" if items else "excluded"
        reason = "rebuilt from clear AADL facts" if items else "no clear AGREE/property/structural target available"

    selected = bool(items)
    output_dir = ""
    if selected:
        src_dir = req_path.parent
        dst_dir = output_root / label
        shutil.copytree(src_dir, dst_dir)
        dst_req = dst_dir / req_path.name
        dst_req.write_text(format_requirement_text(items) + "\n", encoding="utf-8")
        sidecar = dst_dir / f"{req_path.stem}_Expected.json"
        sidecar.write_text(
            json.dumps(
                {
                    "case": case_num,
                    "letter": letter,
                    "target": target,
                    "action": action,
                    "old_quality": old_quality,
                    "source_old_req": old_req,
                    "natural_requirement": format_requirement_text(items),
                    "requirement_items": [item_to_json(item) for item in items],
                    "quality_policy": {
                        "traceable": "Every item has trace_refs and expected_check metadata tied to AADL facts.",
                        "kept_vague_terms_out": VAGUE_TERMS,
                        "principle": "Every generated sentence must name an explicit property assignment or structural connection; ordinary feature declarations are not used as rebuilt requirements.",
                    },
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        output_dir = str(dst_dir)

    classes: dict[str, int] = {}
    for item in items:
        classes[item.requirement_class] = classes.get(item.requirement_class, 0) + 1
    return CaseResult(
        case_num=case_num,
        letter=letter,
        label=label,
        target=target,
        selected=selected,
        action=action,
        reason=reason,
        old_quality=old_quality,
        old_req_path=str(req_path),
        base_path=str(base_path),
        output_dir=output_dir,
        requirement_count=len(items),
        classes=classes,
        items=items,
    )


def classify_old_requirement(old_req: str, features: list[Feature]) -> str:
    text = normalize_space(old_req)
    lower = text.lower()
    if not text:
        return "empty"
    vague_hits = [term for term in VAGUE_TERMS if term in lower]
    explicit_relation = bool(
        re.search(
            r"\b(equals?|equal to|greater than|less than|at least|at most|between|set .* to|shall be true|shall be false|if\b|whenever\b|otherwise\b)",
            lower,
        )
    )
    numeric_or_bool = bool(re.search(r"\b\d+(?:\.\d+)?\b|\btrue\b|\bfalse\b", lower))
    feature_refs = mentioned_feature_names(text, features)
    if explicit_relation and (numeric_or_bool or len(feature_refs) >= 2) and not vague_hits:
        return "high_quality"
    if vague_hits:
        return "vague"
    return "not_enough_explicit_structure"


def mentioned_feature_names(text: str, features: list[Feature]) -> list[str]:
    refs = []
    for feature in features:
        if re.search(rf"\b{re.escape(feature.name)}\b", text):
            refs.append(feature.name)
    return refs


def build_rebuilt_items(
    component: str,
    implementation: str,
    features: list[Feature],
    connections: list[Connection],
    properties: list[PropertyAssignment],
    max_items: int,
) -> list[RequirementItem]:
    items: list[RequirementItem] = []
    items.extend(build_structural_items(implementation, connections, min(2, max_items)))
    remaining = max_items - len(items)
    if remaining > 0:
        items.extend(build_property_items(implementation, properties, remaining))
    return items[:max_items]


def build_structural_items(implementation: str, connections: list[Connection], limit: int) -> list[RequirementItem]:
    items: list[RequirementItem] = []
    if not implementation:
        return items
    for connection in connections:
        items.append(
            RequirementItem(
                text=(
                    f"The {implementation} implementation shall declare connection {connection.name} "
                    f"from {connection.source} to {connection.destination}."
                ),
                requirement_class="structural_check",
                expected_output_type="structural_check",
                trace_refs=[implementation, connection.name, connection.source, connection.destination],
                expected_check={
                    "kind": "connection",
                    "owner": implementation,
                    "connection": connection.name,
                    "source": connection.source,
                    "destination": connection.destination,
                },
            )
        )
        if len(items) >= limit:
            break
    return items


def build_property_items(
    implementation: str,
    properties: list[PropertyAssignment],
    limit: int,
) -> list[RequirementItem]:
    items: list[RequirementItem] = []
    for prop in properties:
        if prop.owner_kind == "connection":
            owner = implementation or prop.owner
            text = (
                f"The {owner} implementation shall assign {prop.name} on connection {prop.element} "
                f"as {prop.value}."
            )
        else:
            text = f"The {prop.owner} {prop.owner_kind} shall assign {prop.name} as {prop.value}."
        items.append(
            RequirementItem(
                text=text,
                requirement_class="property_check",
                expected_output_type="property_check",
                trace_refs=[prop.owner, prop.element, prop.name, prop.value],
                expected_check={
                    "kind": "property",
                    "owner": prop.owner,
                    "owner_kind": prop.owner_kind,
                    "element": prop.element,
                    "property": prop.name,
                    "value": prop.value,
                },
            )
        )
        if len(items) >= limit:
            break
    return items


def dedupe_items(items: list[RequirementItem]) -> list[RequirementItem]:
    seen: set[str] = set()
    deduped: list[RequirementItem] = []
    for item in items:
        key = normalize_space(item.text).lower()
        if key not in seen:
            seen.add(key)
            deduped.append(item)
    return deduped


def extract_features(aadl_text: str, component: str) -> list[Feature]:
    block = extract_component_type_block(aadl_text, component)
    return extract_features_from_block(component, block) if block else []


def extract_features_from_block(owner: str, block: str) -> list[Feature]:
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
        direction = normalize_space(match.group(2) or "in out")
        category = normalize_space(match.group(3) or "data")
        aadl_type = normalize_space(match.group(4) or "")
        features.append(
            Feature(
                owner=owner,
                name=name,
                direction=direction,
                category=category,
                aadl_type=aadl_type,
                scalar=infer_scalar(aadl_type, category),
            )
        )
    return features


def infer_scalar(aadl_type: str, category: str) -> str:
    text = f"{aadl_type} {category}".lower()
    if "boolean" in text or re.search(r"\bbool\b", text):
        return "bool"
    if any(token in text for token in ["integer", "int", "float", "real", "double"]):
        return "numeric"
    if "event" in category.lower():
        return "event"
    return "opaque"


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


def find_implementation_name(aadl_text: str, component: str) -> str:
    if not component:
        return ""
    match = re.search(
        rf"(?im)^\s*(?:system|process|thread|device|abstract|subprogram|processor)\s+implementation\s+({re.escape(component)}\.[A-Za-z_][A-Za-z0-9_]*)\b",
        aadl_text,
    )
    return match.group(1) if match else ""


def extract_implementation_block(aadl_text: str, implementation: str) -> str:
    if not implementation:
        return ""
    kind = r"(?:system|process|thread|device|abstract|subprogram|processor)"
    start_re = re.compile(rf"(?im)^\s*{kind}\s+implementation\s+{re.escape(implementation)}\b.*$")
    match = start_re.search(aadl_text)
    if not match:
        return ""
    end_re = re.compile(rf"(?im)^\s*end\s+{re.escape(implementation)}\s*;")
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


def extract_connections(aadl_text: str, implementation: str) -> list[Connection]:
    block = extract_implementation_block(aadl_text, implementation)
    section = extract_section(block, "connections")
    if not section:
        return []
    pattern = re.compile(
        r"(?ims)^\s*([A-Za-z_][A-Za-z0-9_]*)\s*:\s*"
        r"([A-Za-z][A-Za-z\s]*?)\s+"
        r"([^;{\n]+?)\s*->\s*([^;{\n]+?)"
        r"(?:\s*\{(.*?)\})?\s*;"
    )
    connections: list[Connection] = []
    for match in pattern.finditer(section):
        name = match.group(1)
        kind = normalize_space(match.group(2))
        source = normalize_space(match.group(3))
        destination = normalize_space(match.group(4))
        body = match.group(5) or ""
        props = [
            {"name": prop_name, "value": prop_value}
            for prop_name, prop_value in extract_property_pairs(body)
        ]
        connections.append(
            Connection(
                owner=implementation,
                name=name,
                kind=kind,
                source=source,
                destination=destination,
                properties=props,
            )
        )
    return connections


def extract_properties(
    aadl_text: str,
    implementation: str,
    connections: list[Connection],
) -> list[PropertyAssignment]:
    block = extract_implementation_block(aadl_text, implementation)
    props: list[PropertyAssignment] = []
    for connection in connections:
        for pair in connection.properties:
            props.append(
                PropertyAssignment(
                    owner=implementation,
                    owner_kind="connection",
                    element=connection.name,
                    name=pair["name"],
                    value=pair["value"],
                )
            )
    property_section = extract_section(block, "properties")
    for prop_name, prop_value in extract_property_pairs(property_section):
        props.append(
            PropertyAssignment(
                owner=implementation,
                owner_kind="implementation",
                name=prop_name,
                value=prop_value,
            )
        )
    return props


def extract_property_pairs(text: str) -> list[tuple[str, str]]:
    pairs: list[tuple[str, str]] = []
    pattern = re.compile(r"(?im)([A-Za-z_][A-Za-z0-9_:]*)\s*=>\s*([^;{}]+)\s*;")
    for match in pattern.finditer(text):
        pairs.append((normalize_space(match.group(1)), normalize_space(match.group(2))))
    return pairs


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "")).strip()


def format_requirement_text(items: list[RequirementItem]) -> str:
    return " ".join(normalize_space(item.text).rstrip(".") + "." for item in items)


def item_to_json(item: RequirementItem) -> dict[str, Any]:
    data = asdict(item)
    if data.get("expected_check") is None:
        data["expected_check"] = {}
    return data


def write_root_metadata(
    source_root: Path,
    output_root: Path,
    results: list[CaseResult],
    source_map_by_case: dict[int, dict[str, str]],
) -> None:
    selected_cases = {result.case_num for result in results if result.selected}
    source_map = source_root / "Case_Source_Map.csv"
    if source_map.exists() and source_map_by_case:
        rows = [source_map_by_case[num] for num in sorted(selected_cases) if num in source_map_by_case]
        if rows:
            with (output_root / "Case_Source_Map.csv").open("w", encoding="utf-8-sig", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
                writer.writeheader()
                writer.writerows(rows)

    selected = [result for result in results if result.selected]
    class_counts: dict[str, int] = {}
    action_counts: dict[str, int] = {}
    for result in selected:
        action_counts[result.action] = action_counts.get(result.action, 0) + 1
        for key, value in result.classes.items():
            class_counts[key] = class_counts.get(key, 0) + value
    readme = [
        "# Curated Mixed Source Requirements",
        "",
        "This source root was generated from the old `Exp_Data/Sources` cases.",
        "AADL files are copied unchanged. Requirement files are either kept from",
        "already precise cases or rebuilt from explicit AADL facts.",
        "",
        "## Quality Boundary",
        "",
        "- Keep precise existing requirements with explicit variables, operators, and values.",
        "- Rebuild vague requirements only when a clear connection or property target exists in the AADL text.",
        "- Exclude cases that cannot be grounded in exact connections or property assignments.",
        "- Do not keep ordinary feature-declaration lists as requirements.",
        "- Avoid vague phrases such as valid values, correct type, normal operation, legal boundaries, and assumed environmental conditions.",
        "",
        "## Counts",
        "",
        f"- Cases considered: {len(results)}",
        f"- Cases selected: {len(selected)}",
        f"- Requirement sentences selected: {sum(result.requirement_count for result in selected)}",
        f"- Actions: {json.dumps(action_counts, ensure_ascii=False)}",
        f"- Classes: {json.dumps(class_counts, ensure_ascii=False)}",
        "",
        "## Traceability",
        "",
        "Each selected case includes a `*_Expected.json` sidecar. Every requirement",
        "item contains `trace_refs` and `expected_check` entries pointing to exact",
        "AADL components, connections, properties, endpoints, or values.",
    ]
    (output_root / "DATASET_README.md").write_text("\n".join(readme) + "\n", encoding="utf-8")


def write_report(report_root: Path, output_root: Path, results: list[CaseResult]) -> None:
    manifest_json = report_root / "manifest.json"
    manifest_json.write_text(
        json.dumps([result_to_json(result) for result in results], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    fields = [
        "case_num",
        "letter",
        "label",
        "target",
        "selected",
        "action",
        "reason",
        "old_quality",
        "requirement_count",
        "classes",
        "output_dir",
        "old_req_path",
    ]
    with (report_root / "manifest.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for result in results:
            row = result_to_json(result)
            writer.writerow({field: json.dumps(row[field], ensure_ascii=False) if field == "classes" else row.get(field, "") for field in fields})

    selected = [result for result in results if result.selected]
    excluded = [result for result in results if not result.selected]
    action_counts: dict[str, int] = {}
    class_counts: dict[str, int] = {}
    old_quality_counts: dict[str, int] = {}
    reason_counts: dict[str, int] = {}
    for result in results:
        old_quality_counts[result.old_quality] = old_quality_counts.get(result.old_quality, 0) + 1
        if not result.selected:
            reason_counts[result.reason] = reason_counts.get(result.reason, 0) + 1
        else:
            action_counts[result.action] = action_counts.get(result.action, 0) + 1
            for key, value in result.classes.items():
                class_counts[key] = class_counts.get(key, 0) + value
    lines = [
        "# Mixed Source Requirement Curation Report",
        "",
        f"- Output root: {output_root}",
        f"- Cases considered: {len(results)}",
        f"- Cases selected: {len(selected)}",
        f"- Cases excluded: {len(excluded)}",
        f"- Requirement sentences selected: {sum(result.requirement_count for result in selected)}",
        "",
        "## Counts",
        "",
        f"- Actions: `{json.dumps(action_counts, ensure_ascii=False)}`",
        f"- Classes: `{json.dumps(class_counts, ensure_ascii=False)}`",
        f"- Old quality: `{json.dumps(old_quality_counts, ensure_ascii=False)}`",
        "",
        "## Exclusion Reasons",
        "",
    ]
    for reason, count in sorted(reason_counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- {count}: {reason}")
    lines.extend(["", "## Sample Selected Requirements", ""])
    for result in selected[:80]:
        lines.append(f"- {result.label} [{result.action}] {format_requirement_text(result.items)}")
    (report_root / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def result_to_json(result: CaseResult) -> dict[str, Any]:
    data = asdict(result)
    data["items"] = [item_to_json(item) for item in result.items]
    return data


if __name__ == "__main__":
    raise SystemExit(main())
