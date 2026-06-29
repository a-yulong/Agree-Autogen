# Case13 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 66.46
- Initial validation errors: 10
- Final validation errors: 10

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 10
- Warnings: 1

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 2064
- completion_tokens: 1956
- total_tokens: 4020

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 30: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@230232b0{platform:/resource/CaseProject/modified_model.aadl#AviateControlLevel.AviateControlLevel_public.GCAS_Monitor.GCAS_Monitor_impl.agree}' must be set
2. /CaseProject/modified_model.aadl | line 30: mismatched input '{' expecting RULE_ANNEXTEXT
3. /CaseProject/modified_model.aadl | line 32: mismatched character ' ' expecting '>'
4. /CaseProject/modified_model.aadl | line 33: mismatched character ' ' expecting '>'
5. /CaseProject/modified_model.aadl | line 36: mismatched character ' ' expecting '>'
6. /CaseProject/modified_model.aadl | line 39: mismatched character ' ' expecting '>'
7. /CaseProject/modified_model.aadl | line 39: mismatched character '=' expecting '-'
8. /CaseProject/modified_model.aadl | line 42: mismatched character ' ' expecting '>'
9. /CaseProject/modified_model.aadl | line 45: mismatched character ' ' expecting '>'
10. /CaseProject/modified_model.aadl | line 46: mismatched character ' ' expecting '>'
