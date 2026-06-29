# Case436 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 41.98
- Initial validation errors: 1
- Final validation errors: 1

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 1
- Warnings: 0

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 1064
- completion_tokens: 875
- total_tokens: 1939

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 31: Couldn't resolve reference to property definition 'Agree_Assertions'. Property set name may be missing.
