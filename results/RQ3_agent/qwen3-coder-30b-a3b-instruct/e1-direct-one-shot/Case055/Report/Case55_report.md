# Case55 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 46.43
- Initial validation errors: 12
- Final validation errors: 12

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 12
- Warnings: 0

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 699
- completion_tokens: 517
- total_tokens: 1216

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 61: Assume statements are allowed only in component types
2. /CaseProject/modified_model.aadl | line 61: Couldn't resolve reference to 'Input'.
3. /CaseProject/modified_model.aadl | line 61: left and right sides of binary expression '<' are of type '<error>' and 'int', but must be of the same type
4. /CaseProject/modified_model.aadl | line 61: left side of binary expression '<' is of type '<error>' but must be of type'int' or 'real'
5. /CaseProject/modified_model.aadl | line 61: missing RULE_STRING at ':'
6. /CaseProject/modified_model.aadl | line 61: named thing must be an expression with a type
7. /CaseProject/modified_model.aadl | line 64: Couldn't resolve reference to 'Output'.
8. /CaseProject/modified_model.aadl | line 64: Guarantee statements are allowed only in component types
9. /CaseProject/modified_model.aadl | line 64: left and right sides of binary expression '<' are of type '<error>' and 'int', but must be of the same type
10. /CaseProject/modified_model.aadl | line 64: left side of binary expression '<' is of type '<error>' but must be of type'int' or 'real'
11. /CaseProject/modified_model.aadl | line 64: missing RULE_STRING at ':'
12. /CaseProject/modified_model.aadl | line 64: named thing must be an expression with a type
