param(
  [string]$RepoRoot = "C:\Users\25780\Desktop\py_item\DeepSeek\Agree-Autogen_v2.0",
  [string]$SourceRoot = "C:\Users\25780\Desktop\Exp_Data\Sources",
  [string]$ResultRoot = "C:\Users\25780\Desktop\Exp_Data\Result_v4.0\00_smoke",
  [int]$MaxRepairRounds = 5,
  [string]$OpenRouterKey = $env:AGREE_MODEL_API_KEY
)

$ErrorActionPreference = "Stop"

if (-not $OpenRouterKey) {
  $keyFile = "C:\Users\25780\Documents\Playground\run_openrouter_cases_A.py"
  if (Test-Path -LiteralPath $keyFile) {
    $OpenRouterKey = [regex]::Match((Get-Content -LiteralPath $keyFile -Raw), 'sk-or-v1-[A-Za-z0-9]+').Value
  }
}
if (-not $OpenRouterKey) {
  throw "OpenRouter API key not found."
}

Set-Location -LiteralPath $RepoRoot

$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"
$env:AGREE_SOURCE_ROOT = $SourceRoot
$env:AGREE_DOCS_DIR = Join-Path $RepoRoot "knowledge_base"
$env:AGREE_MODEL_BASE_URL = "https://openrouter.ai/api/v1"
$env:AGREE_MODEL_API_KEY = $OpenRouterKey
$env:AADL_INSPECTOR_PATH = "E:\AI-1.10\bin\AADLInspector.exe"
$env:JAVA_HOME = "D:\jdk17"
$env:OSATE_HOME = "E:\osate2-2.12.0-vfinal-win32.win32.x86_64"
$env:AGREE_VALIDATOR_ROOT = Join-Path $RepoRoot "tools\agree-validator"
$env:AGREE_AADL_LIB_DIRS = @(
  "D:\AADL_Lib_workspace\AADLib_Test\src\property_set",
  "D:\AADL_Lib_workspace\AADLib_Test\src",
  "E:\AADLib-master\AADLib-master\src\property_set",
  "E:\AADLib-master\AADLib-master\src"
) -join [System.IO.Path]::PathSeparator
$env:AGREE_MAX_REPAIR_ROUNDS = [string]$MaxRepairRounds

$models = @(
  @{ Slug = "qwen3-coder-30b-a3b-instruct"; Id = "qwen/qwen3-coder-30b-a3b-instruct" },
  @{ Slug = "llama-3.1-70b-instruct"; Id = "meta-llama/llama-3.1-70b-instruct" },
  @{ Slug = "gemma-3-27b-it"; Id = "google/gemma-3-27b-it" },
  @{ Slug = "codestral-2508"; Id = "mistralai/codestral-2508" },
  @{ Slug = "phi-4-mini-instruct"; Id = "microsoft/phi-4-mini-instruct" }
)

$caseIds = @(1, 111, 249)

New-Item -ItemType Directory -Force -Path $ResultRoot | Out-Null
$logRoot = Join-Path $ResultRoot "_logs"
New-Item -ItemType Directory -Force -Path $logRoot | Out-Null
$summary = Join-Path $logRoot "smoke_summary.txt"
"Result v4 smoke started: $(Get-Date -Format o)" | Set-Content -LiteralPath $summary -Encoding UTF8
"Source root: $SourceRoot" | Add-Content -LiteralPath $summary -Encoding UTF8
"Cases: $($caseIds -join ', ')" | Add-Content -LiteralPath $summary -Encoding UTF8

foreach ($model in $models) {
  foreach ($caseId in $caseIds) {
    $settingResult = Join-Path $ResultRoot (Join-Path $model.Slug "e2-full-rag")
    $logPath = Join-Path $logRoot "$($model.Slug)_case$('{0:D2}' -f $caseId)_e2.log"
    Write-Host "============================================================" -ForegroundColor Cyan
    Write-Host "Smoke model: $($model.Slug) case=$caseId setting=E2"
    Write-Host "Result: $settingResult"
    Write-Host "============================================================" -ForegroundColor Cyan

    $ErrorActionPreference = "Continue"
    python .\scripts\run_existing_batch.py `
      --source-root $SourceRoot `
      --case-from $caseId `
      --case-to $caseId `
      --setting E2 `
      --result-root $settingResult `
      --llm-base-url "https://openrouter.ai/api/v1" `
      --llm-api-key $OpenRouterKey `
      --llm-model-name $model.Id `
      --max-repair-rounds $MaxRepairRounds `
      2>&1 | Tee-Object -FilePath $logPath

    $exitCode = $LASTEXITCODE
    $ErrorActionPreference = "Stop"
    "$($model.Slug) case=$caseId exit=$exitCode at $(Get-Date -Format o)" | Add-Content -LiteralPath $summary -Encoding UTF8
    if ($exitCode -eq 75) {
      "Provider stop detected." | Add-Content -LiteralPath $summary -Encoding UTF8
      exit 75
    }
  }
}

python .\scripts\aggregate_experiment_results.py --result-root $ResultRoot | Tee-Object -FilePath (Join-Path $logRoot "aggregate_smoke.log")
"Result v4 smoke finished: $(Get-Date -Format o)" | Add-Content -LiteralPath $summary -Encoding UTF8
Write-Host "Smoke finished." -ForegroundColor Green
