param(
  [string]$RepoRoot = "C:\Users\25780\Desktop\py_item\DeepSeek\Agree-Autogen_v2.0",
  [string]$ResultRoot = "C:\Users\25780\Desktop\Exp_Data\Result_v4.0\rq1_gpt54_full_20260622_high_stable",
  [string]$SeedRoot = "C:\Users\25780\Desktop\Exp_Data\Result_v4.0\gpt54_yunwu_random10_20260622_high_stable",
  [string]$ApiKeyFile = "C:\Users\25780\Desktop\py_item\key\Yunwu_API_key.txt",
  [string]$BaseUrl = "https://yunwu.ai/v1",
  [string]$ModelName = "gpt-5.4-high:stable",
  [int]$MaxParallel = 4,
  [int]$MaxAttempts = 3
)

$ErrorActionPreference = "Stop"
Set-Location -LiteralPath $RepoRoot

if (-not (Test-Path -LiteralPath $ApiKeyFile)) {
  throw "Yunwu API key file not found: $ApiKeyFile"
}
$apiKey = (Get-Content -LiteralPath $ApiKeyFile -Raw).Trim()
if ([string]::IsNullOrWhiteSpace($apiKey)) {
  throw "Yunwu API key file is empty: $ApiKeyFile"
}

$modelSlug = "gpt-5.4-yunwu-high-stable"
$settingSlug = "e2-full-agree-autogen"
$modelRoot = Join-Path $ResultRoot $modelSlug
$settingRoot = Join-Path $modelRoot $settingSlug
$logDir = Join-Path $ResultRoot "_logs"
New-Item -ItemType Directory -Force -Path $settingRoot, $logDir | Out-Null

$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"
$env:PYTHONUNBUFFERED = "1"
$env:AGREE_SOURCE_ROOT = "C:\Users\25780\Desktop\Exp_Data\Sources"
$env:AGREE_DOCS_DIR = Join-Path $RepoRoot "knowledge_base"
$env:AGREE_MODEL_BASE_URL = $BaseUrl
$env:AGREE_MODEL_NAME = $ModelName
$env:AGREE_MODEL_API_KEY = $apiKey
$env:AGREE_MODEL_WIRE_API = "responses"
$env:AGREE_LLM_MAX_RETRIES = "4"
$env:AGREE_MAX_COMPLETION_TOKENS = "60000"
$env:AGREE_MAX_REPAIR_ROUNDS = "5"
$env:AADL_INSPECTOR_PATH = "E:\AI-1.10\bin\AADLInspector.exe"
$env:JAVA_HOME = "D:\jdk17"
$env:OSATE_HOME = "E:\osate2-2.12.0-vfinal-win32.win32.x86_64"
$env:AGREE_AADL_LIB_DIRS = @(
  "D:\AADL_Lib_workspace\AADLib_Test\src\property_set",
  "D:\AADL_Lib_workspace\AADLib_Test\src",
  "E:\AADLib-master\AADLib-master\src\property_set",
  "E:\AADLib-master\AADLib-master\src"
) -join [System.IO.Path]::PathSeparator

$manifest = [ordered]@{
  suite = "RQ1 GPT-5.4-high Yunwu full 459"
  created_at = (Get-Date -Format o)
  cases = "1-459"
  setting = "E2"
  setting_slug = $settingSlug
  model = $ModelName
  wire_api = "responses"
  base_url = $BaseUrl
  routing = "stable / success_rate"
  max_output_tokens = 60000
  max_parallel = $MaxParallel
  max_attempts = $MaxAttempts
  seed_root = $SeedRoot
  result_root = $ResultRoot
}
$manifest | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $ResultRoot "manifest.json") -Encoding UTF8

function Get-ReportState {
  param([int]$CaseNum, [string]$Root = $settingRoot)
  $caseLabel = "Case{0:D2}" -f $CaseNum
  $report = Join-Path $Root ("{0}\Report\{0}_report.json" -f $caseLabel)
  if (-not (Test-Path -LiteralPath $report)) {
    return [pscustomobject]@{ Complete = $false; Retryable = $true; Success = $false; StageError = "missing_report"; Report = $report }
  }
  try {
    $payload = Get-Content -LiteralPath $report -Raw | ConvertFrom-Json
    $keys = @($payload.PSObject.Properties.Name)
    if (-not ($keys -contains "case_num") -or -not ($keys -contains "success")) {
      return [pscustomobject]@{ Complete = $false; Retryable = $true; Success = $false; StageError = "incomplete_report"; Report = $report }
    }
    $stageError = [string]$payload.stage_error
    return [pscustomobject]@{
      Complete = [string]::IsNullOrWhiteSpace($stageError)
      Retryable = -not [string]::IsNullOrWhiteSpace($stageError)
      Success = [bool]$payload.success
      StageError = $stageError
      Report = $report
    }
  } catch {
    return [pscustomobject]@{ Complete = $false; Retryable = $true; Success = $false; StageError = "report_parse_error: $($_.Exception.Message)"; Report = $report }
  }
}

# Reuse completed, provider-clean reports from the random-10 suite.
$seedSettingRoot = Join-Path $SeedRoot "$modelSlug\$settingSlug"
$seededCases = @()
if (Test-Path -LiteralPath $seedSettingRoot) {
  foreach ($caseNum in 1..459) {
    $seedState = Get-ReportState -CaseNum $caseNum -Root $seedSettingRoot
    if (-not $seedState.Complete) { continue }
    $sourceCase = Join-Path $seedSettingRoot ("Case{0}" -f $caseNum)
    $targetCase = Join-Path $settingRoot ("Case{0}" -f $caseNum)
    if (-not (Test-Path -LiteralPath $targetCase)) {
      Copy-Item -LiteralPath $sourceCase -Destination $targetCase -Recurse -Force
    }
    $seededCases += $caseNum
  }
}
$seededCases | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $ResultRoot "seeded_cases.json") -Encoding UTF8

$pending = [System.Collections.Generic.Queue[int]]::new()
$attempts = @{}
foreach ($caseNum in 1..459) {
  $state = Get-ReportState -CaseNum $caseNum
  if (-not $state.Complete) {
    $pending.Enqueue($caseNum)
    $attempts[$caseNum] = 0
  }
}

$active = @{}
$completed = @()
$permanentFailures = @()

function Write-SuiteState {
  $payload = [ordered]@{
    updated_at = (Get-Date -Format o)
    pending = @($pending.ToArray())
    active = @($active.Values | ForEach-Object { $_.CaseNum })
    completed_count = $completed.Count + $seededCases.Count
    seeded_cases = $seededCases
    permanent_failures = $permanentFailures
  }
  $payload | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath (Join-Path $ResultRoot "runner_state.json") -Encoding UTF8
}

function Start-CaseRun {
  param([int]$CaseNum)
  $attempts[$CaseNum] = [int]$attempts[$CaseNum] + 1
  $attempt = $attempts[$CaseNum]
  $stdout = Join-Path $logDir ("Case{0}_attempt{1}_stdout.log" -f $CaseNum, $attempt)
  $stderr = Join-Path $logDir ("Case{0}_attempt{1}_stderr.log" -f $CaseNum, $attempt)
  $arguments = @(
    ".\scripts\run_case.py",
    "--case-num", "$CaseNum",
    "--setting", "E2",
    "--max-repair-rounds", "5",
    "--result-root", $settingRoot,
    "--llm-base-url", $BaseUrl,
    "--llm-model-name", $ModelName,
    "--use-rag"
  )
  $process = Start-Process -FilePath "python" -ArgumentList $arguments -WorkingDirectory $RepoRoot -WindowStyle Hidden -RedirectStandardOutput $stdout -RedirectStandardError $stderr -PassThru
  Write-Host ("Started Case{0} attempt={1} pid={2}" -f $CaseNum, $attempt, $process.Id) -ForegroundColor Cyan
  return [pscustomobject]@{ Process = $process; CaseNum = $CaseNum; Attempt = $attempt; Stdout = $stdout; Stderr = $stderr }
}

Write-Host ("Seeded {0} completed random-sample case(s). Pending full-suite cases: {1}" -f $seededCases.Count, $pending.Count) -ForegroundColor Green

while ($pending.Count -gt 0 -or $active.Count -gt 0) {
  while ($pending.Count -gt 0 -and $active.Count -lt $MaxParallel) {
    $caseNum = $pending.Dequeue()
    $run = Start-CaseRun -CaseNum $caseNum
    $active[$run.Process.Id] = $run
  }

  Write-SuiteState
  Start-Sleep -Seconds 5

  foreach ($pidKey in @($active.Keys)) {
    $run = $active[$pidKey]
    $run.Process.Refresh()
    if (-not $run.Process.HasExited) { continue }

    $run.Process.WaitForExit()
    $exitCode = $run.Process.ExitCode
    $state = Get-ReportState -CaseNum $run.CaseNum
    $active.Remove($pidKey)

    if ($state.Complete) {
      $completed += [pscustomobject]@{
        case_num = $run.CaseNum
        attempt = $run.Attempt
        exit_code = $exitCode
        success = $state.Success
        finished_at = (Get-Date -Format o)
      }
      Write-Host ("Finished Case{0} success={1} attempt={2}" -f $run.CaseNum, $state.Success, $run.Attempt) -ForegroundColor Green
    } elseif ($run.Attempt -lt $MaxAttempts) {
      Write-Host ("Retrying Case{0}: {1}" -f $run.CaseNum, $state.StageError) -ForegroundColor Yellow
      $pending.Enqueue($run.CaseNum)
    } else {
      $failure = [pscustomobject]@{
        case_num = $run.CaseNum
        attempts = $run.Attempt
        exit_code = $exitCode
        stage_error = $state.StageError
        failed_at = (Get-Date -Format o)
      }
      $permanentFailures += $failure
      Write-Host ("Permanent stage failure Case{0}: {1}" -f $run.CaseNum, $state.StageError) -ForegroundColor Red
    }
    Write-SuiteState
  }
}

$completed | Sort-Object case_num | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $ResultRoot "process_summary.json") -Encoding UTF8
$permanentFailures | Sort-Object case_num | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $ResultRoot "permanent_stage_failures.json") -Encoding UTF8

python .\scripts\aggregate_experiment_results.py --result-root $ResultRoot
$aggregateExit = $LASTEXITCODE
if ($aggregateExit -ne 0) {
  throw "Aggregation failed with exit code $aggregateExit"
}

Write-Host "Full RQ1 suite finished: $ResultRoot" -ForegroundColor Green
