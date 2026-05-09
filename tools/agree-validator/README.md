# Standalone AGREE Validator

This directory contains the source code for the standalone AGREE syntax and semantic validation CLI used by Agree-Autogen.

The validator embeds OSATE/AADL2 and AGREE Xtext services in a command-line workflow. It loads AADL projects, registers the AGREE annex parser and linker, resolves model references, runs Xtext validation, and emits a compact JSON report.

## Components

```text
tools/agree-validator/
|-- build.ps1
|-- run-validator.ps1
`-- src/main/java/org/agreeautogen/validator/
    |-- AgreeValidationCli.java
    |-- StandaloneAgreeAnnexParser.java
    |-- StandaloneAgreeAnnexLinkingService.java
    |-- DebugIssueCodes.java
    `-- InspectAgreeAnnex.java
```

## Validation flow

1. Initialize `Aadl2StandaloneSetup` and `AgreeStandaloneSetup`.
2. Register the AGREE annex parser and linking service with `AnnexRegistry`.
3. Load project AADL files with platform-resource URIs.
4. Load referenced workspace projects and optional external AADL libraries.
5. Load OSATE contributed AADL resources while avoiding duplicates already present in the case project.
6. Run `IResourceValidator` on loaded Xtext resources.
7. Filter duplicate-package diagnostics and optionally focus output on a target AADL file.
8. Emit JSON with `infos`, `warnings`, `errors`, and normalized issue records.

## Build

PowerShell:

```powershell
$env:JAVA_HOME = "path/to/jdk17"
$env:OSATE_HOME = "path/to/osate"
.\tools\agree-validator\build.ps1
```

The compiled classes are written to `tools/agree-validator/out/`, which is intentionally ignored by Git.

## Run

```powershell
.\tools\agree-validator\run-validator.ps1 `
  -Workspace "path/to/workspace" `
  -Project "path/to/workspace/CaseProject" `
  -OsateHome $env:OSATE_HOME `
  -JavaHome $env:JAVA_HOME `
  -FocusFile "modified_model.aadl" `
  -Output "validation-report.json"
```

The main Python pipeline calls the same Java entry point:

```text
org.agreeautogen.validator.AgreeValidationCli
```

## Static AADL libraries

If a local experiment requires additional AADL libraries, place legally redistributable `.aadl` files under `tools/agree-validator/static-libs/` or pass external folders with `--lib-dir`.

This repository does not bundle third-party OSATE or AGREE library snapshots by default. Many of those files originate from external projects and should only be redistributed when their license explicitly allows it.
