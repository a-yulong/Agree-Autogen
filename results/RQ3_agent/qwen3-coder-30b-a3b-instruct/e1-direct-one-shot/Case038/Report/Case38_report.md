# Case38 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 43.60
- Initial validation errors: 10
- Final validation errors: 10

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 10
- Warnings: 4

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 1432
- completion_tokens: 475
- total_tokens: 1907

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 15: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@4a1dda83{platform:/resource/CaseProject/modified_model.aadl#Transmission.Transmission_public.Speed_Control.Speed_Control_Impl.agree}' must be set
2. /CaseProject/modified_model.aadl | line 15: mismatched input '{' expecting RULE_ANNEXTEXT
3. /CaseProject/modified_model.aadl | line 17: mismatched character ' ' expecting '>'
4. /CaseProject/modified_model.aadl | line 18: mismatched character ' ' expecting '>'
5. /CaseProject/modified_model.aadl | line 19: mismatched character ' ' expecting '>'
6. /CaseProject/modified_model.aadl | line 26: mismatched character ' ' expecting '>'
7. /CaseProject/modified_model.aadl | line 29: mismatched character ' ' expecting '>'
8. /CaseProject/modified_model.aadl | line 32: mismatched character ' ' expecting '>'
9. /CaseProject/modified_model.aadl | line 35: mismatched character ' ' expecting '>'
10. /CaseProject/modified_model.aadl | line 38: mismatched character ' ' expecting '>'
