# Case139 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 44.65
- Initial validation errors: 6
- Final validation errors: 6

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 6
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
- completion_tokens: 1653
- total_tokens: 3433

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 225: missing 'end' at 'verify'
2. /CaseProject/modified_model.aadl | line 226: mismatched input 'property' expecting ';'
3. /CaseProject/modified_model.aadl | line 229: mismatched character ' ' expecting '>'
4. /CaseProject/modified_model.aadl | line 229: mismatched character '=' expecting '-'
5. /CaseProject/modified_model.aadl | line 229: no viable alternative at character '>'
6. /CaseProject/modified_model.aadl | line 229: no viable alternative at character '|'
