# Experiment results

The directory names retain historical experiment IDs. For the current manuscript's RQ1--RQ3, use `paper/data/source_manifest.json` for run selection and `paper/data/statistics/` for recomputed results.

| Directory | Content |
| --- | --- |
| `RQ1_full_e2_rag_models/` | Full-framework model runs, including an earlier GPT provider-failure run. |
| `RQ2_rag_topk/` | Retrieval-depth runs. |
| `RQ3_agent/` | Direct baseline and analysis ablations. |
| `RQ4_optimization/` | Digest, guidance, and target-context ablations. |
| `paper_runs/gpt-5.4-high-stable/` | Final GPT run selected for the current manuscript. |
| `expert_review/` | Full/Direct paired rubric inputs and ratings. |
| `expert_review_rq1_full/` | Five-model paired rubric inputs and ratings. |

Per-case reports retain validator outcomes, repair counts, measured cost, and stage errors. Provider/stage errors and validator rejection are distinct outcomes.

## Historical summaries

`completed_experiments_summary.*` and `all_experiments_summary_20260622.*` are historical summaries. They do not select the final manuscript GPT run and their zero-valued timing columns must not be used as measured execution cost. Their directory IDs are not the current manuscript's RQ labels.

## Current statistics

Run `python paper/scripts/recompute_statistics.py` from the repository root. The source selections and case-level extracts are documented in `paper/README.md`. This recomputes exact numerical results without regenerating figures or calling model services.
