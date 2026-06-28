# Experiments

The released experiments use the 459 benchmark cases in `data/benchmark/cases` and the same JSON report schema across all settings.

## Experiment Axes

- **Model comparison:** run the full AGREE-AutoGen workflow with different base models.
- **Retrieval configuration:** compare balanced retrieval against smaller and larger retrieval depths.
- **Agent contribution:** compare the full workflow against direct generation and analysis-stage ablations.
- **Optimization ablation:** isolate retrieval digest, agent strategy guidance, and target-context expansion.

## Runner

`run_experiment.py` is a thin wrapper around `scripts/run_existing_batch.py`.

```powershell
python experiments/run_experiment.py `
  --setting E2 `
  --benchmark data/benchmark/cases `
  --start 1 `
  --end 10 `
  --output-dir outputs/e2_cases_1_10
```

Full runs require model-provider credentials and the validator dependencies described in `docs/validator_setup.md`. The committed result summaries under `results/` were computed from completed per-case JSON reports.
