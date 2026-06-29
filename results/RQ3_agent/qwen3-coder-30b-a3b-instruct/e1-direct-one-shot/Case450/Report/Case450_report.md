# Case450 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 55.84
- Initial validation errors: 3
- Final validation errors: 3

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 2
- AGREE errors: 1
- Warnings: 16

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 14144
- completion_tokens: 663
- total_tokens: 14807

## Final Diagnostics

1. flyByWire_hard (identifier) is not a package or a property set visible or existing
2. Cannot analyze AADL specifications
3. /CaseProject/modified_model.aadl | line 75: Couldn't resolve reference to property definition 'Agree_Code'. Property set name may be missing.
