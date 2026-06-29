# Case166 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 73.42
- Initial validation errors: 4
- Final validation errors: 4

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 4
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
- completion_tokens: 1604
- total_tokens: 3378

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 225: missing 'end' at 'verify'
2. /CaseProject/modified_model.aadl | line 226: mismatched character '=' expecting '-'
3. /CaseProject/modified_model.aadl | line 226: mismatched input 'property' expecting ';'
4. /CaseProject/modified_model.aadl | line 226: no viable alternative at character '|'
