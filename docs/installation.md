# Installation

## Python

AGREE-AutoGen targets Python 3.9 or later.

## Virtual environment with pip

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

## Optional conda environment

```powershell
conda create -n agree-autogen python=3.10
conda activate agree-autogen
pip install -r requirements.txt
pip install -e .
```

## Optional Docker

A Docker image is not currently provided in this repository. A future Docker setup should still mount external validator installations or install redistributable validator dependencies explicitly.

## LLM API configuration

Set an OpenAI-compatible endpoint and API key:

```powershell
$env:AGREE_MODEL_BASE_URL = "https://api.example.com/v1"
$env:AGREE_MODEL_API_KEY = "replace-with-your-key"
$env:AGREE_MODEL_NAME = "your-model-name"
```

Do not commit `.env` files or real keys.

## AADL Inspector configuration

AADL-level validation requires a local AADL Inspector executable:

```powershell
$env:AADL_INSPECTOR_PATH = "path/to/AADLInspector.exe"
```

If this variable is not configured, validator wrappers should report `not_configured` instead of crashing.

## AGREE validator configuration

AGREE-level validation requires Java, OSATE, and the standalone validator:

```powershell
$env:JAVA_HOME = "path/to/jdk17"
$env:OSATE_HOME = "path/to/osate"
$env:AGREE_VALIDATOR_ROOT = "./tools/agree-validator"
.\tools\agree-validator\build.ps1
```

The validator depends on local OSATE/AGREE installations and does not bundle third-party tool distributions.
