# Standalone AGREE Validator Setup

AGREE-AutoGen uses a standalone validator to check fused AADL+AGREE artifacts from the command line. The validator embeds OSATE/AADL2 and AGREE Xtext services, loads the case project and supporting AADL libraries, resolves model references, runs validation, and emits JSON diagnostics.

## Location

```text
tools/agree-validator/
  build.ps1
  run-validator.ps1
  src/main/java/org/agreeautogen/validator/
  static-libs/
  out/
```

The Java entry point is:

```text
org.agreeautogen.validator.AgreeValidationCli
```

## Requirements

The validator requires:

- JDK 17;
- OSATE with AGREE support;
- compiled validator classes under `tools/agree-validator/out`;
- AADL support libraries under `tools/agree-validator/static-libs`.

OSATE is an external dependency and is not redistributed in this repository.

## Build

```powershell
$env:JAVA_HOME = "D:\jdk17"
$env:OSATE_HOME = "E:\osate2-2.12.0-vfinal-win32.win32.x86_64"

.\tools\agree-validator\build.ps1
```

The build writes compiled classes to:

```text
tools/agree-validator/out/
```

## Run

```powershell
.\tools\agree-validator\run-validator.ps1 `
  -Workspace "<workspace-dir>" `
  -Project "<workspace-dir>\CaseProject" `
  -JavaHome $env:JAVA_HOME `
  -OsateHome $env:OSATE_HOME `
  -FocusFile "model.aadl" `
  -Output "<workspace-dir>\validation-report.json"
```

The output is a JSON report:

```json
{
  "infos": 0,
  "warnings": 0,
  "errors": 0,
  "issues": []
}
```

Files with validation errors produce diagnostic records and a failing validator exit status. Experiment scripts record these diagnostics as case outcomes.

## Resource Loading

The validator loads resources from several locations:

- AADL files under the temporary case project;
- optional `--lib-dir` directories;
- bundled files under `tools/agree-validator/static-libs`;
- OSATE plugin resources;
- referenced workspace projects when present.

The experiment pipeline prepares temporary projects so that case-specific dependencies are visible to the validator. This keeps the Java validator focused on loading and validating resources, while the Python pipeline manages case layout and dependency preparation.

## Static Libraries

`static-libs/` contains reusable AADL and AGREE support files such as:

- `Base_Types.aadl`;
- `AGREE_Stdlib.aadl`;
- `AGREE_PLTL.aadl`;
- `Agree_Nodes.aadl`;
- common AADL property sets.

Only redistributable support files should be committed. Third-party tool installations should remain external dependencies.

## Diagnostics in Experiments

Validator diagnostics are used in two ways:

- to determine whether a final artifact is accepted;
- to guide bounded repair when repair is enabled.

A validator failure is not the same as a stage error. It means the pipeline completed and produced an artifact, but the artifact did not pass validation.
