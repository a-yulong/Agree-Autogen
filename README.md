# AGREE-AutoGen

AGREE-AutoGen is a multi-agent framework for generating and validating AGREE contracts from natural-language requirements and AADL architecture models. It treats contract generation as a sequence of constrained decisions: retrieved AGREE/AADL knowledge constrains the available formal patterns, architecture analysis constrains the visible model scope, requirement analysis constrains formalization intent, generation produces candidate AGREE clauses, model fusion inserts the clauses into the appropriate AADL owner, and validation-guided repair uses tool diagnostics to make bounded corrections.

The repository is designed as a research artifact. It contains the implementation, prompts, validation interface, retrieval resources, experiment configuration, and result-processing scripts needed to inspect the method and reproduce the reported analyses.

## Highlights

- Scope-aware AADL analysis for identifying visible component features, owners, connections, properties, and insertion targets.
- Requirement analysis that separates behavioral intent from structural descriptions before formalization.
- Retrieval-augmented AGREE generation using curated syntax, scope, example, and defensive-rule knowledge.
- Controlled model fusion that inserts or replaces AGREE annexes without rewriting unrelated AADL model content.
- Validation-guided repair through a standalone AGREE validator and focused diagnostic feedback.
- Experiment scripts for model comparison, retrieval settings, agent ablations, optimization ablations, reruns, and metric aggregation.

## Repository Contents

```text
configs/             Runtime configuration templates
data/                Public examples and benchmark manifests
docs/                Architecture, reproducibility, experiment, and schema documentation
experiments/         Experiment settings, lightweight runners, and metric utilities
knowledge_base/      Curated retrieval sources and processed knowledge assets
prompts/             Agent prompts used by the pipeline
scripts/             Single-case, batch, rerun, and aggregation entry points
src/agree_autogen/   Pipeline implementation
tests/               Unit tests and offline smoke checks
tools/               Standalone AGREE validation tool
```

The artifact boundary is described in `ARTIFACT_SCOPE.md`.

## Quick Start

Create an environment and install the package:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

Run an offline dry run on the bundled example:

```powershell
python scripts/run_files.py `
  --requirement data/examples/gf_monitor/requirement.txt `
  --aadl data/examples/gf_monitor/input.aadl `
  --output-dir outputs/gf_monitor_dry `
  --setting E2 `
  --skip-validation `
  --dry-run
```

Run the offline test subset:

```powershell
python -m pytest -q tests/test_fusion.py tests/test_model_analyst.py tests/test_validators.py tests/test_metrics.py tests/test_build_rag_index.py tests/test_experiment_configs.py tests/test_run_files_cli.py
```

Full generation requires an OpenAI-compatible model endpoint:

```powershell
$env:AGREE_MODEL_BASE_URL = "https://api.example.com/v1"
$env:AGREE_MODEL_API_KEY = "replace-with-your-key"
$env:AGREE_MODEL_NAME = "model-name"
```

Use `.env.example` as a template. Do not commit real credentials.

## Validation Tool

The standalone AGREE validator is included under `tools/agree-validator/`. It provides a Java command-line interface that loads AADL projects, AGREE annexes, bundled static libraries, and OSATE/AGREE plugin resources, then emits JSON diagnostics.

The validator requires a local JDK and OSATE/AGREE installation. OSATE itself is not redistributed in this repository.

See `docs/validator_setup.md` for setup and command examples.

## Experiments and Results

The experiment scripts support:

- model comparison;
- retrieval setting selection;
- agent ablation;
- optimization ablation;
- rerun of missing or provider-failed cases;
- aggregate metric generation.

Experiment design is documented in `docs/experiment_design.md`. Result formats and metric definitions are documented in `docs/result_schema.md`.

Complete result artifacts should be placed under `results/` or attached as a release asset when the per-case reports are too large for the repository. The repository should retain aggregate summaries, manifests, and checksums so that reported metrics can be traced back to case-level records.

## Reproducibility

The repository distinguishes three reproduction levels:

- offline inspection of code, prompts, configurations, and results;
- local smoke execution with bundled examples and a local validator setup;
- full experiment execution with model-provider credentials.

See `docs/reproducibility.md` for commands, dependencies, and expected outputs.

## Citation

If you use AGREE-AutoGen in academic work, cite this repository. See `CITATION.cff`.

## License

The code is released under the MIT License. See `LICENSE`. Third-party tools and source documents may have their own licenses; see the relevant documentation and source manifests.
