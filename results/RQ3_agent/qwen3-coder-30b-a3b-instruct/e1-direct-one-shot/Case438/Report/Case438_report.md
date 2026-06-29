# Case438 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 55.25
- Initial validation errors: 5
- Final validation errors: 5

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 2
- AGREE errors: 3
- Warnings: 16

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 14132
- completion_tokens: 847
- total_tokens: 14979

## Final Diagnostics

1. autopilot_hard (identifier) is not a package or a property set visible or existing
2. Cannot analyze AADL specifications
3. /CaseProject/modified_model.aadl | line 28: Duplicate Element 'Pression' in PublicPackageSection 'autopilot_hard_public'
4. /CaseProject/modified_model.aadl | line 105: Duplicate Element 'Pression' in PublicPackageSection 'autopilot_hard_public'
5. /CaseProject/modified_model.aadl | line 109: Couldn't resolve reference to property definition 'AGREE_Bounds'. Property set name may be missing.
