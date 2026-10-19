"""Rewrite curated traceable requirements into paragraph-style requirements.

The generated `Req.txt` files are intentionally natural-language paragraphs.
Detailed per-item traceability remains in each `*_Expected.json` sidecar.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
from pathlib import Path
from typing import Any


DEFAULT_INPUT_ROOT = Path(r"C:\Users\25780\Desktop\Exp_Data\Sources_Curated_BehaviorStyle_20260603")
DEFAULT_OUTPUT_ROOT = Path(r"C:\Users\25780\Desktop\Exp_Data\Sources_Curated_ParagraphStyle_20260603")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create paragraph-style req texts with trace sidecars.")
    parser.add_argument("--input-root", default=str(DEFAULT_INPUT_ROOT))
    parser.add_argument("--output-root", default=str(DEFAULT_OUTPUT_ROOT))
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    input_root = Path(args.input_root)
    output_root = Path(args.output_root)
    if output_root.exists():
        if not args.force:
            raise RuntimeError(f"Output root exists: {output_root}. Use --force.")
        shutil.rmtree(output_root)
    output_root.mkdir(parents=True, exist_ok=True)

    selected: list[Path] = []
    manifest_rows: list[dict[str, Any]] = []
    for case_dir in sorted(iter_case_dirs(input_root), key=lambda p: natural_key(p.name)):
        case_label = case_dir.name.split("_", 1)[0]
        req_path = case_dir / f"{case_label}_Req.txt"
        sidecar_path = case_dir / f"{case_label}_Req_Expected.json"
        if not req_path.exists() or not sidecar_path.exists():
            continue
        sidecar = json.loads(sidecar_path.read_text(encoding="utf-8", errors="replace"))
        if sidecar.get("action") == "kept_existing_high_quality":
            paragraph = req_path.read_text(encoding="utf-8", errors="replace").strip()
            reason = "kept existing paragraph-style behavior requirement"
        else:
            paragraph = build_paragraph(sidecar)
            reason = "grouped traceable items into paragraph-style requirement"
        if not paragraph:
            manifest_rows.append({"label": case_dir.name, "selected": False, "reason": "empty paragraph"})
            continue
        dst_dir = output_root / case_dir.name
        shutil.copytree(case_dir, dst_dir)
        (dst_dir / req_path.name).write_text(paragraph + "\n", encoding="utf-8")
        sidecar["natural_requirement_before_paragraph_rewrite"] = sidecar.get("natural_requirement", "")
        sidecar["natural_requirement"] = paragraph
        sidecar["paragraph_style_policy"] = {
            "rule": "Req.txt is written as a natural-language requirement paragraph; per-item traceability stays in requirement_items.",
            "basis": "Front-110 AGREE-derived requirements generally combine function, assumptions, guarantees, and implementation notes into 1-4 sentence paragraphs.",
        }
        (dst_dir / sidecar_path.name).write_text(json.dumps(sidecar, ensure_ascii=False, indent=2), encoding="utf-8")
        selected.append(dst_dir)
        manifest_rows.append({"label": case_dir.name, "selected": True, "reason": reason})

    copy_maps(input_root, output_root, {path.name for path in selected})
    write_manifest(output_root, manifest_rows)
    write_readme(output_root, selected)
    print(f"Input labels: {len(list(iter_case_dirs(input_root)))}")
    print(f"Selected labels: {len(selected)}")
    print(f"Output root: {output_root}")
    return 0


def iter_case_dirs(root: Path) -> list[Path]:
    return [child for child in root.iterdir() if child.is_dir() and re.fullmatch(r"Case\d+_[A-Z]", child.name)]


def natural_key(text: str) -> list[Any]:
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", text)]


def build_paragraph(sidecar: dict[str, Any]) -> str:
    items = sidecar.get("requirement_items", [])
    if not items:
        return ""
    target = sidecar.get("target", "")
    owner = common_owner(items) or target or "The target component"
    component = owner.split(".", 1)[0] if owner else target

    connections = [item for item in items if (item.get("expected_check") or {}).get("kind") == "connection"]
    properties = [item for item in items if (item.get("expected_check") or {}).get("kind") == "property"]

    sentences: list[str] = []
    intro = build_intro(component, owner, connections, properties)
    if intro:
        sentences.append(intro)
    flow_sentence = build_flow_sentence(owner, connections)
    if flow_sentence:
        sentences.append(flow_sentence)
    timing_sentence = build_timing_sentence(owner, properties)
    if timing_sentence:
        sentences.append(timing_sentence)
    resource_sentence = build_resource_sentence(owner, properties)
    if resource_sentence:
        sentences.append(resource_sentence)
    binding_sentence = build_binding_sentence(owner, properties)
    if binding_sentence:
        sentences.append(binding_sentence)
    entry_sentence = build_entrypoint_sentence(owner, properties)
    if entry_sentence:
        sentences.append(entry_sentence)
    return " ".join(sentence for sentence in sentences if sentence)


def common_owner(items: list[dict[str, Any]]) -> str:
    owners = []
    for item in items:
        check = item.get("expected_check") or {}
        owner = check.get("owner")
        if owner:
            owners.append(owner)
    if not owners:
        return ""
    return max(set(owners), key=owners.count)


def build_intro(component: str, owner: str, connections: list[dict[str, Any]], properties: list[dict[str, Any]]) -> str:
    if connections and properties:
        return f"The {component} component shall define the implementation-level data routing and execution constraints for {owner}."
    if connections:
        return f"The {component} component shall define the implementation-level signal routing for {owner}."
    if properties:
        categories = property_categories(properties)
        if "timing" in categories:
            return f"The {component} component shall execute according to the scheduling and timing constraints defined for {owner}."
        if "binding" in categories:
            return f"The {component} component shall use the deployment bindings defined for {owner}."
        if "resource" in categories:
            return f"The {component} component shall respect the resource constraints allocated to {owner}."
        return f"The {component} component shall follow the implementation constraints defined for {owner}."
    return ""


def property_categories(properties: list[dict[str, Any]]) -> set[str]:
    categories: set[str] = set()
    for item in properties:
        name = basename((item.get("expected_check") or {}).get("property", "")).lower()
        if name in {"dispatch_protocol", "period", "deadline", "compute_execution_time", "compute_execution_time", "priority", "dispatch_offset"}:
            categories.add("timing")
        if any(token in name for token in ["binding"]):
            categories.add("binding")
        if name in {"mass", "power_consume", "latency"} or "required_bandwidth" in name or name == "timing":
            categories.add("resource")
    return categories


def build_flow_sentence(owner: str, connections: list[dict[str, Any]]) -> str:
    if not connections:
        return ""
    parts = []
    for item in connections[:4]:
        check = item.get("expected_check") or {}
        source = check.get("source", "")
        dest = check.get("destination", "")
        conn = check.get("connection", "")
        flow = infer_flow_label(source, dest)
        parts.append(f"{flow} from {source} to {dest} through {conn}")
    if len(parts) == 1:
        return f"In the implementation layer, {owner} shall route the {parts[0]}."
    return f"In the implementation layer, {owner} shall route " + join_series(parts) + "."


def build_timing_sentence(owner: str, properties: list[dict[str, Any]]) -> str:
    by_name = property_map(properties)
    pieces = []
    if "Dispatch_Protocol" in by_name:
        pieces.append(f"use the {by_name['Dispatch_Protocol']} dispatch protocol")
    if "Period" in by_name:
        pieces.append(f"execute with a period of {by_name['Period']}")
    if "Deadline" in by_name or "deadline" in by_name:
        pieces.append(f"meet a deadline of {by_name.get('Deadline') or by_name.get('deadline')}")
    compute = by_name.get("Compute_Execution_Time") or by_name.get("Compute_Execution_time")
    if compute:
        pieces.append(f"complete compute execution within {compute}")
    if "Priority" in by_name:
        pieces.append(f"run at priority {by_name['Priority']}")
    if "Dispatch_Offset" in by_name:
        pieces.append(f"start dispatch with an offset of {by_name['Dispatch_Offset']}")
    if not pieces:
        return ""
    return f"The implementation shall " + join_series(pieces) + "."


def build_resource_sentence(owner: str, properties: list[dict[str, Any]]) -> str:
    resource_phrases = []
    for item in properties:
        check = item.get("expected_check") or {}
        name = basename(check.get("property", ""))
        value = check.get("value", "")
        element = check.get("element", "")
        if "Required_Bandwidth" in name:
            resource_phrases.append(f"reserve {value} bandwidth for connection {element}")
        elif name == "Mass":
            resource_phrases.append(f"allocate mass as {value}")
        elif name == "Power_Consume":
            resource_phrases.append(f"allocate power consumption as {value}")
        elif name == "Latency":
            resource_phrases.append(f"keep the latency of {element or owner} within {value}")
        elif name.lower() == "timing" and element:
            resource_phrases.append(f"use {value} communication timing on connection {element}")
    if not resource_phrases:
        return ""
    return f"Additionally, {owner} shall " + join_series(resource_phrases) + "."


def build_binding_sentence(owner: str, properties: list[dict[str, Any]]) -> str:
    phrases = []
    for item in properties:
        check = item.get("expected_check") or {}
        name = basename(check.get("property", "")).lower()
        value = check.get("value", "")
        if "processor_binding" in name:
            phrases.append(f"bind {applies_target(value) or 'the specified element'} to processor {clean_reference(value)}")
        elif "memory_binding" in name:
            phrases.append(f"bind {applies_target(value) or 'the specified element'} to memory {clean_reference(value)}")
        elif "function_binding" in name:
            phrases.append(f"bind {applies_target(value) or 'the specified element'} to function {clean_reference(value)}")
    if not phrases:
        return ""
    return f"The deployment mapping shall " + join_series(phrases[:4]) + "."


def build_entrypoint_sentence(owner: str, properties: list[dict[str, Any]]) -> str:
    entries = []
    for item in properties:
        check = item.get("expected_check") or {}
        name = basename(check.get("property", ""))
        value = check.get("value", "")
        if name == "Compute_Entrypoint":
            entries.append(value)
    if not entries:
        return ""
    return f"The implementation shall invoke compute entrypoint {entries[0]}."


def property_map(properties: list[dict[str, Any]]) -> dict[str, str]:
    values = {}
    for item in properties:
        check = item.get("expected_check") or {}
        values.setdefault(basename(check.get("property", "")), check.get("value", ""))
    return values


def basename(name: str) -> str:
    return name.split("::")[-1]


def infer_flow_label(source: str, destination: str) -> str:
    text = f"{source} {destination}".lower()
    if any(token in text for token in ["ctrl", "control", "cmd", "command"]):
        return "control signal"
    if any(token in text for token in ["data", "raw", "msg", "message", "table", "packet"]):
        return "data flow"
    if any(token in text for token in ["event", "toggle", "request"]):
        return "event flow"
    return "signal flow"


def clean_reference(value: str) -> str:
    match = re.search(r"\(reference\s*\(([^)]+)\)\)", value, flags=re.IGNORECASE)
    return match.group(1) if match else value


def applies_target(value: str) -> str:
    match = re.search(r"\bapplies\s+to\s+(.+)$", value, flags=re.IGNORECASE)
    return match.group(1).strip() if match else ""


def join_series(parts: list[str]) -> str:
    parts = [part for part in parts if part]
    if not parts:
        return ""
    if len(parts) == 1:
        return parts[0]
    if len(parts) == 2:
        return f"{parts[0]} and {parts[1]}"
    return ", ".join(parts[:-1]) + f", and {parts[-1]}"


def copy_maps(input_root: Path, output_root: Path, selected_labels: set[str]) -> None:
    for name, label_field in [("Case_Renumber_Map.csv", "NewLabel")]:
        src = input_root / name
        if not src.exists():
            continue
        rows = [row for row in csv.DictReader(src.open("r", encoding="utf-8-sig")) if row.get(label_field) in selected_labels]
        if rows:
            with (output_root / name).open("w", encoding="utf-8-sig", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
                writer.writeheader()
                writer.writerows(rows)
    source_map = input_root / "Case_Source_Map.csv"
    if source_map.exists():
        selected_cases = {str(int(label.split("_", 1)[0].replace("Case", ""))) for label in selected_labels}
        rows = [row for row in csv.DictReader(source_map.open("r", encoding="utf-8-sig")) if str(int(row.get("Case", "0"))) in selected_cases]
        if rows:
            with (output_root / "Case_Source_Map.csv").open("w", encoding="utf-8-sig", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
                writer.writeheader()
                writer.writerows(rows)


def write_manifest(output_root: Path, rows: list[dict[str, Any]]) -> None:
    fields = ["label", "selected", "reason"]
    with (output_root / "ParagraphStyle_Manifest.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_readme(output_root: Path, selected: list[Path]) -> None:
    unique_cases = {int(re.match(r"Case(\d+)_", path.name).group(1)) for path in selected}
    lines = [
        "# Paragraph-Style Curated Requirements",
        "",
        "This dataset keeps traceability metadata from the behavior-style root,",
        "but rewrites rebuilt `Req.txt` files as paragraph-style natural-language",
        "requirements rather than item-by-item AADL fact lists.",
        "",
        "## Counts",
        "",
        f"- Selected A/B labels: {len(selected)}",
        f"- Unique cases: {len(unique_cases)}",
        "",
        "## Design",
        "",
        "- Natural-language text is grouped by implementation purpose.",
        "- Connection items are expressed as data/control/signal routing behavior.",
        "- Scheduling, timing, resource, and binding properties are expressed as implementation constraints.",
        "- Detailed per-item traceability remains in each `*_Expected.json` sidecar.",
    ]
    (output_root / "DATASET_README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
