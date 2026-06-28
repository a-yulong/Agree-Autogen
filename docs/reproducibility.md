# Reproducibility

This repository supports three reproducibility levels:

1. offline inspection of benchmark inputs, prompts, knowledge sources, code, and released aggregate results;
2. dry-run execution without model-provider calls or external validators;
3. full generation and validation with an OpenAI-compatible model endpoint, JDK 17, OSATE/AGREE, and the standalone validator.

## Install

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

## Offline Tests

```powershell
python -m pytest -q
```

These tests use the released benchmark files and do not call an LLM provider.

## Dry Run On A Released Case

```powershell
python scripts/run_files.py `
  --requirement data/benchmark/cases/Case01/Case01_Req.txt `
  --aadl data/benchmark/cases/Case01/Case01_Base.aadl `
  --output-dir outputs/case01_dry `
  --setting E2 `
  --skip-validation `
  --dry-run
```

Expected files:

```text
outputs/case01_dry/
  dry_run_report.json
  input.aadl
  requirement.txt
```

## Model-Backed Run

Configure any OpenAI-compatible endpoint:

```powershell
$env:AGREE_MODEL_BASE_URL = "https://api.example.com/v1"
$env:AGREE_MODEL_API_KEY = "replace-with-your-key"
$env:AGREE_MODEL_NAME = "model-name"
```

Run a small benchmark slice:

```powershell
python experiments/run_experiment.py `
  --setting E2 `
  --benchmark data/benchmark/cases `
  --start 1 `
  --end 5 `
  --output-dir outputs/e2_cases_1_5
```

## Validator Setup

Full validation additionally requires:

- JDK 17;
- a local OSATE installation with AGREE support;
- the validator source under `tools/agree-validator`.

Build the validator:

```powershell
$env:JAVA_HOME = "path\to\jdk17"
$env:OSATE_HOME = "path\to\osate"
.\tools\agree-validator\build.ps1
```

The pipeline reads bundled AADL support files from `tools/agree-validator/static-libs` and `tools/agree-validator/dependency_resources`.

## Result Aggregation

Aggregate per-case reports:

```powershell
python scripts/aggregate_experiment_results.py --result-root outputs/e2_cases_1_5
```

The released aggregate result files under `results/` were computed from per-case JSON reports using this reporting schema. The complete per-case result tree is distributed as an external archive artifact because it is too large and file-heavy for the main Git history.
