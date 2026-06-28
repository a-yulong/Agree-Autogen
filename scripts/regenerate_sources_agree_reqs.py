"""Regenerate Sources requirements with AGREE-oriented natural language.

The generator is intentionally conservative. It uses only the main AADL model
text for requirement semantics, prefers visible runtime symbols, and skips
cases where no non-placeholder AGREE-style behavior can be formed.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


DEFAULT_INPUT = Path(r"C:\Users\25780\Desktop\Exp_Data\Sources")
DEFAULT_OUTPUT = Path(r"C:\Users\25780\Desktop\Exp_Data\Sources_AGREE_Regenerated_20260606")


COMPONENT_KIND = r"system|process|thread|device|abstract"


@dataclass(frozen=True)
class Feature:
    name: str
    direction: str
    category: str
    type_text: str
    scalar: str


@dataclass(frozen=True)
class Component:
    name: str
    kind: str
    block: str
    features: tuple[Feature, ...]


@dataclass(frozen=True)
class GeneratedRequirement:
    target: str
    natural_requirement: str
    expected_agree_hint: str
    trace_refs: tuple[str, ...]
    visible_symbols: tuple[dict[str, str], ...]
    pattern: str
    score: int


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-root", default=str(DEFAULT_INPUT))
    parser.add_argument("--output-root", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--max-labels", type=int, default=0)
    args = parser.parse_args()

    input_root = Path(args.input_root)
    output_root = Path(args.output_root)
    if output_root.exists():
        shutil.rmtree(output_root)
    output_root.mkdir(parents=True, exist_ok=True)

    source_dirs = sorted(
        [p for p in input_root.iterdir() if p.is_dir() and re.fullmatch(r"Case\d+_[A-Z]", p.name)],
        key=lambda p: natural_key(p.name),
    )
    generated: list[dict] = []
    next_case = 1
    for source_dir in source_dirs:
        source_case = parse_case_dir(source_dir)
        if not source_case:
            continue
        source_num, source_letter = source_case
        base_path = source_dir / f"Case{source_num:02d}_Base.aadl"
        if not base_path.exists():
            base_path = source_dir / f"Case{source_num:02d}_Base.txt"
        if not base_path.exists():
            continue
        aadl = base_path.read_text(encoding="utf-8", errors="replace")
        requirement = generate_requirement(aadl, source_dir)
        if requirement is None:
            continue

        case_num = next_case
        next_case += 1
        new_label = f"Case{case_num:02d}_{source_letter}"
        new_dir = output_root / new_label
        copy_case_skeleton(source_dir, new_dir, source_num, case_num)
        write_requirement_files(new_dir, case_num, source_dir.name, source_num, source_letter, requirement)
        generated.append(
            {
                "new_label": new_label,
                "source_label": source_dir.name,
                "target": requirement.target,
                "pattern": requirement.pattern,
                "score": requirement.score,
                "natural_requirement": requirement.natural_requirement,
                "expected_agree_hint": requirement.expected_agree_hint,
            }
        )
        if args.max_labels and len(generated) >= args.max_labels:
            break

    write_manifest(output_root, generated)
    print(f"Generated labels: {len(generated)}")
    print(f"Output root: {output_root}")
    return 0


def natural_key(text: str) -> list[object]:
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", text)]


def parse_case_dir(path: Path) -> tuple[int, str] | None:
    match = re.fullmatch(r"Case(\d+)_([A-Z])", path.name)
    if not match:
        return None
    return int(match.group(1)), match.group(2)


def copy_case_skeleton(source_dir: Path, target_dir: Path, source_num: int, target_num: int) -> None:
    target_dir.mkdir(parents=True, exist_ok=True)
    source_base = source_dir / f"Case{source_num:02d}_Base.aadl"
    if not source_base.exists():
        source_base = source_dir / f"Case{source_num:02d}_Base.txt"
    aadl_text = source_base.read_text(encoding="utf-8", errors="replace")
    (target_dir / f"Case{target_num:02d}_Base.aadl").write_text(aadl_text, encoding="utf-8")
    (target_dir / f"Case{target_num:02d}_Base.txt").write_text(aadl_text, encoding="utf-8")

    # Preserve local dependency .aadl files, but put them under the current case
    # number so existing collection logic does not expose old case numbers.
    dependency_files = []
    for path in source_dir.rglob("*.aadl"):
        if path.name in {f"Case{source_num:02d}_Base.aadl", f"Case{source_num:02d}_Base.txt"}:
            continue
        if path.parent == source_dir and path.name.startswith(f"Case{source_num:02d}_Base"):
            continue
        dependency_files.append(path)
    if dependency_files:
        dep_dir = target_dir / f"Case{target_num:02d}"
        dep_dir.mkdir(exist_ok=True)
        used_names: set[str] = set()
        for path in dependency_files:
            name = path.name
            if name.lower() in used_names:
                name = f"{path.parent.name}_{name}"
            used_names.add(name.lower())
            shutil.copy2(path, dep_dir / name)


def write_requirement_files(
    case_dir: Path,
    case_num: int,
    source_label: str,
    source_num: int,
    source_letter: str,
    req: GeneratedRequirement,
) -> None:
    (case_dir / f"Case{case_num:02d}_Req.txt").write_text(req.natural_requirement + "\n", encoding="utf-8")
    sidecar = {
        "case": case_num,
        "letter": case_dir.name.rsplit("_", 1)[-1],
        "target": req.target,
        "action": "regenerated_agree_oriented",
        "source_label": source_label,
        "source_case": source_num,
        "source_letter": source_letter,
        "requirement_class": "agree_generatable",
        "natural_requirement": req.natural_requirement,
        "expected_agree_hint": req.expected_agree_hint,
        "trace_refs": list(req.trace_refs),
        "visible_symbols": list(req.visible_symbols),
        "generation_pattern": req.pattern,
        "quality_score": req.score,
        "quality_policy": {
            "guide": "C:/Users/25780/Desktop/AGREE_AutoGen_SourceReq_Regeneration_Guide_20260606.md",
            "principle": "Prefer executable AGREE behavior over structural or property restatement.",
            "rejects": [
                "pure connection routing requirements",
                "processor or memory binding requirements",
                "type-membership validity claims",
                "placeholder true/false guarantees",
                "self-equality clauses",
                "invented validity predicates or hidden fields",
            ],
        },
    }
    (case_dir / f"Case{case_num:02d}_Req_Expected.json").write_text(
        json.dumps(sidecar, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def write_manifest(output_root: Path, rows: list[dict]) -> None:
    manifest = {
        "generated_labels": len(rows),
        "unique_source_labels": len({row["source_label"] for row in rows}),
        "policy": "AGREE behavior requirements only; structural/property-only cases skipped.",
        "rows": rows,
    }
    (output_root / "_regeneration_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    lines = [
        "# Regenerated AGREE-Oriented Sources",
        "",
        f"- Generated labels: {len(rows)}",
        f"- Unique source labels: {len({row['source_label'] for row in rows})}",
        "- Policy: AGREE behavior requirements only; structural/property-only cases skipped.",
        "",
        "## Examples",
        "",
    ]
    for row in rows[:30]:
        lines.append(f"### {row['new_label']} from {row['source_label']}")
        lines.append("")
        lines.append(f"- Target: `{row['target']}`")
        lines.append(f"- Pattern: `{row['pattern']}`")
        lines.append(f"- Score: `{row['score']}`")
        lines.append("")
        lines.append(row["natural_requirement"])
        lines.append("")
        lines.append("```agree")
        lines.append(row["expected_agree_hint"])
        lines.append("```")
        lines.append("")
    (output_root / "_regeneration_summary.md").write_text("\n".join(lines), encoding="utf-8")


def generate_requirement(aadl: str, source_dir: Path) -> GeneratedRequirement | None:
    components = extract_components(aadl)
    if not components:
        return None
    target_from_sidecar = read_target_from_sidecar(source_dir)
    ordered = sorted(
        components,
        key=lambda comp: (
            0 if comp.name == target_from_sidecar else 1,
            -component_score(comp),
            comp.name.lower(),
        ),
    )
    for component in ordered:
        req = generate_for_component(component)
        if req is not None:
            return req
    return None


def read_target_from_sidecar(source_dir: Path) -> str:
    sidecars = list(source_dir.glob("*_Req_Expected.json"))
    if not sidecars:
        return ""
    try:
        data = json.loads(sidecars[0].read_text(encoding="utf-8", errors="replace"))
        return str(data.get("target") or "")
    except Exception:
        return ""


def component_score(component: Component) -> int:
    inputs = [f for f in component.features if f.direction == "in"]
    outputs = [f for f in component.features if f.direction == "out"]
    numeric_inputs = [f for f in inputs if f.scalar == "numeric"]
    numeric_outputs = [f for f in outputs if f.scalar == "numeric"]
    bool_inputs = [f for f in inputs if f.scalar == "bool"]
    bool_outputs = [f for f in outputs if f.scalar == "bool"]
    score = 0
    score += 10 * bool(outputs)
    score += 8 * bool(inputs)
    score += 6 * bool(numeric_outputs)
    score += 6 * bool(numeric_inputs)
    score += 5 * bool(bool_outputs)
    score += 4 * bool(bool_inputs)
    score += min(len(component.features), 8)
    return score


def generate_for_component(component: Component) -> GeneratedRequirement | None:
    inputs = [f for f in component.features if f.direction == "in"]
    outputs = [f for f in component.features if f.direction == "out"]
    numeric_inputs = [f for f in inputs if f.scalar == "numeric"]
    numeric_outputs = [f for f in outputs if f.scalar == "numeric"]
    bool_inputs = [f for f in inputs if f.scalar == "bool"]
    bool_outputs = [f for f in outputs if f.scalar == "bool"]

    if bool_outputs and numeric_inputs:
        out = choose_feature(bool_outputs, ("request", "alarm", "fault", "enable", "valid", "active")) or bool_outputs[0]
        inp = choose_feature(numeric_inputs, ("altitude", "distance", "speed", "temp", "pressure", "value")) or numeric_inputs[0]
        threshold = threshold_for(inp.name)
        req = (
            f"The {component.name} component shall monitor the {inp.name} input and drive the {out.name} output as a "
            f"threshold response. When {inp.name} is less than or equal to {threshold}, {out.name} shall be true; "
            f"otherwise, {out.name} shall be false."
        )
        agree = (
            'annex agree {**\n'
            f'  guarantee "{out.name} threshold response": {out.name} = (if {inp.name} <= {threshold} then true else false);\n'
            '**};'
        )
        return make_req(component, req, agree, (inp, out), "numeric_threshold_to_bool", 96)

    if numeric_outputs and len(numeric_inputs) >= 2:
        out = choose_feature(numeric_outputs, ("total", "sum", "command", "output", "speed", "altitude")) or numeric_outputs[0]
        left, right = numeric_inputs[0], numeric_inputs[1]
        req = (
            f"The {component.name} component shall compute the {out.name} output from the {left.name} and {right.name} "
            f"inputs. The {out.name} output shall equal the sum of {left.name} and {right.name} during each evaluation step."
        )
        agree = (
            'annex agree {**\n'
            f'  guarantee "{out.name} sum": {out.name} = {left.name} + {right.name};\n'
            '**};'
        )
        return make_req(component, req, agree, (left, right, out), "numeric_sum", 94)

    if numeric_outputs and numeric_inputs:
        out = numeric_outputs[0]
        inp = numeric_inputs[0]
        req = (
            f"The {component.name} component shall propagate the numeric behavior of {inp.name} to {out.name}. "
            f"For every step, the {out.name} output shall equal the current {inp.name} input."
        )
        agree = (
            'annex agree {**\n'
            f'  guarantee "{out.name} follows {inp.name}": {out.name} = {inp.name};\n'
            '**};'
        )
        return make_req(component, req, agree, (inp, out), "numeric_output_equals_input", 92)

    if bool_outputs and bool_inputs:
        out = bool_outputs[0]
        inp = bool_inputs[0]
        req = (
            f"The {component.name} component shall propagate the Boolean control state from {inp.name} to {out.name}. "
            f"The {out.name} output shall be true exactly when {inp.name} is true."
        )
        agree = (
            'annex agree {**\n'
            f'  guarantee "{out.name} follows {inp.name}": {out.name} = {inp.name};\n'
            '**};'
        )
        return make_req(component, req, agree, (inp, out), "bool_output_equals_input", 92)

    if numeric_outputs:
        out = numeric_outputs[0]
        low, high = range_for(out.name)
        req = (
            f"The {component.name} component shall keep the {out.name} output within its commanded numeric envelope. "
            f"At every step, {out.name} shall be greater than or equal to {low} and less than or equal to {high}."
        )
        agree = (
            'annex agree {**\n'
            f'  guarantee "{out.name} range": {out.name} >= {low} and {out.name} <= {high};\n'
            '**};'
        )
        return make_req(component, req, agree, (out,), "numeric_output_range", 88)

    return None


def make_req(
    component: Component,
    natural_requirement: str,
    expected_agree_hint: str,
    features: Iterable[Feature],
    pattern: str,
    score: int,
) -> GeneratedRequirement:
    symbols = tuple(
        {
            "name": f.name,
            "direction": f.direction,
            "category": f.category,
            "type": f.type_text,
            "scalar": f.scalar,
        }
        for f in features
    )
    trace_refs = tuple(dict.fromkeys([component.name] + [f.name for f in features]))
    return GeneratedRequirement(
        target=component.name,
        natural_requirement=natural_requirement,
        expected_agree_hint=expected_agree_hint,
        trace_refs=trace_refs,
        visible_symbols=symbols,
        pattern=pattern,
        score=score,
    )


def choose_feature(features: list[Feature], keywords: tuple[str, ...]) -> Feature | None:
    for keyword in keywords:
        for feature in features:
            if keyword.lower() in feature.name.lower():
                return feature
    return None


def threshold_for(name: str) -> str:
    lower = name.lower()
    if "altitude" in lower or "height" in lower:
        return "30.0"
    if "distance" in lower:
        return "10.0"
    if "temp" in lower:
        return "20.0"
    if "speed" in lower or "velocity" in lower:
        return "0.0"
    return "0.0"


def range_for(name: str) -> tuple[str, str]:
    lower = name.lower()
    if "heading" in lower:
        return "0.0", "360.0"
    if "latitude" in lower:
        return "-90.0", "90.0"
    if "longitude" in lower:
        return "-180.0", "180.0"
    if "time" in lower:
        return "0.0", "100.0"
    if "velocity" in lower or "speed" in lower:
        return "-100.0", "100.0"
    return "0.0", "100.0"


def extract_components(aadl: str) -> list[Component]:
    components: list[Component] = []
    pattern = re.compile(
        rf"(?ims)^\s*({COMPONENT_KIND})\s+(?!implementation\b)([A-Za-z_][A-Za-z0-9_]*)\b.*?^\s*end\s+\2\s*;",
    )
    for match in pattern.finditer(aadl):
        kind, name = match.group(1).lower(), match.group(2)
        block = match.group(0)
        features = tuple(extract_features(block))
        if features:
            components.append(Component(name=name, kind=kind, block=block, features=features))
    return components


def extract_features(block: str) -> list[Feature]:
    section = extract_section(block, "features")
    if not section:
        return []
    features: list[Feature] = []
    pattern = re.compile(
        r"(?im)^\s*([A-Za-z_][A-Za-z0-9_]*)\s*:\s*"
        r"(?:(in|out|in\s+out)\s+)?"
        r"(?:(event\s+data|event|data)\s+)?port\s+([^;{]+)"
    )
    for match in pattern.finditer(section):
        name = match.group(1)
        direction = re.sub(r"\s+", " ", match.group(2) or "in out").strip().lower()
        category = re.sub(r"\s+", " ", match.group(3) or "data").strip().lower() + " port"
        type_text = re.sub(r"\s+", " ", match.group(4) or "").strip()
        features.append(
            Feature(
                name=name,
                direction=direction,
                category=category,
                type_text=type_text,
                scalar=infer_scalar(type_text, category),
            )
        )
    return features


def extract_section(block: str, name: str) -> str:
    match = re.search(
        rf"(?ims)^\s*{re.escape(name)}\s*$"
        r"(.*?)(?=^\s*(?:features|subcomponents|connections|flows|properties|modes|calls|annex|end\b)\s*)",
        block,
    )
    return match.group(1) if match else ""


def infer_scalar(type_text: str, category: str) -> str:
    text = f"{type_text} {category}".lower()
    if "boolean" in text or re.search(r"\bbool\b", text):
        return "bool"
    if any(token in text for token in ("float", "real", "double", "integer", "int", "unsigned", "long", "short")):
        return "numeric"
    if "event" in text:
        return "event"
    return "opaque"


if __name__ == "__main__":
    raise SystemExit(main())
