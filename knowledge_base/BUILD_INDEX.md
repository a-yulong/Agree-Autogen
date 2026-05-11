# Build Index Guide

The current public pipeline builds its retrieval index at runtime from a prepared document directory.

## Default Paths

- Config template knowledge directory: `./knowledge_base`
- Direct-file runner environment override: `AGREE_DOCS_DIR`
- Pipeline vector cache: `./vectorstore_cache`
- Generation collection: `agree-unified-generate-v3`
- Validation collection: `agree-code-v3`

`configs/rag_config.yaml` documents the preferred public configuration. The active runtime values are defined in `src/agree_autogen/pipeline.py`.

## Supported Runtime Formats

The production pipeline currently loads:

- `.pdf`
- `.txt`

The lightweight helper `src/agree_autogen/rag/knowledge_loader.py` lists:

- `.txt`
- `.md`
- `.csv`

If curated material is authored as Markdown or YAML, convert or export it into `.txt` files before using the current pipeline RAG path.

## Build Procedure

1. Prepare source material under one document directory.

   ```text
   knowledge_base/curated/ksyn/
   knowledge_base/curated/kexp/
   knowledge_base/curated/kdef/
   ```

2. Export the selected chunks to top-level `.txt` or `.pdf` files in the directory that will be passed to the pipeline.

   Example:

   ```text
   knowledge_base/local_rag_docs/agree_syntax_notes.txt
   knowledge_base/local_rag_docs/verified_examples.txt
   knowledge_base/local_rag_docs/defensive_rules.txt
   ```

3. Point the runtime to the prepared directory.

   ```powershell
   $env:AGREE_DOCS_DIR = "knowledge_base/local_rag_docs"
   ```

4. Run the pipeline with RAG enabled.

   ```powershell
   python scripts/run_files.py --requirement data/examples/gf_monitor/requirement.txt --aadl data/examples/gf_monitor/input.aadl --output-dir outputs/gf_monitor --skip-validation
   ```

5. The first RAG-enabled run creates or reuses Chroma collections under `./vectorstore_cache`.

## Inspection Helper

The helper command below lists knowledge files recognized by the lightweight loader:

```powershell
python -m agree_autogen.rag.build_index --knowledge-base-dir knowledge_base
```

This command is an inspection helper in the public release. It does not currently build the production Chroma index used by `AGREEVerificationPipeline`.
