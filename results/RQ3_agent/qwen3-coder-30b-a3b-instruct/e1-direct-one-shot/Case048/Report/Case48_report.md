# Case48 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 36.37
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

- prompt_tokens: 699
- completion_tokens: 527
- total_tokens: 1226

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 9: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@2aa5bd48{platform:/resource/CaseProject/modified_model.aadl#Integer_Toy_Extended.Integer_Toy_Extended_public.A.agree}' must be set
2. /CaseProject/modified_model.aadl | line 9: mismatched input '{' expecting RULE_ANNEXTEXT
3. /CaseProject/modified_model.aadl | line 11: mismatched character ' ' expecting '-'
4. /CaseProject/modified_model.aadl | line 14: mismatched character ' ' expecting '-'
