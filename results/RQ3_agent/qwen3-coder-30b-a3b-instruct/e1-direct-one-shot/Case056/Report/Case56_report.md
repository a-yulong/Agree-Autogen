# Case56 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 43.77
- Initial validation errors: 4
- Final validation errors: 4

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 4
- Warnings: 0

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 576
- completion_tokens: 419
- total_tokens: 995

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 45: Assume statements are allowed only in component types
2. /CaseProject/modified_model.aadl | line 45: mismatched input '<' expecting RULE_STRING
3. /CaseProject/modified_model.aadl | line 48: Guarantee statements are allowed only in component types
4. /CaseProject/modified_model.aadl | line 48: mismatched input '<' expecting RULE_STRING
