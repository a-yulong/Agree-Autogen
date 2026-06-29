# Usage

## Install

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

## Dry Run

```powershell
python scripts/run_files.py `
  --requirement data/benchmark/cases/Case001/Case001_Req.txt `
  --aadl data/benchmark/cases/Case001/Case001_Base.aadl `
  --output-dir outputs/Case001_dry `
  --disable-rag `
  --skip-validation `
  --dry-run
```

## Model Configuration

AGREE-AutoGen uses an OpenAI-compatible endpoint:

```powershell
$env:AGREE_MODEL_BASE_URL = "https://api.example.com/v1"
$env:AGREE_MODEL_API_KEY = "replace-with-your-key"
$env:AGREE_MODEL_NAME = "model-name"
```

## Run Released Benchmark Cases

```powershell
python scripts/run_existing_batch.py `
  --source-root data/benchmark/cases `
  --case-from 1 `
  --case-to 10 `
  --canonical-one-per-number `
  --setting E2 `
  --result-root outputs/e2_cases_1_10
```

## Validation Tools

AADL-level validation uses AADL Inspector when configured. AGREE-level validation uses `tools/agree-validator`.

```powershell
$env:AADL_INSPECTOR_PATH = "path/to/aadl-inspector"
$env:JAVA_HOME = "path/to/jdk17"
$env:OSATE_HOME = "path/to/osate"
$env:AGREE_VALIDATOR_ROOT = "tools/agree-validator"
```

If validators are not configured, wrappers return a configuration status rather than reporting validation success.

