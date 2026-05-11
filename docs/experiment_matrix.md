# Experiment Matrix

| ID | Setting | RAG | Repair | Model Analyst | Requirement Analyst | Fusion | Public status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | Bare Model | Off | Off | Off | Off | Off | Template; requires direct-generation runtime switch |
| E2 | Full Framework | On | On | On | On | On | Executable with configured LLM and case-layout data |
| E3 | NoRAG | Off | On | On | On | On | Executable with configured LLM and case-layout data |
| E4 | NoRepair | On | Off | On | On | On | Template; requires repair-loop switch |
| E5 | No Model Analyst | On | On | Off | On | On | Template; requires model-analyst switch and fallback representation |
| E6 | No Requirement Analyst | On | On | On | Off | On | Template; requires requirement-analyst switch |
| E7 | No Dual Analysts | On | On | Off | Off | On | Template; requires both analyst switches |

Configuration files are under `experiments/configs/`.

Sample results under `experiments/sample_results/` document the result-file format used by `compute_metrics.py`. They are not paper benchmark results.
