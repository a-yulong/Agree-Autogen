# Case17 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 53.26
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

- prompt_tokens: 2110
- completion_tokens: 2033
- total_tokens: 4143

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 99: missing 'end' at 'agree_nodes'
2. /CaseProject/modified_model.aadl | line 100: mismatched input ':' expecting ';'
3. /CaseProject/modified_model.aadl | line 100: missing '.' at 'numberServicesTrue'
4. /CaseProject/modified_model.aadl | line 106: mismatched character ' ' expecting '>'
5. /CaseProject/modified_model.aadl | line 115: mismatched character ' ' expecting '>'
6. /CaseProject/modified_model.aadl | line 116: no viable alternative at character '>'
7. /CaseProject/modified_model.aadl | line 117: mismatched character ' ' expecting '>'
8. /CaseProject/modified_model.aadl | line 117: no viable alternative at character '>'
9. /CaseProject/modified_model.aadl | line 123: mismatched character ' ' expecting '>'
10. /CaseProject/modified_model.aadl | line 126: mismatched character ' ' expecting '>'
11. /CaseProject/modified_model.aadl | line 127: mismatched character ' ' expecting '>'
12. /CaseProject/modified_model.aadl | line 127: no viable alternative at character '>'
13. /CaseProject/modified_model.aadl | line 133: mismatched character ' ' expecting '>'
14. /CaseProject/modified_model.aadl | line 134: mismatched input '.' expecting ';'
