# Contributing

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

## Checks

Run before opening a pull request:

```powershell
python -m compileall src experiments scripts tests
python -m pytest -q
```

The test suite must not require real LLM credentials, AADL Inspector, OSATE, or the AGREE validator.

## Pull Requests

- Keep changes scoped.
- Do not commit `.env`, API keys, generated outputs, vector stores, logs, or private benchmark data.
- Do not add third-party standards, manuals, or datasets unless redistribution is explicitly permitted.
- Update docs and tests when behavior changes.

