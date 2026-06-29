# Case257 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 180.22
- Initial validation errors: 15
- Final validation errors: 15

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 15
- Warnings: 2

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3686
- completion_tokens: 3510
- total_tokens: 7196

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 197: Couldn't resolve reference to ThreadSubcomponentType 'doors_int.imp'.
2. /CaseProject/modified_model.aadl | line 233: Couldn't resolve reference to ConnectionEnd 'cll'.
3. /CaseProject/modified_model.aadl | line 236: Couldn't resolve reference to ConnectionEnd 'door2'.
4. /CaseProject/modified_model.aadl | line 237: Couldn't resolve reference to ConnectionEnd 'door1'.
5. /CaseProject/modified_model.aadl | line 285: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@10618775{platform:/resource/CaseProject/modified_model.aadl#DMS.DMS_public.door_handler.imp.agree}' must be set
6. /CaseProject/modified_model.aadl | line 285: mismatched input '{' expecting RULE_ANNEXTEXT
7. /CaseProject/modified_model.aadl | line 290: mismatched character ' ' expecting '>'
8. /CaseProject/modified_model.aadl | line 291: mismatched character ' ' expecting '>'
9. /CaseProject/modified_model.aadl | line 292: mismatched character ' ' expecting '>'
10. /CaseProject/modified_model.aadl | line 297: mismatched character ' ' expecting '>'
11. /CaseProject/modified_model.aadl | line 297: mismatched character '=' expecting '-'
12. /CaseProject/modified_model.aadl | line 297: no viable alternative at character '>'
13. /CaseProject/modified_model.aadl | line 298: extraneous input 'property' expecting RULE_ID
14. /CaseProject/modified_model.aadl | line 298: mismatched input ';' expecting '.'
15. /CaseProject/modified_model.aadl | line 300: missing EOF at '}'
