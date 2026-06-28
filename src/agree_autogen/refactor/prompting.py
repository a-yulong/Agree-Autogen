"""Prompt-template loading and section extraction helpers."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict


class PromptLibrary:
    def __init__(self, prompts_dir: str | Path | None = None):
        repo_root = Path(__file__).resolve().parents[3]
        self.prompts_dir = Path(prompts_dir or repo_root / "prompts")

    def render(self, name: str, **values: Any) -> str:
        path = self.prompts_dir / f"{name}.txt"
        if not path.exists():
            raise FileNotFoundError(f"Prompt template not found: {path}")
        text = path.read_text(encoding="utf-8", errors="replace")
        safe_values = {key: self._stringify(value) for key, value in values.items()}
        return text.format(**safe_values)

    def _stringify(self, value: Any) -> str:
        if isinstance(value, str):
            return value
        return json.dumps(value, ensure_ascii=False, indent=2)


def extract_section(text: str, tag: str) -> str:
    pattern = rf"<{re.escape(tag)}>\s*(.*?)\s*</{re.escape(tag)}>"
    match = re.search(pattern, text or "", flags=re.DOTALL | re.IGNORECASE)
    return match.group(1).strip() if match else ""


def extract_json_object(text: str) -> Dict[str, Any]:
    start = (text or "").find("{")
    if start < 0:
        raise ValueError("No JSON object found in model response")
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
                    return json.loads(text[start : index + 1])
    raise ValueError("No complete JSON object found in model response")


def strip_code_fence(text: str) -> str:
    text = re.sub(r"<think>.*?</think>", "", text or "", flags=re.DOTALL | re.IGNORECASE).strip()
    fenced = re.search(r"```(?:aadl|text)?\s*(.*?)```", text, flags=re.DOTALL | re.IGNORECASE)
    if fenced:
        return fenced.group(1).strip()
    return re.sub(r"(?im)^\s*```(?:aadl|text)?\s*$", "", text).strip()


def normalize_agree_annex_delimiters(text: str) -> str:
    """Normalize common LLM formatting variants of AGREE annex delimiters.

    OSATE expects the annex text delimiters to be attached to the opening and
    closing braces: `annex agree {** ... **};`. Some models split these tokens
    across lines as `annex agree {` followed by `**`, which AADL parses as a
    malformed annex before AGREE can analyze the contract body.
    """
    normalized = text or ""
    normalized = re.sub(
        r"annex\s+agree\s*\{\s*\*\*",
        "annex agree {**",
        normalized,
        flags=re.IGNORECASE,
    )
    normalized = re.sub(
        r"\*\*\s*\}\s*;?",
        "**};",
        normalized,
        flags=re.IGNORECASE,
    )
    normalized = re.sub(
        r"(?im)(\b(?:const|eq)\s+[A-Za-z_][A-Za-z0-9_]*\s*:\s*)integer\b",
        r"\1int",
        normalized,
    )
    normalized = re.sub(
        r"(?im)(\b(?:const|eq)\s+[A-Za-z_][A-Za-z0-9_]*\s*:\s*)boolean\b",
        r"\1bool",
        normalized,
    )
    return normalized
