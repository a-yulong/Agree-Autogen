# Artifact

This repository is the public AGREE-AutoGen artifact.

## Included

- Source code for the current multi-agent pipeline.
- Direct-file CLI and legacy case-layout CLI.
- Standalone AGREE validator source.
- Public GF_Monitor example.
- Sample RAG knowledge base with toy `Ksyn`, `Kexp`, and `Kdef` entries.
- Experiment configuration files for E1-E7.
- Toy sample result JSON files for metrics parsing.
- Tests and GitHub Actions CI.

## Not Included

- Full private benchmark data.
- Paper benchmark results.
- Non-redistributable AADL/AGREE manuals or standards text.
- Local OSATE, AADL Inspector, or Java installations.
- API keys, vector stores, generated logs, or generated outputs.

## Minimal Run

```powershell
python scripts/run_files.py --requirement data/examples/gf_monitor/requirement.txt --aadl data/examples/gf_monitor/input.aadl --output-dir outputs/gf_monitor --disable-rag --skip-validation --dry-run
```

The command checks inputs and writes a dry-run report without calling an LLM or external validator.
