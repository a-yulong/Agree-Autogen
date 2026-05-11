# AGREE-AutoGen

AGREE-AutoGen is a research artifact for generating AGREE contracts for AADL architectures from natural-language requirements. It combines architecture analysis, requirement decomposition, AGREE synthesis, model fusion, and validation-guided repair to produce fused AADL+AGREE artifacts.

## What Is Included

- Multi-agent pipeline source in `src/agree_autogen/`.
- Direct-file and case-layout runners in `scripts/`.
- Standalone AGREE validator source in `tools/agree-validator/`.
- A GF_Monitor minimal example in `data/examples/gf_monitor/`.
- Curated RAG source package in `knowledge_base/`.
- Experiment settings and metric scripts in `experiments/`.
- Tests that run without model credentials or external validators.

## Quick Start

Install:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

Run the example dry run:

```powershell
python scripts/run_files.py --requirement data/examples/gf_monitor/requirement.txt --aadl data/examples/gf_monitor/input.aadl --output-dir outputs/gf_monitor --disable-rag --skip-validation --dry-run
```

Configure an OpenAI-compatible endpoint before full generation:

```powershell
$env:AGREE_MODEL_BASE_URL = "https://api.example.com/v1"
$env:AGREE_MODEL_API_KEY = "replace-with-your-key"
$env:AGREE_MODEL_NAME = "model-name"
```

See `docs/usage.md` for runners and validator configuration.

## Knowledge Base

The RAG artifact is organized as real source files plus processed retrieval files:

- `knowledge_base/raw/kdef/Attention.txt` -> Kdef.
- `knowledge_base/raw/kexp/AGREE_code_knowledge_dataset.txt` -> Kexp.
- `knowledge_base/raw/ksyn/AGREE_knowledge_dataset_en.pdf` and `knowledge_base/raw/ksyn/AGREE_Users_Guide.pdf` -> Ksyn.
- `knowledge_base/raw/ksyn/AADL_AS5506C.local_source.md` records the AADL AS5506C local Ksyn source.
- `knowledge_base/processed/` contains Markdown and JSONL files derived from the raw sources.
- `knowledge_base/sources.yaml`: source inventory.
- `knowledge_base/local_sources.example.yaml`: local PDF source manifest template.

Build the lightweight local corpus manifest:

```powershell
python scripts/build_rag_index.py --dry-run
python scripts/build_rag_index.py --knowledge-base knowledge_base --output knowledge_base/index
```

See `docs/knowledge_base.md` for source preparation and runtime RAG usage.

## Experiments

Experiment settings are consolidated in `experiments/settings.yaml`.

```powershell
python experiments/run_experiment.py --setting E2 --benchmark data/Sources --output-dir outputs/e2 --start 1 --end 10 --letters A
python experiments/run_experiment.py --setting E3 --benchmark data/Sources --output-dir outputs/e3 --start 1 --end 10 --letters A
python experiments/compute_metrics.py --results-dir outputs/e2 --output outputs/e2/metrics.csv
```

E2 and E3 are connected to the public case-layout runner. Other ablations are recorded in `settings.yaml` with their required runtime switches.

## Repository Layout

```text
configs/             Runtime configuration templates
data/examples/       Public examples
docs/                Usage, artifact, knowledge-base, and experiment notes
experiments/         Experiment settings, runner, metrics, sample reports
knowledge_base/      Curated RAG source package and local source manifest
scripts/             User-facing CLIs
src/agree_autogen/   Pipeline implementation
tests/               Unit and CLI tests
tools/               Standalone AGREE validator source
```

## Citation

If you use AGREE-AutoGen in academic work, cite this repository. See `CITATION.cff`.

## License

MIT License. See `LICENSE`.
