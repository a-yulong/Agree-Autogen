# Installation

## Python Environment

AGREE-AutoGen targets Python 3.9 or later.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Conda is also supported:

```powershell
conda create -n agree-autogen python=3.10
conda activate agree-autogen
```

## Package Installation

```powershell
pip install -r requirements.txt
pip install -e .
```

## Model API Configuration

The runtime expects an OpenAI-compatible chat-completions endpoint:

```powershell
$env:AGREE_MODEL_BASE_URL = "https://api.example.com/v1"
$env:AGREE_MODEL_API_KEY = "replace-with-your-key"
$env:AGREE_MODEL_NAME = "your-model-name"
```

Use `--dry-run` to check local inputs without model credentials.

## Optional Validation Tools

AADL Inspector:

```powershell
$env:AADL_INSPECTOR_PATH = "path/to/AADLInspector.exe"
```

Standalone AGREE validator:

```powershell
$env:JAVA_HOME = "path/to/jdk17"
$env:OSATE_HOME = "path/to/osate"
$env:AGREE_VALIDATOR_ROOT = "./tools/agree-validator"
.\tools\agree-validator\build.ps1
```

Missing validation tools are reported as `not_configured`.

## Optional RAG Index

The current pipeline builds Chroma indexes from `AGREE_DOCS_DIR` when RAG is enabled. The public `knowledge_base/` directory contains layout and policy files only.

For smoke tests, use `--disable-rag`.

