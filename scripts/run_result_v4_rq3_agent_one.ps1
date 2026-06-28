param(
  [Parameter(Mandatory=$true)]
  [ValidateSet("e1-direct-one-shot", "e4-no-repair", "e5-no-model-analyst", "e6-no-requirement-analyst", "e7-no-dual-analysts")]
  [string]$Name,
  [string]$ModelId = "qwen/qwen3-coder-30b-a3b-instruct",
  [string]$ModelSlug = "qwen3-coder-30b-a3b-instruct",
  [string]$RepoRoot = "C:\Users\25780\Desktop\py_item\DeepSeek\Agree-Autogen_v2.0",
  [string]$SourceRoot = "C:\Users\25780\Desktop\Exp_Data\Sources",
  [string]$ResultRoot = "C:\Users\25780\Desktop\Exp_Data\Result_v4.0\post_rq1_full",
  [int]$Start = 1,
  [int]$End = 459,
  [int]$MaxRepairRounds = 5,
  [string]$OpenRouterKey = $env:AGREE_MODEL_API_KEY
)

$ErrorActionPreference = "Stop"

$settingMap = @{
  "e1-direct-one-shot" = "E1"
  "e4-no-repair" = "E4"
  "e5-no-model-analyst" = "E5"
  "e6-no-requirement-analyst" = "E6"
  "e7-no-dual-analysts" = "E7"
}
$Setting = $settingMap[$Name]

if (-not $OpenRouterKey) {
  $keyFile = "C:\Users\25780\Documents\Playground\run_openrouter_cases_A.py"
  if (Test-Path -LiteralPath $keyFile) {
    $OpenRouterKey = [regex]::Match((Get-Content -LiteralPath $keyFile -Raw), 'sk-or-v1-[A-Za-z0-9]+').Value
  }
}
if (-not $OpenRouterKey) {
  throw "OpenRouter API key not found. Set AGREE_MODEL_API_KEY before running this script."
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

$env:AGREE_RAG_DIGEST = "1"
$env:AGREE_RAG_ENHANCED = "1"
$env:AGREE_AGENT_CARD_GUIDANCE = "1"
$env:AGREE_TARGET_CONTEXT_MODE = "focused"
Remove-Item "Env:AGREE_TARGET_CONTEXT_MAX_CHARS" -ErrorAction SilentlyContinue
$env:AGREE_RAG_KSYN_COUNT = "3"
$env:AGREE_RAG_KEXP_COUNT = "3"
$env:AGREE_RAG_KDEF_COUNT = "3"

$settingResult = Join-Path $ResultRoot (Join-Path "RQ3_agent" (Join-Path $ModelSlug $Name))
$logRoot = Join-Path $ResultRoot "_logs"
New-Item -ItemType Directory -Force -Path $settingResult | Out-Null
New-Item -ItemType Directory -Force -Path $logRoot | Out-Null
$logPath = Join-Path $logRoot ("RQ3_agent.{0}.{1}.log" -f $ModelSlug, $Name)

([ordered]@{
  timestamp = Get-Date -Format o
  suite = "RQ3_agent_one"
  name = $Name
  setting = $Setting
  model_slug = $ModelSlug
  model_id = $ModelId
  source_root = $SourceRoot
  result_root = $settingResult
  case_range = "$Start-$End"
} | ConvertTo-Json -Depth 4) | Set-Content -LiteralPath (Join-Path $ResultRoot ("post_rq1_manifest_RQ3_{0}_{1}.json" -f $Name, $PID)) -Encoding UTF8

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "RQ3 agent ablation: $Name"
Write-Host "Setting: $Setting"
Write-Host "Model: $ModelSlug ($ModelId)"
Write-Host "Result: $settingResult"
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
  Tee-Object -FilePath (Join-Path $logRoot ("RQ3_agent.{0}.{1}.aggregate.log" -f $ModelSlug, $Name))

if ($exitCode -eq 75) {
  throw "Provider quota/rate/billing-like stop detected in RQ3/$Name."
}
if ($exitCode -ne 0) {
  throw "RQ3/$Name exited with code $exitCode."
}

Write-Host "RQ3 agent ablation finished: $Name" -ForegroundColor Green
