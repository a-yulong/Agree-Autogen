# Knowledge Chunk Format

The RAG corpus should be prepared as short, traceable chunks. Each chunk should state its role, source, and intended use. The current pipeline indexes `.pdf` and `.txt` files, so structured YAML examples should be exported to text before runtime retrieval.

## Recommended Text Chunk Header

```text
ID: kdef.identifier_grounding
Role: Kdef
Source: project-curated rule
Applies to: AGREE generation and repair
Validation status: reviewed

Rule:
Generated AGREE clauses must only use component, port, type, and package identifiers available in the Model Analyst output or explicitly imported by the AADL model.

Example:
Do not invent a port named alarm when the AADL feature is alarm_out.
```

## Recommended Triplet Fields

For `Kexp` examples, keep the alignment explicit:

- `RequirementNL`
- `LogicProp`
- `CodeAGREE`
- `AADL scope`
- `Identifiers used`
- `Validation status`
- `Source note`

## Runtime Preparation

The current public runner retrieves from prepared document text. Keep curated source files under `knowledge_base/curated/`, then export selected chunks into `.txt` files under the directory referenced by `AGREE_DOCS_DIR`.
