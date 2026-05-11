# Knowledge Base

AGREE-AutoGen supports retrieval-augmented generation through a prepared local corpus. The corpus is organized around source roles and then exported into runtime documents.

## Source Roles

- `Ksyn`: AGREE/AADL syntax, scope, type, and temporal-expression guidance.
- `Kexp`: verified RequirementNL-LogicProp-CodeAGREE examples.
- `Kdef`: defensive generation and repair rules from project experience.

The source inventory is maintained in `knowledge_base/SOURCE_INDEX.md` and `knowledge_base/sources.yaml`.

## Runtime Loading

The current pipeline indexes top-level `.pdf` and `.txt` files from the configured document directory. Direct-file runs use `AGREE_DOCS_DIR` when set; otherwise they pass `knowledge_base/` to the pipeline.

Recommended preparation:

```text
knowledge_base/curated/ksyn/
knowledge_base/curated/kexp/
knowledge_base/curated/kdef/
knowledge_base/local_rag_docs/
```

Export selected curated chunks to `.txt` files under `knowledge_base/local_rag_docs/`, then set:

```powershell
$env:AGREE_DOCS_DIR = "knowledge_base/local_rag_docs"
```

The vector cache is created under `./vectorstore_cache`.

See `knowledge_base/BUILD_INDEX.md` for the build procedure and `knowledge_base/FORMAT.md` for chunk formatting.
