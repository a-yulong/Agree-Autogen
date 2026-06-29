# Case151 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 47.63
- Initial validation errors: 7
- Final validation errors: 7

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 7
- Warnings: 2

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 1780
- completion_tokens: 1687
- total_tokens: 3467

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 227: Property statement 'bounded_speed_input' is of type 'ErrorTypeDef' but must be of type 'bool'
2. /CaseProject/modified_model.aadl | line 227: Property statments are allowed only in component annexes
3. /CaseProject/modified_model.aadl | line 227: mismatched input ';' expecting '='
4. /CaseProject/modified_model.aadl | line 230: Property statement 'speed_bounds' is of type 'ErrorTypeDef' but must be of type 'bool'
5. /CaseProject/modified_model.aadl | line 230: Property statments are allowed only in component annexes
6. /CaseProject/modified_model.aadl | line 230: mismatched input ';' expecting '='
7. /CaseProject/modified_model.aadl | line 232: mismatched character ' ' expecting ']'
