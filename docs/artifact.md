# Artifact Contents

This artifact contains the source code, prompts, configurations, retrieval resources, validation tool, examples, tests, experiment scripts, and result-processing utilities for AGREE-AutoGen.

## Included

- Multi-agent pipeline implementation under `src/agree_autogen/`.
- Direct-file, case-layout, batch, rerun, and aggregation scripts under `scripts/`.
- Agent prompts under `prompts/`.
- Runtime and experiment configuration under `configs/` and `experiments/`.
- Curated retrieval sources under `knowledge_base/`.
- Standalone AGREE validator source and support libraries under `tools/agree-validator/`.
- Public examples under `data/examples/`.
- Tests and smoke checks under `tests/`.
- Result release area under `results/`.

## Documentation Map

- `README.md`: project overview and quick start.
- `ARTIFACT_SCOPE.md`: repository boundary and release policy.
- `docs/architecture.md`: method and pipeline architecture.
- `docs/reproducibility.md`: setup, tests, dry runs, validation, and experiment reruns.
- `docs/experiment_design.md`: research questions, controlled variables, and metrics.
- `docs/result_schema.md`: per-case report fields and aggregate metric definitions.
- `docs/validator_setup.md`: standalone validator setup and resource loading.
- `docs/known_limitations.md`: reproducibility and interpretation boundaries.

## External Configuration

Model endpoints and validation tools are connected through environment variables and command-line parameters. The artifact does not include provider credentials or a redistributed OSATE installation.
