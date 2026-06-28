param(
  [string]$RepoRoot = "C:\Users\25780\Desktop\py_item\DeepSeek\Agree-Autogen_v2.0",
  [string]$ResultRoot = "C:\Users\25780\Desktop\Exp_Data\Result_v4.0\gpt5_yunwu_random10_20260622_budget60000",
  [string]$ApiKeyFile = "C:\Users\25780\Desktop\py_item\key\Yunwu_API_key.txt",
  [string]$BaseUrl = "https://yunwu.ai/v1",
  [string]$ModelName = "gpt-5:stable",
  [int]$MaxParallel = 3
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

$cases = @(58, 96, 127, 214, 265, 332, 371, 374, 386, 435)
$modelSlug = "gpt-5-yunwu-stable"
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
  suite = "RQ1 GPT-5 Yunwu random 10"
  created_at = (Get-Date -Format o)
  sample_seed = 20260622
  cases = $cases
  setting = "E2"
  setting_slug = $settingSlug
  model = $ModelName
  base_url = $BaseUrl
  routing = "stable / success_rate"
  max_parallel = $MaxParallel
  result_root = $ResultRoot
}
$manifest | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $ResultRoot "manifest.json") -Encoding UTF8

$pending = [System.Collections.Generic.Queue[int]]::new()
foreach ($caseNum in $cases) { $pending.Enqueue($caseNum) }
$active = @{}
$completed = @()

function Start-CaseRun {
  param([int]$CaseNum)
  $stdout = Join-Path $logDir ("Case{0}_stdout.log" -f $CaseNum)
  $stderr = Join-Path $logDir ("Case{0}_stderr.log" -f $CaseNum)
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
  Write-Host ("Started Case{0} pid={1}" -f $CaseNum, $process.Id) -ForegroundColor Cyan
  return [pscustomobject]@{ Process = $process; CaseNum = $CaseNum; Stdout = $stdout; Stderr = $stderr }
}

while ($pending.Count -gt 0 -or $active.Count -gt 0) {
  while ($pending.Count -gt 0 -and $active.Count -lt $MaxParallel) {
    $caseNum = $pending.Dequeue()
    $run = Start-CaseRun -CaseNum $caseNum
    $active[$run.Process.Id] = $run
  }

  Start-Sleep -Seconds 5
  foreach ($pidKey in @($active.Keys)) {
    $run = $active[$pidKey]
    $run.Process.Refresh()
    if ($run.Process.HasExited) {
      $run.Process.WaitForExit()
      $exitCode = $run.Process.ExitCode
      $completed += [pscustomobject]@{
        case_num = $run.CaseNum
        exit_code = $exitCode
        stdout = $run.Stdout
        stderr = $run.Stderr
        finished_at = (Get-Date -Format o)
      }
      $active.Remove($pidKey)
      $color = if ($exitCode -eq 0) { "Green" } else { "Red" }
      Write-Host ("Finished Case{0} exit={1}" -f $run.CaseNum, $exitCode) -ForegroundColor $color
    }
  }
}

$completed | Sort-Object case_num | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $ResultRoot "process_summary.json") -Encoding UTF8

python .\scripts\aggregate_experiment_results.py --result-root $ResultRoot
$aggregateExit = $LASTEXITCODE
if ($aggregateExit -ne 0) {
  throw "Aggregation failed with exit code $aggregateExit"
}

Write-Host "Random 10 suite finished: $ResultRoot" -ForegroundColor Green
