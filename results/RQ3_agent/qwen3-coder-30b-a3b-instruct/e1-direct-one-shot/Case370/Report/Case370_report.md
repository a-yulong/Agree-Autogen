# Case370 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 61.86
- Initial validation errors: 3
- Final validation errors: 3

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 3
- Warnings: 2

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 4566
- completion_tokens: 2923
- total_tokens: 7489

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 262: Couldn't resolve reference to property definition 'AGREE_Bounded'. Property set name may be missing.
2. /CaseProject/modified_model.aadl | line 263: Couldn't resolve reference to property definition 'AGREE_Guard'. Property set name may be missing.
3. /CaseProject/modified_model.aadl | line 264: mismatched input '.' expecting ';'
