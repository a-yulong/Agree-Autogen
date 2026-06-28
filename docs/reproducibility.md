# Reproducibility

This document describes how to inspect, smoke-test, and rerun AGREE-AutoGen experiments. The artifact separates offline checks from executions that require external tools or model-provider credentials.

## Environment

The core Python package requires:

- Python 3.9 or later;
- dependencies listed in `requirements.txt`;
- PowerShell for the provided Windows experiment launchers.

The standalone AGREE validator additionally requires:

- JDK 17;
- a local OSATE installation with AGREE support;
- the validator classes and static libraries under `tools/agree-validator/`.

Model-backed generation requires an OpenAI-compatible endpoint configured through environment variables:

```powershell
$env:AGREE_MODEL_BASE_URL = "https://api.example.com/v1"
$env:AGREE_MODEL_API_KEY = "replace-with-your-key"
$env:AGREE_MODEL_NAME = "model-name"
```

Provider credentials are intentionally not part of the repository.

## Installation

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

## Offline Checks

The following tests do not call a model provider and do not require OSATE:

```powershell
python -m pytest -q tests/test_fusion.py tests/test_model_analyst.py tests/test_validators.py tests/test_metrics.py tests/test_build_rag_index.py tests/test_experiment_configs.py tests/test_run_files_cli.py
```

These tests cover model parsing utilities, fusion behavior, validator wrappers, metrics, experiment configuration, retrieval-index utilities, and the direct-file CLI.

## Dry-Run Execution

The bundled `GF_Monitor` example can be used to check the command-line interface and artifact output layout:

```powershell
python scripts/run_files.py `
  --requirement data/examples/gf_monitor/requirement.txt `
  --aadl data/examples/gf_monitor/input.aadl `
  --output-dir outputs/gf_monitor_dry `
  --setting E2 `
  --skip-validation `
  --dry-run
```

Expected output:

```text
outputs/gf_monitor_dry/
  dry_run_report.json
  input.aadl
  requirement.txt
```

This check validates paths, configuration loading, and report emission without calling an LLM or external validator.

## Validator Check

Set the Java and OSATE paths:

```powershell
$env:JAVA_HOME = "D:\jdk17"
$env:OSATE_HOME = "E:\osate2-2.12.0-vfinal-win32.win32.x86_64"
```

Run the standalone validator:

```powershell
.\tools\agree-validator\run-validator.ps1 `
  -Workspace "<workspace-dir>" `
  -Project "<workspace-dir>\CaseProject" `
  -JavaHome $env:JAVA_HOME `
  -OsateHome $env:OSATE_HOME `
  -FocusFile "model.aadl" `
  -Output "<workspace-dir>\validation-report.json"
```

A clean validation report has the following form:

```json
{
  "infos": 0,
  "warnings": 0,
  "errors": 0,
  "issues": []
}
```

Validation failures are reported as JSON diagnostics and should be treated according to the experiment policy. A validator failure is a case outcome, not an infrastructure failure.

## Single-Case Generation

After configuring model credentials, run:

```powershell
python scripts/run_files.py `
  --requirement data/examples/gf_monitor/requirement.txt `
  --aadl data/examples/gf_monitor/input.aadl `
  --output-dir outputs/gf_monitor_e2 `
  --setting E2
```

The output directory contains copied inputs, intermediate artifacts, generated AADL/AGREE content, validation records, and a JSON report.

## Case-Layout Execution

For benchmark-style datasets with case directories, use:

```powershell
python scripts/run_case.py `
  --case-root "<case-directory>" `
  --output-root "<output-directory>" `
  --setting E2
```

For existing case ranges, use:

```powershell
python scripts/run_existing_batch.py `
  --source-root "<source-root>" `
  --output-root "<output-root>" `
  --start 1 `
  --end 459 `
  --setting E2
```

PowerShell launchers under `scripts/` provide the experiment-specific orchestration used for the reported RQ suites.

## Aggregating Results

Aggregate per-case reports with:

```powershell
python scripts/aggregate_experiment_results.py `
  --result-root "<result-root>" `
  --output "<aggregate-output>"
```

The aggregate files should be used for paper tables and repository summaries. Field definitions are documented in `docs/result_schema.md`.

## Rerun Policy

The experiment pipeline distinguishes model outputs from infrastructure interruptions:

- ordinary AADL/AGREE validator failures are retained as experimental outcomes;
- missing reports may be rerun;
- API, provider, quota, timeout, or empty-response stage errors may be rerun;
- reruns should be scoped to the affected cases and should not overwrite confirmed validator-failure outcomes without a documented reason.

This policy preserves the distinction between a model producing an invalid contract and a service interruption preventing the case from completing.

## Reproduction Boundaries

Full reproduction depends on external model services. Provider routing, model revisions, quota state, and transient availability can affect generated outputs. The repository therefore supports two complementary checks:

- deterministic inspection of prompts, code, configurations, knowledge sources, and stored results;
- rerun-based reproduction using the documented environment and scripts.

Reported metrics should be traced to stored per-case records whenever exact model outputs cannot be regenerated byte-for-byte.
