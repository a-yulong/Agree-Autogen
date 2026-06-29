# Case267 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 55.89
- Initial validation errors: 3
- Final validation errors: 3

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 3
- Warnings: 0

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3689
- completion_tokens: 3349
- total_tokens: 7038

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 275: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@120df990{platform:/resource/CaseProject/modified_model.aadl#DMS.DMS_public.door_handler.imp.AGREE}' must be set
2. /CaseProject/modified_model.aadl | line 275: mismatched input '{' expecting RULE_ANNEXTEXT
3. /CaseProject/modified_model.aadl | line 279: mismatched character ' ' expecting '>'
