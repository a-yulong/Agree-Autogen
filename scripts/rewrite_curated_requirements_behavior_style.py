"""Rewrite traceable curated requirements into a more requirement-like style.

The input root is expected to contain sidecar `*_Expected.json` files from
`curate_sources_requirements_mixed.py`.  This script keeps the original AADL
files and trace metadata, but rewrites rebuilt connection/property checks into
more natural, implementation-grounded requirements.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DEFAULT_INPUT_ROOT = Path(r"C:\Users\25780\Desktop\Exp_Data\Sources_Curated_Traceable_Tight_20260601_renumbered")
DEFAULT_OUTPUT_ROOT = Path(r"C:\Users\25780\Desktop\Exp_Data\Sources_Curated_BehaviorStyle_20260603")

LOW_VALUE_PROPERTIES = {
    "Source_Text",
    "Source_Name",
    "Source_Language",
    "Compute_Entrypoint_Source_Text",
    "compute_entrypoint_call_sequence",
}

LOW_VALUE_PROPERTY_FRAGMENTS = {
    "source_text",
    "source_language",
    "source_name",
    "entrypoint_source_text",
}


@dataclass(frozen=True)
class RewriteResult:
    text: str
    keep: bool
    reason: str


def main() -> int:
    parser = argparse.ArgumentParser(description="Rewrite curated reqs into front-110-like natural requirements.")
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

    selected_dirs: list[Path] = []
    manifest_rows: list[dict[str, Any]] = []
    for case_dir in sorted(iter_case_dirs(input_root), key=lambda p: natural_key(p.name)):
        case_label = case_dir.name.split("_", 1)[0]
        req_path = case_dir / f"{case_label}_Req.txt"
        sidecar_path = case_dir / f"{case_label}_Req_Expected.json"
        if not req_path.exists() or not sidecar_path.exists():
            continue
        sidecar = json.loads(sidecar_path.read_text(encoding="utf-8", errors="replace"))
        action = sidecar.get("action", "")
        if action == "kept_existing_high_quality":
            rewritten_text = req_path.read_text(encoding="utf-8", errors="replace").strip()
            if has_unsupported_vague_contract(rewritten_text):
                rewritten_items = []
                keep = False
                reasons = ["excluded kept requirement with unsupported type-validity/legal-boundary wording"]
            else:
                rewritten_items = sidecar.get("requirement_items", [])
                keep = True
                reasons = ["kept existing AGREE-like behavior requirement"]
        else:
            rewritten_items = []
            reasons = []
            for item in sidecar.get("requirement_items", []):
                result = rewrite_item(item)
                reasons.append(result.reason)
                if result.keep:
                    new_item = dict(item)
                    new_item["source_text_before_behavior_style_rewrite"] = item.get("text", "")
                    new_item["text"] = result.text
                    new_item["rewrite_style"] = "front_110_inspired_requirement"
                    rewritten_items.append(new_item)
            keep = bool(rewritten_items)
            rewritten_text = format_requirement_text([item["text"] for item in rewritten_items])

        if not keep:
            manifest_rows.append(
                {
                    "label": case_dir.name,
                    "selected": False,
                    "action": action,
                    "item_count": 0,
                    "reason": "; ".join(sorted(set(reasons))) or "no kept item",
                }
            )
            continue

        dst_dir = output_root / case_dir.name
        shutil.copytree(case_dir, dst_dir)
        (dst_dir / req_path.name).write_text(rewritten_text + "\n", encoding="utf-8")
        sidecar["natural_requirement_before_behavior_style_rewrite"] = sidecar.get("natural_requirement", "")
        sidecar["natural_requirement"] = rewritten_text
        sidecar["requirement_items"] = rewritten_items
        sidecar["behavior_style_policy"] = {
            "basis": "front-110 AGREE-derived requirements favor implementable behavior, constants, assumptions, guarantees, routing, and bounded properties.",
            "excluded_property_names": sorted(LOW_VALUE_PROPERTIES),
            "rule": "Do not describe unsupported validity/legal-boundary semantics unless the AADL model exposes variables, values, or properties that can implement them.",
        }
        (dst_dir / sidecar_path.name).write_text(json.dumps(sidecar, ensure_ascii=False, indent=2), encoding="utf-8")
        selected_dirs.append(dst_dir)
        manifest_rows.append(
            {
                "label": case_dir.name,
                "selected": True,
                "action": action,
                "item_count": len(rewritten_items),
                "reason": "; ".join(sorted(set(reasons))),
            }
        )

    rewrite_maps(input_root, output_root, selected_dirs)
    write_readme(output_root, manifest_rows)
    write_manifest(output_root, manifest_rows)
    print(f"Input case labels: {len(list(iter_case_dirs(input_root)))}")
    print(f"Selected case labels: {len(selected_dirs)}")
    print(f"Output root: {output_root}")
    return 0


def iter_case_dirs(root: Path) -> list[Path]:
    dirs = []
    for child in root.iterdir():
        if child.is_dir() and re.fullmatch(r"Case\d+_[A-Z]", child.name):
            dirs.append(child)
    return dirs


def natural_key(text: str) -> list[Any]:
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", text)]


def rewrite_item(item: dict[str, Any]) -> RewriteResult:
    check = item.get("expected_check") or {}
    kind = check.get("kind", "")
    if kind == "connection":
        return rewrite_connection(item, check)
    if kind == "property":
        return rewrite_property(item, check)
    return RewriteResult(item.get("text", "").strip(), True, "kept non-rebuilt behavior item")


def rewrite_connection(item: dict[str, Any], check: dict[str, Any]) -> RewriteResult:
    owner = check.get("owner", "")
    connection = check.get("connection", "")
    source = check.get("source", "")
    destination = check.get("destination", "")
    flow = infer_flow_label(source, destination)
    text = (
        f"The {owner} implementation shall route the {flow} from {source} "
        f"to {destination} through connection {connection}."
    )
    return RewriteResult(text, True, "rewrote connection as routing requirement")


def rewrite_property(item: dict[str, Any], check: dict[str, Any]) -> RewriteResult:
    owner = check.get("owner", "")
    element = check.get("element", "")
    prop = check.get("property", "")
    value = check.get("value", "")
    bare = prop.split("::")[-1]
    if bare in LOW_VALUE_PROPERTIES or prop in LOW_VALUE_PROPERTIES or any(fragment in bare.lower() for fragment in LOW_VALUE_PROPERTY_FRAGMENTS):
        return RewriteResult("", False, f"excluded low-value metadata property {prop}")

    target = f"connection {element}" if element else f"the {owner} implementation"
    lower_bare = bare.lower()
    if lower_bare in {"dispatch_protocol"}:
        text = f"The {owner} implementation shall execute using the {value} dispatch protocol."
    elif lower_bare == "period":
        text = f"The {owner} implementation shall execute with a period of {value}."
    elif lower_bare == "deadline":
        text = f"The {owner} implementation shall meet a deadline of {value}."
    elif lower_bare in {"compute_execution_time", "compute_execution_time"}:
        text = f"The {owner} implementation shall complete its compute execution within {value}."
    elif lower_bare == "compute_entrypoint":
        text = f"The {owner} implementation shall invoke compute entrypoint {value}."
    elif lower_bare == "priority":
        text = f"The {owner} implementation shall run at priority {value}."
    elif "required_bandwidth" in lower_bare:
        text = f"The {owner} implementation shall reserve {value} bandwidth for connection {element}."
    elif "timing" == lower_bare:
        text = f"The {owner} implementation shall use {value} communication timing on connection {element}."
    elif "latency" == lower_bare:
        text = f"The {owner} implementation shall keep the latency of {element or owner} within {value}."
    elif "processor_binding" in lower_bare:
        applies = applies_target(value)
        text = f"The {owner} implementation shall bind {applies or 'the specified element'} to processor {clean_reference(value)}."
    elif "memory_binding" in lower_bare:
        applies = applies_target(value)
        text = f"The {owner} implementation shall bind {applies or 'the specified element'} to memory {clean_reference(value)}."
    elif "function_binding" in lower_bare:
        applies = applies_target(value)
        text = f"The {owner} implementation shall bind {applies or 'the specified element'} to function {clean_reference(value)}."
    elif lower_bare in {"mass", "power_consume"}:
        noun = "mass" if lower_bare == "mass" else "power consumption"
        text = f"The {owner} implementation shall allocate {noun} as {value}."
    elif lower_bare == "dispatch_offset":
        text = f"The {owner} implementation shall start dispatch with an offset of {value}."
    else:
        return RewriteResult("", False, f"excluded unsupported metadata/property {prop}")
    return RewriteResult(text, True, "rewrote property as implementation requirement")


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


def has_unsupported_vague_contract(text: str) -> bool:
    lower = text.lower()
    unsupported_pairs = [
        ("legal", "type"),
        ("valid", "type"),
        ("valid", "data"),
        ("conform", "data type"),
        ("data type constraints", ""),
        ("normal operation", ""),
        ("environmental conditions", ""),
    ]
    for left, right in unsupported_pairs:
        if left in lower and (not right or right in lower):
            return True
    return False


def format_requirement_text(texts: list[str]) -> str:
    return " ".join(normalize_sentence(text) for text in texts if text.strip())


def normalize_sentence(text: str) -> str:
    text = re.sub(r"\s+", " ", text.strip())
    return text if text.endswith(".") else text + "."


def rewrite_maps(input_root: Path, output_root: Path, selected_dirs: list[Path]) -> None:
    selected_labels = {path.name for path in selected_dirs}
    renumber = input_root / "Case_Renumber_Map.csv"
    if renumber.exists():
        rows = [row for row in csv.DictReader(renumber.open("r", encoding="utf-8-sig")) if row.get("NewLabel") in selected_labels]
        if rows:
            with (output_root / "Case_Renumber_Map.csv").open("w", encoding="utf-8-sig", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
                writer.writeheader()
                writer.writerows(rows)
    source_map = input_root / "Case_Source_Map.csv"
    if source_map.exists():
        selected_cases = {label.split("_", 1)[0].replace("Case", "").lstrip("0") or "0" for label in selected_labels}
        rows = [row for row in csv.DictReader(source_map.open("r", encoding="utf-8-sig")) if str(int(row.get("Case", "0"))) in selected_cases]
        if rows:
            with (output_root / "Case_Source_Map.csv").open("w", encoding="utf-8-sig", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
                writer.writeheader()
                writer.writerows(rows)


def write_manifest(output_root: Path, rows: list[dict[str, Any]]) -> None:
    fields = ["label", "selected", "action", "item_count", "reason"]
    with (output_root / "BehaviorStyle_Manifest.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_readme(output_root: Path, rows: list[dict[str, Any]]) -> None:
    selected = [row for row in rows if row["selected"]]
    kept = [row for row in selected if row["action"] == "kept_existing_high_quality"]
    rebuilt = [row for row in selected if row["action"] == "rebuilt_from_aadl"]
    total_items = sum(int(row["item_count"]) for row in selected)
    lines = [
        "# Behavior-Style Curated Requirements",
        "",
        "This dataset rewrites the traceable curated requirements into a more natural",
        "front-110-inspired style. AADL files and trace sidecars are preserved.",
        "",
        "## Policy",
        "",
        "- Keep AGREE-derived/high-quality behavior requirements.",
        "- Rewrite connection checks as routing/signal-flow requirements.",
        "- Rewrite scheduling/resource/binding properties as implementation requirements.",
        "- Exclude low-value code metadata properties such as Source_Text and Source_Language.",
        "- Do not invent validity fields, data ranges, legal boundaries, or normal-operation flags not present in the AADL model.",
        "",
        "## Counts",
        "",
        f"- Selected A/B labels: {len(selected)}",
        f"- Kept behavior labels: {len(kept)}",
        f"- Rebuilt labels: {len(rebuilt)}",
        f"- Requirement items: {total_items}",
    ]
    (output_root / "DATASET_README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
