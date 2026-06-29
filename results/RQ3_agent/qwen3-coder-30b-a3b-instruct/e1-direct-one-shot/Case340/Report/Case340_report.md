# Case340 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 49.81
- Initial validation errors: 2
- Final validation errors: 2

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 2
- Warnings: 2

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 4544
- completion_tokens: 2871
- total_tokens: 7415

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 259: mismatched input 'send_data_to_autopilot_task' expecting ';'
2. /CaseProject/modified_model.aadl | line 259: missing 'end' at 'contract'
