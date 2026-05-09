# Agree-Autogen Runtime

This package contains the production runtime for the Agree-Autogen pipeline.

## Entry point

Use the repository-level `run_case.py` entry point for single-case experiments.

Example:

```powershell
python run_case.py --case-num 1 --case-letter A --use-rag --llm-base-url https://api.example.com/v1 --llm-api-key YOUR_KEY --llm-model-name YOUR_MODEL --result-root results
```

## Module map

| File | Responsibility |
| --- | --- |
| `runtime.py` | Runtime config, model config, token accounting, file-link formatting, Windows pop-up monitor, recorder imports. |
| `agents.py` | Conversation, BaseAgent, requirements analyst, AGREE generator, AADL model analyst, AADL merger, validator/repair agent. |
| `pipeline.py` | AGREEVerificationPipeline, RAG vectorstores, dependency sync, AADL Inspector, standalone AGREE validator, full orchestration. |
| `case_runner.py` | Case input loading, target component extraction, related AADL model collection, single-case runner. |
| `run_case.py` | Repository-level CLI entry point. |

## Design principle

The runtime is organized around explicit responsibility boundaries:

- Runtime configuration and accounting live in `runtime.py`.
- Agent prompts and model-facing behavior live in `agents.py`.
- Validator integration and orchestration live in `pipeline.py`.
- Dataset loading and target-component extraction live in `case_runner.py`.

## Smoke test result

Validated with:

- Case: `Case01_A`
- A smoke test should complete with generated reports under the configured result root.
