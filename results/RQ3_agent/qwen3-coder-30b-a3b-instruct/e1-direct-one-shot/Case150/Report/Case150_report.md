# Case150 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 51.00
- Initial validation errors: 7
- Final validation errors: 7

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 7
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
- completion_tokens: 1705
- total_tokens: 3479

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 228: mismatched input 'property' expecting 'end'
2. /CaseProject/modified_model.aadl | line 247: mismatched character ' ' expecting '>'
3. /CaseProject/modified_model.aadl | line 247: mismatched character '=' expecting '-'
4. /CaseProject/modified_model.aadl | line 247: no viable alternative at character '>'
5. /CaseProject/modified_model.aadl | line 248: mismatched character ' ' expecting '>'
6. /CaseProject/modified_model.aadl | line 248: mismatched character '=' expecting '-'
7. /CaseProject/modified_model.aadl | line 248: no viable alternative at character '>'
