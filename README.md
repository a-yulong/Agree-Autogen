# AGREE-AutoGen

AGREE-AutoGen is a validation-centered multi-agent framework for generating AGREE contracts for AADL architectures from natural-language requirements. Given a requirement and a target AADL model, the framework generates and fuses AGREE annexes into an AADL+AGREE artifact that can be checked by external AADL/AGREE validation tools.

The repository provides the current research prototype, configuration templates, prompt templates, a minimal public example, experiment script templates, and a standalone AGREE validator CLI source tree. External validation depends on local installations such as AADL Inspector, OSATE, Java, and AGREE.

## Inputs and Outputs

Inputs:

- Natural-language requirement text.
- AADL architecture model.
- Optional related AADL package files.
- Optional retrieval knowledge base.

Output:

- A fused AADL+AGREE artifact.
- Validation diagnostics and repair reports when external validators are configured.
- Per-case experiment artifacts such as first-pass code, repaired code, report JSON, and report Markdown.

## Framework Components

### Model Analyst Agent

Extracts AADL topology, component hierarchy, interfaces, port names, port directions, data types, data-flow relations, and valid AGREE scopes.

### Requirement Analyst Agent

Decomposes natural-language requirements into atomic functional units and aligns requirement entities with grounded AADL identifiers.

### AGREE Generator Agent

Generates AGREE clauses from atomic requirements, architecture representations, and retrieved knowledge when RAG is enabled.

### Model Fusion Agent

Inserts generated AGREE clauses into the appropriate AADL component type or implementation scope while preserving the original architecture.

### Validation-and-Repair Agent

Runs AADL-level and AGREE-level validation when the external tools are configured, then iteratively repairs diagnostics until zero errors or the repair limit is reached.

### RAG Knowledge Base

The knowledge base is organized as:

- `Ksyn`: AADL/AGREE syntax and semantic rules.
- `Kexp`: verified exemplar triples.
- `Kdef`: defensive heuristic rules.

The public repository contains only structure, policy, and redistributable examples. License-unclear third-party materials are not redistributed.

## Repository Structure

```text
.
|-- run_case.py                         # Single-case CLI for the current case-layout runner
|-- configs/                            # YAML configuration templates
|-- prompts/                            # Agent prompt templates for review and reproduction
|-- knowledge_base/                     # Public knowledge-base layout and policy
|-- data/
|   |-- examples/gf_monitor/            # Minimal illustrative example
|   `-- benchmark/                      # Benchmark metadata template
|-- docs/                               # Installation, quick start, pipeline, benchmark, reproduction, troubleshooting
|-- experiments/                        # E1-E7 and metrics CLI templates
|-- scripts/run_batch.py                # Batch runner for the current case-layout pipeline
|-- src/
|   |-- agree_autogen/
|   |   |-- agents.py                   # Current agent implementations and in-code prompts
|   |   |-- pipeline.py                 # Current orchestration, RAG, validation, repair loop
|   |   |-- case_runner.py              # Case loading and target-component extraction
|   |   |-- runtime.py                  # Runtime config, token accounting, utilities
|   |   |-- metrics/                    # Lightweight metric helpers
|   |   |-- rag/                        # RAG helper placeholders for future refactoring
|   |   |-- validators/                 # Lightweight validator wrappers
|   |   `-- utils/                      # Small utility helpers
|   |-- experiment_recorder.py          # Report and artifact generation
|   `-- error_type_analyzer.py          # T1-T5 error classification
|-- tests/                              # Unit tests that do not require LLMs or external validators
`-- tools/agree-validator/              # Standalone AGREE validator CLI source
```

## Installation

Python 3.9 or later is recommended.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

See `docs/installation.md` for conda and validator configuration details.

## Environment Variables

Core model configuration:

- `AGREE_MODEL_BASE_URL`
- `AGREE_MODEL_API_KEY`
- `AGREE_MODEL_NAME`

Data and output paths:

- `AGREE_SOURCE_ROOT`
- `AGREE_RESULT_ROOT`
- `AGREE_DOCS_DIR`

Validation tools:

- `AADL_INSPECTOR_PATH`
- `JAVA_HOME`
- `OSATE_HOME`
- `AGREE_VALIDATOR_ROOT`

Copy `.env.example` to a local `.env` if desired, but never commit real credentials.

## Quick Start with GF_Monitor

The public GF_Monitor example is located in:

```text
data/examples/gf_monitor/
```

It includes:

- `requirement.txt`
- `input.aadl`
- `expected_output.aadl`

The example is illustrative and should be validated with a local OSATE/AGREE installation before being treated as a benchmark artifact.

The current production entry point uses the `CaseXX_A` benchmark layout:

```powershell
python scripts/prepare_gf_monitor_case.py --case-num 1 --case-letter A --source-root ./data/Sources
python run_case.py --case-num 1 --case-letter A --use-rag --result-root ./results
```

For a no-RAG smoke run:

```powershell
python run_case.py --case-num 1 --case-letter A --no-rag --result-root ./results
```

See `docs/quick_start.md` for details and current limitations.

## Build the RAG Index

The current pipeline builds Chroma indexes from the configured document directory when RAG is enabled. Public knowledge-base folders are provided under `knowledge_base/`.

To inspect redistributable knowledge files:

```powershell
python -m agree_autogen.rag.build_index --knowledge-base-dir ./knowledge_base
```

Full RAG execution requires a local corpus configured through `AGREE_DOCS_DIR` or the relevant configuration template.

## Validation Tool Configuration

AADL-level validation requires AADL Inspector. AGREE-level validation requires Java, OSATE, and the standalone validator:

```powershell
$env:JAVA_HOME = "path/to/jdk17"
$env:OSATE_HOME = "path/to/osate"
$env:AGREE_VALIDATOR_ROOT = "./tools/agree-validator"
.\tools\agree-validator\build.ps1
```

Lightweight wrappers return `not_configured` when external tools are unavailable. The full pipeline requires the external tools for validation-ready execution.

## Experiment Reproduction Overview

Experiment entry points are provided under `experiments/`:

- `run_e1_bare_model.py`: direct-generation baseline template.
- `run_e2_full_framework.py`: full pipeline runner using the current batch runner.
- `run_ablation.py`: ablation entry point; E3 NoRAG is executable, E4-E7 are templates pending runtime switches.
- `run_cross_model.py`: batch execution for an environment-configured model.
- `compute_metrics.py`: aggregate metrics from report JSON files.

Example:

```powershell
python experiments/run_e2_full_framework.py --start 1 --end 10 --letters A --result-root ./results
python experiments/compute_metrics.py --results-dir ./results --output ./results/metrics/metrics.csv
```

No experimental conclusions are included in this repository by default.

## Tests

The provided tests do not require a real LLM API, AADL Inspector, or AGREE validator:

```powershell
pytest -q
```

## Citation

If you use AGREE-AutoGen in academic work, please cite this repository. A `CITATION.cff` file is provided.

## License

This project is released under the MIT License. See `LICENSE`.

## Data and Third-Party Resource Notice

This repository does not redistribute license-unclear standards, official manuals, private datasets, generated vector stores, local OSATE installations, or API keys. Users must obtain third-party tools and non-redistributable resources separately.
