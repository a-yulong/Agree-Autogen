# Case227 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 55.41
- Initial validation errors: 5
- Final validation errors: 5

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 5
- Warnings: 0

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3692
- completion_tokens: 3411
- total_tokens: 7103

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 302: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexLibraryImpl@282c4da0{platform:/resource/CaseProject/modified_model.aadl#DMS.DMS_public.agree}' must be set
2. /CaseProject/modified_model.aadl | line 302: mismatched input '{' expecting RULE_ANNEXTEXT
3. /CaseProject/modified_model.aadl | line 305: mismatched character ' ' expecting '>'
4. /CaseProject/modified_model.aadl | line 305: mismatched character '=' expecting '-'
5. /CaseProject/modified_model.aadl | line 305: no viable alternative at character '>'
