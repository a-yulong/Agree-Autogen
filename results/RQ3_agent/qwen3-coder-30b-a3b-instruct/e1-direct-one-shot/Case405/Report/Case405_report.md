# Case405 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 61.31
- Initial validation errors: 12
- Final validation errors: 12

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 2
- AGREE errors: 10
- Warnings: 6

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 6794
- completion_tokens: 1761
- total_tokens: 8555

## Final Diagnostics

1. Ardupilot_Software (identifier) is not a package or a property set visible or existing
2. Cannot analyze AADL specifications
3. /CaseProject/modified_model.aadl | line 228: mismatched input 'property' expecting 'end'
4. /CaseProject/modified_model.aadl | line 248: mismatched character ' ' expecting '>'
5. /CaseProject/modified_model.aadl | line 249: mismatched character ' ' expecting '>'
6. /CaseProject/modified_model.aadl | line 252: mismatched character ' ' expecting '>'
7. /CaseProject/modified_model.aadl | line 252: mismatched character '=' expecting '-'
8. /CaseProject/modified_model.aadl | line 252: no viable alternative at character '>'
9. /CaseProject/modified_model.aadl | line 252: no viable alternative at character '|'
10. /CaseProject/modified_model.aadl | line 253: mismatched character ' ' expecting '>'
11. /CaseProject/modified_model.aadl | line 253: mismatched character '=' expecting '-'
12. /CaseProject/modified_model.aadl | line 253: no viable alternative at character '>'
