# Case18 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 63.26
- Initial validation errors: 11
- Final validation errors: 11

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 11
- Warnings: 3

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 2057
- completion_tokens: 3132
- total_tokens: 5189

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 117: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@6ef4cbe1{platform:/resource/CaseProject/modified_model.aadl#AviateControlLevel.AviateControlLevel_public.GCAS_Recovery.GCAS_Recovery_impl.agree}' must be set
2. /CaseProject/modified_model.aadl | line 117: mismatched input '{' expecting RULE_ANNEXTEXT
3. /CaseProject/modified_model.aadl | line 122: mismatched character ' ' expecting '>'
4. /CaseProject/modified_model.aadl | line 122: mismatched character '=' expecting '-'
5. /CaseProject/modified_model.aadl | line 122: no viable alternative at character '>'
6. /CaseProject/modified_model.aadl | line 123: mismatched character ' ' expecting '>'
7. /CaseProject/modified_model.aadl | line 123: mismatched character '=' expecting '-'
8. /CaseProject/modified_model.aadl | line 123: no viable alternative at character '>'
9. /CaseProject/modified_model.aadl | line 126: mismatched character ' ' expecting '>'
10. /CaseProject/modified_model.aadl | line 129: no viable alternative at character '>'
11. /CaseProject/modified_model.aadl | line 261: mismatched input '<EOF>' expecting 'end'
