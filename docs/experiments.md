# Experiments

Experiment configuration is stored in `experiments/settings.yaml` and the experiment launch scripts under `scripts/`.

The evaluation studies four dimensions:

- base model behavior under a fixed generation pipeline;
- retrieval support and retrieval configuration;
- contribution of analysis agents;
- optimization mechanisms inside the full workflow.

The detailed design is documented in `docs/experiment_design.md`. Result fields and metric definitions are documented in `docs/result_schema.md`.

## Running a Case-Layout Experiment

```powershell
python experiments/run_experiment.py `
  --setting E2 `
  --benchmark data/Sources `
  --output-dir outputs/e2 `
  --start 1 `
  --end 10 `
  --letters A
```

## Computing Metrics

```powershell
python experiments/compute_metrics.py `
  --results-dir outputs/e2 `
  --output outputs/e2/metrics.csv
```

For released experiment suites, prefer the RQ-specific launchers and aggregation scripts under `scripts/`, because they preserve the run configuration used for paper-level results.

## Benchmark Metadata

Recommended benchmark metadata fields:

- `case_id`;
- `case_type`;
- `requirement_path`;
- `aadl_path`;
- `target_component`;
- `data_source`;
- `access_status`;
- `notes`.

Each released result set should record its benchmark manifest and aggregation command.
