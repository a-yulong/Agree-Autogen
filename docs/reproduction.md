# Reproduction

This document describes the intended experiment settings. Full benchmark data may require separate access.

## Experiment settings

- E1 Bare Model: direct-generation baseline with RAG, repair, model analysis, requirement analysis, and fusion disabled where supported.
- E2 Full Framework: complete AGREE-AutoGen pipeline.
- E3 NoRAG: disable retrieval augmentation.
- E4 NoRepair: disable iterative repair.
- E5 No Model Analyst: disable model-analysis agent.
- E6 No Requirement Analyst: disable requirement-analysis agent.
- E7 No Dual Analysts: disable both model and requirement analysts.

The current public scripts provide command-line templates for these settings. Some ablations require additional integration with the full benchmark runner.

## Run scripts

```powershell
python experiments/run_e2_full_framework.py --start 1 --end 10 --letters A
python experiments/run_ablation.py --setting E3 --start 1 --end 10 --letters A
```

## Metrics

- FVSR: final validation success rate.
- ZRR: zero-repair rate.
- IEC: initial error count.
- ARR: average repair rounds.
- RRR: rescue rate for cases fixed after initially failing.
- MFR: multi-round failure ratio.
- ART: average runtime.
- ATC: average token consumption.

Use:

```powershell
python experiments/compute_metrics.py --results-dir ./results --output ./results/metrics/metrics.csv
```

Do not report experimental conclusions from private or incomplete data without documenting the dataset and configuration.

