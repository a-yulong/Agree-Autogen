# Case172 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 96.51
- Initial validation errors: 3
- Final validation errors: 3

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 3
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
- completion_tokens: 1591
- total_tokens: 3367

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 227: Property statement 'angle_bounded' is of type 'ErrorTypeDef' but must be of type 'bool'
2. /CaseProject/modified_model.aadl | line 227: Property statments are allowed only in component annexes
3. /CaseProject/modified_model.aadl | line 227: mismatched input ':' expecting '='
