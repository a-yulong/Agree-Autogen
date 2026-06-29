# Case428 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 127.22
- Initial validation errors: 7
- Final validation errors: 7

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 7
- Warnings: 1

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3678
- completion_tokens: 3427
- total_tokens: 7105

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 301: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@282c4da0{platform:/resource/CaseProject/modified_model.aadl#DMS.DMS_public.doors_int.imp.agree}' must be set
2. /CaseProject/modified_model.aadl | line 301: mismatched input '{' expecting RULE_ANNEXTEXT
3. /CaseProject/modified_model.aadl | line 305: mismatched character ' ' expecting '>'
4. /CaseProject/modified_model.aadl | line 305: no viable alternative at character '|'
5. /CaseProject/modified_model.aadl | line 306: mismatched input ';' expecting '.'
6. /CaseProject/modified_model.aadl | line 307: extraneous input '}' expecting 'end'
7. /CaseProject/modified_model.aadl | line 308: mismatched input '.' expecting ';'
