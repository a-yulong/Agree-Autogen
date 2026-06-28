param(
  [string]$RepoRoot = "C:\Users\25780\Desktop\py_item\DeepSeek\Agree-Autogen_v2.0",
  [string]$RandomRoot = "C:\Users\25780\Desktop\Exp_Data\Result_v4.0\gpt54_yunwu_random10_20260622_high_stable",
  [string]$FullRoot = "C:\Users\25780\Desktop\Exp_Data\Result_v4.0\rq1_gpt54_full_20260622_high_stable",
  [int]$PollSeconds = 60
)

$ErrorActionPreference = "Stop"
$expectedCases = @(58, 96, 127, 214, 265, 332, 371, 374, 386, 435)
$modelSlug = "gpt-5.4-yunwu-high-stable"
$settingSlug = "e2-full-agree-autogen"
$randomSetting = Join-Path $RandomRoot "$modelSlug\$settingSlug"
$transitionLog = Join-Path $RandomRoot "full459_transition.log"

function Write-TransitionLog {
  param([string]$Message)
  $line = "$(Get-Date -Format o) $Message"
  $line | Add-Content -LiteralPath $transitionLog -Encoding UTF8
  Write-Host $line
}

function Get-CleanCompleteCases {
  $complete = @()
  foreach ($caseNum in $expectedCases) {
    $report = Join-Path $randomSetting ("Case{0}\Report\Case{0}_report.json" -f $caseNum)
    if (-not (Test-Path -LiteralPath $report)) { continue }
    try {
      $payload = Get-Content -LiteralPath $report -Raw | ConvertFrom-Json
      $keys = @($payload.PSObject.Properties.Name)
      if (($keys -contains "case_num") -and ($keys -contains "success") -and [string]::IsNullOrWhiteSpace([string]$payload.stage_error)) {
        $complete += $caseNum
      }
    } catch {
      continue
    }
  }
  return $complete
}

Write-TransitionLog "Waiting for clean completion of random-10 suite before starting full459."
while ($true) {
  $complete = @(Get-CleanCompleteCases)
  $randomWorkers = @(Get-CimInstance Win32_Process | Where-Object {
    $_.CommandLine -like "*run_rq1_gpt54_yunwu_random10.ps1*" -or
    ($_.CommandLine -like "*run_case.py*" -and $_.CommandLine -like "*gpt54_yunwu_random10_20260622_high_stable*")
  })
  Write-TransitionLog ("random_complete={0}/10 random_processes={1}" -f $complete.Count, $randomWorkers.Count)

  if ($complete.Count -eq 10 -and $randomWorkers.Count -eq 0) { break }
  Start-Sleep -Seconds $PollSeconds
}

$existingFull = @(Get-CimInstance Win32_Process | Where-Object {
  $_.CommandLine -like "*run_rq1_gpt54_yunwu_full459.ps1*" -or
  ($_.CommandLine -like "*run_case.py*" -and $_.CommandLine -like "*rq1_gpt54_full_20260622_high_stable*")
})
if ($existingFull.Count -gt 0) {
  Write-TransitionLog "Full459 runner/workers already active; not starting a duplicate."
  exit 0
}

New-Item -ItemType Directory -Force -Path $FullRoot | Out-Null
$stdout = Join-Path $FullRoot "runner_stdout.log"
$stderr = Join-Path $FullRoot "runner_stderr.log"
$script = Join-Path $RepoRoot "scripts\run_rq1_gpt54_yunwu_full459.ps1"
$process = Start-Process -FilePath "powershell.exe" -ArgumentList @(
  "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", $script
) -WorkingDirectory $RepoRoot -WindowStyle Hidden -RedirectStandardOutput $stdout -RedirectStandardError $stderr -PassThru
Write-TransitionLog ("Started full459 runner pid={0}; max_parallel=4; result_root={1}" -f $process.Id, $FullRoot)
