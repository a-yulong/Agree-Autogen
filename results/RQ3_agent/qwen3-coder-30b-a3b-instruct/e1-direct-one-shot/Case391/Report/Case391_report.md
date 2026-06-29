# Case391 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 40.57
- Initial validation errors: 2
- Final validation errors: 2

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 2
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
- completion_tokens: 1383
- total_tokens: 5227

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 77: Couldn't resolve reference to property definition 'AGREE::Assumptions'.
2. /CaseProject/modified_model.aadl | line 78: Couldn't resolve reference to property definition 'AGREE::Guarantees'.
