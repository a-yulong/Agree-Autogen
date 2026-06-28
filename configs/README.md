# Configuration

Configuration files define model access, retrieval behavior, validation settings, and experiment defaults. They are intended to make runs reproducible without hard-coding credentials or local paths in scripts.

## Files

| File | Purpose |
|---|---|
| `model.yaml` | OpenAI-compatible model endpoint settings and environment-variable names. |
| `rag.yaml` | Retrieval model, chunking, top-k, and knowledge-base paths. |
| `validator.yaml` | External validator configuration. |
| `experiments.yaml` | Lightweight experiment defaults. |
| `excluded_cases_large_model.json` | Case exclusions used by selected large-model runs. |

## Model Configuration

`model.yaml` stores provider-independent settings such as:

- model name;
- temperature;
- maximum completion tokens;
- request timeout;
- environment-variable names for API key and base URL.

Real credentials should be supplied through environment variables:

```powershell
$env:AGREE_MODEL_BASE_URL = "https://api.example.com/v1"
$env:AGREE_MODEL_API_KEY = "replace-with-your-key"
$env:AGREE_MODEL_NAME = "model-name"
```

Do not commit `.env` files or concrete API keys.

## Retrieval Configuration

`rag.yaml` controls:

- embedding model;
- chunk size and overlap;
- top-k retrieval count;
- similarity threshold;
- knowledge-base directory;
- local index/cache paths.

The retrieval configuration should be recorded with every experiment result because it changes the information visible to downstream agents.

## Validator Configuration

`validator.yaml` should identify how the Python pipeline calls external validation tools. Machine-specific paths should be supplied through environment variables or documented command-line parameters.

## Experiment Configuration

Experiment configuration files should use descriptive setting names in documentation and preserve machine-readable identifiers in manifests. Result folders should record the exact configuration used to generate them.
