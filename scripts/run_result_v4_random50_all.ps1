param(
  [string]$RepoRoot = "C:\Users\25780\Desktop\py_item\DeepSeek\Agree-Autogen_v2.0",
  [string]$SourceRoot = "C:\Users\25780\Desktop\Exp_Data\Sources",
  [string]$ResultRoot = "C:\Users\25780\Desktop\Exp_Data\Result_v4.0",
  [int]$CaseCount = 50,
  [int]$Seed = 20260608,
  [int]$MaxRepairRounds = 5
)

$ErrorActionPreference = "Stop"

Set-Location -LiteralPath $RepoRoot

$models = @(
  @{ Slug = "qwen3-coder-30b-a3b-instruct"; Id = "qwen/qwen3-coder-30b-a3b-instruct" },
  @{ Slug = "llama-3.1-70b-instruct"; Id = "meta-llama/llama-3.1-70b-instruct" },
  @{ Slug = "gemma-3-27b-it"; Id = "google/gemma-3-27b-it" },
  @{ Slug = "codestral-2508"; Id = "mistralai/codestral-2508" },
  @{ Slug = "phi-4-mini-instruct"; Id = "microsoft/phi-4-mini-instruct" }
)

New-Item -ItemType Directory -Force -Path $ResultRoot | Out-Null
Get-ChildItem -LiteralPath $ResultRoot -Force | Remove-Item -Recurse -Force

$runRoot = Join-Path $ResultRoot "random50_full_rag"
$logRoot = Join-Path $runRoot "_logs"
New-Item -ItemType Directory -Force -Path $logRoot | Out-Null

$availableCases = Get-ChildItem -LiteralPath $SourceRoot -Directory |
  Where-Object { $_.Name -match '^Case\d+(?:_[AB])?$' } |
  ForEach-Object { $_.Name } |
  Sort-Object {
    if ($_ -match '^Case(\d+)(?:_([AB]))?$') {
      [int]$matches[1]
    } else {
      [int]::MaxValue
    }
  }, {
    if ($_ -match '^Case\d+_([AB])$') {
      $matches[1]
    } else {
      ''
    }
  }

if ($availableCases.Count -lt $CaseCount) {
  throw "Only $($availableCases.Count) cases available, cannot sample $CaseCount."
}

$rng = [System.Random]::new($Seed)
$selected = $availableCases | Sort-Object { $rng.Next() } | Select-Object -First $CaseCount |
  Sort-Object {
    if ($_ -match '^Case(\d+)(?:_([AB]))?$') {
      [int]$matches[1]
    } else {
      [int]::MaxValue
    }
  }, {
    if ($_ -match '^Case\d+_([AB])$') {
      $matches[1]
    } else {
      ''
    }
  }
$caseListPath = Join-Path $runRoot "selected_cases_random50_seed$Seed.txt"
$selected | Set-Content -LiteralPath $caseListPath -Encoding ASCII

([ordered]@{
  started_at = Get-Date -Format o
  seed = $Seed
  case_count = $CaseCount
  selected_cases = $selected
  setting = "E2"
  rag = "digest_full_framework"
  max_repair_rounds = $MaxRepairRounds
  models = $models
} | ConvertTo-Json -Depth 6) |
  Set-Content -LiteralPath (Join-Path $runRoot "run_manifest.json") -Encoding UTF8

$workerScript = Join-Path $RepoRoot "scripts\run_result_v4_random50_worker.ps1"
foreach ($model in $models) {
  $args = @(
    "-NoExit",
    "-ExecutionPolicy", "Bypass",
    "-File", "`"$workerScript`"",
    "-ModelSlug", "`"$($model.Slug)`"",
    "-ModelId", "`"$($model.Id)`"",
    "-CaseListPath", "`"$caseListPath`"",
    "-RepoRoot", "`"$RepoRoot`"",
    "-SourceRoot", "`"$SourceRoot`"",
    "-ResultRoot", "`"$runRoot`"",
    "-MaxRepairRounds", "$MaxRepairRounds"
  )
  Start-Process -FilePath "powershell.exe" -ArgumentList $args -WorkingDirectory $RepoRoot
  "[$(Get-Date -Format o)] started $($model.Slug) in separate PowerShell window" |
    Add-Content -LiteralPath (Join-Path $logRoot "dispatcher.log") -Encoding UTF8
}

Write-Host "Started random50 full-RAG run." -ForegroundColor Green
Write-Host "Run root: $runRoot"
Write-Host "Selected cases: $caseListPath"
Write-Host "Logs: $logRoot"
