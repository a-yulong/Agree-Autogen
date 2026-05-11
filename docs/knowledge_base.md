# Knowledge Base

The RAG artifact is organized into three roles:

- `Kdef`: defensive generation and repair rules.
- `Kexp`: verified AGREE examples and code patterns.
- `Ksyn`: syntax, semantic, and AADL scope guidance.

## Included Sources

`knowledge_base/sources.yaml` records the source inventory.

- `raw/kdef/Attention.txt` is Kdef and is processed into `processed/kdef/attention_zh.md` and `processed/kdef/defensive_rules.jsonl`.
- `raw/kexp/AGREE_code_knowledge_dataset.txt` is Kexp and is processed into `processed/kexp/agree_code_knowledge_dataset.txt` and `processed/kexp/agree_examples.jsonl`.
- `raw/ksyn/AGREE_knowledge_dataset_en.pdf` and `raw/ksyn/AGREE_Users_Guide.pdf` are Ksyn AGREE sources.
- `raw/ksyn/AADL_AS5506C.local_source.md` records AADL AS5506C as a local Ksyn source.

The AADL AS5506C raw PDF is configured locally through `knowledge_base/local_sources.yaml` using `knowledge_base/local_sources.example.yaml` as a template.

## Building the Local Corpus

```powershell
python scripts/build_rag_index.py --dry-run
python scripts/build_rag_index.py --knowledge-base knowledge_base --output knowledge_base/index
```

The script reads `raw/`, `processed/`, and `sources.yaml`. It supports `.txt`, `.md`, `.jsonl`, `.yaml`, `.yml`, and PDF extraction when the installed environment provides a PDF parser. It writes:

```text
knowledge_base/index/manifest.json
knowledge_base/index/corpus.jsonl
```

The generated index files are ignored by Git. Use the generated corpus or exported TXT/PDF files as the runtime RAG document directory through `AGREE_DOCS_DIR`.

## Runtime RAG

The current pipeline builds Chroma collections from `.pdf` and `.txt` files in `AGREE_DOCS_DIR` or the provided document directory. The static knowledge base supplies syntax and examples; case-specific AADL identifiers come from the Model Analyst Agent.
