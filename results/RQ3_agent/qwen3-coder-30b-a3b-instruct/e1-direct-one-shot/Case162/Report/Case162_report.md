# Case162 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 71.76
- Initial validation errors: 4
- Final validation errors: 4

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 4
- Warnings: 2

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 1774
- completion_tokens: 1613
- total_tokens: 3387

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 228: Property statement 'angle_bound' is of type 'ErrorTypeDef' but must be of type 'bool'
2. /CaseProject/modified_model.aadl | line 228: Property statments are allowed only in component annexes
3. /CaseProject/modified_model.aadl | line 228: mismatched character ' ' expecting ']'
4. /CaseProject/modified_model.aadl | line 228: mismatched input ':' expecting '='
