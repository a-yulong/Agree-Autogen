"""Internal parsing and normalization helpers for variable LLM outputs."""

from __future__ import annotations

import ast
import json
import re
from dataclasses import dataclass, field
from typing import Any, Dict, List

from .prompting import normalize_agree_annex_delimiters, strip_code_fence


@dataclass
class RecoveryResult:
    value: Any
    actions: List[Dict[str, Any]] = field(default_factory=list)


def _action(stage: str, action: str, detail: str = "", confidence: str = "medium") -> Dict[str, Any]:
    return {"stage": stage, "action": action, "detail": detail, "confidence": confidence}


def recover_json_object(text: str, stage: str, defaults: Dict[str, Any] | None = None) -> RecoveryResult:
    actions: List[Dict[str, Any]] = []
    candidates = [text or "", strip_code_fence(text or "")]
    extracted = _extract_braced_json(text or "")
    if extracted:
        candidates.append(extracted)
        actions.append(_action(stage, "extracted_json_object", "Recovered first balanced JSON object."))
    for candidate in candidates:
        cleaned = _clean_json_like(candidate)
        for payload in (candidate, cleaned):
            try:
                value = json.loads(payload)
                if isinstance(value, dict):
                    return RecoveryResult(_apply_defaults(value, defaults, actions, stage), actions)
            except Exception:
                pass
            try:
                value = ast.literal_eval(payload)
                if isinstance(value, dict):
                    actions.append(_action(stage, "parsed_python_literal", "Parsed JSON-like object with Python literal parser."))
                    return RecoveryResult(_apply_defaults(value, defaults, actions, stage), actions)
            except Exception:
                pass
    raise ValueError("No recoverable JSON object found in model response")


def recover_section(text: str, tag: str, stage: str) -> RecoveryResult:
    pattern = rf"<{re.escape(tag)}>\s*(.*?)\s*</{re.escape(tag)}>"
    match = re.search(pattern, text or "", flags=re.DOTALL | re.IGNORECASE)
    if match:
        return RecoveryResult(match.group(1).strip(), [])
    if tag.upper() in {"REPAIRED_AADL", "FUSED_AADL"}:
        package = recover_aadl_artifact(text, stage)
        if package.value:
            package.actions.insert(0, _action(stage, f"missing_{tag.lower()}_tag", "Recovered AADL artifact without the requested section tag."))
            return package
    if "AGREE_CLAUSES" in tag.upper():
        annexes = extract_annex_blocks(text)
        if annexes:
            return RecoveryResult("\n\n".join(annexes), [_action(stage, f"missing_{tag.lower()}_tag", "Recovered annex block without the requested section tag.")])
        clauses = extract_agree_clauses(text)
        if clauses:
            return RecoveryResult("\n".join(clauses), [_action(stage, f"missing_{tag.lower()}_tag", "Recovered AGREE clauses without the requested section tag.")])
    return RecoveryResult("", [_action(stage, f"missing_{tag.lower()}_tag", "No recoverable section content found.", "low")])


def recover_aadl_artifact(text: str, stage: str) -> RecoveryResult:
    actions: List[Dict[str, Any]] = []
    cleaned = normalize_agree_annex_delimiters(strip_code_fence(text or ""))
    if cleaned != (text or "").strip():
        actions.append(_action(stage, "normalized_text_or_annex_delimiters", "Normalized code fence or annex delimiter formatting."))
    package = _extract_package_block(cleaned)
    if package:
        actions.append(_action(stage, "recovered_package_block", "Recovered complete AADL package block.", "high"))
        return RecoveryResult(package, actions)
    annexes = extract_annex_blocks(cleaned)
    if annexes:
        actions.append(_action(stage, "recovered_annex_blocks", "Recovered AGREE annex block(s) without full package.", "medium"))
        return RecoveryResult("\n\n".join(annexes), actions)
    return RecoveryResult(cleaned.strip(), actions)


def extract_annex_blocks(text: str) -> List[str]:
    normalized = normalize_agree_annex_delimiters(text or "")
    return [m.group(0).strip() for m in re.finditer(r"annex\s+agree\s*\{\*\*.*?\*\*\}\s*;", normalized, flags=re.IGNORECASE | re.DOTALL)]


def extract_agree_clauses(text: str) -> List[str]:
    normalized = normalize_agree_annex_delimiters(strip_code_fence(text or ""))
    clauses: List[str] = []
    patterns = [
        r"\b(?:guarantee|assume)\s+(?:\"[^\"]*\"\s*)?:\s*.*?;",
        r"\b(?:eq|const)\s+[A-Za-z_][A-Za-z0-9_]*\s*:.*?;",
        r"\bassign\s+[A-Za-z_][A-Za-z0-9_]*\s*=.*?;",
        r"\bassert\s*\(.*?\)\s*;",
    ]
    for pattern in patterns:
        clauses.extend(match.group(0).strip() for match in re.finditer(pattern, normalized, flags=re.IGNORECASE | re.DOTALL))
    return clauses


def recover_or_transform_annex(text: str, target_scope: str, visible_outputs: List[str], stage: str) -> RecoveryResult:
    actions: List[Dict[str, Any]] = []
    normalized = normalize_agree_annex_delimiters(strip_code_fence(text or ""))
    annexes = extract_annex_blocks(normalized)
    if annexes:
        normalized = "\n\n".join(annexes)
    if target_scope == "component_implementation":
        transformed = _transform_implementation_guarantees_to_assign(normalized, visible_outputs)
        if transformed != normalized:
            actions.append(_action(stage, "transformed_implementation_guarantee_to_assign", "Recovered assignment intent from implementation-scope guarantee."))
            normalized = transformed
    return RecoveryResult(normalized.strip(), actions)


def _transform_implementation_guarantees_to_assign(text: str, visible_outputs: List[str]) -> str:
    if not visible_outputs:
        return text
    body = text
    for output in visible_outputs:
        body = _convert_if_then_else_guarantee(body, output)
        body = _convert_implication_guarantee(body, output)
    return body


def _convert_if_then_else_guarantee(text: str, output: str) -> str:
    pattern = re.compile(
        rf"guarantee\s+(?:\"[^\"]*\"\s*)?:\s*if\s+(?P<cond>.*?)\s+then\s+{re.escape(output)}\s*=\s*(?P<then>.*?)\s+else\s+{re.escape(output)}\s*=\s*(?P<else>.*?);",
        flags=re.IGNORECASE | re.DOTALL,
    )

    def repl(match: re.Match[str]) -> str:
        cond = _one_line(match.group("cond"))
        then_value = _one_line(match.group("then"))
        else_value = _one_line(match.group("else"))
        return f"assign {output} = if {cond} then {then_value} else {else_value};"

    return pattern.sub(repl, text)


def _convert_implication_guarantee(text: str, output: str) -> str:
    pattern = re.compile(
        rf"guarantee\s+(?:\"[^\"]*\"\s*)?:\s*(?P<cond>.*?)=>\s*{re.escape(output)}\s*=\s*(?P<value>.*?);",
        flags=re.IGNORECASE | re.DOTALL,
    )

    def repl(match: re.Match[str]) -> str:
        cond = _one_line(match.group("cond"))
        value = _one_line(match.group("value"))
        return f"-- recovered conditional assignment intent: if {cond} then {output} = {value};"

    return pattern.sub(repl, text)


def _one_line(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def _extract_package_block(text: str) -> str:
    match = re.search(r"\bpackage\s+([A-Za-z_][A-Za-z0-9_]*)\b.*?^\s*end\s+\1\s*;", text or "", flags=re.IGNORECASE | re.DOTALL | re.MULTILINE)
    return match.group(0).strip() if match else ""


def _extract_braced_json(text: str) -> str:
    start = (text or "").find("{")
    if start < 0:
        return ""
    depth = 0
    in_string = False
    escape = False
    for index in range(start, len(text)):
        char = text[index]
        if in_string:
            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif char == '"':
                in_string = False
        else:
            if char == '"':
                in_string = True
            elif char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    return text[start : index + 1]
    return ""


def _clean_json_like(text: str) -> str:
    cleaned = strip_code_fence(text or "")
    cleaned = re.sub(r",\s*([}\]])", r"\1", cleaned)
    return cleaned.strip()


def _apply_defaults(value: Dict[str, Any], defaults: Dict[str, Any] | None, actions: List[Dict[str, Any]], stage: str) -> Dict[str, Any]:
    if not defaults:
        return value
    for key, default in defaults.items():
        if key not in value:
            value[key] = default
            actions.append(_action(stage, "filled_missing_field", f"Filled missing field: {key}", "high"))
    return value
