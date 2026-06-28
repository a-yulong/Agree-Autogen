param(
  [string]$ModelSlug = "qwen3-coder-30b-a3b-instruct",
  [string]$RepoRoot = "C:\Users\25780\Desktop\py_item\DeepSeek\Agree-Autogen_v2.0",
  [string]$SourceRoot = "C:\Users\25780\Desktop\Exp_Data\Sources",
  [string]$ResultRoot = "C:\Users\25780\Desktop\Exp_Data\Result_v4.0\post_rq1_full",
  [int]$ExpectedCases = 459,
  [int]$MaxRepairRounds = 5,
  [int]$PollSeconds = 60,
  [string[]]$Names = @(),
  [switch]$WaitForIdle,
  [switch]$DryRun
)

$ErrorActionPreference = "Stop"

$settings = @(
  [pscustomobject]@{ Name = "e2-digest-topk111"; TopK = 1 },
  [pscustomobject]@{ Name = "e2-digest-topk555"; TopK = 5 },
  [pscustomobject]@{ Name = "e2-digest-topk777"; TopK = 7 }
)
if ($Names.Count -gt 0) {
  $wanted = @{}
  foreach ($name in $Names) {
    $wanted[$name] = $true
  }
  $settings = @($settings | Where-Object { $wanted.ContainsKey($_.Name) })
  if ($settings.Count -eq 0) {
    throw "No known RQ2 top-k settings matched -Names: $($Names -join ', ')"
  }
}

function Get-ActiveRq2Process {
  Get-CimInstance Win32_Process |
    Where-Object {
      $_.CommandLine -and
      $_.CommandLine -match 'run_result_v4_rq2_topk_one\.ps1|run_existing_batch\.py|run_case\.py' -and
      $_.CommandLine -match 'e2-digest-topk111|e2-digest-topk555|e2-digest-topk777' -and
      $_.CommandLine -notmatch 'Get-CimInstance|run_result_v4_rq2_topk_rerun_needed'
    }
}

function Test-PathUnder {
  param(
    [Parameter(Mandatory=$true)][string]$Path,
    [Parameter(Mandatory=$true)][string]$Root
  )
  $resolvedRoot = [System.IO.Path]::GetFullPath($Root).TrimEnd('\') + '\'
  $resolvedPath = [System.IO.Path]::GetFullPath($Path)
  return $resolvedPath.StartsWith($resolvedRoot, [System.StringComparison]::OrdinalIgnoreCase)
}

function Get-CaseNumberFromName {
  param([string]$Name)
  if ($Name -match '^Case(\d+)(?:_[AB])?$') {
    return [int]$Matches[1]
  }
  return $null
}

function Get-ReportPath {
  param(
    [string]$SettingDir,
    [int]$CaseNum
  )
  $label = "Case{0:D2}" -f $CaseNum
  return Join-Path (Join-Path (Join-Path $SettingDir $label) "Report") ("{0}_report.json" -f $label)
}

function Test-RerunnableStageError {
  param($Report)
  if ($null -eq $Report.stage_error) {
    return $false
  }
  $text = [string]$Report.stage_error
  $patterns = @(
    'No recoverable JSON object found',
    'Remote end closed connection',
    'Connection aborted',
    'Connection reset',
    'Read timed out',
    'timed out',
    'timeout',
    '502',
    '503',
    '504',
    'Bad Gateway',
    'Service Unavailable',
    'Gateway Timeout',
    'rate limit',
    'quota',
    'provider',
    'API',
    'network',
    'temporar'
  )
  foreach ($pattern in $patterns) {
    if ($text -match $pattern) {
      return $true
    }
  }
  return $false
}

function Get-SettingAudit {
  param(
    [string]$SettingName,
    [string]$SettingDir
  )
  $rows = New-Object System.Collections.Generic.List[object]
  for ($caseNum = 1; $caseNum -le $ExpectedCases; $caseNum++) {
    $reportPath = Get-ReportPath -SettingDir $SettingDir -CaseNum $caseNum
    if (-not (Test-Path -LiteralPath $reportPath)) {
      $rows.Add([pscustomobject]@{
        setting = $SettingName
        case_num = $caseNum
        case_label = ("Case{0:D2}" -f $caseNum)
        reason_type = "missing_report"
        detail = "Expected report JSON is absent."
        report_json = $reportPath
      })
      continue
    }
    try {
      $report = Get-Content -LiteralPath $reportPath -Raw | ConvertFrom-Json
    } catch {
      $rows.Add([pscustomobject]@{
        setting = $SettingName
        case_num = $caseNum
        case_label = ("Case{0:D2}" -f $caseNum)
        reason_type = "corrupt_report_json"
        detail = $_.Exception.Message
        report_json = $reportPath
      })
      continue
    }
    if (Test-RerunnableStageError -Report $report) {
      $rows.Add([pscustomobject]@{
        setting = $SettingName
        case_num = $caseNum
        case_label = ("Case{0:D2}" -f $caseNum)
        reason_type = "rerunnable_stage_error"
        detail = [string]$report.stage_error
        report_json = $reportPath
      })
    }
  }
  return $rows
}

if ($WaitForIdle) {
  Write-Host "Waiting for active RQ2 top-k workers to become idle..." -ForegroundColor Cyan
  while ($true) {
    $active = @(Get-ActiveRq2Process)
    if ($active.Count -eq 0) {
      break
    }
    $summary = $active | ForEach-Object {
      if ($_.CommandLine -match 'e2-digest-topk111') { "topk111" }
      elseif ($_.CommandLine -match 'e2-digest-topk555') { "topk555" }
      elseif ($_.CommandLine -match 'e2-digest-topk777') { "topk777" }
      else { "rq2" }
    } | Group-Object | ForEach-Object { "{0}:{1}" -f $_.Name, $_.Count }
    Write-Host ("Still active: {0}; sleeping {1}s" -f ($summary -join ", "), $PollSeconds)
    Start-Sleep -Seconds $PollSeconds
  }
}

$rq2Root = Join-Path $ResultRoot (Join-Path "RQ2_rag" $ModelSlug)
if (-not (Test-Path -LiteralPath $rq2Root)) {
  throw "RQ2 result root not found: $rq2Root"
}

$auditRows = New-Object System.Collections.Generic.List[object]
foreach ($setting in $settings) {
  $settingDir = Join-Path $rq2Root $setting.Name
  if (-not (Test-Path -LiteralPath $settingDir)) {
    throw "Setting result directory not found: $settingDir"
  }
  foreach ($row in (Get-SettingAudit -SettingName $setting.Name -SettingDir $settingDir)) {
    $auditRows.Add($row)
  }
}

$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$auditPath = Join-Path $ResultRoot ("rq2_topk_rerun_needed_{0}.csv" -f $timestamp)
$auditRows | Export-Csv -NoTypeInformation -Encoding UTF8 -LiteralPath $auditPath
Write-Host ("Rerun audit written: {0}" -f $auditPath) -ForegroundColor Cyan

if ($auditRows.Count -eq 0) {
  Write-Host "No missing reports or rerunnable stage errors found." -ForegroundColor Green
  exit 0
}

Write-Host ("Cases needing rerun: {0}" -f $auditRows.Count) -ForegroundColor Yellow
if ($DryRun) {
  $auditRows | Group-Object setting, reason_type | Select-Object Name, Count | Format-Table -AutoSize
  exit 0
}

foreach ($setting in $settings) {
  $settingRows = @($auditRows | Where-Object { $_.setting -eq $setting.Name })
  if ($settingRows.Count -eq 0) {
    continue
  }
  $settingDir = Join-Path $rq2Root $setting.Name
  $minCase = [int](($settingRows | Measure-Object -Property case_num -Minimum).Minimum)
  $maxCase = [int](($settingRows | Measure-Object -Property case_num -Maximum).Maximum)

  Write-Host ("Preparing {0}: {1} case(s), range Case{2:D2}-Case{3:D2}" -f $setting.Name, $settingRows.Count, $minCase, $maxCase) -ForegroundColor Yellow

  foreach ($row in $settingRows) {
    $reportJson = [string]$row.report_json
    if (-not (Test-PathUnder -Path $reportJson -Root $settingDir)) {
      throw "Refusing to delete outside setting dir: $reportJson"
    }
    $reportMd = $reportJson -replace '\.json$', '.md'
    if (Test-Path -LiteralPath $reportJson) {
      Remove-Item -LiteralPath $reportJson -Force
    }
    if ((Test-Path -LiteralPath $reportMd) -and (Test-PathUnder -Path $reportMd -Root $settingDir)) {
      Remove-Item -LiteralPath $reportMd -Force
    }
  }

  $runner = Join-Path $RepoRoot "scripts\run_result_v4_rq2_topk_one.ps1"
  if (-not (Test-Path -LiteralPath $runner)) {
    throw "Top-k runner not found: $runner"
  }
  Write-Host ("Rerunning {0} through existing resume runner..." -f $setting.Name) -ForegroundColor Cyan
  & powershell -NoProfile -ExecutionPolicy Bypass -File $runner `
    -Name $setting.Name `
    -TopK $setting.TopK `
    -RepoRoot $RepoRoot `
    -SourceRoot $SourceRoot `
    -ResultRoot $ResultRoot `
    -Start $minCase `
    -End $maxCase `
    -MaxRepairRounds $MaxRepairRounds
  if ($LASTEXITCODE -ne 0) {
    throw ("Rerun failed for {0} with exit code {1}" -f $setting.Name, $LASTEXITCODE)
  }
}

Write-Host "RQ2 top-k rerun pass completed." -ForegroundColor Green
