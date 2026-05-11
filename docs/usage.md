# Usage

## Installation

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

Optional conda setup:

```powershell
conda env create -f environment.yml
conda activate agree-autogen
```

## Model Configuration

AGREE-AutoGen uses an OpenAI-compatible chat-completions endpoint:

```powershell
$env:AGREE_MODEL_BASE_URL = "https://api.example.com/v1"
$env:AGREE_MODEL_API_KEY = "replace-with-your-key"
$env:AGREE_MODEL_NAME = "model-name"
```

## Direct File Run

Start with a dry run:

```powershell
python scripts/run_files.py --requirement data/examples/gf_monitor/requirement.txt --aadl data/examples/gf_monitor/input.aadl --output-dir outputs/gf_monitor --disable-rag --skip-validation --dry-run
```

Run generation after model credentials are configured:

```powershell
python scripts/run_files.py --requirement data/examples/gf_monitor/requirement.txt --aadl data/examples/gf_monitor/input.aadl --output-dir outputs/gf_monitor --skip-validation
```

## Case-Layout Run

```powershell
python scripts/run_case.py --case-num 1 --case-letter A --result-root outputs/case01
python scripts/run_batch.py --start 1 --end 10 --letters A B --result-root outputs/batch
```

The case-layout runner expects `CaseXX_A/CaseXX_Base.txt` and `CaseXX_A/CaseXX_Req.txt` under `AGREE_SOURCE_ROOT` or `data/Sources`.

## Validation Tools

AADL-level validation uses AADL Inspector when configured. AGREE-level validation uses the standalone validator under `tools/agree-validator/`.

Common environment variables:

```powershell
$env:AADL_INSPECTOR_PATH = "path/to/aadl-inspector"
$env:JAVA_HOME = "path/to/jdk17"
$env:OSATE_HOME = "path/to/osate"
$env:AGREE_VALIDATOR_ROOT = "tools/agree-validator"
```

If validators are not configured, wrappers return a configuration status rather than reporting validation success.

## Common Failures

| Symptom | Likely cause | Action |
| --- | --- | --- |
| missing model configuration | model endpoint variables are unset | set `AGREE_MODEL_BASE_URL`, `AGREE_MODEL_API_KEY`, and `AGREE_MODEL_NAME` |
| RAG directory not found | `AGREE_DOCS_DIR` points to a missing path | set it to a prepared corpus directory or use `--disable-rag` |
| validator not configured | Java, OSATE, or validator paths are missing | configure validation variables or use `--skip-validation` |
| unsupported experiment setting | runtime switch is not implemented | check `experiments/settings.yaml` |
