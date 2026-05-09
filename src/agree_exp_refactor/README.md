# agree_exp_refactor

This directory is the refactored baseline extracted from `demo15.py`.

## Entry point

Use `C:\Users\25780\Desktop\py_item\DeepSeek\demo16.py` for new experiments.

Example:

```powershell
D:\anaconda\envs\new\python.exe C:\Users\25780\Desktop\py_item\DeepSeek\demo16.py --case-num 1 --case-letter A --use-rag --llm-base-url https://api.silra.cn/v1 --llm-api-key YOUR_KEY --llm-model-name qwen3-coder-30b-a3b-instruct --result-root C:\Users\25780\Desktop\Exp_Data\Result\demo16-smoke
```

## Module map

| File | Responsibility |
| --- | --- |
| `runtime.py` | Runtime config, model config, token accounting, file-link formatting, Windows pop-up monitor, recorder imports. |
| `agents.py` | Conversation, BaseAgent, requirements analyst, AGREE generator, AADL model analyst, AADL merger, validator/repair agent. |
| `pipeline.py` | AGREEVerificationPipeline, RAG vectorstores, dependency sync, AADL Inspector, standalone AGREE validator, full orchestration. |
| `case_runner.py` | Case input loading, target component extraction, related AADL model collection, single-case runner. |
| `demo16.py` | Thin CLI entry point. |

## Refactor principle

The first refactor is intentionally conservative:

- Keep the verified behavior from `demo15.py`.
- Split responsibilities by runtime / agents / pipeline / case IO / CLI.
- Avoid changing prompts and validation semantics in the same step.
- Make future edits local: model config in `runtime.py`, prompts and agent behavior in `agents.py`, validators and orchestration in `pipeline.py`, case loading in `case_runner.py`.

## Smoke test result

Validated with:

- Case: `Case01_A`
- Model: `qwen3-coder-30b-a3b-instruct`
- Result root: `C:\Users\25780\Desktop\Exp_Data\Result\demo16-smoke`
- Outcome: completed successfully, final validation passed after 4 repair iterations.
