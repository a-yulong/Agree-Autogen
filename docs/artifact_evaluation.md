# Reproducing the experiments

1. Install the Python environment using `README.md`.
2. Inspect a case in `data/benchmark/cases/`: its AADL input, requirement, and expected relations share the same case identifier.
3. Inspect the complete stage templates in `prompts/` and their calls in `src/agree_autogen/refactor/agents.py`.
4. Run the offline case example with `--skip-validation --dry-run`.
5. Build the validator with JDK 17 and OSATE/AGREE, then run the case with validation.
6. Select the experiment configuration in `experiments/`; the original batch runners are in `experiments/original_runs/`.
7. Run `python paper/scripts/recompute_statistics.py` to compute the manuscript statistics from the stored measurements.

Dataset screening records are in `data/preparation/`. The scoring table and rubric are in `results/review_master/`. Validator test inputs are in `data/validator_checks/test_case/`, with recorded outputs in `results/validator_checks/test_results_v4/`.
