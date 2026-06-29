# Case29 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 40.28
- Initial validation errors: 6
- Final validation errors: 6

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 6
- Warnings: 3

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 885
- completion_tokens: 193
- total_tokens: 1078

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 9: Couldn't resolve reference to DataSubcomponentType 'real'.
2. /CaseProject/modified_model.aadl | line 14: missing EOF at 'var'
3. /CaseProject/modified_model.aadl | line 18: mismatched character '<EOF>' expecting '''
4. /CaseProject/modified_model.aadl | line 23: mismatched input 'features' expecting 'end'
5. /CaseProject/modified_model.aadl | line 24: no viable alternative at input 'port'
6. /CaseProject/modified_model.aadl | line 25: mismatched input '.' expecting ';'
