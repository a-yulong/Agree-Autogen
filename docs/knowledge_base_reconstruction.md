# Knowledge Base Reconstruction

AGREE-AutoGen uses a local retrieval corpus to provide AGREE syntax guidance, verified examples, and defensive repair rules. The public repository now documents the source inventory and directory layout used to reconstruct that corpus.

## Source Inventory

Start with:

- `knowledge_base/SOURCE_INDEX.md`
- `knowledge_base/sources.yaml`
- `knowledge_base/manifests/public_sources.yaml`
- `knowledge_base/manifests/local_sources.example.yaml`

The corpus is organized into three knowledge roles:

| Role | Purpose | Prepared directory |
| --- | --- | --- |
| `Ksyn` | AGREE/AADL syntax, scope, typing, and temporal-expression guidance | `knowledge_base/curated/ksyn/` |
| `Kexp` | Verified RequirementNL-LogicProp-CodeAGREE examples | `knowledge_base/curated/kexp/` |
| `Kdef` | Defensive generation and repair rules | `knowledge_base/curated/kdef/` |

Case-specific AADL topology is extracted from the input model by the Model Analyst Agent. Static KB content should guide syntax and patterns; it should not replace runtime architecture analysis.

## Runtime Format

The current pipeline indexes top-level `.pdf` and `.txt` files from the directory passed as `docs_directory`. In direct-file runs, this directory is selected by `AGREE_DOCS_DIR`; otherwise it defaults to `knowledge_base/`.

If curated material is maintained as Markdown, YAML, or CSV, export selected chunks into `.txt` files before running with RAG enabled.

## Build Steps

1. Prepare source notes and examples under `knowledge_base/curated/ksyn/`, `knowledge_base/curated/kexp/`, and `knowledge_base/curated/kdef/`.
2. Export selected chunks into a runtime document directory, for example `knowledge_base/local_rag_docs/`.
3. Set:

   ```powershell
   $env:AGREE_DOCS_DIR = "knowledge_base/local_rag_docs"
   ```

4. Run the framework with RAG enabled. The first run creates Chroma collections under `./vectorstore_cache`.

See `knowledge_base/BUILD_INDEX.md` for the detailed build guide.
