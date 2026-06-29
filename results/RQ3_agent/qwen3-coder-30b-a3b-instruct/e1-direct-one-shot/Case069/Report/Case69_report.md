# Case69 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 74.68
- Initial validation errors: 10
- Final validation errors: 10

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 10
- Warnings: 5

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 2745
- completion_tokens: 1845
- total_tokens: 4590

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 75: no viable alternative at input 'dataaocs'
2. /CaseProject/modified_model.aadl | line 78: no viable alternative at input 'port'
3. /CaseProject/modified_model.aadl | line 79: no viable alternative at input 'port'
4. /CaseProject/modified_model.aadl | line 80: no viable alternative at input 'port'
5. /CaseProject/modified_model.aadl | line 81: no viable alternative at input 'port'
6. /CaseProject/modified_model.aadl | line 82: no viable alternative at input 'port'
7. /CaseProject/modified_model.aadl | line 83: no viable alternative at input 'port'
8. /CaseProject/modified_model.aadl | line 84: no viable alternative at input 'port'
9. /CaseProject/modified_model.aadl | line 85: no viable alternative at input 'port'
10. /CaseProject/modified_model.aadl | line 93: missing EOF at 'thread'
