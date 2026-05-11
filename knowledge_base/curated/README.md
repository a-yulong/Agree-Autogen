# Curated Knowledge

Place prepared RAG material here after source review and normalization.

Suggested groups:

- `ksyn/`: AGREE/AADL syntax and scope guidance.
- `kexp/`: verified RequirementNL-LogicProp-CodeAGREE examples.
- `kdef/`: project-curated defensive rules and repair heuristics.
- `examples/`: small format examples used by tests and documentation.

The current runtime pipeline indexes `.pdf` and `.txt` files from the directory passed to `AGREEVerificationPipeline`. If material is stored here as Markdown, YAML, or CSV, export selected chunks to `.txt` before using the production RAG path.
