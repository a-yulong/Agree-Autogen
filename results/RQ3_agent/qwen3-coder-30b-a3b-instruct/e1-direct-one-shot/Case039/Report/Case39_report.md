# Case39 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 29.58
- Initial validation errors: 14
- Final validation errors: 14

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 14
- Warnings: 10

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 1368
- completion_tokens: 415
- total_tokens: 1783

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 24: missing 'end' at 'components'
2. /CaseProject/modified_model.aadl | line 25: mismatched input ':' expecting ';'
3. /CaseProject/modified_model.aadl | line 25: mismatched input '::' expecting 'end'
4. /CaseProject/modified_model.aadl | line 25: missing '.' at 'previous_actual'
5. /CaseProject/modified_model.aadl | line 26: Duplicate Element 'Base_Types' in PublicPackageSection 'Transmission_public'
6. /CaseProject/modified_model.aadl | line 26: mismatched input '::' expecting 'end'
7. /CaseProject/modified_model.aadl | line 27: Duplicate Element 'Base_Types' in PublicPackageSection 'Transmission_public'
8. /CaseProject/modified_model.aadl | line 27: mismatched input '::' expecting 'end'
9. /CaseProject/modified_model.aadl | line 28: Duplicate Element 'Base_Types' in PublicPackageSection 'Transmission_public'
10. /CaseProject/modified_model.aadl | line 28: mismatched input '::' expecting 'end'
11. /CaseProject/modified_model.aadl | line 35: mismatched character ' ' expecting '>'
12. /CaseProject/modified_model.aadl | line 36: mismatched character ' ' expecting '>'
13. /CaseProject/modified_model.aadl | line 38: mismatched character ' ' expecting '>'
14. /CaseProject/modified_model.aadl | line 40: missing EOF at 'end'
