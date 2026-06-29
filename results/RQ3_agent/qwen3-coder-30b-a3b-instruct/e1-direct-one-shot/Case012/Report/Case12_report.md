# Case12 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 63.03
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

- prompt_tokens: 2066
- completion_tokens: 1898
- total_tokens: 3964

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 30: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@4975dda1{platform:/resource/CaseProject/modified_model.aadl#AviateControlLevel.AviateControlLevel_public.GCAS_Monitor.GCAS_Monitor_impl.agree}' must be set
2. /CaseProject/modified_model.aadl | line 30: mismatched input '{' expecting RULE_ANNEXTEXT
3. /CaseProject/modified_model.aadl | line 32: mismatched character ' ' expecting '>'
4. /CaseProject/modified_model.aadl | line 32: mismatched character '=' expecting '-'
5. /CaseProject/modified_model.aadl | line 35: mismatched character '=' expecting '-'
6. /CaseProject/modified_model.aadl | line 38: mismatched character ' ' expecting '>'
7. /CaseProject/modified_model.aadl | line 41: mismatched character ' ' expecting '>'
