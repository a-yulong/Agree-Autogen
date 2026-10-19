# Experiments

All selected configurations use the 459 cases in `data/benchmark/cases/`.

| Manuscript comparison | Configurations |
| --- | --- |
| RQ1 | Full framework and Direct generation |
| RQ2 | Retrieval depths, analysis-stage ablations, digest, strategy guidance, and target-context ablations |
| RQ3 | Full framework with five model backbones |

The selected result directories are listed in `paper/data/source_manifest.json`. The original batch scripts are in `experiments/original_runs/`.

```powershell
python experiments/run_experiment.py `
  --setting E2 `
  --benchmark data/benchmark/cases `
  --start 1 `
  --end 10 `
  --output-dir outputs/e2_cases_1_10
```

Aggregate a run:

```powershell
python scripts/aggregate_experiment_results.py --result-root outputs/e2_cases_1_10
```

Recompute manuscript tables:

```powershell
python paper/scripts/recompute_statistics.py
```
