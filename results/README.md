# Experiment Results

This directory contains the released AGREE-AutoGen experiment outputs used for the reported RQ1-RQ4 analysis.

## Result Sets

| Directory | Content |
|---|---|
| `RQ1_full_e2_rag_models/` | Full E2 pipeline results for the model comparison. |
| `RQ2_rag_topk/` | Retrieval top-k comparison under the Qwen setting, including the balanced 3-3-3 baseline. |
| `RQ3_agent/` | Agent-ablation results for direct generation and the analyst-ablation settings retained in the final study. |
| `RQ4_optimization/` | Optimization-ablation results for raw RAG without digest, no agent strategy guidance, and full target context. |

Each setting directory contains per-case outputs under `Case001` to `Case459` when the setting has completed the full benchmark. A case directory preserves the generated reports and intermediate artifacts produced by the run.

## Aggregate Tables

The root CSV and Markdown files summarize the same result set:

- `completed_experiments_summary.csv`
- `completed_experiments_summary.md`
- `all_experiments_summary_20260622.csv`
- `all_experiments_summary_20260622.md`

The aggregate tables report completed cases, final successes, final failures, stage errors, first-pass successes, repair-round counts, and timing/token statistics when available.

## Metric Source

Metrics are computed from `Case*_report.json` files. A case is counted as completed when its report contains a case identifier and a success field. Validator failures remain experimental failures. Provider or stage errors are counted separately when the report marks them as stage errors.
