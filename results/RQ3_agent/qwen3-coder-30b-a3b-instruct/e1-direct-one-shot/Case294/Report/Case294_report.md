# Case294 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 129.49
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

- prompt_tokens: 4589
- completion_tokens: 2854
- total_tokens: 7443

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 275: Couldn't resolve reference to property definition 'AGREE_Bounded_Input'. Property set name may be missing.
2. /CaseProject/modified_model.aadl | line 275: mismatched input '=>' expecting ';'
3. /CaseProject/modified_model.aadl | line 275: no viable alternative at input '=>'
