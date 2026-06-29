# Configuration

Configuration files define model access, retrieval behavior, validation settings, and experiment defaults. They are intended to make runs reproducible without hard-coding credentials or local paths in scripts.

## Files

| File | Purpose |
|---|---|
| `model.yaml` | OpenAI-compatible model endpoint settings and environment-variable names. |
| `rag.yaml` | Retrieval model, chunking, top-k, and knowledge-base paths. |
| `validator.yaml` | External validator configuration. |
| `experiments.yaml` | Benchmark run defaults. |

## Model Configuration

`model.yaml` stores provider-independent settings such as:

- model name;
- temperature;
- maximum completion tokens;
- request timeout;
- environment-variable names for API key and base URL.

Credentials are supplied through environment variables:

```powershell
$env:AGREE_MODEL_BASE_URL = "https://api.example.com/v1"
$env:AGREE_MODEL_API_KEY = "replace-with-your-key"
$env:AGREE_MODEL_NAME = "qwen3-coder-30b-a3b-instruct"
```

## Retrieval Configuration

`rag.yaml` records the balanced retrieval setting used for the main RAG pipeline:

- embedding model;
- chunk size and overlap;
- three knowledge-role retrieval counts;
- similarity threshold;
- knowledge-base directory;
- local index/cache paths.

The main setting retrieves three syntax/scope items, three example-pattern items, and three defensive-rule items before digesting them into compact guidance.

## Validator Configuration

`validator.yaml` records the validation and bounded repair settings used in the released pipeline.

## Experiment Configuration

`experiments.yaml` points to the released benchmark under `data/benchmark/cases` and enables the full AGREE-AutoGen pipeline.
