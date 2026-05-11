# Quick Start

## Inputs

GF_Monitor example:

- `data/examples/gf_monitor/requirement.txt`
- `data/examples/gf_monitor/input.aadl`
- `data/examples/gf_monitor/expected_output.aadl`

The expected output is illustrative and should be checked with local OSATE/AGREE tools before use as a benchmark artifact.

## Dry Run

```powershell
python scripts/run_files.py `
  --requirement data/examples/gf_monitor/requirement.txt `
  --aadl data/examples/gf_monitor/input.aadl `
  --output-dir outputs/gf_monitor `
  --disable-rag `
  --skip-validation `
  --dry-run
```

Expected outputs:

```text
outputs/gf_monitor/dry_run_report.json
outputs/gf_monitor/requirement.txt
outputs/gf_monitor/input.aadl
```

The dry run does not call an LLM or external validators.

## Generation Run

Set model configuration:

```powershell
$env:AGREE_MODEL_BASE_URL = "https://api.example.com/v1"
$env:AGREE_MODEL_API_KEY = "replace-with-your-key"
$env:AGREE_MODEL_NAME = "your-model-name"
```

Run:

```powershell
python scripts/run_files.py `
  --requirement data/examples/gf_monitor/requirement.txt `
  --aadl data/examples/gf_monitor/input.aadl `
  --output-dir outputs/gf_monitor `
  --disable-rag `
  --skip-validation
```

Expected outputs when generation succeeds:

```text
outputs/gf_monitor/generated_output.aadl
outputs/gf_monitor/final_output.aadl
outputs/gf_monitor/report.json
```

If model configuration is missing, `report.json` records the configuration error.

## Case-Layout Runner

The legacy benchmark runner remains available:

```powershell
python scripts/prepare_gf_monitor_case.py --case-num 1 --case-letter A --source-root ./data/Sources
python run_case.py --case-num 1 --case-letter A --no-rag --result-root ./results
```

Reports are written under `results/CaseXX_A/Report/`.

