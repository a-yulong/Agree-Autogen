# Case215 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 151.22
- Initial validation errors: 11
- Final validation errors: 11

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 11
- Warnings: 2

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3692
- completion_tokens: 3397
- total_tokens: 7089

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 197: Couldn't resolve reference to ThreadSubcomponentType 'doors_int.imp'.
2. /CaseProject/modified_model.aadl | line 233: Couldn't resolve reference to ConnectionEnd 'cll'.
3. /CaseProject/modified_model.aadl | line 236: Couldn't resolve reference to ConnectionEnd 'door2'.
4. /CaseProject/modified_model.aadl | line 237: Couldn't resolve reference to ConnectionEnd 'door1'.
5. /CaseProject/modified_model.aadl | line 284: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@1e92c3b6{platform:/resource/CaseProject/modified_model.aadl#DMS.DMS_public.door_handler.imp.agree}' must be set
6. /CaseProject/modified_model.aadl | line 284: mismatched input '{' expecting RULE_ANNEXTEXT
7. /CaseProject/modified_model.aadl | line 285: mismatched input 'properties' expecting 'end'
8. /CaseProject/modified_model.aadl | line 286: Couldn't resolve reference to property definition 'Bounded_Input'. Property set name may be missing.
9. /CaseProject/modified_model.aadl | line 287: Couldn't resolve reference to property definition 'Input_Bounds'. Property set name may be missing.
10. /CaseProject/modified_model.aadl | line 287: mismatched input ',' expecting ';'
11. /CaseProject/modified_model.aadl | line 289: missing EOF at '}'
