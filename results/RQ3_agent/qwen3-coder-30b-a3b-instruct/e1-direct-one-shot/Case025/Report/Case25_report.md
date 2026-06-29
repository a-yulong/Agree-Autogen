# Case25 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 42.93
- Initial validation errors: 13
- Final validation errors: 13

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 13
- Warnings: 2

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 976
- completion_tokens: 801
- total_tokens: 1777

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 59: Couldn't resolve reference to SystemSubcomponentType 'heater.impl'.
2. /CaseProject/modified_model.aadl | line 60: Couldn't resolve reference to SystemSubcomponentType 'cooler.impl'.
3. /CaseProject/modified_model.aadl | line 61: Couldn't resolve reference to SystemSubcomponentType 'controller.impl'.
4. /CaseProject/modified_model.aadl | line 66: Couldn't resolve reference to ConnectionEnd 'user_request'.
5. /CaseProject/modified_model.aadl | line 67: Couldn't resolve reference to ConnectionEnd 'enabled'.
6. /CaseProject/modified_model.aadl | line 67: Couldn't resolve reference to ConnectionEnd 'heater_on'.
7. /CaseProject/modified_model.aadl | line 68: Couldn't resolve reference to ConnectionEnd 'cooler_on'.
8. /CaseProject/modified_model.aadl | line 68: Couldn't resolve reference to ConnectionEnd 'enabled'.
9. /CaseProject/modified_model.aadl | line 69: Couldn't resolve reference to ConnectionEnd 'tempin'.
10. /CaseProject/modified_model.aadl | line 81: mismatched input 'port' expecting ';'
11. /CaseProject/modified_model.aadl | line 81: no viable alternative at input ';'
12. /CaseProject/modified_model.aadl | line 82: no viable alternative at input 'port'
13. /CaseProject/modified_model.aadl | line 86: mismatched input '.' expecting ';'
