# Case143 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 46.10
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

- prompt_tokens: 1780
- completion_tokens: 1631
- total_tokens: 3411

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 149: Duplicate Element 'thr_throttle_simulation.i' in PublicPackageSection 'Ardupilot_Software_public'
2. /CaseProject/modified_model.aadl | line 225: Duplicate Element 'thr_throttle_simulation.i' in PublicPackageSection 'Ardupilot_Software_public'
3. /CaseProject/modified_model.aadl | line 227: Couldn't resolve reference to property definition 'Agree::Assumptions'.
4. /CaseProject/modified_model.aadl | line 228: Couldn't resolve reference to property definition 'Agree::Guarantees'.
