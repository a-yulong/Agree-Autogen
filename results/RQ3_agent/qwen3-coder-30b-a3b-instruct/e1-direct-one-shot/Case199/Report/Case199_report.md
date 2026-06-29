# Case199 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 61.10
- Initial validation errors: 14
- Final validation errors: 14

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 14
- Warnings: 2

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3687
- completion_tokens: 3429
- total_tokens: 7116

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 197: Couldn't resolve reference to ThreadSubcomponentType 'doors_int.imp'.
2. /CaseProject/modified_model.aadl | line 233: Couldn't resolve reference to ConnectionEnd 'cll'.
3. /CaseProject/modified_model.aadl | line 236: Couldn't resolve reference to ConnectionEnd 'door2'.
4. /CaseProject/modified_model.aadl | line 237: Couldn't resolve reference to ConnectionEnd 'door1'.
5. /CaseProject/modified_model.aadl | line 285: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@5882b202{platform:/resource/CaseProject/modified_model.aadl#DMS.DMS_public.door_handler.imp.agree}' must be set
6. /CaseProject/modified_model.aadl | line 285: mismatched input '{' expecting RULE_ANNEXTEXT
7. /CaseProject/modified_model.aadl | line 286: mismatched input 'properties' expecting 'end'
8. /CaseProject/modified_model.aadl | line 289: Couldn't resolve reference to property definition 'ecam_info'. Property set name may be missing.
9. /CaseProject/modified_model.aadl | line 289: mismatched character ' ' expecting '>'
10. /CaseProject/modified_model.aadl | line 289: missing '=>' at '('
11. /CaseProject/modified_model.aadl | line 289: no viable alternative at character '>'
12. /CaseProject/modified_model.aadl | line 289: no viable alternative at input '0'
13. /CaseProject/modified_model.aadl | line 290: mismatched input 'properties' expecting RULE_ID
14. /CaseProject/modified_model.aadl | line 291: missing EOF at '}'
