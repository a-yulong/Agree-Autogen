# Case429 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 71.12
- Initial validation errors: 8
- Final validation errors: 8

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 8
- Warnings: 2

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3680
- completion_tokens: 3413
- total_tokens: 7093

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 289: Duplicate Element 'doors_int' in PublicPackageSection 'DMS_public'
2. /CaseProject/modified_model.aadl | line 301: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@120df990{platform:/resource/CaseProject/modified_model.aadl#DMS.DMS_public.doors_int.imp.agree}' must be set
3. /CaseProject/modified_model.aadl | line 301: mismatched input '{' expecting RULE_ANNEXTEXT
4. /CaseProject/modified_model.aadl | line 304: Duplicate Element 'doors_int' in PublicPackageSection 'DMS_public'
5. /CaseProject/modified_model.aadl | line 304: extraneous input ';' expecting 'end'
6. /CaseProject/modified_model.aadl | line 304: mismatched input 'system' expecting 'end'
7. /CaseProject/modified_model.aadl | line 307: mismatched input 'property' expecting 'end'
8. /CaseProject/modified_model.aadl | line 308: mismatched character ' ' expecting '>'
