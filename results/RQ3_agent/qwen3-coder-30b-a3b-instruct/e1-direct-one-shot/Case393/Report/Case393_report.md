# Case393 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 43.13
- Initial validation errors: 2
- Final validation errors: 2

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 2
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
- completion_tokens: 1358
- total_tokens: 5198

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 136: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Alpha3'. For classifier references use classifier( <ref> ).
2. /CaseProject/modified_model.aadl | line 136: Couldn't resolve reference to property definition 'AGREE::Bound'.
