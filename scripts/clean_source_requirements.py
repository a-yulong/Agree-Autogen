"""Clean source requirement texts using local AADL context.

The script rewrites `CaseXX_Req.txt` files into clearer technical English while
keeping them as natural-language requirements. It does not generate AGREE and it
does not add any validation or quality gate to the pipeline.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_ROOT = Path(r"C:\Users\25780\Desktop\Exp_Data\Sources")
DEFAULT_REPORT_ROOT = Path(r"C:\Users\25780\Desktop\Exp_Data\SourceReq_Cleaning")
KEY_SOURCE_FILES = [
    Path(r"C:\Users\25780\Documents\Playground\run_qwen3_e_experiments.py"),
    Path(r"C:\Users\25780\Documents\Playground\run_demo16_cases_01_10A.py"),
    Path(r"C:\Users\25780\Documents\Playground\run_openrouter_cases_A.py"),
]


@dataclass(frozen=True)
class CaseItem:
    case_num: int
    letter: str
    case_dir: Path
    label: str
    req_path: Path
    base_path: Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Clean AGREE-AutoGen source requirement files.")
    parser.add_argument("--source-root", default=str(DEFAULT_SOURCE_ROOT))
    parser.add_argument("--report-root", default=str(DEFAULT_REPORT_ROOT))
    parser.add_argument("--model", default=os.environ.get("AGREE_REQ_CLEAN_MODEL") or os.environ.get("AGREE_MODEL_NAME") or "qwen3-coder-30b-a3b-instruct")
    parser.add_argument("--base-url", default=os.environ.get("AGREE_MODEL_BASE_URL") or "https://api.silra.cn/v1")
    parser.add_argument("--api-key", default=os.environ.get("AGREE_MODEL_API_KEY") or os.environ.get("AGREE_LLM_API_KEY") or os.environ.get("OPENROUTER_API_KEY") or "")
    parser.add_argument("--cases", default="", help="Comma-separated case numbers or ranges, e.g. 1,5,20-30.")
    parser.add_argument("--letters", default="A,B", help="Comma-separated letters, default A,B.")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--write", action="store_true", help="Overwrite active Req.txt files after backing them up.")
    parser.add_argument("--force", action="store_true", help="Clean even when a previous cleaned copy exists in the run cache.")
    parser.add_argument("--sleep", type=float, default=0.0)
    args = parser.parse_args()

    source_root = Path(args.source_root)
    stamp = time.strftime("%Y%m%d_%H%M%S")
    run_root = Path(args.report_root) / f"req_clean_{stamp}"
    run_root.mkdir(parents=True, exist_ok=True)
    backup_root = source_root / f"_req_backup_before_clean_{stamp}"
    if args.write:
        backup_root.mkdir(parents=True, exist_ok=True)

    api_key = args.api_key or find_api_key()
    if not api_key:
        raise RuntimeError("No LLM API key found. Set AGREE_MODEL_API_KEY, AGREE_LLM_API_KEY, or OPENROUTER_API_KEY.")

    source_map = load_source_map(source_root / "Case_Source_Map.csv")
    items = discover_cases(source_root, parse_cases(args.cases), parse_letters(args.letters))
    if args.limit:
        items = items[: args.limit]
    print(f"Requirement files selected: {len(items)}", flush=True)
    print(f"Run root: {run_root}", flush=True)
    print(f"Write mode: {args.write}", flush=True)

    cache_path = run_root / "clean_cache.json"
    cache: dict[str, str] = {}
    manifest: list[dict[str, Any]] = []
    failures: list[dict[str, str]] = []

    for index, item in enumerate(items, 1):
        print(f"[{index}/{len(items)}] {item.label}", flush=True)
        try:
            original_req = item.req_path.read_text(encoding="utf-8", errors="replace").strip()
            aadl_text = item.base_path.read_text(encoding="utf-8", errors="replace")
            map_row = source_map.get(item.case_num, {})
            target = map_row.get("Target", "")
            context = build_aadl_context(aadl_text, target)
            prompt = build_prompt(item, original_req, context, map_row)
            cache_key = sha256(
                json.dumps(
                    {
                        "requirement": original_req,
                        "context": context,
                        "source": map_row.get("Source", ""),
                        "target": map_row.get("Target", ""),
                        "package": map_row.get("Package", ""),
                    },
                    ensure_ascii=False,
                    sort_keys=True,
                )
            )
            case_report = run_root / item.label
            case_report.mkdir(parents=True, exist_ok=True)
            (case_report / "llm_input.txt").write_text(prompt, encoding="utf-8")
            if cache_key in cache and not args.force:
                cleaned = cache[cache_key]
            else:
                cleaned = call_llm(args.base_url, api_key, args.model, prompt)
                cache[cache_key] = cleaned
                cache_path.write_text(json.dumps(cache, indent=2, ensure_ascii=False), encoding="utf-8")
            cleaned = normalize_cleaned_requirement(cleaned)
            (case_report / "original_req.txt").write_text(original_req + "\n", encoding="utf-8")
            (case_report / "cleaned_req.txt").write_text(cleaned + "\n", encoding="utf-8")
            (case_report / "llm_output.txt").write_text(cleaned + "\n", encoding="utf-8")
            changed = cleaned.strip() != original_req.strip()
            if args.write and changed:
                rel_dir = item.case_dir.relative_to(source_root)
                backup_dir = backup_root / rel_dir
                backup_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item.req_path, backup_dir / item.req_path.name)
                item.req_path.write_text(cleaned + "\n", encoding="utf-8")
            manifest.append(
                {
                    "case": item.case_num,
                    "letter": item.letter,
                    "label": item.label,
                    "changed": changed,
                    "source": map_row.get("Source", ""),
                    "target": target,
                    "req_path": str(item.req_path),
                    "report_dir": str(case_report),
                }
            )
            if args.sleep:
                time.sleep(args.sleep)
        except Exception as exc:  # noqa: BLE001
            print(f"FAILED {item.label}: {exc}", flush=True)
            failures.append({"label": item.label, "error": repr(exc)})

    write_manifest(run_root, manifest, failures, args.write, backup_root if args.write else None)
    print(f"Done. changed={sum(1 for row in manifest if row['changed'])}; failures={len(failures)}", flush=True)
    print(f"Summary: {run_root / 'summary.md'}", flush=True)
    return 0 if not failures else 1


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
    values = {part.strip().upper() for part in text.split(",") if part.strip()}
    return values or {"A", "B"}


def discover_cases(source_root: Path, case_filter: set[int] | None, letters: set[str]) -> list[CaseItem]:
    items: list[CaseItem] = []
    for case_dir in sorted(source_root.iterdir(), key=lambda p: natural_key(p.name)):
        if not case_dir.is_dir():
            continue
        match = re.fullmatch(r"Case(\d+)_([AB])", case_dir.name, flags=re.IGNORECASE)
        if not match:
            continue
        case_num = int(match.group(1))
        letter = match.group(2).upper()
        if case_filter is not None and case_num not in case_filter:
            continue
        if letter not in letters:
            continue
        label = f"Case{case_num:02d}_{letter}"
        case_label = f"Case{case_num:02d}"
        req_path = case_dir / f"{case_label}_Req.txt"
        base_path = case_dir / f"{case_label}_Base.aadl"
        if not base_path.exists():
            base_path = case_dir / f"{case_label}_Base.txt"
        if req_path.exists() and base_path.exists():
            items.append(CaseItem(case_num, letter, case_dir, label, req_path, base_path))
    return items


def natural_key(text: str) -> list[Any]:
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", text)]


def load_source_map(path: Path) -> dict[int, dict[str, str]]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return {int(row["Case"]): row for row in csv.DictReader(handle) if row.get("Case", "").isdigit()}


def build_aadl_context(aadl_text: str, target: str) -> str:
    header = extract_package_header(aadl_text)
    summaries = summarize_components(aadl_text)
    target_blocks = []
    if target:
        target_blocks.extend(extract_component_blocks(aadl_text, target))
        if "." in target:
            target_blocks.extend(extract_component_blocks(aadl_text, target.split(".", 1)[0]))
        else:
            target_blocks.extend(extract_component_blocks(aadl_text, f"{target}."))
    unique_blocks = []
    seen = set()
    for block in target_blocks:
        key = sha256(block)
        if key not in seen:
            seen.add(key)
            unique_blocks.append(block)
    target_context = "\n\n".join(unique_blocks[:8])
    if len(target_context) > 9000:
        target_context = target_context[:9000] + "\n-- [context truncated]"
    component_summary = "\n".join(summaries[:80])
    return (
        "<package_context>\n"
        f"{header}\n"
        "</package_context>\n\n"
        "<target_component_blocks>\n"
        f"{target_context or 'No exact target block was isolated; use the component summary.'}\n"
        "</target_component_blocks>\n\n"
        "<component_summary>\n"
        f"{component_summary}\n"
        "</component_summary>"
    )


def extract_package_header(aadl_text: str) -> str:
    lines = []
    for line in aadl_text.splitlines():
        stripped = line.strip()
        if stripped.lower().startswith(("package ", "public", "with ")):
            lines.append(line)
        if len(lines) >= 40:
            break
    return "\n".join(lines)


def extract_component_blocks(aadl_text: str, name_or_prefix: str) -> list[str]:
    escaped = re.escape(name_or_prefix.rstrip("."))
    if name_or_prefix.endswith("."):
        name_pattern = escaped + r"\.[A-Za-z_][A-Za-z0-9_]*"
    else:
        name_pattern = escaped
    kind = r"(?:system|process|thread|device|abstract|subprogram|data|bus|memory|processor)"
    start_re = re.compile(rf"(?im)^\s*{kind}(?:\s+implementation)?\s+({name_pattern})\b.*$")
    blocks: list[str] = []
    for match in start_re.finditer(aadl_text):
        comp_name = match.group(1)
        end_re = re.compile(rf"(?im)^\s*end\s+{re.escape(comp_name)}\s*;")
        end = end_re.search(aadl_text, match.end())
        if end:
            blocks.append(aadl_text[match.start() : end.end()].strip())
    return blocks


def summarize_components(aadl_text: str) -> list[str]:
    kind = r"(system|process|thread|device|abstract|subprogram|data|bus|memory|processor)"
    comp_re = re.compile(rf"(?im)^\s*{kind}(?:\s+implementation)?\s+([A-Za-z_][A-Za-z0-9_.]*)\b")
    feature_re = re.compile(r"(?im)^\s*([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(in|out|in out)?\s*(event\s+data|event|data|feature|parameter|bus access|data access)?\s*(?:port|access|parameter)?\s*([^;{]*)")
    summaries = []
    for match in comp_re.finditer(aadl_text):
        name = match.group(2)
        end_match = re.search(rf"(?im)^\s*end\s+{re.escape(name)}\s*;", aadl_text[match.end() :])
        block = aadl_text[match.start() : match.end() + (end_match.end() if end_match else 1200)]
        features = []
        for fmatch in feature_re.finditer(block):
            feature = " ".join(part.strip() for part in fmatch.groups(default="") if part.strip())
            if feature and not feature.lower().startswith(("features", "properties")):
                features.append(feature)
        if features:
            summaries.append(f"{name}: " + "; ".join(features[:18]))
        else:
            summaries.append(f"{name}: no explicit features in isolated block")
    return summaries


def build_prompt(item: CaseItem, original_req: str, aadl_context: str, map_row: dict[str, str]) -> str:
    metadata = {
        "case": item.case_num,
        "letter": item.letter,
        "source": map_row.get("Source", ""),
        "package": map_row.get("Package", ""),
        "kind": map_row.get("Kind", ""),
        "target": map_row.get("Target", ""),
    }
    return f"""You clean natural-language requirements for an AADL-to-AGREE generation dataset.

Goal:
Rewrite the requirement so it is precise, scoped to the intended AADL component, and easier for a downstream LLM to translate into AGREE.

What to preserve:
- Preserve the original intent and all explicitly stated behavior.
- Preserve exact AADL identifiers when they are relevant: component names, implementation names, port names, data types, constants, and units.
- Keep the output as natural-language requirements. Do not write AGREE, AADL annexes, JSON, markdown headings, commentary, or analysis.

How to improve:
- Replace vague references such as "the component", "valid state", "safe boundary", "device output", or "input command" with the exact target component, implementation, ports, and data types visible in the AADL context when the intent supports it.
- If a requirement mentions assumptions or guarantees, make clear which facts are assumptions about inputs/environment and which facts are guarantees about outputs/internal behavior.
- If the AADL context only exposes Boolean ports, describe Boolean constraints as Boolean conditions, not numeric 0/1 comparisons.
- If the AADL context exposes numeric ports, keep numeric comparisons type-compatible and use the requirement's stated constants.
- Do not invent domain behavior that is not supported by the original requirement or by names/comments in the AADL model.

Return only the cleaned requirement text.

<case_metadata>
{json.dumps(metadata, ensure_ascii=False, indent=2)}
</case_metadata>

<original_requirement>
{original_req}
</original_requirement>

{aadl_context}
"""


def call_llm(base_url: str, api_key: str, model: str, prompt: str) -> str:
    url = base_url.rstrip("/") + "/chat/completions"
    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a careful requirements editor for AADL and AGREE datasets."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.0,
        "max_tokens": 1200,
    }
    data = json.dumps(body, ensure_ascii=False).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    if "openrouter.ai" in base_url:
        headers["X-OpenRouter-Title"] = "AGREE-AutoGen Source Requirement Cleaning"
    last_error: Exception | None = None
    for attempt in range(1, 4):
        try:
            request = urllib.request.Request(url, data=data, headers=headers, method="POST")
            with urllib.request.urlopen(request, timeout=180) as response:
                payload = json.loads(response.read().decode("utf-8", errors="replace"))
            text = (payload["choices"][0].get("message", {}).get("content") or "").strip()
            if not text:
                raise RuntimeError("empty LLM response")
            return text
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")[:1200]
            last_error = RuntimeError(f"HTTP {exc.code}: {detail}")
        except Exception as exc:  # noqa: BLE001
            last_error = exc
        time.sleep(2 * attempt)
    raise RuntimeError(f"LLM call failed after retries: {last_error}")


def normalize_cleaned_requirement(text: str) -> str:
    text = re.sub(r"(?is)<think>.*?</think>", "", text or "").strip()
    fence = re.search(r"(?is)```(?:text|markdown)?\s*(.*?)```", text)
    if fence:
        text = fence.group(1).strip()
    text = re.sub(r"(?im)^\s*(cleaned requirement|rewritten requirement)\s*:\s*", "", text).strip()
    replacements = {
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2013": "-",
        "\u2014": "-",
        "\u2026": "...",
        "鈥攕": "-s",
        "鈥攁": "-a",
        "鈥斺": "-",
        "鈥": "'",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def find_api_key() -> str:
    for path in KEY_SOURCE_FILES:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        match = re.search(r'API_KEY\s*=\s*"([^"]+)"', text)
        if match:
            return match.group(1)
        match = re.search(r'DEFAULT_API_KEY\s*=\s*"([^"]+)"', text)
        if match:
            return match.group(1)
    return ""


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()


def write_manifest(
    run_root: Path,
    manifest: list[dict[str, Any]],
    failures: list[dict[str, str]],
    write_mode: bool,
    backup_root: Path | None,
) -> None:
    (run_root / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    (run_root / "failures.json").write_text(json.dumps(failures, indent=2, ensure_ascii=False), encoding="utf-8")
    changed = sum(1 for row in manifest if row.get("changed"))
    lines = [
        "# Source Requirement Cleaning",
        "",
        f"- Processed: {len(manifest)}",
        f"- Changed: {changed}",
        f"- Failed: {len(failures)}",
        f"- Write mode: {write_mode}",
    ]
    if backup_root is not None:
        lines.append(f"- Backup root: {backup_root}")
    lines.extend(["", "## Changed Cases"])
    for row in manifest:
        if row.get("changed"):
            lines.append(f"- {row['label']}: {row.get('source', '')} target={row.get('target', '')}")
    if failures:
        lines.extend(["", "## Failures"])
        for failure in failures:
            lines.append(f"- {failure['label']}: {failure['error']}")
    (run_root / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
