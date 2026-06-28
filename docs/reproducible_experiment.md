# Reproducible Minimal Experiment

This note describes the minimal setup for reproducing the public AGREE-AutoGen runners from a fresh clone. It focuses on the Case01_A smoke runs used before larger RQ1 experiments.

## 1. Runtime Requirements

- Python: 3.9 or newer.
- Java/JDK: JDK 17.
- OSATE: an OSATE installation with a `plugins/` directory.
- AADL Inspector: optional for AADL-level static parsing, but required for the full validation path.
- OpenAI-compatible LLM endpoint, such as OpenRouter.

Install Python dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

## 2. Environment Variables

Configure the model endpoint:

```powershell
$env:AGREE_MODEL_BASE_URL = "https://openrouter.ai/api/v1"
$env:AGREE_MODEL_API_KEY = "replace-with-your-openrouter-key"
$env:AGREE_MODEL_NAME = "qwen/qwen3-coder-30b-a3b-instruct"
```

Configure validators:

```powershell
$env:JAVA_HOME = "path\to\jdk17"
$env:OSATE_HOME = "path\to\osate"
$env:AADL_INSPECTOR_PATH = "path\to\AADLInspector.exe"
$env:AGREE_VALIDATOR_ROOT = "$PWD\tools\agree-validator"
```

For Windows consoles, UTF-8 output is recommended:

```powershell
$env:PYTHONIOENCODING = "utf-8"
$env:PYTHONUTF8 = "1"
```

## 3. Build the Standalone AGREE Validator

The validator classes are intentionally not committed. Build them after cloning:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\agree-validator\build.ps1 `
  -JavaHome $env:JAVA_HOME `
  -OsateHome $env:OSATE_HOME
```

Successful build output creates:

```text
tools/agree-validator/out/
```

Do not reuse older validator builds whose main class is `com.example.agreevalidator.AgreeValidationCli`. This repository expects:

```text
org.agreeautogen.validator.AgreeValidationCli
```

## 4. Benchmark Layout

The case runner expects:

```text
AGREE_SOURCE_ROOT/
  Case01_A/
    Case01_Base.txt
    Case01_Req.txt
    Case01/
      referenced_package.aadl
```

Set the source root if the benchmark is outside `data/Sources`:

```powershell
$env:AGREE_SOURCE_ROOT = "path\to\Sources"
```

## 5. Run Case01_A / E1 Bare Model

E1 performs one direct generation pass without RAG, Requirement Analyst, Model Analyst, fusion staging, or repair. It still runs the same AADL/AGREE validators and writes the same report structure.

```powershell
python scripts/run_case.py `
  --setting E1 `
  --case-num 1 `
  --case-letter A `
  --result-root outputs\e1_case01
```

Expected report files:

```text
outputs/e1_case01/Case01_A/Report/Case01_report.json
outputs/e1_case01/Case01_A/Report/Case01_report.md
```

## 6. Run Case01_A / E2 Full AGREE-AutoGen

E2 runs the full pipeline with RAG, Model Analyst, Requirement Analyst, AGREE Generator, Model Fusion, and validation-guided repair.

```powershell
python scripts/run_case.py `
  --setting E2 `
  --case-num 1 `
  --case-letter A `
  --use-rag `
  --result-root outputs\e2_case01
```

By default, the runner recursively loads RAG documents from:

```text
knowledge_base/
```

You can override this with:

```powershell
$env:AGREE_DOCS_DIR = "path\to\knowledge_base"
```

## 7. Run via Experiment Entry Point

```powershell
python experiments/run_experiment.py `
  --setting E1 `
  --benchmark $env:AGREE_SOURCE_ROOT `
  --output-dir outputs\rq1_e1_case01 `
  --start 1 `
  --end 1 `
  --letters A

python experiments/run_experiment.py `
  --setting E2 `
  --benchmark $env:AGREE_SOURCE_ROOT `
  --output-dir outputs\rq1_e2_case01 `
  --start 1 `
  --end 1 `
  --letters A
```

## 8. How to Confirm Validators Really Ran

Open `Case01_report.json` and check:

```json
"validation_summary": {
  "aadl_inspector_executed": true,
  "agree_validator_executed": true,
  "agree_raw_output_present": true,
  "inspection_raw_output_present": true
}
```

The markdown report also contains a `Reproducibility Metadata` section with the same execution flags.

## 9. Common Failures

| Symptom | Likely cause | Action |
| --- | --- | --- |
| `AGREE_MODEL_API_KEY is not configured` | Missing model endpoint key | Set `AGREE_MODEL_API_KEY`. |
| `No PDF, TXT, or MD documents found in RAG directory` | Wrong `AGREE_DOCS_DIR` | Point it to `knowledge_base` or another directory containing `.pdf`, `.txt`, or `.md` files. |
| `Standalone validator output directory not found` | Validator was not built | Run `tools/agree-validator/build.ps1`. |
| `ClassNotFoundException: org.agreeautogen.validator.AgreeValidationCli` | Wrong validator build or stale validator root | Rebuild this repository's `tools/agree-validator` and set `AGREE_VALIDATOR_ROOT` to it. |
| AADL Inspector report exists but all AADL errors are zero | AADL Inspector produced a successful Tcl-array report | This is expected; check `inspection_raw_output_present` to confirm the report was read. |
| Console output breaks on Windows | Console encoding issue | Set `PYTHONIOENCODING=utf-8` and `PYTHONUTF8=1`; reports are written as UTF-8. |
