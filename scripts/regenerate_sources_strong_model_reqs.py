"""Regenerate AGREE-oriented source requirements from AADL with strict executability.

This script is intentionally independent from the older requirement-generation
scripts. It does not read old Req text or old expected targets. It builds fresh
requirements from the main AADL model, using a compact set of AGREE-executable
patterns inspired by the first-110 contract-grounded cases:

- numeric range guarantees
- numeric passthrough guarantees
- same-family numeric sum guarantees
- threshold-to-Boolean guarantees
- Boolean passthrough / implication guarantees
- assumption + guarantee pairs over visible scalar ports
- simple conditional numeric output guarantees

The generator deliberately excludes event/event data ports, subcomponent paths,
AADL property/binding/routing requirements, and opaque/user-defined data types
unless their visible port type is a direct Base_Types scalar.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
from dataclasses import dataclass
from pathlib import Path


DEFAULT_INPUT = Path(r"C:\Users\25780\Desktop\Exp_Data\Sources_backup_before_fresh_agree_20260606_225112")
DEFAULT_CURRENT = Path(r"C:\Users\25780\Desktop\Exp_Data\Sources")
DEFAULT_OUTPUT = Path(r"C:\Users\25780\Desktop\Exp_Data\Sources_StrongModel_AGREE_20260607")
DEFAULT_STATIC_LIBS = Path(
    r"C:\Users\25780\Desktop\py_item\DeepSeek\Agree-Autogen_v2.0\tools\agree-validator\static-libs"
)

COMPONENT_KIND = r"system|process|thread|device|abstract"


@dataclass(frozen=True)
class Feature:
    name: str
    direction: str
    category: str
    type_text: str
    scalar: str
    family: str


@dataclass(frozen=True)
class Component:
    name: str
    kind: str
    block: str
    features: tuple[Feature, ...]


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
    parser.add_argument("--aadl-root", default=None)
    parser.add_argument("--current-root", default=str(DEFAULT_CURRENT))
    parser.add_argument("--output-root", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--static-libs", default=str(DEFAULT_STATIC_LIBS))
    parser.add_argument("--min-source-case", type=int, default=111)
    parser.add_argument("--start-case", type=int, default=111)
    parser.add_argument("--max-per-source", type=int, default=4)
    parser.add_argument("--replace-sources", action="store_true")
    args = parser.parse_args()

    input_root = Path(args.input_root)
    current_root = Path(args.current_root)
    output_root = Path(args.output_root)
    static_libs = Path(args.static_libs)
    static_names, static_units = static_library_keys(static_libs)

    if output_root.exists():
        shutil.rmtree(output_root)
    output_root.mkdir(parents=True, exist_ok=True)

    generated: list[dict] = []
    next_case = args.start_case
    source_items = list_source_items(input_root, Path(args.aadl_root) if args.aadl_root else None, args.min_source_case)
    for source_index, source in enumerate(source_items, 1):
        aadl_path = source["aadl_path"]
        aadl = aadl_path.read_text(encoding="utf-8", errors="replace")
        requirements = generate_requirements_from_aadl(aadl)
        kept = 0
        for req in requirements:
            case_num = next_case
            next_case += 1
            kept += 1
            source_letter = "A" if source_index % 2 else "B"
            new_label = f"{case_prefix(case_num)}_{source_letter}"
            new_dir = output_root / new_label
            copy_source_assets(
                source=source,
                target_dir=new_dir,
                target_num=case_num,
                static_names=static_names,
                static_units=static_units,
            )
            write_requirement(new_dir, case_num, source["source_label"], req)
            generated.append(
                {
                    "new_label": new_label,
                    "source_label": source["source_label"],
                    "target": req.target,
                    "source": req.source,
                    "score": req.score,
                    "natural_requirement": req.text,
                    "expected_agree_hint": req.agree_hint,
                }
            )
            if kept >= args.max_per_source:
                break

    write_manifest(output_root, generated)
    write_quality_audit(output_root, generated)

    if args.replace_sources:
        replace_sources(current_root, output_root)

    print(f"Generated strong-model labels: {len(generated)}")
    print(f"Output root: {output_root}")
    return 0


def list_source_items(input_root: Path, aadl_root: Path | None, min_source_case: int) -> list[dict]:
    if aadl_root:
        files = [
            path
            for path in sorted(aadl_root.rglob("*.aadl"), key=lambda p: natural_key(str(p.relative_to(aadl_root))))
            if path.is_file() and path.stat().st_size > 0 and path.stat().st_size < 80_000
        ]
        return [
            {
                "kind": "aadl_file",
                "aadl_path": path,
                "source_label": str(path.relative_to(aadl_root)).replace("\\", "/"),
                "source_dir": path.parent,
            }
            for path in files
        ]

    items: list[dict] = []
    for source_dir in sorted_case_dirs(input_root):
        parsed = parse_case_dir(source_dir)
        if not parsed:
            continue
        source_num, _source_letter = parsed
        if source_num < min_source_case:
            continue
        aadl_path = find_case_file(source_dir, source_num, "_Base.aadl") or find_case_file(
            source_dir, source_num, "_Base.txt"
        )
        if not aadl_path:
            continue
        items.append(
            {
                "kind": "case_dir",
                "aadl_path": aadl_path,
                "source_label": source_dir.name,
                "source_dir": source_dir,
                "source_num": source_num,
            }
        )
    return items


def case_prefix(num: int) -> str:
    return f"Case{num:02d}" if num < 100 else f"Case{num}"


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


def find_case_file(case_dir: Path, num: int, suffix: str) -> Path | None:
    candidates = [case_dir / f"{case_prefix(num)}{suffix}", case_dir / f"Case{num}{suffix}"]
    return next((path for path in candidates if path.exists()), None)


def generate_requirements_from_aadl(aadl: str) -> list[Requirement]:
    requirements: list[Requirement] = []
    for component in sorted(extract_components(aadl), key=lambda item: (-component_score(item), item.name.lower())):
        requirements.extend(synthesize_component_requirements(component))
    return requirements


def synthesize_component_requirements(component: Component) -> list[Requirement]:
    inputs = [f for f in component.features if f.direction == "in"]
    outputs = [f for f in component.features if f.direction == "out"]
    nums_in = [f for f in inputs if f.scalar == "numeric"]
    nums_out = [f for f in outputs if f.scalar == "numeric"]
    bools_in = [f for f in inputs if f.scalar == "bool"]
    bools_out = [f for f in outputs if f.scalar == "bool"]

    out: list[Requirement] = []

    # Pattern 0: explicit input assumptions, common in the first-110 cases.
    for signal in ranked(nums_in)[:2]:
        low, high = range_for(signal.name, signal.family)
        text = (
            f"The {component.name} component shall operate under a bounded input condition for {signal.name}. "
            f"The environment shall keep {signal.name} greater than or equal to {low} and less than or equal to {high}."
        )
        agree = annex(f'assume "{signal.name} input range": {signal.name} >= {low} and {signal.name} <= {high};')
        out.append(make_requirement(component, text, agree, (signal,), "strong_numeric_input_assumption", 87))

    for signal in ranked(bools_in)[:1]:
        text = (
            f"The {component.name} component shall operate under a Boolean input condition on {signal.name}. "
            f"The environment shall provide {signal.name} as true whenever this contract is evaluated."
        )
        agree = annex(f'assume "{signal.name} input true": {signal.name};')
        out.append(make_requirement(component, text, agree, (signal,), "strong_bool_input_assumption", 84))

    # Pattern 1: output range guarantee.
    for signal in ranked(nums_out)[:2]:
        low, high = range_for(signal.name, signal.family)
        text = (
            f"The {component.name} component shall bound the {signal.name} output at every evaluation step. "
            f"The {signal.name} value shall be greater than or equal to {low} and less than or equal to {high}."
        )
        agree = annex(f'guarantee "{signal.name} range": {signal.name} >= {low} and {signal.name} <= {high};')
        out.append(make_requirement(component, text, agree, (signal,), "strong_numeric_range", 88))

    # Pattern 2: numeric passthrough when same scalar family is visible.
    for dest in ranked(nums_out):
        src = first_same_family(nums_in, dest)
        if src:
            text = (
                f"The {component.name} component shall preserve the current {src.name} value on {dest.name}. "
                f"For each evaluation step, the {dest.name} output shall equal the {src.name} input."
            )
            agree = annex(f'guarantee "{dest.name} follows {src.name}": {dest.name} = {src.name};')
            out.append(make_requirement(component, text, agree, (src, dest), "strong_numeric_passthrough", 91))
            break

    # Pattern 3: numeric sum only when all operands are same family.
    for dest in ranked(nums_out):
        same = [f for f in ranked(nums_in) if f.family == dest.family and f.name != dest.name]
        if len(same) >= 2:
            left, right = same[0], same[1]
            text = (
                f"The {component.name} component shall compute {dest.name} from {left.name} and {right.name}. "
                f"At each evaluation step, {dest.name} shall equal the sum of {left.name} and {right.name}."
            )
            agree = annex(f'guarantee "{dest.name} sum": {dest.name} = {left.name} + {right.name};')
            out.append(make_requirement(component, text, agree, (left, right, dest), "strong_numeric_sum", 94))
            break

    # Pattern 4: Boolean output driven by numeric threshold.
    for dest in ranked(bools_out):
        src = ranked(nums_in)[0] if nums_in else None
        if src:
            threshold = threshold_for(src.name, src.family)
            text = (
                f"The {component.name} component shall derive the Boolean output {dest.name} from {src.name}. "
                f"When {src.name} is greater than {threshold}, {dest.name} shall be true; otherwise {dest.name} shall be false."
            )
            agree = annex(
                f'guarantee "{dest.name} threshold": {dest.name} = (if {src.name} > {threshold} then true else false);'
            )
            out.append(make_requirement(component, text, agree, (src, dest), "strong_threshold_to_bool", 94))
            break

    # Pattern 5: Boolean passthrough/equivalence.
    for dest in ranked(bools_out):
        src = ranked(bools_in)[0] if bools_in else None
        if src:
            text = (
                f"The {component.name} component shall propagate the Boolean control state from {src.name} to {dest.name}. "
                f"The {dest.name} output shall be true exactly when {src.name} is true."
            )
            agree = annex(f'guarantee "{dest.name} follows {src.name}": {dest.name} = {src.name};')
            out.append(make_requirement(component, text, agree, (src, dest), "strong_bool_passthrough", 91))
            break

    # Pattern 6: Boolean implication.
    for dest in ranked(bools_out):
        src = ranked(bools_in)[1] if len(bools_in) > 1 else None
        if src:
            text = (
                f"The {component.name} component shall assert {dest.name} whenever {src.name} is true. "
                f"If {src.name} is false, this requirement imposes no additional condition on {dest.name}."
            )
            agree = annex(f'guarantee "{src.name} implies {dest.name}": {src.name} => {dest.name};')
            out.append(make_requirement(component, text, agree, (src, dest), "strong_bool_implication", 89))
            break

    # Pattern 7: assumption + bounded output guarantee.
    if nums_in and nums_out:
        src = ranked(nums_in)[0]
        dest = first_same_family(nums_out, src) or ranked(nums_out)[0]
        in_low, in_high = range_for(src.name, src.family)
        out_low, out_high = range_for(dest.name, dest.family)
        text = (
            f"The {component.name} component shall operate under a bounded {src.name} input envelope. "
            f"It shall assume {src.name} remains between {in_low} and {in_high}, and shall guarantee {dest.name} remains between {out_low} and {out_high}."
        )
        agree = annex(
            f'assume "{src.name} input range": {src.name} >= {in_low} and {src.name} <= {in_high};\n'
            f'  guarantee "{dest.name} bounded under input range": {dest.name} >= {out_low} and {dest.name} <= {out_high};'
        )
        out.append(make_requirement(component, text, agree, (src, dest), "strong_assume_range_guarantee", 90))

    # Pattern 8: conditional numeric output from a Boolean input.
    if bools_in and nums_out:
        ctrl = ranked(bools_in)[0]
        dest = ranked(nums_out)[0]
        active, inactive = conditional_values_for(dest.name, dest.family)
        text = (
            f"The {component.name} component shall select the {dest.name} command from the Boolean input {ctrl.name}. "
            f"When {ctrl.name} is true, {dest.name} shall equal {active}; otherwise {dest.name} shall equal {inactive}."
        )
        agree = annex(f'guarantee "{dest.name} selected by {ctrl.name}": {dest.name} = (if {ctrl.name} then {active} else {inactive});')
        out.append(make_requirement(component, text, agree, (ctrl, dest), "strong_bool_to_numeric_condition", 92))

    # Pattern 9: conditional numeric output from a numeric threshold. This avoids
    # adding unlike numeric families while still producing first-110 style
    # if/then/otherwise behavior.
    if nums_in and nums_out:
        src = ranked(nums_in)[0]
        dest = ranked(nums_out)[0]
        threshold = threshold_for(src.name, src.family)
        high_value, low_value = conditional_values_for(dest.name, dest.family)
        text = (
            f"The {component.name} component shall select {dest.name} according to the current {src.name} value. "
            f"When {src.name} is greater than {threshold}, {dest.name} shall equal {high_value}; otherwise {dest.name} shall equal {low_value}."
        )
        agree = annex(
            f'guarantee "{dest.name} threshold selection": {dest.name} = (if {src.name} > {threshold} then {high_value} else {low_value});'
        )
        out.append(make_requirement(component, text, agree, (src, dest), "strong_numeric_threshold_to_numeric", 91))

    return dedupe_requirements(out)


def annex(body: str) -> str:
    return f"annex agree {{**\n  {body}\n**}};"


def make_requirement(
    component: Component,
    text: str,
    agree_hint: str,
    features: tuple[Feature, ...],
    source: str,
    score: int,
) -> Requirement:
    symbols = tuple(
        {
            "name": feature.name,
            "direction": feature.direction,
            "category": feature.category,
            "type": feature.type_text,
            "scalar": feature.scalar,
            "family": feature.family,
        }
        for feature in features
    )
    refs = tuple(dict.fromkeys([component.name] + [f.name for f in features]))
    return Requirement(component.name, text, agree_hint, refs, symbols, source, score)


def dedupe_requirements(items: list[Requirement]) -> list[Requirement]:
    out: list[Requirement] = []
    seen: set[str] = set()
    for item in items:
        key = normalize_text(item.text)
        if key not in seen:
            seen.add(key)
            out.append(item)
    return out


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def ranked(features: list[Feature]) -> list[Feature]:
    preferred = (
        "output",
        "out",
        "cmd",
        "command",
        "speed",
        "altitude",
        "velocity",
        "distance",
        "temperature",
        "temp",
        "pressure",
        "mode",
        "alarm",
        "fault",
        "enable",
        "valid",
        "input",
        "in",
    )

    def score(feature: Feature) -> tuple[int, str]:
        name = feature.name.lower()
        best = min((i for i, token in enumerate(preferred) if token in name), default=99)
        return (best, name)

    return sorted(features, key=score)


def first_same_family(features: list[Feature], other: Feature) -> Feature | None:
    return next((feature for feature in ranked(features) if feature.family == other.family and feature.name != other.name), None)


def threshold_for(name: str, family: str) -> str:
    lower = name.lower()
    if family == "int":
        if "heading" in lower:
            return "180"
        if "altitude" in lower or "height" in lower:
            return "30"
        if "distance" in lower:
            return "10"
        if "speed" in lower or "velocity" in lower:
            return "0"
        return "0"
    if "heading" in lower:
        return "180.0"
    if "altitude" in lower or "height" in lower:
        return "30.0"
    if "distance" in lower:
        return "10.0"
    if "speed" in lower or "velocity" in lower:
        return "0.0"
    return "0.0"


def range_for(name: str, family: str) -> tuple[str, str]:
    lower = name.lower()
    if family == "int":
        if "heading" in lower:
            return "0", "360"
        if "latitude" in lower:
            return "-90", "90"
        if "longitude" in lower:
            return "-180", "180"
        if "time" in lower:
            return "0", "100"
        if "speed" in lower or "velocity" in lower:
            return "-100", "100"
        return "0", "100"
    if "heading" in lower:
        return "0.0", "360.0"
    if "latitude" in lower:
        return "-90.0", "90.0"
    if "longitude" in lower:
        return "-180.0", "180.0"
    if "time" in lower:
        return "0.0", "100.0"
    if "speed" in lower or "velocity" in lower:
        return "-100.0", "100.0"
    return "0.0", "100.0"


def conditional_values_for(name: str, family: str) -> tuple[str, str]:
    lower = name.lower()
    if family == "int":
        if "velocity" in lower or "speed" in lower:
            return "10", "0"
        return "1", "0"
    if "velocity" in lower or "speed" in lower:
        return "10.0", "0.0"
    return "1.0", "0.0"


def extract_components(aadl: str) -> list[Component]:
    out: list[Component] = []
    pattern = re.compile(
        rf"(?ims)^\s*({COMPONENT_KIND})\s+(?!implementation\b)([A-Za-z_][A-Za-z0-9_]*)\b.*?^\s*end\s+\2\s*;",
    )
    for match in pattern.finditer(aadl):
        kind, name, block = match.group(1).lower(), match.group(2), match.group(0)
        features = tuple(extract_features(block))
        if has_usable_symbols(features):
            out.append(Component(name, kind, block, features))
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
        scalar, family = infer_scalar(type_text, category)
        out.append(Feature(name, direction, category, type_text, scalar, family))
    return out


def extract_section(block: str, name: str) -> str:
    match = re.search(
        rf"(?ims)^\s*{name}\s*$"
        r"(.*?)(?=^\s*(?:features|subcomponents|connections|flows|properties|modes|calls|annex|end\b)\s*)",
        block,
    )
    return match.group(1) if match else ""


def infer_scalar(type_text: str, category: str) -> tuple[str, str]:
    category_l = category.lower()
    type_l = type_text.lower().strip()
    if "event" in category_l:
        return "event", "event"
    if "data port" not in category_l:
        return "opaque", "opaque"
    if not (
        type_l.startswith("base_types::")
        or type_l in {"integer", "int", "real", "float", "double", "boolean", "bool"}
    ):
        return "opaque", "opaque"
    if "boolean" in type_l or re.search(r"\bbool\b", type_l):
        return "bool", "bool"
    if any(token in type_l for token in ("float", "real", "double")):
        return "numeric", "real"
    if any(token in type_l for token in ("integer", "int", "unsigned", "long", "short")):
        return "numeric", "int"
    return "opaque", "opaque"


def has_usable_symbols(features: tuple[Feature, ...]) -> bool:
    return any(f.scalar in {"numeric", "bool"} for f in features)


def component_score(component: Component) -> int:
    inputs = [f for f in component.features if f.direction == "in" and f.scalar in {"numeric", "bool"}]
    outputs = [f for f in component.features if f.direction == "out" and f.scalar in {"numeric", "bool"}]
    score = 20 if inputs and outputs else 0
    score += 12 if any(f.scalar == "numeric" for f in inputs + outputs) else 0
    score += 10 if any(f.scalar == "bool" for f in inputs + outputs) else 0
    score += min(len(inputs) + len(outputs), 10)
    return score


def static_library_keys(static_libs: Path) -> tuple[set[str], set[str]]:
    names: set[str] = set()
    units: set[str] = set()
    unit_re = re.compile(r"(?im)^\s*(?:package|property\s+set)\s+([A-Za-z][A-Za-z0-9_]*)\b")
    if not static_libs.exists():
        return names, units
    for file in static_libs.glob("*.aadl"):
        names.add(file.name.lower())
        text = file.read_text(encoding="utf-8", errors="replace")
        units.update(match.group(1).lower() for match in unit_re.finditer(text))
    return names, units


def copy_case_assets(
    source_dir: Path,
    target_dir: Path,
    source_num: int,
    target_num: int,
    static_names: set[str],
    static_units: set[str],
) -> None:
    target_dir.mkdir(parents=True, exist_ok=True)
    source_base = find_case_file(source_dir, source_num, "_Base.aadl") or find_case_file(source_dir, source_num, "_Base.txt")
    if not source_base:
        raise FileNotFoundError(f"Missing base model in {source_dir}")
    aadl = source_base.read_text(encoding="utf-8", errors="replace")
    target_prefix = case_prefix(target_num)
    (target_dir / f"{target_prefix}_Base.aadl").write_text(aadl, encoding="utf-8")
    (target_dir / f"{target_prefix}_Base.txt").write_text(aadl, encoding="utf-8")

    dep_files = [
        path
        for path in source_dir.rglob("*.aadl")
        if path.resolve() != source_base.resolve()
        and not path.name.lower().startswith(f"{case_prefix(source_num).lower()}_base")
        and not is_static_duplicate(path, static_names, static_units)
    ]
    dep_dir = target_dir / target_prefix
    dep_dir.mkdir(exist_ok=True)
    seen: set[str] = set()
    for dep in dep_files:
        name = dep.name
        if name.lower() in seen:
            name = f"{dep.parent.name}_{name}"
        seen.add(name.lower())
        shutil.copy2(dep, dep_dir / name)


def copy_source_assets(
    source: dict,
    target_dir: Path,
    target_num: int,
    static_names: set[str],
    static_units: set[str],
) -> None:
    if source["kind"] == "case_dir":
        copy_case_assets(
            source_dir=source["source_dir"],
            target_dir=target_dir,
            source_num=source["source_num"],
            target_num=target_num,
            static_names=static_names,
            static_units=static_units,
        )
        return

    target_dir.mkdir(parents=True, exist_ok=True)
    target_prefix = case_prefix(target_num)
    aadl_path: Path = source["aadl_path"]
    aadl = aadl_path.read_text(encoding="utf-8", errors="replace")
    (target_dir / f"{target_prefix}_Base.aadl").write_text(aadl, encoding="utf-8")
    (target_dir / f"{target_prefix}_Base.txt").write_text(aadl, encoding="utf-8")

    dep_dir = target_dir / target_prefix
    dep_dir.mkdir(exist_ok=True)
    seen: set[str] = set()
    for dep in sorted(aadl_path.parent.glob("*.aadl")):
        if dep.resolve() == aadl_path.resolve():
            continue
        if is_static_duplicate(dep, static_names, static_units):
            continue
        name = dep.name
        if name.lower() in seen:
            name = f"{dep.parent.name}_{name}"
        seen.add(name.lower())
        shutil.copy2(dep, dep_dir / name)


def is_static_duplicate(path: Path, static_names: set[str], static_units: set[str]) -> bool:
    if path.name.lower() in static_names:
        return True
    unit_re = re.compile(r"(?im)^\s*(?:package|property\s+set)\s+([A-Za-z][A-Za-z0-9_]*)\b")
    text = path.read_text(encoding="utf-8", errors="replace")
    units = {match.group(1).lower() for match in unit_re.finditer(text)}
    return bool(units & static_units)


def write_requirement(target_dir: Path, case_num: int, source_label: str, req: Requirement) -> None:
    prefix = case_prefix(case_num)
    (target_dir / f"{prefix}_Req.txt").write_text(req.text + "\n", encoding="utf-8")
    sidecar = {
        "case": case_num,
        "letter": target_dir.name.rsplit("_", 1)[-1],
        "target": req.target,
        "action": "strong_model_regenerated_from_main_aadl_only",
        "source_label": source_label,
        "requirement_class": "agree_generatable",
        "natural_requirement": req.text,
        "expected_agree_hint": req.agree_hint,
        "trace_refs": list(req.trace_refs),
        "visible_symbols": list(req.symbols),
        "generation_source": req.source,
        "quality_score": req.score,
        "quality_policy": {
            "uses_old_req": False,
            "uses_old_sidecar_target": False,
            "uses_event_or_event_data_ports": False,
            "uses_only_base_type_scalar_ports": True,
            "style_reference": "first_110_contract_grounded_cases",
        },
    }
    (target_dir / f"{prefix}_Req_Expected.json").write_text(
        json.dumps(sidecar, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def write_manifest(output_root: Path, rows: list[dict]) -> None:
    manifest = {
        "generated_labels": len(rows),
        "policy": "Strong-model AGREE-executable requirements generated from main AADL only.",
        "uses_old_req": False,
        "uses_old_sidecar_target": False,
        "patterns": sorted({row["source"] for row in rows}),
        "rows": rows,
    }
    (output_root / "_strong_generation_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    lines = [
        "# Strong-Model AGREE Requirement Regeneration",
        "",
        f"- Generated labels: {len(rows)}",
        "- Old Req input: no",
        "- Old sidecar target input: no",
        "- Event/event data ports used: no",
        "- User-defined opaque data ports used: no",
        "",
    ]
    for row in rows[:60]:
        lines.extend(
            [
                f"## {row['new_label']} from {row['source_label']}",
                "",
                f"- Target: `{row['target']}`",
                f"- Pattern: `{row['source']}`",
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
    (output_root / "_strong_generation_summary.md").write_text("\n".join(lines), encoding="utf-8")


def write_quality_audit(output_root: Path, rows: list[dict]) -> None:
    csv_path = output_root / "_strong_generation_audit.csv"
    with csv_path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "new_label",
                "source_label",
                "target",
                "source",
                "score",
                "natural_requirement",
                "expected_agree_hint",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


def replace_sources(current_sources: Path, generated_root: Path) -> None:
    backup = current_sources.with_name("Sources_backup_before_strong_model_regen_20260607")
    suffix = 1
    while backup.exists():
        suffix += 1
        backup = current_sources.with_name(f"Sources_backup_before_strong_model_regen_20260607_{suffix}")
    shutil.move(str(current_sources), str(backup))
    shutil.copytree(generated_root, current_sources)
    print(f"Backup: {backup}")
    print(f"Replaced Sources: {current_sources}")


if __name__ == "__main__":
    raise SystemExit(main())
