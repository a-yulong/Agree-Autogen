# Case358 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 60.72
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

- prompt_tokens: 4566
- completion_tokens: 2921
- total_tokens: 7487

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 262: Couldn't resolve reference to property definition 'Agree_Lemma'. Property set name may be missing.
2. /CaseProject/modified_model.aadl | line 265: mismatched input '.' expecting ';'
