# Case373 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 57.89
- Initial validation errors: 10
- Final validation errors: 10

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 10
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
- completion_tokens: 2928
- total_tokens: 7494

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 263: Property statments are allowed only in component annexes
2. /CaseProject/modified_model.aadl | line 263: left side of binary expression '=>' is of type '<error>' but must be of type 'bool'
3. /CaseProject/modified_model.aadl | line 263: missing '=' at 'is'
4. /CaseProject/modified_model.aadl | line 265: Couldn't resolve reference to 'Cde_AileronL_Output'.
5. /CaseProject/modified_model.aadl | line 265: Couldn't resolve reference to 't'.
6. /CaseProject/modified_model.aadl | line 265: left and right sides of binary expression '<=' are of type '<error>' and 'int', but must be of the same type
7. /CaseProject/modified_model.aadl | line 265: left and right sides of binary expression '<=' are of type 'int' and '<error>', but must be of the same type
8. /CaseProject/modified_model.aadl | line 265: left side of binary expression '<=' is of type '<error>' but must be of type'int' or 'real'
9. /CaseProject/modified_model.aadl | line 265: right side of binary expression '<=' is of type '<error>' but must be of type'int' or 'real'
10. /CaseProject/modified_model.aadl | line 266: missing EOF at 'end'
