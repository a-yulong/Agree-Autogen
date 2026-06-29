# Case302 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 96.33
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

- prompt_tokens: 4589
- completion_tokens: 2854
- total_tokens: 7443

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 275: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'P_Input'. For classifier references use classifier( <ref> ).
2. /CaseProject/modified_model.aadl | line 275: Couldn't resolve reference to property definition 'AGREE_Bounded_Input'. Property set name may be missing.
