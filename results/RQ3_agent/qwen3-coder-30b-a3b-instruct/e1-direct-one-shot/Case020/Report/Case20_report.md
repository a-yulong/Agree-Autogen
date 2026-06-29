# Case20 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 53.99
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

- prompt_tokens: 1062
- completion_tokens: 877
- total_tokens: 1939

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 30: no viable alternative at input 'variable'
2. /CaseProject/modified_model.aadl | line 31: mismatched input '.' expecting ';'
