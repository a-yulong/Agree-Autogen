# Artifact

This artifact contains the AGREE-AutoGen source code, public GF_Monitor example, real RAG source package, experiment settings, metric scripts, tests, and standalone AGREE validator source.

Release scope:

- Multi-agent pipeline source under `src/agree_autogen/`.
- Direct-file and case-layout runners under `scripts/`.
- RAG source package under `knowledge_base/`, including Kdef `Attention.txt`, Kexp `AGREE_code_knowledge_dataset.txt`, and Ksyn AGREE PDFs.
- E1-E7 settings and sample metric reports under `experiments/`.
- Minimal example under `data/examples/gf_monitor/`.

Local configuration is required for model endpoints and external validation tools. AADL AS5506C is recorded as a local Ksyn source through `knowledge_base/local_sources.example.yaml`.
