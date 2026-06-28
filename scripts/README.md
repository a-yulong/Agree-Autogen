# Scripts

This directory contains command-line entry points for single-case execution, batch execution, experiment launchers, reruns, aggregation, and data preparation.

## Recommended Entry Points

| Script | Purpose |
|---|---|
| `run_files.py` | Run AGREE-AutoGen from one requirement file and one AADL file. |
| `run_case.py` | Run a single benchmark-layout case. |
| `run_existing_batch.py` | Run a range of existing benchmark cases. |
| `aggregate_experiment_results.py` | Aggregate per-case reports into summary files. |
| `build_rag_index.py` | Build or inspect retrieval assets from `knowledge_base/`. |

## Experiment Launchers

The PowerShell launchers encode the reported experiment suites:

| Script | Purpose |
|---|---|
| `run_result_v4_rq1.ps1` | Model-comparison experiment launcher. |
| `run_result_v4_rq2_topk_one.ps1` | Retrieval-setting run for one configuration. |
| `run_result_v4_rq2_topk_rerun_needed.ps1` | Scoped rerun helper for missing or provider-failed retrieval cases. |
| `run_result_v4_rq3_agent_one.ps1` | Agent-ablation run for one setting. |
| `run_result_v4_rq4_optimization_one.ps1` | Optimization-ablation run for one setting. |
| `run_result_v4_post_rq1_all.ps1` | Multi-setting orchestration after the model-comparison phase. |

Experiment launchers may contain Windows and PowerShell assumptions. When adapting them to another machine, update paths through parameters or environment variables rather than editing source logic where possible.

## Rerun Helpers

Rerun scripts should be used only for:

- missing reports;
- provider errors;
- quota interruptions;
- timeout or empty-response stage errors;
- other infrastructure failures documented in the run log.

They should not silently replace ordinary validator failures.

## Data-Preparation Utilities

Several scripts support dataset and requirement preparation:

- `clean_source_requirements.py`;
- `curate_sources_requirements_mixed.py`;
- `generate_aadllib_requirements.py`;
- `regenerate_sources_agree_reqs.py`;
- `regenerate_sources_fresh_agree_reqs.py`;
- `regenerate_sources_strong_model_reqs.py`;
- `rewrite_curated_requirements_behavior_style.py`;
- `rewrite_curated_requirements_paragraph_style.py`;
- `translate_sources_to_english.py`.

These utilities are included for traceability and future dataset maintenance. They are not required for running the bundled example.

## Aggregation

Use `aggregate_experiment_results.py` to compute metrics from per-case reports. Aggregation should read JSON reports rather than relying on process completion markers or console logs.
