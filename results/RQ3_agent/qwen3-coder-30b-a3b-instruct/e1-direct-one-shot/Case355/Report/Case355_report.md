# Case355 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 112.08
- Initial validation errors: 11
- Final validation errors: 11

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 11
- Warnings: 2

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 4555
- completion_tokens: 2927
- total_tokens: 7482

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 112: Property statments are allowed only in component annexes
2. /CaseProject/modified_model.aadl | line 112: left and right sides of binary expression '>=' are of type '<error>' and 'int', but must be of the same type
3. /CaseProject/modified_model.aadl | line 112: left side of binary expression '>=' is of type '<error>' but must be of type'int' or 'real'
4. /CaseProject/modified_model.aadl | line 112: missing '=' at 'is'
5. /CaseProject/modified_model.aadl | line 113: mismatched character '\r' expecting ']'
6. /CaseProject/modified_model.aadl | line 114: Couldn't resolve reference to 'Data_Output'.
7. /CaseProject/modified_model.aadl | line 114: Couldn't resolve reference to 't'.
8. /CaseProject/modified_model.aadl | line 114: left and right sides of binary expression '<=' are of type '<error>' and 'int', but must be of the same type
9. /CaseProject/modified_model.aadl | line 114: left side of binary expression '<=' is of type '<error>' but must be of type'int' or 'real'
10. /CaseProject/modified_model.aadl | line 115: missing EOF at 'end'
11. /CaseProject/modified_model.aadl | line 119: mismatched character '\r' expecting ']'
