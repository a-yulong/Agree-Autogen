param(
    [Parameter(Mandatory = $true)]
    [string]$Workspace,

    [Parameter(Mandatory = $true)]
    [string]$Project,

    [string]$OsateHome = $env:OSATE_HOME,
    [string]$JavaHome = $env:JAVA_HOME,
    [string]$Output = "",
    [string]$FocusFile = "",
    [string[]]$LibDir = @(),
    [switch]$FailOnWarning
)

$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$outDir = Join-Path $projectRoot "out"

if (-not (Test-Path $outDir)) {
    throw "Compiled classes not found. Run build.ps1 first."
}
if (-not $JavaHome) {
    throw "JAVA_HOME is not set. Provide -JavaHome or set JAVA_HOME."
}
if (-not $OsateHome) {
    throw "OSATE_HOME is not set. Provide -OsateHome or set OSATE_HOME."
}
if (-not $Output) {
    $Output = Join-Path $projectRoot "validation-report.json"
}

$env:JAVA_HOME = $JavaHome
$env:Path = "$JavaHome\bin;$env:Path"

$classpath = "$outDir;$(Join-Path $OsateHome 'plugins\*')"
$java = Join-Path $JavaHome "bin\java.exe"
if (-not (Test-Path $java)) {
    $java = "java"
}

$argsList = @(
    "-cp", $classpath,
    "org.agreeautogen.validator.AgreeValidationCli",
    "--workspace", $Workspace,
    "--project", $Project,
    "--osate-home", $OsateHome,
    "--output", $Output
)

if ($FocusFile) {
    $argsList += @("--focus-file", $FocusFile)
}
foreach ($dir in $LibDir) {
    $argsList += @("--lib-dir", $dir)
}
if ($FailOnWarning) {
    $argsList += "--fail-on-warning"
}

& $java @argsList
if ($LASTEXITCODE -ne 0) {
    throw "AGREE validator failed with exit code $LASTEXITCODE"
}
