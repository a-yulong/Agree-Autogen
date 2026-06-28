# Scripts

This directory contains the core entry points used to inspect and reproduce the released artifact.

## Core Runners

- `run_files.py`: run the pipeline on one AADL file and one requirement file.
- `run_case.py`: run one numbered benchmark case.
- `run_existing_batch.py`: run a range of released benchmark cases from `data/benchmark/cases`.
- `aggregate_experiment_results.py`: compute aggregate metrics from per-case reports.
- `build_rag_index.py`: inspect or build retrieval assets from `knowledge_base`.

## Typical Commands

Offline dry run on a released case:

```powershell
python scripts/run_files.py `
  --requirement data/benchmark/cases/Case01/Case01_Req.txt `
  --aadl data/benchmark/cases/Case01/Case01_Base.aadl `
  --output-dir outputs/case01_dry `
  --setting E2 `
  --skip-validation `
  --dry-run
```

Run a small benchmark subset with a configured model endpoint:

```powershell
python scripts/run_existing_batch.py `
  --source-root data/benchmark/cases `
  --case-from 1 `
  --case-to 5 `
  --canonical-one-per-number `
  --setting E2 `
  --result-root outputs/e2_cases_1_5
```

Aggregate reports:

```powershell
python scripts/aggregate_experiment_results.py --result-root outputs/e2_cases_1_5
```
