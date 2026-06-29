# Case147 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 85.52
- Initial validation errors: 14
- Final validation errors: 14

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 14
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
- completion_tokens: 1611
- total_tokens: 3391

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 227: Property statments are allowed only in component annexes
2. /CaseProject/modified_model.aadl | line 227: left and right sides of binary expression '-' are of type '<error>' and 'int', but must be of the same type
3. /CaseProject/modified_model.aadl | line 227: left side of binary expression '-' is of type '<error>' but must be of type'int' or 'real'
4. /CaseProject/modified_model.aadl | line 227: left side of binary expression '<=' is of type '<error>' but must be of type'int' or 'real'
5. /CaseProject/modified_model.aadl | line 227: missing '=' at 'is'
6. /CaseProject/modified_model.aadl | line 227: named thing must be an expression with a type
7. /CaseProject/modified_model.aadl | line 227: right side of binary expression '<=' is of type '<error>' but must be of type'int' or 'real'
8. /CaseProject/modified_model.aadl | line 228: Couldn't resolve reference to 's'.
9. /CaseProject/modified_model.aadl | line 228: Couldn't resolve reference to 'speed'.
10. /CaseProject/modified_model.aadl | line 228: left and right sides of binary expression '<=' are of type '<error>' and 'int', but must be of the same type
11. /CaseProject/modified_model.aadl | line 228: left side of binary expression '<=' is of type '<error>' but must be of type'int' or 'real'
12. /CaseProject/modified_model.aadl | line 228: mismatched character ' ' expecting ']'
13. /CaseProject/modified_model.aadl | line 228: named thing must be an expression with a type
14. /CaseProject/modified_model.aadl | line 229: missing EOF at 'end'
