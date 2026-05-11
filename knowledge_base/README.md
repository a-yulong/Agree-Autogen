# Knowledge Base

This directory contains the RAG knowledge base used by AGREE-AutoGen.

## Source Roles

- `raw/kdef/Attention.txt`: Kdef defensive heuristic rules.
- `raw/kexp/AGREE_code_knowledge_dataset.txt`: Kexp AGREE code exemplar dataset.
- `raw/ksyn/AGREE_knowledge_dataset_en.pdf`: Ksyn AGREE syntax and semantic source.
- `raw/ksyn/AGREE_Users_Guide.pdf`: Ksyn AGREE user-guide source.
- `raw/ksyn/AADL_AS5506C.local_source.md`: Ksyn local-source note for AADL AS5506C.

`sources.yaml` records the mapping from source files to Ksyn, Kexp, and Kdef roles. `local_sources.example.yaml` shows how to configure the AADL AS5506C local PDF and optional additional local sources.

## Processed Files

- `processed/kdef/attention_zh.md`
- `processed/kdef/defensive_rules.jsonl`
- `processed/kexp/agree_code_knowledge_dataset.txt`
- `processed/kexp/agree_examples.jsonl`
- `processed/ksyn/agree_syntax_notes.md`
- `processed/ksyn/aadl_scope_notes.md`

## Build RAG Index

```powershell
python scripts/build_rag_index.py --dry-run
python scripts/build_rag_index.py --knowledge-base knowledge_base --output knowledge_base/index
```

The script scans `raw/`, `processed/`, and `sources.yaml`. Generated files under `index/` are local build artifacts; only `.gitkeep` is tracked.
