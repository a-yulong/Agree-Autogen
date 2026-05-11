# AGREE-AutoGen

AGREE-AutoGen is a research prototype for generating AGREE contracts for AADL architectures from natural-language requirements. It takes a natural-language requirement and an AADL architecture as input, then produces a fused AADL+AGREE artifact with optional validation and repair.

External validation requires local AADL/AGREE tooling. The repository includes a dry-run path, prompt templates, configuration templates, a minimal public example, experiment entry points, and standalone AGREE validator source.

## Key Features

- Multi-agent workflow: Model Analyst Agent, Requirement Analyst Agent, AGREE Generator Agent, Model Fusion Agent, and Validation-and-Repair Agent.
- Direct-file CLI for `requirement.txt + input.aadl` inputs.
- Legacy case-layout runner for benchmark-style experiments.
- RAG knowledge-base layout with `Ksyn`, `Kexp`, and `Kdef`.
- Report generation for first-pass artifacts, final artifacts, diagnostics, tokens, runtime, and repair rounds.
- Lightweight tests that do not require an LLM API or external AADL/AGREE validators.

## Workflow Overview

```text
natural-language requirement + AADL architecture
        |
        v
Model Analyst + Requirement Analyst
        |
        v
AGREE Generator + RAG Knowledge Base
        |
        v
Model Fusion
        |
        v
Validation-and-Repair
        |
        v
fused AADL+AGREE artifact
```

## Repository Layout

```text
configs/                  YAML configuration templates
data/examples/gf_monitor/ Minimal public example
docs/                     Installation, quick start, pipeline, benchmark, reproduction, troubleshooting
experiments/              Experiment and metrics entry points
knowledge_base/           Public RAG layout and redistribution policy
prompts/                  Agent prompt templates
scripts/                  Direct-file, case preparation, and batch CLIs
src/agree_autogen/        Runtime package
tests/                    Unit tests independent of LLMs and validators
tools/agree-validator/    Standalone AGREE validator CLI source
```

## Installation

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

See [docs/installation.md](docs/installation.md) for conda, model API, RAG, and validation-tool configuration.

## Quick Start

Run the GF_Monitor dry run. This checks inputs and configuration without calling an LLM or external validators:

```powershell
python scripts/run_files.py `
  --requirement data/examples/gf_monitor/requirement.txt `
  --aadl data/examples/gf_monitor/input.aadl `
  --output-dir outputs/gf_monitor `
  --disable-rag `
  --skip-validation `
  --dry-run
```

Expected files:

```text
outputs/gf_monitor/dry_run_report.json
outputs/gf_monitor/requirement.txt
outputs/gf_monitor/input.aadl
```

To run generation, configure an OpenAI-compatible endpoint:

```powershell
$env:AGREE_MODEL_BASE_URL = "https://api.example.com/v1"
$env:AGREE_MODEL_API_KEY = "replace-with-your-key"
$env:AGREE_MODEL_NAME = "your-model-name"
```

Then run the same command without `--dry-run`. Use `--skip-validation` until local AADL Inspector and AGREE validator tools are configured.

## Configuration

Configuration templates are in `configs/`.

Common environment variables:

- `AGREE_MODEL_BASE_URL`, `AGREE_MODEL_API_KEY`, `AGREE_MODEL_NAME`
- `AGREE_SOURCE_ROOT`, `AGREE_RESULT_ROOT`, `AGREE_DOCS_DIR`
- `AADL_INSPECTOR_PATH`, `JAVA_HOME`, `OSATE_HOME`, `AGREE_VALIDATOR_ROOT`

Do not commit `.env` files or credentials.

## Experiments and Reproduction

Experiment entry points are in `experiments/`.

```powershell
python experiments/run_e2_full_framework.py --start 1 --end 10 --letters A --result-root ./results
python experiments/run_ablation.py --setting E3 --start 1 --end 10 --letters A --result-root ./results
python experiments/compute_metrics.py --results-dir ./results --output ./results/metrics/metrics.csv
```

E2 Full Framework and E3 NoRAG are connected to the current case-layout runner. E1 Bare Model, E4 NoRepair, E5 No Model Analyst, E6 No Requirement Analyst, and E7 No Dual Analysts are provided as experiment-entry templates pending dedicated runtime switches.

No benchmark data or experimental conclusions are bundled by default.

## Validation Tools

AADL-level validation requires AADL Inspector. AGREE-level validation requires Java, OSATE, and the standalone validator under `tools/agree-validator/`.

```powershell
$env:JAVA_HOME = "path/to/jdk17"
$env:OSATE_HOME = "path/to/osate"
$env:AGREE_VALIDATOR_ROOT = "./tools/agree-validator"
.\tools\agree-validator\build.ps1
```

If validation tools are absent, wrappers report `not_configured`; they do not report validation success.

## Tests

```powershell
python -m compileall src experiments scripts tests
python -m pytest -q
```

## Data and Third-Party Resources

This repository does not redistribute license-unclear standards, official manuals, private datasets, generated vector stores, local tool installations, or API keys. Users must obtain non-redistributable resources separately.

## Citation

If you use AGREE-AutoGen in academic work, cite this repository. See [CITATION.cff](CITATION.cff).

## License

MIT License. See [LICENSE](LICENSE).

