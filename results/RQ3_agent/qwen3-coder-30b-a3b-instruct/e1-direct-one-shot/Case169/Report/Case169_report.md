# Case169 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 49.16
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

- prompt_tokens: 1776
- completion_tokens: 1704
- total_tokens: 3480

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 228: mismatched input 'property' expecting 'end'
2. /CaseProject/modified_model.aadl | line 233: mismatched character ' ' expecting '>'
3. /CaseProject/modified_model.aadl | line 237: mismatched character ' ' expecting '>'
4. /CaseProject/modified_model.aadl | line 244: mismatched character ' ' expecting '>'
5. /CaseProject/modified_model.aadl | line 244: mismatched character '=' expecting '-'
6. /CaseProject/modified_model.aadl | line 244: no viable alternative at character '>'
