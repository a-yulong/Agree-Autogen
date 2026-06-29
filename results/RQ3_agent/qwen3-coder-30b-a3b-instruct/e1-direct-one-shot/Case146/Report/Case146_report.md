# Case146 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 46.20
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

- prompt_tokens: 1774
- completion_tokens: 1630
- total_tokens: 3404

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 227: Duplicate Element 'angle_bound'
2. /CaseProject/modified_model.aadl | line 227: Property statement 'angle_bound' is of type 'ErrorTypeDef' but must be of type 'bool'
3. /CaseProject/modified_model.aadl | line 227: Property statments are allowed only in component annexes
4. /CaseProject/modified_model.aadl | line 227: mismatched input 'in' expecting '='
5. /CaseProject/modified_model.aadl | line 228: Duplicate Element 'angle_bound'
6. /CaseProject/modified_model.aadl | line 228: Property statments are allowed only in component annexes
7. /CaseProject/modified_model.aadl | line 228: left side of binary expression '<=' is of type '<error>' but must be of type'int' or 'real'
8. /CaseProject/modified_model.aadl | line 228: missing '=' at 'is'
9. /CaseProject/modified_model.aadl | line 228: right side of binary expression '<=' is of type '<error>' but must be of type'int' or 'real'
10. /CaseProject/modified_model.aadl | line 229: Couldn't resolve reference to 'angle'.
11. /CaseProject/modified_model.aadl | line 229: Couldn't resolve reference to 'i'.
12. /CaseProject/modified_model.aadl | line 229: mismatched character ' ' expecting ']'
13. /CaseProject/modified_model.aadl | line 229: mismatched input '(' expecting ';'
14. /CaseProject/modified_model.aadl | line 229: named thing must be an expression with a type
