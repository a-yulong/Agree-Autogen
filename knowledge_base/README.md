# Knowledge Base

The knowledge base provides retrieval support for AGREE-AutoGen. It is used to supply compact AGREE/AADL rules, verified patterns, and defensive constraints to the generation pipeline.

The knowledge base is not treated as a general document dump. Its purpose is to improve grounded contract generation by making relevant syntax, scope, and example knowledge available at the point where agents need it.

## Knowledge Roles

The repository organizes retrieval sources into three roles:

- **Syntax and scope knowledge:** AGREE syntax, AADL scoping rules, annex placement, visible identifiers, property sets, and type references.
- **Example-pattern knowledge:** verified AGREE snippets and contract patterns that illustrate valid forms.
- **Defensive-rule knowledge:** constraints that discourage unsupported constructs, invisible identifiers, unlabeled assumptions or guarantees, and accidental copying of irrelevant examples.

These roles are recorded in `sources.yaml`.

## Directory Layout

```text
knowledge_base/
  raw/             Source documents and local source notes
  processed/       Curated markdown, text, and JSONL retrieval inputs
  index/           Local retrieval index output
  sources.yaml     Source inventory
```

`index/` is a generated local artifact. The repository should track only the files required to rebuild or inspect the index.

## Source Inventory

Representative sources include:

- `raw/kdef/Attention.txt`;
- `raw/kexp/AGREE_code_knowledge_dataset.txt`;
- `raw/ksyn/AGREE_knowledge_dataset_en.pdf`;
- `raw/ksyn/AGREE_Users_Guide.pdf`;
- `raw/ksyn/AADL_AS5506C.local_source.md`.

Processed files include:

- `processed/kdef/attention_en.md`;
- `processed/kdef/defensive_rules.jsonl`;
- `processed/kexp/agree_code_knowledge_dataset.txt`;
- `processed/ksyn/agree_syntax_notes.md`;
- `processed/ksyn/aadl_scope_notes.md`.

## Retrieval Digest

AGREE-AutoGen does not pass long retrieved documents directly to every downstream agent. Retrieved material is summarized into digest rules that emphasize:

- visible identifiers and owner scope;
- labeled `assume` and `guarantee` clauses;
- valid AGREE expression operands;
- placement of type-level and implementation-level content;
- common invalid patterns to avoid.

The digest stage reduces noise and lowers the risk of copying irrelevant examples.

## Building Retrieval Assets

Dry-run the index builder:

```powershell
python scripts/build_rag_index.py --dry-run
```

Build the local retrieval index:

```powershell
python scripts/build_rag_index.py `
  --knowledge-base knowledge_base `
  --output knowledge_base/index
```

Generated vector-store or cache directories should not be committed unless the release explicitly documents them as reproducibility artifacts.

## Licensing and Source Boundaries

Knowledge-base files may originate from specifications, guides, examples, and curated notes. Each source should be listed in `sources.yaml` with enough information to identify its role and origin. Materials with uncertain redistribution rights should be referenced through source notes rather than copied into the repository.
