# Case66 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 88.39
- Initial validation errors: 2
- Final validation errors: 2

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 2
- Warnings: 7

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 4860
- completion_tokens: 1969
- total_tokens: 6829

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 86: Couldn't resolve reference to ConnectionEnd 'attitude_window'.
2. /CaseProject/modified_model.aadl | line 87: Couldn't resolve reference to ConnectionEnd 'check_thresholds'.
