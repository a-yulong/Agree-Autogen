# Case314 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 108.53
- Initial validation errors: 1
- Final validation errors: 1

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 1
- Warnings: 2

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 4589
- completion_tokens: 2868
- total_tokens: 7457

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 276: Couldn't resolve reference to property definition 'Agree_Assumptions'. Property set name may be missing.
