# Artifact

This artifact contains the AGREE-AutoGen source code, public GF_Monitor example, curated RAG source package, experiment settings, metric scripts, tests, and standalone AGREE validator source.

Release scope:

- Multi-agent pipeline source under `src/agree_autogen/`.
- Direct-file and case-layout runners under `scripts/`.
- RAG source package under `knowledge_base/`.
- E1-E7 settings and sample metric reports under `experiments/`.
- Minimal example under `data/examples/gf_monitor/`.

Local configuration is required for model endpoints and external validation tools. Paper-scale experiments additionally require local benchmark sources and a prepared RAG source manifest.
