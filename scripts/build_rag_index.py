"""Build a lightweight RAG corpus from AGREE-AutoGen knowledge sources."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_KB = REPO_ROOT / "knowledge_base"
SUPPORTED_TEXT = {".txt", ".md", ".jsonl", ".yaml", ".yml"}


def load_yaml(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file) or {}


def collect_repository_sources(kb_root: Path) -> List[Path]:
    roots = [kb_root / "raw", kb_root / "processed"]
    files: List[Path] = []
    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if path.is_file() and (path.suffix.lower() in SUPPORTED_TEXT or path.suffix.lower() == ".pdf"):
                files.append(path)
    source_manifest = kb_root / "sources.yaml"
    if source_manifest.exists():
        files.append(source_manifest)
    return sorted(files)


def collect_local_sources(path: Path | None) -> List[Path]:
    if not path or not path.exists():
        return []
    data = load_yaml(path)
    sources = data.get("sources", {})
    files: List[Path] = []
    for value in sources.values():
        if not isinstance(value, str) or value.startswith("<"):
            continue
        p = Path(value)
        if p.is_file():
            files.append(p)
        elif p.is_dir():
            files.extend(
                item for item in p.rglob("*")
                if item.is_file() and (item.suffix.lower() in SUPPORTED_TEXT or item.suffix.lower() == ".pdf")
            )
        else:
            print(f"warning: local source not found: {value}")
    return sorted(files)


def read_pdf(path: Path) -> str | None:
    try:
        from pypdf import PdfReader
    except Exception:
        print(f"warning: PDF parser is unavailable; skipping {path}")
        return None

    try:
        reader = PdfReader(str(path))
        pages = []
        for page in reader.pages:
            pages.append(page.extract_text() or "")
        return "\n".join(pages).strip()
    except Exception as exc:
        print(f"warning: failed to extract PDF {path}: {exc}")
        return None


def read_records(path: Path, kb_root: Path) -> List[Dict[str, Any]]:
    suffix = path.suffix.lower()
    try:
        source = str(path.relative_to(kb_root))
    except ValueError:
        source = str(path)

    records: List[Dict[str, Any]] = []
    if suffix == ".pdf":
        text = read_pdf(path)
        if text:
            records.append({"id": source, "source": source, "format": "pdf", "text": text})
        return records

    if suffix == ".jsonl":
        with path.open("r", encoding="utf-8") as file:
            for line_no, line in enumerate(file, 1):
                text = line.strip()
                if not text:
                    continue
                records.append({"id": f"{source}:{line_no}", "source": source, "format": "jsonl", "text": text})
        return records

    if suffix in SUPPORTED_TEXT:
        text = path.read_text(encoding="utf-8")
        if text.strip():
            records.append({"id": source, "source": source, "format": suffix.lstrip("."), "text": text})
    return records


def build_index(kb_root: Path, output_dir: Path, include_local_sources: Path | None, dry_run: bool) -> Dict[str, Any]:
    files = collect_repository_sources(kb_root) + collect_local_sources(include_local_sources)
    manifest = {
        "knowledge_base": str(kb_root),
        "sources_yaml": str(kb_root / "sources.yaml"),
        "local_sources": str(include_local_sources) if include_local_sources else None,
        "files": [str(path) for path in files],
        "records": 0,
    }

    print("RAG source files:")
    for path in files:
        print(f"- {path}")

    if dry_run:
        return manifest

    output_dir.mkdir(parents=True, exist_ok=True)
    corpus_path = output_dir / "corpus.jsonl"
    manifest_path = output_dir / "manifest.json"

    records = 0
    with corpus_path.open("w", encoding="utf-8") as corpus:
        for path in files:
            for record in read_records(path, kb_root):
                corpus.write(json.dumps(record, ensure_ascii=False) + "\n")
                records += 1

    manifest["records"] = records
    manifest["corpus"] = str(corpus_path)
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a lightweight RAG corpus from raw and processed knowledge files.")
    parser.add_argument("--knowledge-base", default=str(DEFAULT_KB), help="Knowledge base root.")
    parser.add_argument("--output", default=None, help="Output directory. Defaults to knowledge_base/index.")
    parser.add_argument("--include-local-sources", default=None, help="Optional knowledge_base/local_sources.yaml path.")
    parser.add_argument("--dry-run", action="store_true", help="List source files without writing an index.")
    args = parser.parse_args()

    kb_root = Path(args.knowledge_base)
    if not kb_root.exists():
        print(f"error: knowledge base root not found: {kb_root}")
        return 2

    output_dir = Path(args.output) if args.output else kb_root / "index"
    local_sources = Path(args.include_local_sources) if args.include_local_sources else None
    manifest = build_index(kb_root, output_dir, local_sources, args.dry_run)
    print(f"Discovered {len(manifest['files'])} source file(s)")
    if not args.dry_run:
        print(f"Indexed {manifest['records']} record(s)")
        print(f"Wrote {output_dir / 'manifest.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
