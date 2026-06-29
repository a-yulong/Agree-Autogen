# Case164 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 75.67
- Initial validation errors: 2
- Final validation errors: 2

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 2
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
- completion_tokens: 1721
- total_tokens: 3497

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 225: missing 'end' at 'verify'
2. /CaseProject/modified_model.aadl | line 226: mismatched input 'component' expecting ';'
