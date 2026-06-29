# Case180 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 67.45
- Initial validation errors: 2
- Final validation errors: 2

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 2
- Warnings: 0

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3682
- completion_tokens: 3396
- total_tokens: 7078

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 239: Couldn't resolve reference to property definition 'AGREE_Guarded_By'. Property set name may be missing.
2. /CaseProject/modified_model.aadl | line 240: Couldn't resolve reference to property definition 'AGREE_Assertion'. Property set name may be missing.
