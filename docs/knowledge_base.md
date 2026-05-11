# Knowledge Base

The RAG artifact is organized into three roles:

- `Kdef`: defensive generation and repair rules.
- `Kexp`: verified AGREE examples and code patterns.
- `Ksyn`: syntax, semantic, and AADL scope guidance.

## Included Sources

`knowledge_base/sources.yaml` records the source inventory.

- `Attention.txt` is adapted into `knowledge_base/curated/kdef/attention_zh.md` and `knowledge_base/curated/kdef/defensive_rules.jsonl`.
- `AGREE_code_knowledge_dataset.txt` is stored in `knowledge_base/curated/kexp/` and summarized into `agree_examples.jsonl`.
- Ksyn notes are stored in `knowledge_base/curated/ksyn/` as concise AGREE syntax and AADL scope notes.

PDF references used for paper-scale source preparation are represented through `knowledge_base/local_sources.example.yaml`. The public repository stores notes and manifests, not local PDF corpora.

## Building the Local Corpus

```powershell
python scripts/build_rag_index.py --knowledge-base knowledge_base
```

The script reads `.txt`, `.md`, and `.jsonl` files from `knowledge_base/curated/` and writes:

```text
knowledge_base/index/manifest.json
knowledge_base/index/corpus.jsonl
```

The generated index files are ignored by Git. Use the generated corpus or exported TXT/PDF files as the runtime RAG document directory through `AGREE_DOCS_DIR`.

## Runtime RAG

The current pipeline builds Chroma collections from `.pdf` and `.txt` files in `AGREE_DOCS_DIR` or the provided document directory. The static knowledge base supplies syntax and examples; case-specific AADL identifiers come from the Model Analyst Agent.
