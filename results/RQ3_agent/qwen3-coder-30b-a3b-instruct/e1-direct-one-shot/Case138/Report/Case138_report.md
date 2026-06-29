# Case138 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 50.67
- Initial validation errors: 12
- Final validation errors: 12

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 12
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
- completion_tokens: 1682
- total_tokens: 3456

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 230: Property statments are allowed only in component annexes
2. /CaseProject/modified_model.aadl | line 230: left side of binary expression 'and' is of type '<error>' but must be of type 'bool'
3. /CaseProject/modified_model.aadl | line 230: missing '=' at 'is'
4. /CaseProject/modified_model.aadl | line 230: named thing must be an expression with a type
5. /CaseProject/modified_model.aadl | line 230: right side of binary expression 'and' is of type '<error>' but must be of type 'bool'
6. /CaseProject/modified_model.aadl | line 231: Couldn't resolve reference to 'angle'.
7. /CaseProject/modified_model.aadl | line 231: Couldn't resolve reference to 'i'.
8. /CaseProject/modified_model.aadl | line 231: mismatched character ' ' expecting ']'
9. /CaseProject/modified_model.aadl | line 231: named thing must be an expression with a type
10. /CaseProject/modified_model.aadl | line 231: no viable alternative at input '('
11. /CaseProject/modified_model.aadl | line 232: missing EOF at 'end'
12. /CaseProject/modified_model.aadl | line 236: mismatched character ' ' expecting ']'
