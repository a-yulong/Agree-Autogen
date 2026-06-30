# RQ1 Expert Review Results

This directory contains the neutral expert review for the full RQ1 model comparison. The review covers 459 benchmark cases for each evaluated model, for a total of 2,295 generated artifacts. Each artifact was scored independently by two expert reviewers using the same five-dimension rubric.

The scoring prompt used only the natural-language requirement, the target AADL context, the generated AADL+AGREE artifact, and the rubric. Model identity, validation status, repair history, and setting labels were not included in the prompt.

## Files

- `review_inputs.csv`: scoring inputs for all artifacts.
- `ratings.csv`: per-case expert scores, averaged scores, usability flags, and brief reviewer reasons.
- `summary.csv`: aggregate metrics by evaluated model.
- `system_manifest.csv`: mapping between evaluated model names and their result sources.

## Metrics

- `mean_combined_score`: average of the two expert-weighted scores.
- `review_usable_rate`: fraction of artifacts with combined score at least 4.0.
- `strict_review_usable_rate`: fraction of artifacts with combined score at least 4.0 and no averaged dimension below 3.0.
- `end_to_end_usable_rate`: fraction of artifacts that both pass validation and reach the review-usable threshold.
- `expert_disagreement_rate`: fraction of artifacts where the two expert-weighted scores differ by at least 1.0.

The five scoring dimensions are requirement fidelity, architectural grounding, formalization adequacy, unsupported-content control, and reviewability.
