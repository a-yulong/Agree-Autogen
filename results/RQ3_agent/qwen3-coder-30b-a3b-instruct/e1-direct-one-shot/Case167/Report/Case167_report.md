# Case167 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 73.54
- Initial validation errors: 9
- Final validation errors: 9

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 9
- Warnings: 2

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 1780
- completion_tokens: 1634
- total_tokens: 3414

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 225: missing 'end' at 'verify'
2. /CaseProject/modified_model.aadl | line 226: mismatched input 'property' expecting ';'
3. /CaseProject/modified_model.aadl | line 227: no viable alternative at character '|'
4. /CaseProject/modified_model.aadl | line 228: mismatched character ' ' expecting '>'
5. /CaseProject/modified_model.aadl | line 228: mismatched character '=' expecting '-'
6. /CaseProject/modified_model.aadl | line 228: no viable alternative at character '>'
7. /CaseProject/modified_model.aadl | line 230: mismatched character ' ' expecting '>'
8. /CaseProject/modified_model.aadl | line 230: mismatched character '=' expecting '-'
9. /CaseProject/modified_model.aadl | line 230: no viable alternative at character '>'
