# Agree-Autogen

Agree-Autogen is a multi-agent framework for generating and validating AGREE contracts for AADL models from natural-language requirements.

The framework orchestrates five main agents:

1. AADL model analyst: extracts structured model information.
2. Requirement analyst: extracts atomic propositions from natural-language requirements.
3. AGREE generator: produces AGREE annex candidates for a target component.
4. AADL merger: inserts AGREE annexes into the target AADL model.
5. Validator/repair agent: runs AADL Inspector and a standalone AGREE validator, then repairs validation errors iteratively.

## Repository layout

```text
.
??? run_case.py                         # Single-case CLI entry point
??? src/
?   ??? agree_exp_refactor/
?   ?   ??? runtime.py                  # Runtime config, token accounting, shared utilities
?   ?   ??? agents.py                   # Multi-agent prompts and LLM interaction logic
?   ?   ??? pipeline.py                 # RAG, validators, dependency sync, orchestration
?   ?   ??? case_runner.py              # Case loading and target-component extraction
?   ??? experiment_recorder.py          # Report and artifact generation
?   ??? error_type_analyzer.py          # T1-T5 error classification
??? scripts/
?   ??? run_batch.py                    # Batch runner for A/B experiments
??? docs/
?   ??? architecture.md                 # Design notes
??? data/
?   ??? README.md                       # Expected dataset layout
??? .env.example                        # Configuration template
??? requirements.txt
```

## Installation

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

You also need local AADL/AGREE tooling:

- AADL Inspector executable, configured by `AADL_INSPECTOR_PATH`.
- OSATE installation, configured by `OSATE_HOME`.
- Java 17 or later, configured by `JAVA_HOME`.
- Standalone AGREE validator, configured by `AGREE_VALIDATOR_ROOT`.

## Configuration

Copy `.env.example` to `.env` and fill in your own values. Do not commit `.env`.

The LLM backend must expose an OpenAI-compatible `/chat/completions` endpoint.

Important environment variables:

- `AGREE_MODEL_BASE_URL`
- `AGREE_MODEL_API_KEY`
- `AGREE_MODEL_NAME`
- `AGREE_SOURCE_ROOT`
- `AGREE_RESULT_ROOT`
- `AADL_INSPECTOR_PATH`
- `OSATE_HOME`
- `JAVA_HOME`
- `AGREE_VALIDATOR_ROOT`

## Dataset layout

The default case runner expects cases in this format:

```text
data/Sources/
??? Case01_A/
    ??? Case01_Base.txt
    ??? Case01_Req.txt
    ??? Case01/
        ??? dependency_package_1.aadl
        ??? dependency_package_2.aadl
```

`CaseXX_Base.txt` contains the base AADL model text. `CaseXX_Req.txt` contains the natural-language requirement. The nested `CaseXX/` directory contains AADL dependencies referenced by `with` clauses.

## Run one case

```powershell
python run_case.py `
  --case-num 1 `
  --case-letter A `
  --use-rag `
  --llm-base-url $env:AGREE_MODEL_BASE_URL `
  --llm-api-key $env:AGREE_MODEL_API_KEY `
  --llm-model-name $env:AGREE_MODEL_NAME `
  --result-root ./results
```

## Run a batch

```powershell
python scripts/run_batch.py --start 1 --end 10 --letters A B --result-root ./results
```

## Outputs

Each case writes a report directory under `AGREE_RESULT_ROOT`:

```text
results/Case01_A/Report/
??? Case01_first.txt
??? Case01_initial.txt
??? Case01_fixed.txt
??? Case01_errors.txt
??? Case01_report.md
??? Case01_report.json
```

## Notes

This repository intentionally excludes large vector databases, generated experiment results, local AADL/OSATE installations, and private API keys.

## Citation

If you use this framework in academic work, please cite this repository. A `CITATION.cff` file is provided.
