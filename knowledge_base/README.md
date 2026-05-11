# Knowledge Base

This directory documents how AGREE-AutoGen organizes retrieval material for RAG-assisted AGREE generation and repair.

The public repository provides the source inventory, expected directory layout, format guidance, and small format examples. A working local RAG setup is built by placing prepared source documents under `knowledge_base/curated/` or by pointing `AGREE_DOCS_DIR` to another prepared document directory.

## Runtime Behavior

The current public runner uses `AGREE_DOCS_DIR` when it is set. Otherwise, `scripts/run_files.py` passes `knowledge_base/` to the pipeline. The pipeline currently indexes top-level `.pdf` and `.txt` files in that document directory. The helper loader under `src/agree_autogen/rag/` lists `.txt`, `.md`, and `.csv` files for lightweight inspection, but the production pipeline path is PDF/TXT based.

The vector index is created under `./vectorstore_cache/` by `src/agree_autogen/pipeline.py`. The generation and validation phases use separate Chroma collections.

## Directory Layout

- `SOURCE_INDEX.md`: knowledge source inventory and intended use.
- `BUILD_INDEX.md`: how to prepare source files and build the local retrieval index.
- `FORMAT.md`: recommended structure for curated knowledge chunks.
- `sources.yaml`: machine-readable source inventory.
- `curated/`: prepared local knowledge material grouped as `ksyn`, `kexp`, and `kdef`.
- `curated/examples/`: format examples only; these are not the complete paper knowledge base.
- `manifests/`: public and local source manifests.

## Knowledge Roles

- `Ksyn`: AGREE/AADL syntax, annex placement, typing, and temporal-expression guidance.
- `Kexp`: verified RequirementNL-LogicProp-CodeAGREE examples.
- `Kdef`: defensive generation and repair rules derived from observed failures.

Model-specific architecture facts are primarily extracted from the input AADL model by the Model Analyst Agent. They are not expected to live entirely in the static knowledge base.
