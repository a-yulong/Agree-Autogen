# Case248 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 51.46
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

- prompt_tokens: 3682
- completion_tokens: 3416
- total_tokens: 7098

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 282: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@5882b202{platform:/resource/CaseProject/modified_model.aadl#DMS.DMS_public.door_handler.imp.AGREE}' must be set
2. /CaseProject/modified_model.aadl | line 282: mismatched input '{' expecting RULE_ANNEXTEXT
3. /CaseProject/modified_model.aadl | line 286: mismatched character ' ' expecting '>'
4. /CaseProject/modified_model.aadl | line 288: mismatched character ' ' expecting '>'
