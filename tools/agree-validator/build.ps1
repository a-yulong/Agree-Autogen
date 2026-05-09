param(
    [string]$OsateHome = $env:OSATE_HOME,
    [string]$JavaHome = $env:JAVA_HOME,
    [string]$OutDir = ""
)

$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$srcRoot = Join-Path $projectRoot "src\main\java"
if (-not $OutDir) {
    $OutDir = Join-Path $projectRoot "out"
}

if (-not $JavaHome) {
    throw "JAVA_HOME is not set. Provide -JavaHome or set JAVA_HOME."
}
if (-not (Test-Path $JavaHome)) {
    throw "JDK not found: $JavaHome"
}

if (-not $OsateHome) {
    throw "OSATE_HOME is not set. Provide -OsateHome or set OSATE_HOME."
}
if (-not (Test-Path (Join-Path $OsateHome "plugins"))) {
    throw "OSATE plugins directory not found under: $OsateHome"
}

New-Item -ItemType Directory -Force $OutDir | Out-Null
Get-ChildItem -Recurse -Filter *.class $OutDir -ErrorAction SilentlyContinue | Remove-Item -Force

$env:JAVA_HOME = $JavaHome
$env:Path = "$JavaHome\bin;$env:Path"

$sources = Get-ChildItem -Recurse -Filter *.java $srcRoot | ForEach-Object { $_.FullName }
if (-not $sources) {
    throw "No Java sources found under $srcRoot"
}

$classpath = Join-Path $OsateHome "plugins\*"
$javac = Join-Path $JavaHome "bin\javac.exe"
if (-not (Test-Path $javac)) {
    $javac = "javac"
}

& $javac -encoding UTF-8 -cp $classpath -d $OutDir $sources
if ($LASTEXITCODE -ne 0) {
    throw "javac failed with exit code $LASTEXITCODE"
}
Write-Host "Compiled AGREE validator classes to $OutDir"
