# Case136 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 45.59
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

- prompt_tokens: 1776
- completion_tokens: 1602
- total_tokens: 3378

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 225: mismatched input 'thr_yaw_simulation' expecting ';'
2. /CaseProject/modified_model.aadl | line 225: missing 'end' at 'verify'
3. /CaseProject/modified_model.aadl | line 227: no viable alternative at character '|'
4. /CaseProject/modified_model.aadl | line 227: required (...)+ loop did not match anything at character '.'
