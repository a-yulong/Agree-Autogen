# AGREE-AutoGen

AGREE-AutoGen generates AGREE contracts from natural-language requirements and an existing AADL model. The pipeline extracts architecture facts and requirement items, retrieves AGREE/AADL rules, generates a contract, inserts it into the target component, and repairs validation errors.

## Materials

| Content | Location |
| --- | --- |
| 459 requirement–model cases | `data/benchmark/cases/` |
| Dataset screening tables and per-case checks | `data/preparation/` |
| Knowledge documents, contract examples, and generation rules | `knowledge_base/` |
| Complete agent prompt templates | `prompts/` |
| Pipeline code | `src/agree_autogen/` |
| Original dataset construction scripts | `scripts/` |
| Experiment settings and original batch runners | `experiments/` |
| Recorded prompts, retrieval, integration, and repair for Case003 | `examples/recorded_case003/` |
| Per-case experiment results | `results/` |
| Combined score table, Excel workbook, and scoring rubric | `results/review_master/` |
| Validator test inputs and outputs | `data/validator_checks/`, `results/validator_checks/` |
| Manuscript statistics | `paper/data/statistics/` |

The score table contains 2,754 records. Full/Qwen is shared by the framework comparison and the five-model comparison and appears once in this table.

## Install

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

## Run a case

Configure the model endpoint:

```powershell
$env:AGREE_MODEL_BASE_URL = "https://api.example.com/v1"
$env:AGREE_MODEL_API_KEY = "replace-with-your-key"
$env:AGREE_MODEL_NAME = "model-name"
```

Configure JDK 17 and an OSATE installation with AGREE, then build the validator:

```powershell
$env:JAVA_HOME = "path\to\jdk17"
$env:OSATE_HOME = "path\to\osate"
.\tools\agree-validator\build.ps1
```

```powershell
python scripts/run_files.py `
  --requirement data/benchmark/cases/Case001/Case001_Req.txt `
  --aadl data/benchmark/cases/Case001/Case001_Base.aadl `
  --output-dir outputs/Case001 `
  --setting E2
```

For an offline dry run, append `--skip-validation --dry-run`.

## Recompute results

```powershell
python paper/scripts/recompute_statistics.py
python paper/scripts/rebuild_inputs.py
```

The first command computes validation, repair, runtime, token, and rubric statistics. The second checks the 6,885 selected reports against the stored measurements. The run selection is in `paper/data/source_manifest.json`.

## Experiment runs

The manuscript groups the experiments as follows:

| Comparison | Runs |
| --- | --- |
| RQ1: framework effectiveness | Full and Direct |
| RQ2: ablation and retrieval depth | Analysis stages, retrieval depth, digest, strategy guidance, and target context |
| RQ3: model comparison | Qwen, Codestral, Gemma, GPT, and Llama |

`experiments/original_runs/` contains the original PowerShell batch runners. Their parameters select the repository, input, and output directories. `docs/experiment_design.md` maps their directory names to the manuscript experiments.

## License and citation

See `LICENSE` and `CITATION.cff`.
