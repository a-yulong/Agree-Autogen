# Experiments

`experiments/settings.yaml` defines E1-E7.

| ID | Setting | Public runner status |
| --- | --- | --- |
| E1 | Bare Model | unsupported; requires direct-generation runner |
| E2 | Full Framework | executable |
| E3 | NoRAG | executable |
| E4 | NoRepair | unsupported; requires repair-loop switch |
| E5 | No Model Analyst | unsupported; requires model-analyst switch |
| E6 | No Requirement Analyst | unsupported; requires requirement-analyst switch |
| E7 | No Dual Analysts | unsupported; requires analyst switches |

Run an executable setting:

```powershell
python experiments/run_experiment.py --setting E2 --benchmark data/Sources --output-dir outputs/e2 --start 1 --end 10 --letters A
python experiments/run_experiment.py --setting E3 --benchmark data/Sources --output-dir outputs/e3 --start 1 --end 10 --letters A
```

Compute metrics:

```powershell
python experiments/compute_metrics.py --results-dir outputs/e2 --output outputs/e2/metrics.csv
```

RAG is enabled in E2 and disabled in E3. The full framework uses `AGREE_DOCS_DIR` or the configured knowledge-base directory; `scripts/build_rag_index.py --dry-run` shows the source files available for RAG preparation.

Sample result files under `experiments/sample_results/` document the report format consumed by `compute_metrics.py`.

Recommended benchmark metadata fields:

- `case_id`
- `case_type`
- `requirement_path`
- `aadl_path`
- `target_component`
- `data_source`
- `access_status`
- `notes`
