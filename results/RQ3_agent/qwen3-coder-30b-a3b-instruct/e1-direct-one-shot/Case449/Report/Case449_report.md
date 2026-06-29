# Case449 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 61.31
- Initial validation errors: 5
- Final validation errors: 5

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 2
- AGREE errors: 3
- Warnings: 19

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 14142
- completion_tokens: 728
- total_tokens: 14870

## Final Diagnostics

1. flyByWire_hard (identifier) is not a package or a property set visible or existing
2. Cannot analyze AADL specifications
3. /CaseProject/modified_model.aadl | line 44: Couldn't resolve reference to property definition 'Agree_Lemma'. Property set name may be missing.
4. /CaseProject/modified_model.aadl | line 45: Couldn't resolve reference to property definition 'Agree_Guarantee'. Property set name may be missing.
5. /CaseProject/modified_model.aadl | line 48: missing EOF at 'device'
