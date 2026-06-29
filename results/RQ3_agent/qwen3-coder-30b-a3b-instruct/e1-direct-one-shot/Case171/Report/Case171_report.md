# Case171 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 94.41
- Initial validation errors: 5
- Final validation errors: 5

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 5
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
- completion_tokens: 1624
- total_tokens: 3404

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 225: missing 'end' at 'verify'
2. /CaseProject/modified_model.aadl | line 226: mismatched input 'component' expecting ';'
3. /CaseProject/modified_model.aadl | line 228: no viable alternative at character '|'
4. /CaseProject/modified_model.aadl | line 228: required (...)+ loop did not match anything at character '.'
5. /CaseProject/modified_model.aadl | line 229: mismatched character ' ' expecting '>'
