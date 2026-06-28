param(
    [Parameter(Mandatory = $true)]
    [string]$CasesCsv,

    [Parameter(Mandatory = $true)]
    [string]$ResultRoot,

    [string]$ModelName = "qwen/qwen3-coder-30b-a3b-instruct",
    [string]$WorkerName = "worker"
)

$ErrorActionPreference = "Stop"
$repo = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$cases = $CasesCsv.Split(",") | ForEach-Object { [int]$_.Trim() } | Where-Object { $_ -gt 0 }

$env:PYTHONIOENCODING = "utf-8"
$env:PYTHONUTF8 = "1"
$env:AADL_INSPECTOR_PATH = "E:\AI-1.10\bin\AADLInspector.exe"
$env:JAVA_HOME = "D:\jdk17"
$env:OSATE_HOME = "E:\osate2-2.12.0-vfinal-win32.win32.x86_64"
$env:AGREE_SOURCE_ROOT = "C:\Users\25780\Desktop\Exp_Data\Sources"
$env:AGREE_DOCS_DIR = Join-Path $repo "knowledge_base"
$env:AGREE_RESULT_ROOT = $ResultRoot
$env:AGREE_AADL_LIB_DIRS = @(
    "D:\AADL_Lib_workspace\AADLib_Test\src\property_set",
    "D:\AADL_Lib_workspace\AADLib_Test\src",
    "E:\AADLib-master\AADLib-master\src\property_set",
    "E:\AADLib-master\AADLib-master\src"
) -join [System.IO.Path]::PathSeparator
$env:AGREE_MODEL_BASE_URL = "https://openrouter.ai/api/v1"
$env:AGREE_MODEL_NAME = $ModelName
$env:AGREE_MAX_REPAIR_ROUNDS = "5"

if (-not $env:AGREE_MODEL_API_KEY) {
    throw "AGREE_MODEL_API_KEY is not set in the current environment."
}

New-Item -ItemType Directory -Force -Path $ResultRoot | Out-Null
$logPath = Join-Path $ResultRoot "$WorkerName.log"

"$WorkerName started: $(Get-Date -Format s)" | Tee-Object -FilePath $logPath
"Cases: $($cases -join ', ')" | Tee-Object -FilePath $logPath -Append
"ResultRoot: $ResultRoot" | Tee-Object -FilePath $logPath -Append

foreach ($case in $cases) {
    $label = "Case{0:D2}_A" -f $case
    "`n================================================================================" | Tee-Object -FilePath $logPath -Append
    "Running $label" | Tee-Object -FilePath $logPath -Append
    "================================================================================" | Tee-Object -FilePath $logPath -Append

    $runCase = Join-Path $repo "scripts\run_case.py"
    $caseCommand = @(
        "python",
        "`"$runCase`"",
        "--case-num $case",
        "--case-letter A",
        "--setting E2",
        "--max-repair-rounds 5",
        "--result-root `"$ResultRoot`"",
        "--llm-base-url `"https://openrouter.ai/api/v1`"",
        "--llm-model-name `"$ModelName`"",
        "--use-rag"
    ) -join " "

    cmd.exe /d /c "$caseCommand 2>&1" | Tee-Object -FilePath $logPath -Append

    if ($LASTEXITCODE -eq 75) {
        "Provider quota/rate/billing-like stop detected. Stopping $WorkerName." | Tee-Object -FilePath $logPath -Append
        exit 75
    }
    if ($LASTEXITCODE -ne 0) {
        "Process-level failure for $label with exit code $LASTEXITCODE. Stopping $WorkerName." | Tee-Object -FilePath $logPath -Append
        exit $LASTEXITCODE
    }
}

"`n$WorkerName finished: $(Get-Date -Format s)" | Tee-Object -FilePath $logPath -Append
Write-Host "Finished $WorkerName. Press Enter to close." -ForegroundColor Green
Read-Host | Out-Null
