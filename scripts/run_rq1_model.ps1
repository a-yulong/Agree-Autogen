param(
  [Parameter(Mandatory = $true)]
  [string]$ModelSlug,

  [Parameter(Mandatory = $true)]
  [string]$ModelId,

  [string]$RepoRoot = "C:\Users\25780\Desktop\py_item\DeepSeek\Agree-Autogen",
  [string]$ResultRoot = "C:\Users\25780\Desktop\Exp_Data\Result_v2.0\rq1_full_dataset",
  [int]$Start = 1,
  [int]$End = 910
)

$ErrorActionPreference = "Stop"

Set-Location -LiteralPath $RepoRoot

$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"
$env:AGREE_SOURCE_ROOT = "C:\Users\25780\Desktop\Exp_Data\Sources"
$env:AGREE_DOCS_DIR = Join-Path $RepoRoot "knowledge_base"
$env:AGREE_MODEL_BASE_URL = "https://openrouter.ai/api/v1"
$env:AGREE_MODEL_NAME = $ModelId
$env:AADL_INSPECTOR_PATH = "E:\AI-1.10\bin\AADLInspector.exe"
$env:JAVA_HOME = "D:\jdk17"
$env:OSATE_HOME = "E:\osate2-2.12.0-vfinal-win32.win32.x86_64"
$env:AGREE_AADL_LIB_DIRS = @(
  "D:\AADL_Lib_workspace\AADLib_Test\src\property_set",
  "D:\AADL_Lib_workspace\AADLib_Test\src",
  "E:\AADLib-master\AADLib-master\src\property_set",
  "E:\AADLib-master\AADLib-master\src"
) -join [System.IO.Path]::PathSeparator
$env:AGREE_MAX_REPAIR_ROUNDS = "5"

if (-not $env:AGREE_MODEL_API_KEY) {
  throw "AGREE_MODEL_API_KEY is not configured in this process."
}

$modelRoot = Join-Path $ResultRoot $ModelSlug
$logDir = Join-Path $modelRoot "_logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

$summary = Join-Path $logDir "run_summary.txt"
"RQ1 run started: $(Get-Date -Format o)" | Set-Content -LiteralPath $summary -Encoding UTF8
"Model slug: $ModelSlug" | Add-Content -LiteralPath $summary -Encoding UTF8
"Model id: $ModelId" | Add-Content -LiteralPath $summary -Encoding UTF8
"Range: $Start-$End A,B" | Add-Content -LiteralPath $summary -Encoding UTF8

function Invoke-Rq1Setting {
  param(
    [Parameter(Mandatory = $true)]
    [string]$Setting,
    [Parameter(Mandatory = $true)]
    [string]$SettingSlug
  )

  $settingResult = Join-Path $modelRoot $SettingSlug
  $logPath = Join-Path $logDir "$SettingSlug.log"
  Write-Host "============================================================" -ForegroundColor Cyan
  Write-Host "Model: $ModelSlug"
  Write-Host "Setting: $Setting ($SettingSlug)"
  Write-Host "Cases: $Start-$End A,B"
  Write-Host "Result: $settingResult"
  Write-Host "Log: $logPath"
  Write-Host "============================================================" -ForegroundColor Cyan

  python .\scripts\run_batch.py `
    --start $Start `
    --end $End `
    --letters A B `
    --setting $Setting `
    --result-root $settingResult `
    --llm-base-url "https://openrouter.ai/api/v1" `
    --llm-model-name $ModelId `
    --max-repair-rounds 5 `
    2>&1 | Tee-Object -FilePath $logPath

  $exitCode = $LASTEXITCODE
  "$Setting exit code: $exitCode at $(Get-Date -Format o)" | Add-Content -LiteralPath $summary -Encoding UTF8
  if ($exitCode -ne 0) {
    if ($exitCode -eq 75) {
      Write-Host "Provider quota/rate/billing-like stop detected for $ModelSlug / $Setting." -ForegroundColor Yellow
    } else {
      Write-Host "Non-zero exit for $ModelSlug / $Setting: $exitCode." -ForegroundColor Red
    }
    exit $exitCode
  }
}

Invoke-Rq1Setting -Setting "E1" -SettingSlug "e1-bare-model"
Invoke-Rq1Setting -Setting "E2" -SettingSlug "e2-full-agree-autogen"

"RQ1 run finished: $(Get-Date -Format o)" | Add-Content -LiteralPath $summary -Encoding UTF8
Write-Host "RQ1 model run finished: $ModelSlug" -ForegroundColor Green
