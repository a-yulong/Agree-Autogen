# Case34 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 86.78
- Initial validation errors: 7
- Final validation errors: 7

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 7
- Warnings: 3

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 1907
- completion_tokens: 6184
- total_tokens: 8091

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 156: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@54247647{platform:/resource/CaseProject/modified_model.aadl#tcas.tcas_public.ResponseSelection.impl.agree}' must be set
2. /CaseProject/modified_model.aadl | line 156: mismatched input '{' expecting RULE_ANNEXTEXT
3. /CaseProject/modified_model.aadl | line 169: mismatched character ' ' expecting '>'
4. /CaseProject/modified_model.aadl | line 170: mismatched character ' ' expecting '>'
5. /CaseProject/modified_model.aadl | line 171: mismatched character ' ' expecting '>'
6. /CaseProject/modified_model.aadl | line 172: mismatched character ' ' expecting '>'
7. /CaseProject/modified_model.aadl | line 533: mismatched input '<EOF>' expecting 'end'
