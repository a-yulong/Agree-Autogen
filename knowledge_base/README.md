# Knowledge Base

This directory contains the AGREE-AutoGen RAG artifact.

The curated corpus is organized by role:

- `curated/kdef/`: defensive rules derived from `Attention.txt`.
- `curated/kexp/`: AGREE code examples from `AGREE_code_knowledge_dataset.txt`.
- `curated/ksyn/`: AGREE syntax and AADL scope notes prepared from project rules and local reference sources.

`sources.yaml` records the source inventory. `local_sources.example.yaml` shows how to connect local PDF references for paper-scale indexing without placing those PDFs in the repository.

The runtime pipeline consumes prepared text/PDF documents through `AGREE_DOCS_DIR`. The helper script `scripts/build_rag_index.py` collects curated `.txt`, `.md`, and `.jsonl` sources into `knowledge_base/index/manifest.json` and `knowledge_base/index/corpus.jsonl`. The generated index directory is ignored by Git except for `.gitkeep`.
