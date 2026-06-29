# Case194 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 162.96
- Initial validation errors: 13
- Final validation errors: 13

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 13
- Warnings: 2

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3690
- completion_tokens: 3358
- total_tokens: 7048

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to ThreadSubcomponentType 'doors_int.imp'.
2. /CaseProject/modified_model.aadl | line 231: Couldn't resolve reference to ConnectionEnd 'cll'.
3. /CaseProject/modified_model.aadl | line 234: Couldn't resolve reference to ConnectionEnd 'door2'.
4. /CaseProject/modified_model.aadl | line 235: Couldn't resolve reference to ConnectionEnd 'door1'.
5. /CaseProject/modified_model.aadl | line 283: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@5882b202{platform:/resource/CaseProject/modified_model.aadl#DMS.DMS_public.door_handler.imp.agree}' must be set
6. /CaseProject/modified_model.aadl | line 283: mismatched input '{' expecting RULE_ANNEXTEXT
7. /CaseProject/modified_model.aadl | line 284: mismatched input 'properties' expecting 'end'
8. /CaseProject/modified_model.aadl | line 285: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'D1_engine_running'. For classifier references use classifier( <ref> ).
9. /CaseProject/modified_model.aadl | line 285: Couldn't resolve reference to property definition 'D1_ecam_info'. Property set name may be missing.
10. /CaseProject/modified_model.aadl | line 285: mismatched character ' ' expecting '>'
11. /CaseProject/modified_model.aadl | line 285: missing '=>' at 'D1_engine_running'
12. /CaseProject/modified_model.aadl | line 286: mismatched input 'properties' expecting RULE_ID
13. /CaseProject/modified_model.aadl | line 287: missing EOF at '}'
