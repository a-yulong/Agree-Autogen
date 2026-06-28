param(
  [Parameter(Mandatory=$true)][string]$ModelSlug,
  [Parameter(Mandatory=$true)][string]$ModelId,
  [Parameter(Mandatory=$true)][string]$CaseListPath,
  [string]$RepoRoot = "C:\Users\25780\Desktop\py_item\DeepSeek\Agree-Autogen_v2.0",
  [string]$SourceRoot = "C:\Users\25780\Desktop\Exp_Data\Sources",
  [string]$ResultRoot = "C:\Users\25780\Desktop\Exp_Data\Result_v4.0\random50_full_rag",
  [int]$MaxRepairRounds = 5,
  [string]$OpenRouterKey = $env:AGREE_MODEL_API_KEY,
  [string]$LlmBaseUrl = "https://openrouter.ai/api/v1",
  [string]$WireApi = $env:AGREE_MODEL_WIRE_API
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
$env:AGREE_MODEL_BASE_URL = $LlmBaseUrl
$env:AGREE_MODEL_API_KEY = $OpenRouterKey
if ($WireApi) {
  $env:AGREE_MODEL_WIRE_API = $WireApi
}
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

$caseLabels = Get-Content -LiteralPath $CaseListPath | Where-Object { $_.Trim() } | ForEach-Object { $_.Trim() }
if (-not $caseLabels -or $caseLabels.Count -eq 0) {
  throw "No case ids found in $CaseListPath"
}

$settingResult = Join-Path $ResultRoot (Join-Path $ModelSlug "e2-full-rag")
$logRoot = Join-Path $ResultRoot "_logs"
New-Item -ItemType Directory -Force -Path $settingResult | Out-Null
New-Item -ItemType Directory -Force -Path $logRoot | Out-Null

$workerLog = Join-Path $logRoot "$ModelSlug.worker.log"
$summaryPath = Join-Path $logRoot "$ModelSlug.summary.jsonl"
"[$(Get-Date -Format o)] start model=$ModelSlug id=$ModelId cases=$($caseLabels.Count)" | Tee-Object -FilePath $workerLog

$executed = 0
foreach ($caseLabelRaw in $caseLabels) {
  if ($caseLabelRaw -match '^Case(\d+)(?:_([AB]))?$') {
    $caseId = [int]$Matches[1]
    $caseLetter = if ($Matches[2]) { $Matches[2] } else { "" }
    $caseLabel = if ($caseLetter) { "Case$('{0:D2}' -f $caseId)_$caseLetter" } else { "Case$('{0:D2}' -f $caseId)" }
  } elseif ($caseLabelRaw -match '^(\d+)(?:_([AB]))?$') {
    $caseId = [int]$Matches[1]
    $caseLetter = if ($Matches[2]) { $Matches[2] } else { "" }
    $caseLabel = if ($caseLetter) { "Case$('{0:D2}' -f $caseId)_$caseLetter" } else { "Case$('{0:D2}' -f $caseId)" }
  } else {
    throw "Unsupported case label in ${CaseListPath}: $caseLabelRaw"
  }
  $caseLog = Join-Path $logRoot "$ModelSlug.$caseLabel.log"
  "[$(Get-Date -Format o)] running $ModelSlug $caseLabel" | Tee-Object -FilePath $workerLog -Append

  $ErrorActionPreference = "Continue"
  $runArgs = @(
    ".\scripts\run_case.py",
    "--case-num", "$caseId",
    "--setting", "E2",
    "--max-repair-rounds", "$MaxRepairRounds",
    "--result-root", "$settingResult",
    "--llm-base-url", "$LlmBaseUrl",
    "--llm-api-key", "$OpenRouterKey",
    "--llm-model-name", "$ModelId"
  )
  if ($caseLetter) {
    $runArgs += @("--case-letter", "$caseLetter")
  }
  python @runArgs 2>&1 | Tee-Object -FilePath $caseLog

  $exitCode = $LASTEXITCODE
  $ErrorActionPreference = "Stop"
  $executed += 1
  ([ordered]@{
    timestamp = Get-Date -Format o
    model_slug = $ModelSlug
    model_id = $ModelId
    case_id = $caseLabel
    exit_code = $exitCode
  } | ConvertTo-Json -Compress) | Add-Content -LiteralPath $summaryPath -Encoding UTF8

  if ($exitCode -eq 75) {
    "[$(Get-Date -Format o)] provider stop exit=75 at $caseLabel" | Tee-Object -FilePath $workerLog -Append
    break
  }
}

python .\scripts\aggregate_experiment_results.py --result-root $settingResult 2>&1 |
  Tee-Object -FilePath (Join-Path $logRoot "$ModelSlug.aggregate.log")

([ordered]@{
  timestamp = Get-Date -Format o
  model_slug = $ModelSlug
  model_id = $ModelId
  selected_case_count = $caseLabels.Count
  executed = $executed
  result_root = $settingResult
} | ConvertTo-Json -Depth 4) |
  Set-Content -LiteralPath (Join-Path $settingResult "_worker_completed.json") -Encoding UTF8

"[$(Get-Date -Format o)] finished model=$ModelSlug executed=$executed" | Tee-Object -FilePath $workerLog -Append
