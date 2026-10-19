param(
  [ValidateSet("All", "RQ2", "RQ3", "RQ4")]
  [string]$Suite = "All",
  [string]$ModelId = "qwen/qwen3-coder-30b-a3b-instruct",
  [string]$ModelSlug = "qwen3-coder-30b-a3b-instruct",
  [string]$RepoRoot = "C:\Users\25780\Desktop\py_item\DeepSeek\Agree-Autogen_v2.0",
  [string]$SourceRoot = "C:\Users\25780\Desktop\Exp_Data\Sources",
  [string]$ResultRoot = "C:\Users\25780\Desktop\Exp_Data\Result_v4.0\post_rq1_full",
  [string]$Rq1Root = "C:\Users\25780\Desktop\Exp_Data\Result_v4.0\full_e2_rag_3models_20260608_0510",
  [int]$Start = 1,
  [int]$End = 459,
  [int]$MaxRepairRounds = 5,
  [string]$OpenRouterKey = $env:AGREE_MODEL_API_KEY,
  [switch]$WaitForRq1
)

$ErrorActionPreference = "Stop"

if (-not $OpenRouterKey) {
  $keyFile = "C:\Users\25780\Documents\Playground\run_openrouter_cases_A.py"
  if (Test-Path -LiteralPath $keyFile) {
    $OpenRouterKey = [regex]::Match((Get-Content -LiteralPath $keyFile -Raw), 'sk-or-v1-[A-Za-z0-9]+').Value
  }
}
if (-not $OpenRouterKey) {
  throw "OpenRouter API key not found. Set AGREE_MODEL_API_KEY before running this script."
}

function Initialize-AgreeEnvironment {
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
}

function Get-ReportCount([string]$Directory) {
  if (-not (Test-Path -LiteralPath $Directory)) {
    return 0
  }
  return @(Get-ChildItem -Path $Directory -Recurse -Filter "*_report.md" -ErrorAction SilentlyContinue).Count
}

function Wait-For-Rq1Completion {
  $required = @(
    "qwen3-coder-30b-a3b-instruct",
    "codestral-2508",
    "llama-3.1-70b-instruct",
    "gemma-3-27b-it",
    "gpt-5.4"
  )
  while ($true) {
    $pending = @()
    foreach ($model in $required) {
      $dir = Join-Path $Rq1Root (Join-Path $model "e2-full-rag")
      $count = Get-ReportCount $dir
      if ($count -lt 459) {
        $pending += "$model=$count/459"
      }
    }
    if ($pending.Count -eq 0) {
      Write-Host "RQ1 appears complete for all configured models." -ForegroundColor Green
      return
    }
    Write-Host "Waiting for RQ1 completion: $($pending -join ', ')" -ForegroundColor Yellow
    Start-Sleep -Seconds 300
  }
}

function Invoke-ExperimentRun {
  param(
    [string]$Rq,
    [string]$Name,
    [string]$Setting,
    [hashtable]$EnvOverrides
  )
  Initialize-AgreeEnvironment

  $defaultSwitches = @{
    AGREE_RAG_DIGEST = "1"
    AGREE_RAG_ENHANCED = "1"
    AGREE_AGENT_CARD_GUIDANCE = "1"
    AGREE_TARGET_CONTEXT_MODE = "focused"
    AGREE_TARGET_CONTEXT_MAX_CHARS = ""
    AGREE_RAG_KSYN_COUNT = "3"
    AGREE_RAG_KEXP_COUNT = "3"
    AGREE_RAG_KDEF_COUNT = "3"
  }
  foreach ($key in $defaultSwitches.Keys) {
    $value = $defaultSwitches[$key]
    if ($value -eq "") {
      Remove-Item "Env:$key" -ErrorAction SilentlyContinue
    } else {
      Set-Item "Env:$key" $value
    }
  }
  foreach ($key in $EnvOverrides.Keys) {
    Set-Item "Env:$key" ([string]$EnvOverrides[$key])
  }

  $settingResult = Join-Path $ResultRoot (Join-Path $Rq (Join-Path $ModelSlug $Name))
  $logRoot = Join-Path $ResultRoot "_logs"
  New-Item -ItemType Directory -Force -Path $settingResult | Out-Null
  New-Item -ItemType Directory -Force -Path $logRoot | Out-Null
  $logPath = Join-Path $logRoot "$Rq.$ModelSlug.$Name.log"

  Write-Host "============================================================" -ForegroundColor Cyan
  Write-Host "$Rq $Name"
  Write-Host "Model: $ModelSlug ($ModelId)"
  Write-Host "Setting: $Setting"
  Write-Host "Result: $settingResult"
  $overrideText = (($EnvOverrides.GetEnumerator() | ForEach-Object { $_.Key + '=' + $_.Value } | Sort-Object) -join ', ')
  Write-Host "Env overrides: $overrideText"
  Write-Host "============================================================" -ForegroundColor Cyan

  $runArgs = @(
    ".\scripts\run_existing_batch.py",
    "--source-root", $SourceRoot,
    "--case-from", "$Start",
    "--case-to", "$End",
    "--canonical-one-per-number",
    "--setting", $Setting,
    "--result-root", $settingResult,
    "--llm-base-url", "https://openrouter.ai/api/v1",
    "--llm-model-name", $ModelId,
    "--max-repair-rounds", "$MaxRepairRounds"
  )

  $ErrorActionPreference = "Continue"
  python @runArgs 2>&1 | Tee-Object -FilePath $logPath
  $exitCode = $LASTEXITCODE
  $ErrorActionPreference = "Stop"

  python .\scripts\aggregate_experiment_results.py --result-root $settingResult 2>&1 |
    Tee-Object -FilePath (Join-Path $logRoot "$Rq.$ModelSlug.$Name.aggregate.log")

  if ($exitCode -eq 75) {
    throw "Provider quota/rate/billing-like stop detected in $Rq/$Name."
  }
}

Initialize-AgreeEnvironment
New-Item -ItemType Directory -Force -Path $ResultRoot | Out-Null
$manifestPath = Join-Path $ResultRoot "post_rq1_manifest.json"
$manifest = [ordered]@{
  timestamp = Get-Date -Format o
  suite = $Suite
  model_slug = $ModelSlug
  model_id = $ModelId
  source_root = $SourceRoot
  rq1_root = $Rq1Root
  result_root = $ResultRoot
  case_range = "$Start-$End"
  note = "RQ1 baseline E2 full-rag should be read from Rq1Root; this script runs post-RQ1 ablations."
}
if (($Suite -eq "All") -or -not (Test-Path -LiteralPath $manifestPath)) {
  ($manifest | ConvertTo-Json -Depth 4) | Set-Content -LiteralPath $manifestPath -Encoding UTF8
}
$suiteManifestPath = Join-Path $ResultRoot ("post_rq1_manifest_{0}_{1}.json" -f $Suite, $PID)
($manifest | ConvertTo-Json -Depth 4) | Set-Content -LiteralPath $suiteManifestPath -Encoding UTF8

if ($WaitForRq1) {
  Wait-For-Rq1Completion
}

if ($Suite -in @("All", "RQ2")) {
  Invoke-ExperimentRun -Rq "RQ2_rag" -Name "e3-no-rag" -Setting "E3" -EnvOverrides @{}
  Invoke-ExperimentRun -Rq "RQ2_rag" -Name "e2-digest-topk111" -Setting "E2" -EnvOverrides @{
    AGREE_RAG_KSYN_COUNT = "1"; AGREE_RAG_KEXP_COUNT = "1"; AGREE_RAG_KDEF_COUNT = "1"
  }
  Invoke-ExperimentRun -Rq "RQ2_rag" -Name "e2-digest-topk555" -Setting "E2" -EnvOverrides @{
    AGREE_RAG_KSYN_COUNT = "5"; AGREE_RAG_KEXP_COUNT = "5"; AGREE_RAG_KDEF_COUNT = "5"
  }
  Invoke-ExperimentRun -Rq "RQ2_rag" -Name "e2-digest-topk777" -Setting "E2" -EnvOverrides @{
    AGREE_RAG_KSYN_COUNT = "7"; AGREE_RAG_KEXP_COUNT = "7"; AGREE_RAG_KDEF_COUNT = "7"
  }
}

if ($Suite -in @("All", "RQ3")) {
  Invoke-ExperimentRun -Rq "RQ3_agent" -Name "e1-direct-one-shot" -Setting "E1" -EnvOverrides @{}
  Invoke-ExperimentRun -Rq "RQ3_agent" -Name "e4-no-repair" -Setting "E4" -EnvOverrides @{}
  Invoke-ExperimentRun -Rq "RQ3_agent" -Name "e5-no-model-analyst" -Setting "E5" -EnvOverrides @{}
  Invoke-ExperimentRun -Rq "RQ3_agent" -Name "e6-no-requirement-analyst" -Setting "E6" -EnvOverrides @{}
  Invoke-ExperimentRun -Rq "RQ3_agent" -Name "e7-no-dual-analysts" -Setting "E7" -EnvOverrides @{}
}

if ($Suite -in @("All", "RQ4")) {
  Invoke-ExperimentRun -Rq "RQ4_optimization" -Name "e2-raw-rag-no-digest" -Setting "E2" -EnvOverrides @{
    AGREE_RAG_DIGEST = "0"
  }
  Invoke-ExperimentRun -Rq "RQ4_optimization" -Name "e2-legacy-retrieval-no-enhanced" -Setting "E2" -EnvOverrides @{
    AGREE_RAG_ENHANCED = "0"
  }
  Invoke-ExperimentRun -Rq "RQ4_optimization" -Name "e2-no-agent-card-guidance" -Setting "E2" -EnvOverrides @{
    AGREE_AGENT_CARD_GUIDANCE = "0"
  }
  Invoke-ExperimentRun -Rq "RQ4_optimization" -Name "e2-full-target-context" -Setting "E2" -EnvOverrides @{
    AGREE_TARGET_CONTEXT_MODE = "full"; AGREE_TARGET_CONTEXT_MAX_CHARS = "30000"
  }
}

python .\scripts\aggregate_experiment_results.py --result-root $ResultRoot 2>&1 |
  Tee-Object -FilePath (Join-Path $ResultRoot "_logs\aggregate_post_rq1_all.log")

Write-Host "Post-RQ1 experiment suite finished: $ResultRoot" -ForegroundColor Green
