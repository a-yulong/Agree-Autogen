# Case60 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 115.57
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

- prompt_tokens: 3709
- completion_tokens: 3447
- total_tokens: 7156

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 103: Couldn't resolve reference to 'Agree_Nodes::Brake_Mode'.
2. /CaseProject/modified_model.aadl | line 106: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
3. /CaseProject/modified_model.aadl | line 106: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
4. /CaseProject/modified_model.aadl | line 124: Couldn't resolve reference to 'Agree_Nodes::Brake_Mode'.
5. /CaseProject/modified_model.aadl | line 139: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
6. /CaseProject/modified_model.aadl | line 139: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
7. /CaseProject/modified_model.aadl | line 256: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
8. /CaseProject/modified_model.aadl | line 256: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
9. /CaseProject/modified_model.aadl | line 257: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
10. /CaseProject/modified_model.aadl | line 257: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
11. /CaseProject/modified_model.aadl | line 258: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
12. /CaseProject/modified_model.aadl | line 258: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
13. /CaseProject/modified_model.aadl | line 259: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
14. /CaseProject/modified_model.aadl | line 259: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
