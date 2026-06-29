# Case50 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 45.53
- Initial validation errors: 15
- Final validation errors: 15

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 15
- Warnings: 0

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 705
- completion_tokens: 512
- total_tokens: 1217

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 61: Assume statements are allowed only in component types
2. /CaseProject/modified_model.aadl | line 61: Couldn't resolve reference to 'Input'.
3. /CaseProject/modified_model.aadl | line 61: left and right sides of binary expression '<' are of type '<error>' and 'int', but must be of the same type
4. /CaseProject/modified_model.aadl | line 61: left side of binary expression '<' is of type '<error>' but must be of type'int' or 'real'
5. /CaseProject/modified_model.aadl | line 61: missing RULE_STRING at ':'
6. /CaseProject/modified_model.aadl | line 61: named thing must be an expression with a type
7. /CaseProject/modified_model.aadl | line 64: Couldn't resolve reference to 'Input'.
8. /CaseProject/modified_model.aadl | line 64: Couldn't resolve reference to 'Output'.
9. /CaseProject/modified_model.aadl | line 64: Guarantee statements are allowed only in component types
10. /CaseProject/modified_model.aadl | line 64: left and right sides of binary expression '+' are of type '<error>' and 'int', but must be of the same type
11. /CaseProject/modified_model.aadl | line 64: left side of binary expression '+' is of type '<error>' but must be of type'int' or 'real'
12. /CaseProject/modified_model.aadl | line 64: left side of binary expression '<' is of type '<error>' but must be of type'int' or 'real'
13. /CaseProject/modified_model.aadl | line 64: missing RULE_STRING at ':'
14. /CaseProject/modified_model.aadl | line 64: named thing must be an expression with a type
15. /CaseProject/modified_model.aadl | line 64: right side of binary expression '<' is of type '<error>' but must be of type'int' or 'real'
