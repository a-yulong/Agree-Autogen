# Full/Direct rubric ratings

`review_inputs.csv` stores the requirement, architecture context, generated artifact, and validator outcome for 918 artifacts. `ratings.csv` stores two five-dimension ratings and brief reasons for each artifact. Setting A is Full framework; B is Direct generation.

`expert_1` and `expert_2` identify model-based scoring channels. The columns preserve the recorded schema. The prompt and weights are defined in `scripts/run_expert_review.py`.

Historical `end_to_end_usable` flags use the non-strict score threshold. Recomputed strict semantic and end-to-end results, ICC(2,1), kappa, and disagreement are provided in `paper/data/statistics/`. Run `python paper/scripts/recompute_statistics.py` to regenerate them from individual dimension scores. Raw ratings are not rewritten.
