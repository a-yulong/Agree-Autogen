# Case37 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 50.73
- Initial validation errors: 8
- Final validation errors: 8

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 8
- Warnings: 5

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 1414
- completion_tokens: 448
- total_tokens: 1862

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 15: missing 'end' at 'components'
2. /CaseProject/modified_model.aadl | line 16: mismatched character ' ' expecting '>'
3. /CaseProject/modified_model.aadl | line 16: mismatched input ':' expecting ';'
4. /CaseProject/modified_model.aadl | line 16: missing '.' at 'P'
5. /CaseProject/modified_model.aadl | line 17: mismatched character ' ' expecting '>'
6. /CaseProject/modified_model.aadl | line 18: mismatched character ' ' expecting '>'
7. /CaseProject/modified_model.aadl | line 25: Couldn't resolve reference to property definition 'AGREE::AGREE_Laws'.
8. /CaseProject/modified_model.aadl | line 27: mismatched input '"e_int' = e"' expecting 'end'
