"""Command-line placeholder for building a RAG index."""

import argparse

from .knowledge_loader import list_knowledge_files


def main() -> int:
    parser = argparse.ArgumentParser(description="List redistributable knowledge files for index construction.")
    parser.add_argument("--knowledge-base-dir", default="./knowledge_base")
    args = parser.parse_args()
    files = list_knowledge_files(args.knowledge_base_dir)
    print(f"Found {len(files)} knowledge file(s)")
    for path in files:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

