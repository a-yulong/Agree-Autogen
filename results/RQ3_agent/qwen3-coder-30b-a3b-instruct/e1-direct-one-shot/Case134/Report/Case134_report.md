# Case134 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 49.55
- Initial validation errors: 9
- Final validation errors: 9

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 9
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
- completion_tokens: 1647
- total_tokens: 3421

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 227: Property statement 'angle_bound' is of type 'ErrorTypeDef' but must be of type 'bool'
2. /CaseProject/modified_model.aadl | line 227: Property statments are allowed only in component annexes
3. /CaseProject/modified_model.aadl | line 227: mismatched input 'in' expecting '='
4. /CaseProject/modified_model.aadl | line 229: Property statement 'angle_ge_zero' is of type 'ErrorTypeDef' but must be of type 'bool'
5. /CaseProject/modified_model.aadl | line 229: Property statments are allowed only in component annexes
6. /CaseProject/modified_model.aadl | line 229: mismatched input 'in' expecting '='
7. /CaseProject/modified_model.aadl | line 231: Property statement 'angle_le_hundred' is of type 'ErrorTypeDef' but must be of type 'bool'
8. /CaseProject/modified_model.aadl | line 231: Property statments are allowed only in component annexes
9. /CaseProject/modified_model.aadl | line 231: mismatched input 'in' expecting '='
