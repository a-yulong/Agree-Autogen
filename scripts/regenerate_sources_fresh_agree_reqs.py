"""Freshly regenerate Sources requirements from main AADL models only.

This script deliberately ignores existing Req.txt and Req_Expected.json files.
It uses only each case's main Base AADL model to select AGREE-suitable
components and write new natural-language requirements plus an AGREE hint.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


DEFAULT_INPUT = Path(r"C:\Users\25780\Desktop\Exp_Data\Sources")
DEFAULT_OUTPUT = Path(r"C:\Users\25780\Desktop\Exp_Data\Sources_Fresh_AGREE_20260606")


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
    agree_annex: str


@dataclass(frozen=True)
class Requirement:
    target: str
    text: str
    agree_hint: str
    trace_refs: tuple[str, ...]
    symbols: tuple[dict[str, str], ...]
    source: str
    score: int


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-root", default=str(DEFAULT_INPUT))
    parser.add_argument("--output-root", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--replace-sources", action="store_true")
    parser.add_argument("--min-source-case", type=int, default=1)
    parser.add_argument("--start-case", type=int, default=1)
    parser.add_argument("--max-per-source", type=int, default=2)
    args = parser.parse_args()

    input_root = Path(args.input_root)
    output_root = Path(args.output_root)
    if output_root.exists():
        shutil.rmtree(output_root)
    output_root.mkdir(parents=True, exist_ok=True)

    generated: list[dict] = []
    next_case = args.start_case
    for source_dir in sorted_case_dirs(input_root):
        parsed = parse_case_dir(source_dir)
        if not parsed:
            continue
        source_num, source_letter = parsed
        if source_num < args.min_source_case:
            continue
        base_path = source_dir / f"Case{source_num:02d}_Base.aadl"
        if not base_path.exists():
            base_path = source_dir / f"Case{source_num:02d}_Base.txt"
        if not base_path.exists():
            continue
        aadl = base_path.read_text(encoding="utf-8", errors="replace")
        requirements = generate_requirements_from_aadl(aadl)
        for req_index, requirement in enumerate(requirements[: args.max_per_source], 1):
            case_num = next_case
            next_case += 1
            # Preserve source letter only as a harmless variant marker. The new
            # numbering and requirement content are independent from old reqs.
            new_label = f"Case{case_num:02d}_{source_letter}"
            new_dir = output_root / new_label
            copy_case_assets(source_dir, new_dir, source_num, case_num)
            write_new_req(new_dir, case_num, source_dir.name, requirement)
            generated.append(
                {
                    "new_label": new_label,
                    "source_label": source_dir.name,
                    "target": requirement.target,
                    "source": requirement.source,
                    "score": requirement.score,
                    "natural_requirement": requirement.text,
                    "expected_agree_hint": requirement.agree_hint,
                }
            )

    write_manifest(output_root, generated)
    if args.replace_sources:
        replace_sources(input_root, output_root)
    print(f"Generated fresh labels: {len(generated)}")
    print(f"Output root: {output_root}")
    return 0


def sorted_case_dirs(root: Path) -> list[Path]:
    return sorted(
        [p for p in root.iterdir() if p.is_dir() and re.fullmatch(r"Case\d+_[A-Z]", p.name)],
        key=lambda p: natural_key(p.name),
    )


def natural_key(text: str) -> list[object]:
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", text)]


def parse_case_dir(path: Path) -> tuple[int, str] | None:
    match = re.fullmatch(r"Case(\d+)_([A-Z])", path.name)
    if not match:
        return None
    return int(match.group(1)), match.group(2)


def generate_requirements_from_aadl(aadl: str) -> list[Requirement]:
    components = extract_components(aadl)
    out: list[Requirement] = []
    for component in sorted(components, key=lambda c: (-component_score(c), c.name.lower())):
        req = synthesize_behavior(component)
        if req:
            out.append(req)
    return out


def from_existing_agree(component: Component) -> Requirement | None:
    annex = component.agree_annex.strip()
    if not annex:
        return None
    clauses: list[tuple[str, str, str]] = []
    for line in annex.splitlines():
        clean = line.strip().rstrip(";")
        if not clean or clean.startswith("--"):
            continue
        parsed = parse_agree_clause(clean)
        if parsed:
            clauses.append(parsed)
    semantic_clauses = [c for c in clauses if is_semantic_clause(c)]
    if not semantic_clauses:
        return None
    symbols = tuple(symbol for symbol in component.features if appears_in_any(symbol.name, semantic_clauses))
    if not symbols:
        symbols = component.features[:4]
    readable = naturalize_clauses(component.name, semantic_clauses[:4])
    agree_hint = "annex agree {**\n  " + ";\n  ".join(format_agree_clause(c) for c in semantic_clauses[:4]) + ";\n**};"
    return make_requirement(component, readable, agree_hint, symbols, "existing_agree_backtranslation", 98)


def parse_agree_clause(clean: str) -> tuple[str, str, str] | None:
    match = re.match(r'(?is)^(assume|guarantee)\s+(?:"([^"]+)"|([A-Za-z_][A-Za-z0-9_]*))\s*:\s*(.+)$', clean)
    if match:
        kind = match.group(1).lower()
        label = match.group(2) or match.group(3) or ""
        expr = (match.group(4) or "").strip()
        return (kind, label, expr) if expr else None
    match = re.match(r"(?is)^(eq|const)\s+(.+)$", clean)
    if match:
        expr = (match.group(2) or "").strip()
        if ":" not in expr and "=" not in expr:
            return None
        return (match.group(1).lower(), "", expr)
    match = re.match(r"(?is)^assign\s+(.+)$", clean)
    if match:
        expr = (match.group(1) or "").strip()
        return ("assign", "", expr) if "=" in expr else None
    return None


def is_semantic_clause(clause: tuple[str, str, str]) -> bool:
    kind, _label, expr = clause
    if not expr or expr == ":":
        return False
    if kind in {"assume", "guarantee"} and re.fullmatch(r"(?i)true|false", expr.strip()):
        return False
    if re.fullmatch(r"\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*\1\s*", expr):
        return False
    return True


def format_agree_clause(clause: tuple[str, str, str]) -> str:
    kind, label, expr = clause
    if kind in {"assume", "guarantee"}:
        safe_label = label or kind
        return f'{kind} "{safe_label}": {expr}'
    return f"{kind} {expr}"


def naturalize_clauses(component_name: str, clauses: list[tuple[str, str, str]]) -> str:
    parts = [f"The {component_name} component shall enforce the following AGREE behavior."]
    for kind, label, expr in clauses:
        clean_expr = plain_expr(expr)
        label_text = readable_label(label)
        if kind == "assume":
            parts.append(f"It shall assume that {clean_expr}.")
        elif kind == "guarantee":
            if label_text:
                parts.append(f"For {label_text}, it shall guarantee that {clean_expr}.")
            else:
                parts.append(f"It shall guarantee that {clean_expr}.")
        elif kind == "assign":
            parts.append(f"Its implementation shall assign {clean_expr}.")
        elif kind in {"eq", "const"}:
            parts.append(f"It may define {clean_expr}.")
    return " ".join(parts)


def plain_expr(expr: str) -> str:
    text = expr.strip()
    text = text.replace("=>", "implies")
    text = text.replace(">=", "greater than or equal to")
    text = text.replace("<=", "less than or equal to")
    text = re.sub(r"\s+", " ", text)
    return text


def readable_label(label: str) -> str:
    text = re.sub(r"[_-]+", " ", label or "").strip()
    text = re.sub(r"(?i)\bvalid\b", "bounded", text)
    text = re.sub(r"\s+", " ", text)
    return text


def appears_in_any(name: str, clauses: Iterable[tuple[str, str, str]]) -> bool:
    return any(re.search(rf"\b{re.escape(name)}\b", f"{label} {expr}") for _kind, label, expr in clauses)


def synthesize_behavior(component: Component) -> Requirement | None:
    inputs = [f for f in component.features if f.direction == "in"]
    outputs = [f for f in component.features if f.direction == "out"]
    numeric_inputs = [f for f in inputs if f.scalar == "numeric"]
    numeric_outputs = [f for f in outputs if f.scalar == "numeric"]
    bool_inputs = [f for f in inputs if f.scalar == "bool"]
    bool_outputs = [f for f in outputs if f.scalar == "bool"]

    supervisor_req = synthesize_supervisor_style(component, numeric_inputs, numeric_outputs)
    if supervisor_req:
        return supervisor_req

    if bool_outputs and numeric_inputs:
        out = prefer(bool_outputs, ("request", "alarm", "fault", "enable", "valid", "active")) or bool_outputs[0]
        inp = prefer(numeric_inputs, ("altitude", "distance", "speed", "temp", "pressure", "value")) or numeric_inputs[0]
        threshold = threshold_for(inp.name)
        req = (
            f"The {component.name} component shall evaluate {inp.name} as a threshold condition for {out.name}. "
            f"When {inp.name} is less than or equal to {threshold}, {out.name} shall be true; otherwise, {out.name} shall be false."
        )
        agree = "annex agree {**\n" + f'  guarantee "{out.name} threshold response": {out.name} = (if {inp.name} <= {threshold} then true else false);\n' + "**};"
        return make_requirement(component, req, agree, (inp, out), "fresh_numeric_threshold_to_bool", 94)

    if numeric_outputs and len(numeric_inputs) >= 2:
        out = prefer(numeric_outputs, ("total", "sum", "command", "output", "speed", "altitude", "result")) or numeric_outputs[0]
        left, right = numeric_inputs[0], numeric_inputs[1]
        req = (
            f"The {component.name} component shall compute {out.name} from the current {left.name} and {right.name} inputs. "
            f"At each evaluation step, {out.name} shall equal the sum of {left.name} and {right.name}."
        )
        agree = "annex agree {**\n" + f'  guarantee "{out.name} sum": {out.name} = {left.name} + {right.name};\n' + "**};"
        return make_requirement(component, req, agree, (left, right, out), "fresh_numeric_sum", 92)

    if numeric_outputs and numeric_inputs:
        out, inp = numeric_outputs[0], numeric_inputs[0]
        req = (
            f"The {component.name} component shall provide a direct numeric response from {inp.name} to {out.name}. "
            f"For every evaluation step, the {out.name} output shall equal the current {inp.name} input."
        )
        agree = "annex agree {**\n" + f'  guarantee "{out.name} follows {inp.name}": {out.name} = {inp.name};\n' + "**};"
        return make_requirement(component, req, agree, (inp, out), "fresh_numeric_passthrough", 90)

    if bool_outputs and bool_inputs:
        out, inp = bool_outputs[0], bool_inputs[0]
        req = (
            f"The {component.name} component shall propagate the Boolean control state from {inp.name} to {out.name}. "
            f"The {out.name} output shall be true exactly when {inp.name} is true."
        )
        agree = "annex agree {**\n" + f'  guarantee "{out.name} follows {inp.name}": {out.name} = {inp.name};\n' + "**};"
        return make_requirement(component, req, agree, (inp, out), "fresh_bool_passthrough", 90)

    if numeric_outputs:
        out = numeric_outputs[0]
        low, high = range_for(out.name)
        req = (
            f"The {component.name} component shall keep {out.name} within a bounded numeric envelope. "
            f"At every step, {out.name} shall be greater than or equal to {low} and less than or equal to {high}."
        )
        agree = "annex agree {**\n" + f'  guarantee "{out.name} range": {out.name} >= {low} and {out.name} <= {high};\n' + "**};"
        return make_requirement(component, req, agree, (out,), "fresh_numeric_range", 84)

    return None


def synthesize_supervisor_style(
    component: Component,
    numeric_inputs: list[Feature],
    numeric_outputs: list[Feature],
) -> Requirement | None:
    output = next((f for f in numeric_outputs if "timetofailure" in f.name.lower()), None)
    failure_inputs = [f for f in numeric_inputs if "timetofailure" in f.name.lower()]
    recovery_inputs = [f for f in numeric_inputs if "timetorecovery" in f.name.lower()]
    if not output or len(failure_inputs) < 2:
        return None
    used = tuple(failure_inputs[:3] + recovery_inputs[:3] + [output])
    min_expr = " and ".join(f"{output.name} <= {f.name}" for f in failure_inputs[:3])
    if recovery_inputs:
        recovery_sum = " + ".join(f.name for f in recovery_inputs[:3])
        extra_sentence = f" The component shall also guarantee that {output.name} is greater than the sum of {recovery_sum}."
        extra_clause = f'\n  guarantee "{output.name} exceeds recovery sum": {output.name} > {recovery_sum};'
    else:
        extra_sentence = ""
        extra_clause = ""
    req = (
        f"The {component.name} component shall compute {output.name} as a conservative bound over the subsystem failure-time inputs. "
        f"At every step, {output.name} shall be less than or equal to "
        f"{', '.join(f.name for f in failure_inputs[:3])}.{extra_sentence}"
    )
    agree = (
        "annex agree {**\n"
        f'  guarantee "{output.name} conservative bound": {min_expr};'
        f"{extra_clause}\n"
        "**};"
    )
    return make_requirement(component, req, agree, used, "fresh_supervisor_failure_bound", 95)


def make_requirement(
    component: Component,
    text: str,
    agree_hint: str,
    features: Iterable[Feature],
    source: str,
    score: int,
) -> Requirement:
    selected = tuple(features)
    symbols = tuple(
        {
            "name": f.name,
            "direction": f.direction,
            "category": f.category,
            "type": f.type_text,
            "scalar": f.scalar,
        }
        for f in selected
    )
    refs = tuple(dict.fromkeys([component.name] + [f.name for f in selected]))
    return Requirement(component.name, text, agree_hint, refs, symbols, source, score)


def extract_components(aadl: str) -> list[Component]:
    out: list[Component] = []
    pattern = re.compile(
        rf"(?ims)^\s*({COMPONENT_KIND})\s+(?!implementation\b)([A-Za-z_][A-Za-z0-9_]*)\b.*?^\s*end\s+\2\s*;",
    )
    for match in pattern.finditer(aadl):
        kind, name, block = match.group(1).lower(), match.group(2), match.group(0)
        features = tuple(extract_features(block))
        agree = extract_agree_annex(block)
        if features:
            out.append(Component(name, kind, block, features, agree))
    return out


def extract_features(block: str) -> list[Feature]:
    section = extract_section(block, "features")
    if not section:
        return []
    out: list[Feature] = []
    pattern = re.compile(
        r"(?im)^\s*([A-Za-z_][A-Za-z0-9_]*)\s*:\s*"
        r"(?:(in|out|in\s+out)\s+)?"
        r"(?:(event\s+data|event|data)\s+)?port\s+([^;{]+)"
    )
    for match in pattern.finditer(section):
        name = match.group(1)
        direction = re.sub(r"\s+", " ", match.group(2) or "in out").lower().strip()
        category = re.sub(r"\s+", " ", match.group(3) or "data").lower().strip() + " port"
        type_text = re.sub(r"\s+", " ", match.group(4) or "").strip()
        out.append(Feature(name, direction, category, type_text, infer_scalar(type_text, category)))
    return out


def extract_section(block: str, name: str) -> str:
    match = re.search(
        rf"(?ims)^\s*{name}\s*$"
        r"(.*?)(?=^\s*(?:features|subcomponents|connections|flows|properties|modes|calls|annex|end\b)\s*)",
        block,
    )
    return match.group(1) if match else ""


def extract_agree_annex(block: str) -> str:
    match = re.search(r"(?is)annex\s+agree\s*\{\*\*(.*?)\*\*};?", block)
    return match.group(1).strip() if match else ""


def infer_scalar(type_text: str, category: str) -> str:
    text = f"{type_text} {category}".lower()
    category_l = category.lower()
    type_l = type_text.lower()
    if "event" in category_l:
        return "event"
    if "data port" not in category_l:
        return "opaque"
    if not (
        type_l.startswith("base_types::")
        or type_l in {"integer", "int", "real", "float", "double", "boolean", "bool"}
    ):
        return "opaque"
    if "boolean" in text or re.search(r"\bbool\b", text):
        return "bool"
    if any(token in text for token in ("float", "real", "double", "integer", "int", "unsigned", "long", "short")):
        return "numeric"
    return "opaque"


def component_score(component: Component) -> int:
    inputs = [f for f in component.features if f.direction == "in"]
    outputs = [f for f in component.features if f.direction == "out"]
    score = 20 if component.agree_annex else 0
    score += 12 if inputs and outputs else 0
    score += 8 if any(f.scalar == "numeric" for f in component.features) else 0
    score += 8 if any(f.scalar == "bool" for f in component.features) else 0
    score += min(len(component.features), 8)
    return score


def prefer(features: list[Feature], keywords: tuple[str, ...]) -> Feature | None:
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


def copy_case_assets(source_dir: Path, target_dir: Path, source_num: int, target_num: int) -> None:
    target_dir.mkdir(parents=True, exist_ok=True)
    base_path = source_dir / f"Case{source_num:02d}_Base.aadl"
    if not base_path.exists():
        base_path = source_dir / f"Case{source_num:02d}_Base.txt"
    aadl = base_path.read_text(encoding="utf-8", errors="replace")
    (target_dir / f"Case{target_num:02d}_Base.aadl").write_text(aadl, encoding="utf-8")
    (target_dir / f"Case{target_num:02d}_Base.txt").write_text(aadl, encoding="utf-8")
    dep_files = [
        p for p in source_dir.rglob("*.aadl")
        if p.resolve() != base_path.resolve()
        and not p.name.startswith(f"Case{source_num:02d}_Base")
    ]
    if dep_files:
        dep_dir = target_dir / f"Case{target_num:02d}"
        dep_dir.mkdir(exist_ok=True)
        seen: set[str] = set()
        for dep in dep_files:
            name = dep.name
            if name.lower() in seen:
                name = f"{dep.parent.name}_{name}"
            seen.add(name.lower())
            shutil.copy2(dep, dep_dir / name)


def write_new_req(target_dir: Path, case_num: int, source_label: str, req: Requirement) -> None:
    (target_dir / f"Case{case_num:02d}_Req.txt").write_text(req.text + "\n", encoding="utf-8")
    sidecar = {
        "case": case_num,
        "letter": target_dir.name.rsplit("_", 1)[-1],
        "target": req.target,
        "action": "fresh_regenerated_from_main_aadl_only",
        "source_label": source_label,
        "requirement_class": "agree_generatable",
        "natural_requirement": req.text,
        "expected_agree_hint": req.agree_hint,
        "trace_refs": list(req.trace_refs),
        "visible_symbols": list(req.symbols),
        "generation_source": req.source,
        "quality_score": req.score,
        "quality_policy": {
            "guide": "C:/Users/25780/Desktop/AGREE_AutoGen_SourceReq_Regeneration_Guide_20260606.md",
            "uses_old_req": False,
            "uses_old_sidecar_target": False,
            "uses_direct_referenced_declarations_for_semantics": False,
        },
    }
    (target_dir / f"Case{case_num:02d}_Req_Expected.json").write_text(
        json.dumps(sidecar, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def write_manifest(output_root: Path, rows: list[dict]) -> None:
    manifest = {
        "generated_labels": len(rows),
        "policy": "Fresh requirements generated from main AADL models only.",
        "uses_old_req": False,
        "uses_old_sidecar_target": False,
        "rows": rows,
    }
    (output_root / "_fresh_generation_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    lines = [
        "# Fresh AGREE-Oriented Sources",
        "",
        f"- Generated labels: {len(rows)}",
        "- Uses old Req.txt: no",
        "- Uses old sidecar target: no",
        "- Uses direct referenced declarations for requirement semantics: no",
        "",
    ]
    for row in rows[:40]:
        lines.extend(
            [
                f"## {row['new_label']} from {row['source_label']}",
                "",
                f"- Target: `{row['target']}`",
                f"- Source: `{row['source']}`",
                f"- Score: `{row['score']}`",
                "",
                row["natural_requirement"],
                "",
                "```agree",
                row["expected_agree_hint"],
                "```",
                "",
            ]
        )
    (output_root / "_fresh_generation_summary.md").write_text("\n".join(lines), encoding="utf-8")


def replace_sources(current_sources: Path, generated_root: Path) -> None:
    backup = current_sources.with_name("Sources_backup_before_fresh_agree_20260606")
    suffix = 1
    while backup.exists():
        suffix += 1
        backup = current_sources.with_name(f"Sources_backup_before_fresh_agree_20260606_{suffix}")
    shutil.move(str(current_sources), str(backup))
    shutil.copytree(generated_root, current_sources)
    print(f"Backup: {backup}")
    print(f"Replaced Sources: {current_sources}")


if __name__ == "__main__":
    raise SystemExit(main())
