# Case142 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 63.60
- Initial validation errors: 3
- Final validation errors: 3

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 3
- Warnings: 3

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 1774
- completion_tokens: 3284
- total_tokens: 5058

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 225: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexLibraryImpl@401e02b4{platform:/resource/CaseProject/modified_model.aadl#Ardupilot_Software.Ardupilot_Software_public.agree}' must be set
2. /CaseProject/modified_model.aadl | line 225: mismatched input '{' expecting RULE_ANNEXTEXT
3. /CaseProject/modified_model.aadl | line 329: no viable alternative at input '<EOF>'
