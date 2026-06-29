# Case430 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 108.04
- Initial validation errors: 5
- Final validation errors: 5

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 5
- Warnings: 2

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3679
- completion_tokens: 3451
- total_tokens: 7130

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 301: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@2baac4a7{platform:/resource/CaseProject/modified_model.aadl#DMS.DMS_public.doors_int.imp.agree}' must be set
2. /CaseProject/modified_model.aadl | line 301: mismatched input '{' expecting RULE_ANNEXTEXT
3. /CaseProject/modified_model.aadl | line 308: mismatched input ';' expecting '.'
4. /CaseProject/modified_model.aadl | line 309: mismatched input 'package' expecting RULE_ID
5. /CaseProject/modified_model.aadl | line 310: missing EOF at 'end'
