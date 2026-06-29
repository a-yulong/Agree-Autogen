# Case35 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 61.39
- Initial validation errors: 4
- Final validation errors: 4

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 4
- Warnings: 7

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 2437
- completion_tokens: 529
- total_tokens: 2966

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 25: 'Actual' and 'Actual_Speed' have incompatible classifiers.
2. /CaseProject/modified_model.aadl | line 27: The types of 'Target_Speed' and 'Target' do not match.
3. /CaseProject/modified_model.aadl | line 32: 'State_Out' and 'State_Signal' have incompatible classifiers.
4. /CaseProject/modified_model.aadl | line 36: missing EOF at 'const_tar_speed'
