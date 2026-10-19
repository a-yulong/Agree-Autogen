"""Translate CJK text in experiment sources to English.

The script is intentionally conservative:
- Requirement `.txt` files are translated as whole natural-language texts.
- AADL files translate only CJK text in `--` comments by default.
- Other text-like files are translated only when they are small and clearly textual.
- Identical source text is cached by SHA-256 so A/B duplicates are translated once.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import time
from pathlib import Path
from typing import Dict

from openai import OpenAI


CJK_RE = re.compile(r"[\u4e00-\u9fff]")


def has_cjk(text: str) -> bool:
    return CJK_RE.search(text) is not None


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()


def load_cache(path: Path) -> Dict[str, str]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def save_cache(path: Path, cache: Dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(cache, indent=2, ensure_ascii=False), encoding="utf-8")


def find_api_key() -> str:
    key = os.environ.get("AGREE_MODEL_API_KEY") or os.environ.get("OPENROUTER_API_KEY")
    if key:
        return key
    key_file = Path(r"C:\Users\25780\Documents\Playground\run_openrouter_cases_A.py")
    if key_file.exists():
        match = re.search(r"sk-or-v1-[A-Za-z0-9]+", key_file.read_text(encoding="utf-8", errors="replace"))
        if match:
            return match.group(0)
    raise RuntimeError("No OpenRouter API key found in environment or local key source.")


def translate(client: OpenAI, model: str, text: str, cache: Dict[str, str]) -> str:
    key = sha(text)
    if key in cache:
        return cache[key]
    prompt = (
        "Translate the following Chinese or mixed Chinese-English text into clear technical English.\n"
        "Preserve all AADL/AGREE identifiers, function names, package names, port names, numbers, units, and code snippets exactly.\n"
        "Do not add explanations. Return only the translated English text.\n\n"
        "<TEXT>\n"
        f"{text}\n"
        "</TEXT>"
    )
    last_error = None
    for attempt in range(1, 4):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a precise technical translator for AADL and AGREE experiment datasets."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.0,
                max_tokens=max(1024, min(6000, len(text) * 3)),
            )
            result = (response.choices[0].message.content or "").strip()
            if not result:
                raise RuntimeError("empty translation")
            cache[key] = result
            return result
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            time.sleep(2 * attempt)
    raise RuntimeError(f"Translation failed after retries: {last_error}")


def translate_aadl_comments(client: OpenAI, model: str, text: str, cache: Dict[str, str]) -> str:
    output = []
    for line in text.splitlines(keepends=True):
        newline = ""
        body = line
        if line.endswith("\r\n"):
            body, newline = line[:-2], "\r\n"
        elif line.endswith("\n"):
            body, newline = line[:-1], "\n"
        if "--" in body and has_cjk(body):
            prefix, comment = body.split("--", 1)
            translated = translate(client, model, comment.strip(), cache)
            output.append(f"{prefix}-- {translated}{newline}")
        elif has_cjk(body):
            translated = translate(client, model, body, cache)
            output.append(f"{translated}{newline}")
        else:
            output.append(line)
    return "".join(output)


def translate_file(client: OpenAI, model: str, path: Path, cache: Dict[str, str]) -> bool:
    text = path.read_text(encoding="utf-8", errors="replace")
    if not has_cjk(text):
        return False
    suffix = path.suffix.lower()
    name = path.name.lower()
    if suffix == ".aadl":
        translated = translate_aadl_comments(client, model, text, cache)
    elif name.endswith("_req.txt") or suffix in {".txt", ".md"}:
        translated = translate(client, model, text, cache)
    else:
        translated = translate(client, model, text, cache)
    if translated != text:
        path.write_text(translated, encoding="utf-8")
        return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=r"C:\Users\25780\Desktop\Exp_Data\Sources")
    parser.add_argument("--model", default=os.environ.get("AGREE_TRANSLATION_MODEL", "qwen/qwen3-coder-30b-a3b-instruct"))
    parser.add_argument("--base-url", default=os.environ.get("AGREE_MODEL_BASE_URL", "https://openrouter.ai/api/v1"))
    parser.add_argument("--cache", default=r"C:\Users\25780\Desktop\Exp_Data\translation_cache_en.json")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    root = Path(args.root)
    cache_path = Path(args.cache)
    cache = load_cache(cache_path)
    client = OpenAI(api_key=find_api_key(), base_url=args.base_url)

    candidates = []
    for path in root.rglob("*"):
        if not path.is_file() or ".metadata" in path.parts:
            continue
        if path.suffix.lower() not in {".txt", ".aadl", ".md", ".json", ".yaml", ".yml"}:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        if has_cjk(text):
            candidates.append(path)
    print(f"CJK source files: {len(candidates)}", flush=True)

    changed = 0
    for index, path in enumerate(candidates, 1):
        if args.limit and index > args.limit:
            break
        print(f"[{index}/{len(candidates)}] {path}", flush=True)
        if translate_file(client, args.model, path, cache):
            changed += 1
        if index % 20 == 0:
            save_cache(cache_path, cache)
            print(f"Saved cache; changed={changed}; cache_entries={len(cache)}", flush=True)
    save_cache(cache_path, cache)
    print(f"Done. changed={changed}; cache_entries={len(cache)}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
