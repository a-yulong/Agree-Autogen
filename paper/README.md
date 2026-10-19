# Empirical evaluation records

This directory contains case-level measurements and numerical analysis for the manuscript.

## Recompute

From the repository root, with Python 3.11 or later:

```powershell
python paper/scripts/recompute_statistics.py
```

The script uses the Python standard library and does not call model services. Results are written to `paper/data/statistics/`: validation/repair/cost summaries, subset results, rubric scores, ICC(2,1), Cohen's kappa, and the paired exact McNemar test.

## Inputs

- `data/source_manifest.json`: configurations, result directories, aliases, rating files, and the protocol script.
- `data/source_reports.json`: source paths and SHA-256 checksums for 6,885 selected reports.
- `data/raw/runs/*.json`: fifteen compact extracts of measured success, repair count, runtime, tokens, and stage errors. The extracts contain no manuscript percentages.
- `../results/expert_review/ratings.csv`: 918 Full/Direct artifacts, with two five-dimension ratings per artifact. Setting A is Full; B is Direct.
- `../results/expert_review_rq1_full/ratings.csv`: 2,295 cross-model artifacts. Qwen ratings overlap RQ1 Full and are not counted as another experiment.
- `../scripts/run_expert_review.py`: recorded rubric, weights, and scoring prompt.
- `../results/paper_runs/gpt-5.4-high-stable/`: the final 459-case GPT run used in the manuscript. Machine-local paths are replaced with `[local-path]`; measured fields and diagnostics are retained.

To audit or rebuild compact extracts from all referenced reports:

```powershell
python paper/scripts/rebuild_inputs.py
python paper/scripts/rebuild_inputs.py --write
```

The audit normalizes Git working-tree CRLF to repository LF before hashing. Pre-publication hashes are also retained for path-normalized GPT reports.

## Definitions

Each configuration includes 459 cases, including recorded stage errors. First-pass success is `success=true` with `repair_count=0`. Recovery is `success=true` with `repair_count>0`. Missing repair counts are not imputed. Repair recovery uses all non-first-pass cases as the denominator. Stage errors are counted separately.

Mean runtime and tokens cover all cases. Normalized cost is total cost across all cases divided by finally validated artifacts.

Weights are read from the protocol script: 0.35, 0.25, 0.20, 0.10, 0.10. Strict semantic usability requires the two-channel mean weighted score to reach 4 and every mean dimension to reach 3. Strict end-to-end usability is the intersection with final validation. Exact integer-weighted numerators handle threshold boundaries. Disagreement means a weighted-score difference of at least 1.0.

ICC uses two-way random-effects, absolute-agreement, single-rating ICC(2,1). Cohen's kappa uses each channel's separate strict-usability decision. The paired final-validation comparison uses an exact McNemar test.

The raw `end_to_end_usable` flag uses a combined-score threshold. Current strict end-to-end results also require every mean dimension to reach 3. `expert_1`/`expert_2` are schema identifiers for model-based scoring channels.

## Selection and scope

Full/3-3-3/Qwen is one shared run reused across RQ1, RQ2, and RQ3. The earlier GPT provider-failure run and dated summaries are historical, not current manuscript results. See `docs/experiment_design.md` for the directory mapping.

Case001--Case060 are existing-project cases; Case061--Case459 are model-constructed cases. Dataset preparation and checking records are in `data/preparation/`. Validator test inputs and outputs are in `data/validator_checks/` and `results/validator_checks/`. The consolidated score table is in `results/review_master/`.
