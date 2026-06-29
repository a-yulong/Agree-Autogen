# Case402 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 46.20
- Initial validation errors: 1
- Final validation errors: 1

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 1
- Warnings: 8

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3840
- completion_tokens: 1360
- total_tokens: 5200

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 152: Couldn't resolve reference to property definition 'agree_contract'. Property set name may be missing.
