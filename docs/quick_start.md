# Quick Start

This guide runs the minimal GF_Monitor example.

## 1. Install dependencies

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

## 2. Inspect the example

Input files:

- `data/examples/gf_monitor/requirement.txt`
- `data/examples/gf_monitor/input.aadl`

Illustrative expected output:

- `data/examples/gf_monitor/expected_output.aadl`

## 3. Prepare a case-layout input

The current production entry point expects the `CaseXX_A` benchmark layout described in `data/README.md`. Prepare the public GF_Monitor example as `Case01_A`:

```powershell
python scripts/prepare_gf_monitor_case.py --case-num 1 --case-letter A --source-root ./data/Sources
```

The generated `data/Sources` directory is ignored by Git.

## 4. Run the current case-based pipeline

With a configured LLM endpoint:

```powershell
python run_case.py --case-num 1 --case-letter A --use-rag --result-root ./results
```

For a no-RAG smoke run:

```powershell
python run_case.py --case-num 1 --case-letter A --no-rag --result-root ./results
```

## 5. Validator behavior

If `AADL_INSPECTOR_PATH`, `JAVA_HOME`, `OSATE_HOME`, or `AGREE_VALIDATOR_ROOT` are not configured, external validation cannot run. Lightweight wrappers report `not_configured`; the full pipeline requires the external tools for validation-ready execution.

## 6. Outputs

Generated case reports are written under:

```text
results/CaseXX_A/Report/
```
