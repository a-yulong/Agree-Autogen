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
data/benchmark/cases/    459 benchmark inputs used by the experiments
knowledge_base/          Three retrieval sources: syntax/scope, examples, and defensive rules
prompts/                 Agent prompts used by the pipeline
src/agree_autogen/       Pipeline implementation
tools/agree-validator/   Standalone AGREE validation interface and bundled AADL support files
results/                 Released aggregate and per-case experiment results
scripts/                 Core run and aggregation entry points
tests/                   Offline checks for the released artifact
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

Run an offline dry run on a bundled benchmark case:

```powershell
python scripts/run_files.py `
  --requirement data/benchmark/cases/Case001/Case001_Req.txt `
  --aadl data/benchmark/cases/Case001/Case001_Base.aadl `
  --output-dir outputs/Case001_dry `
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

Use environment variables for credentials. Do not commit real keys.

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

The repository includes the released aggregate summaries and the per-case RQ1-RQ4 result tree under `results/`.

## Reproducibility

The repository supports three reproduction levels:

- offline inspection of code, prompts, configurations, and results;
- local smoke execution with bundled examples and a local validator setup;
- full experiment execution with model-provider credentials.

See `docs/reproducibility.md` for commands, dependencies, and expected outputs.

## Citation

If you use AGREE-AutoGen in academic work, cite this repository. See `CITATION.cff`.

## License

The code is released under the MIT License. See `LICENSE`. Third-party tools and source documents may have their own licenses; see the relevant documentation and source manifests.

