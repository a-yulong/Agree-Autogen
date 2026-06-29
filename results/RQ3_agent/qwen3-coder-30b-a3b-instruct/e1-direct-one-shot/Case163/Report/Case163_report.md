# Case163 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 47.07
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
- completion_tokens: 1632
- total_tokens: 3412

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 225: mismatched input 'thr_throttle_simulation' expecting ';'
2. /CaseProject/modified_model.aadl | line 225: missing 'end' at 'verify'
3. /CaseProject/modified_model.aadl | line 228: mismatched character ' ' expecting '>'
4. /CaseProject/modified_model.aadl | line 228: mismatched character '=' expecting '-'
5. /CaseProject/modified_model.aadl | line 228: no viable alternative at character '>'
