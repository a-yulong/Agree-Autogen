"""Build a lightweight local RAG corpus manifest.

This script packages curated AGREE-AutoGen knowledge files into a JSONL corpus
that can be inspected, archived, or exported to the runtime RAG document
directory. It intentionally does not create a Chroma vector store; the pipeline
creates vector collections at runtime from prepared TXT/PDF documents.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_KB = REPO_ROOT / "knowledge_base"
SUPPORTED_TEXT = {".txt", ".md", ".jsonl"}


def load_yaml(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file) or {}


def iter_curated_files(kb_root: Path) -> Iterable[Path]:
    curated = kb_root / "curated"
    if not curated.exists():
        return []
    return sorted(path for path in curated.rglob("*") if path.is_file() and path.suffix.lower() in SUPPORTED_TEXT)


def iter_local_sources(local_manifest: Path | None) -> Iterable[Path]:
    if not local_manifest or not local_manifest.exists():
        return []
    data = load_yaml(local_manifest)
    paths: List[Path] = []
    for item in data.get("local_sources", []):
        if item.get("enabled") is not True:
            continue
        raw_path = item.get("path")
        if not raw_path or raw_path.startswith("<"):
            continue
        path = Path(raw_path)
        if path.exists() and path.suffix.lower() in SUPPORTED_TEXT:
            paths.append(path)
        elif path.exists() and path.suffix.lower() == ".pdf":
            print(f"warning: PDF source is declared but not extracted by this helper: {path}")
        else:
            print(f"warning: local source not found or unsupported: {raw_path}")
    return paths


def read_records(path: Path, kb_root: Path) -> List[Dict[str, Any]]:
    suffix = path.suffix.lower()
    rel = str(path.relative_to(kb_root)) if path.is_relative_to(kb_root) else str(path)
    records: List[Dict[str, Any]] = []
    if suffix == ".jsonl":
        with path.open("r", encoding="utf-8") as file:
            for line_no, line in enumerate(file, 1):
                text = line.strip()
                if not text:
                    continue
                records.append({
                    "id": f"{rel}:{line_no}",
                    "source": rel,
                    "format": "jsonl",
                    "text": text,
                })
    else:
        text = path.read_text(encoding="utf-8")
        if text.strip():
            records.append({
                "id": rel,
                "source": rel,
                "format": suffix.lstrip("."),
                "text": text,
            })
    return records


def build_index(kb_root: Path, local_manifest: Path | None, output_dir: Path) -> Dict[str, Any]:
    files = list(iter_curated_files(kb_root)) + list(iter_local_sources(local_manifest))
    output_dir.mkdir(parents=True, exist_ok=True)
    corpus_path = output_dir / "corpus.jsonl"
    manifest_path = output_dir / "manifest.json"

    total_records = 0
    with corpus_path.open("w", encoding="utf-8") as corpus:
        for path in files:
            for record in read_records(path, kb_root):
                corpus.write(json.dumps(record, ensure_ascii=False) + "\n")
                total_records += 1

    manifest = {
        "knowledge_base": str(kb_root),
        "source_manifest": str(kb_root / "sources.yaml"),
        "local_manifest": str(local_manifest) if local_manifest else None,
        "files": [str(path.relative_to(kb_root)) if path.is_relative_to(kb_root) else str(path) for path in files],
        "records": total_records,
        "corpus": str(corpus_path),
    }
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a lightweight RAG corpus manifest from curated sources.")
    parser.add_argument("--knowledge-base", default=str(DEFAULT_KB), help="Knowledge base root.")
    parser.add_argument("--local-sources", default=None, help="Optional local_sources.yaml path.")
    parser.add_argument("--output-dir", default=None, help="Output directory for corpus.jsonl and manifest.json.")
    args = parser.parse_args()

    kb_root = Path(args.knowledge_base)
    local_manifest = Path(args.local_sources) if args.local_sources else kb_root / "local_sources.yaml"
    output_dir = Path(args.output_dir) if args.output_dir else kb_root / "index"

    if not kb_root.exists():
        print(f"error: knowledge base root not found: {kb_root}")
        return 2

    manifest = build_index(kb_root, local_manifest if local_manifest.exists() else None, output_dir)
    print(f"Indexed {manifest['records']} record(s)")
    print(f"Wrote {output_dir / 'manifest.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
