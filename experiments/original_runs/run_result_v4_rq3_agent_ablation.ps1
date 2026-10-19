param(
  [Parameter(Mandatory = $true)][string]$ModelId,
  [Parameter(Mandatory = $true)][string]$ModelSlug,
  [string]$RepoRoot = "C:\Users\25780\Desktop\py_item\DeepSeek\Agree-Autogen_v2.0",
  [string]$SourceRoot = "C:\Users\25780\Desktop\Exp_Data\Sources",
  [string]$ResultRoot = "C:\Users\25780\Desktop\Exp_Data\Result_v4.0\RQ3_agent_ablation",
  [int]$Start = 1,
  [int]$End = 500,
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

$settings = @(
  @{ Slug = "e2-full-rag"; Setting = "E2" },
  @{ Slug = "e1-bare"; Setting = "E1" },
  @{ Slug = "e4-no-repair"; Setting = "E4" },
  @{ Slug = "e5-no-model-analyst"; Setting = "E5" },
  @{ Slug = "e6-no-requirement-analyst"; Setting = "E6" },
  @{ Slug = "e7-no-dual-analysts"; Setting = "E7" }
)

New-Item -ItemType Directory -Force -Path $ResultRoot | Out-Null
$logRoot = Join-Path $ResultRoot "_logs"
New-Item -ItemType Directory -Force -Path $logRoot | Out-Null

foreach ($item in $settings) {
  $settingResult = Join-Path $ResultRoot (Join-Path $ModelSlug $item.Slug)
  $logPath = Join-Path $logRoot "$($ModelSlug)_$($item.Slug).log"
  Write-Host "============================================================" -ForegroundColor Cyan
  Write-Host "RQ3 model: $ModelSlug setting=$($item.Setting) slug=$($item.Slug)"
  Write-Host "Result: $settingResult"
  Write-Host "============================================================" -ForegroundColor Cyan

  $ErrorActionPreference = "Continue"
  python .\scripts\run_existing_batch.py `
    --source-root $SourceRoot `
    --case-from $Start `
    --case-to $End `
    --setting $item.Setting `
    --result-root $settingResult `
    --llm-base-url "https://openrouter.ai/api/v1" `
    --llm-api-key $OpenRouterKey `
    --llm-model-name $ModelId `
    --max-repair-rounds $MaxRepairRounds `
    2>&1 | Tee-Object -FilePath $logPath
  $exitCode = $LASTEXITCODE
  $ErrorActionPreference = "Stop"
  python .\scripts\aggregate_experiment_results.py --result-root $ResultRoot | Tee-Object -FilePath (Join-Path $logRoot "aggregate_after_$($item.Slug).log")
  if ($exitCode -eq 75) {
    exit 75
  }
}

python .\scripts\aggregate_experiment_results.py --result-root $ResultRoot | Tee-Object -FilePath (Join-Path $logRoot "aggregate_final.log")
