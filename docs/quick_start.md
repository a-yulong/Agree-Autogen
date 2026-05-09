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

## 3. Run a dry run from direct files

New users should start with the direct-file CLI:

```powershell
python scripts/run_files.py `
  --requirement data/examples/gf_monitor/requirement.txt `
  --aadl data/examples/gf_monitor/input.aadl `
  --output-dir outputs/gf_monitor `
  --disable-rag `
  --skip-validation `
  --dry-run
```

This command does not call an LLM and does not call external validators. It writes `outputs/gf_monitor/dry_run_report.json`.

## 4. Run generation from direct files

Configure a model endpoint first:

```powershell
$env:AGREE_MODEL_BASE_URL = "https://api.example.com/v1"
$env:AGREE_MODEL_API_KEY = "replace-with-your-key"
$env:AGREE_MODEL_NAME = "your-model-name"
```

Then run:

```powershell
python scripts/run_files.py `
  --requirement data/examples/gf_monitor/requirement.txt `
  --aadl data/examples/gf_monitor/input.aadl `
  --output-dir outputs/gf_monitor `
  --disable-rag `
  --skip-validation
```

Expected files:

```text
outputs/gf_monitor/requirement.txt
outputs/gf_monitor/input.aadl
outputs/gf_monitor/generated_output.aadl
outputs/gf_monitor/final_output.aadl
outputs/gf_monitor/report.json
```

If the API key is missing, the script writes `report.json` with a configuration error instead of printing an unhandled traceback.

## 5. Legacy case-layout input

The current production entry point expects the `CaseXX_A` benchmark layout described in `data/README.md`. Prepare the public GF_Monitor example as `Case01_A`:

```powershell
python scripts/prepare_gf_monitor_case.py --case-num 1 --case-letter A --source-root ./data/Sources
```

The generated `data/Sources` directory is ignored by Git.

## 6. Run the current case-based pipeline

With a configured LLM endpoint:

```powershell
python run_case.py --case-num 1 --case-letter A --use-rag --result-root ./results
```

For a no-RAG smoke run:

```powershell
python run_case.py --case-num 1 --case-letter A --no-rag --result-root ./results
```

## 7. Validator behavior

If `AADL_INSPECTOR_PATH`, `JAVA_HOME`, `OSATE_HOME`, or `AGREE_VALIDATOR_ROOT` are not configured, external validation cannot run. Lightweight wrappers report `not_configured`; the full pipeline requires the external tools for validation-ready execution.

## 8. Outputs

Generated case reports are written under:

```text
results/CaseXX_A/Report/
```
