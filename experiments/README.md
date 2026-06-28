# Experiments

This directory contains lightweight experiment configuration, runner utilities, sample reports, and metric computation scripts.

## Files

| File | Purpose |
|---|---|
| `settings.yaml` | Machine-readable experiment settings. |
| `run_experiment.py` | Case-layout experiment runner. |
| `compute_metrics.py` | Metric computation from per-case reports. |
| `sample_results/` | Minimal report examples used for schema and metric checks. |

## Example

```powershell
python experiments/run_experiment.py `
  --setting E2 `
  --benchmark data/Sources `
  --output-dir outputs/e2 `
  --start 1 `
  --end 10 `
  --letters A

python experiments/compute_metrics.py `
  --results-dir outputs/e2 `
  --output outputs/e2/metrics.csv
```

For full released experiment suites, use the RQ-specific launchers and aggregation scripts under `scripts/`. The detailed design is documented in `docs/experiment_design.md`.
