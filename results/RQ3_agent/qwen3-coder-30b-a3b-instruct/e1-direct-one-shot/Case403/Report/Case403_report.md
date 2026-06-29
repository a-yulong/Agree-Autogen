# Case403 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 43.78
- Initial validation errors: 3
- Final validation errors: 3

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 3
- Warnings: 8

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3844
- completion_tokens: 1377
- total_tokens: 5221

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 8: Couldn't resolve reference to ModelUnit 'AGREE'.
2. /CaseProject/modified_model.aadl | line 78: Couldn't resolve reference to property definition 'AGREE::Assumptions'.
3. /CaseProject/modified_model.aadl | line 79: Couldn't resolve reference to property definition 'AGREE::Guarantees'.
