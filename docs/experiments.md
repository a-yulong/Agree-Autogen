# Experiments

The released experiments are organized around the 459 benchmark cases in `data/benchmark/cases`. Every case produces a JSON report, and aggregate tables are computed from those reports.

## Benchmark Inputs

The benchmark contains:

- 459 case directories;
- 459 AADL model files;
- 459 natural-language requirement files;
- 459 requirement-analysis reference files;
- `data/benchmark/cases_manifest.csv` for file-level inventory.

## Experiment Axes

- **RQ1 model comparison:** full AGREE-AutoGen workflow with different base models.
- **RQ2 retrieval configuration:** balanced retrieval compared with smaller and larger retrieval depths.
- **RQ3 agent contribution:** direct generation and analysis-stage ablations compared against the full workflow.
- **RQ4 optimization ablation:** retrieval digest, agent strategy guidance, and target-context expansion.

The exact metrics are defined in `docs/result_schema.md`.

## Running A Benchmark Slice

```powershell
python experiments/run_experiment.py `
  --setting E2 `
  --benchmark data/benchmark/cases `
  --start 1 `
  --end 10 `
  --output-dir outputs/e2_cases_1_10
```

## Aggregating Results

```powershell
python scripts/aggregate_experiment_results.py --result-root outputs/e2_cases_1_10
```

Released aggregate files and per-case result trees are stored under `results/`.
