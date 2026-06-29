# Case209 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 61.83
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

- prompt_tokens: 3686
- completion_tokens: 3421
- total_tokens: 7107

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 197: Couldn't resolve reference to ThreadSubcomponentType 'doors_int.imp'.
2. /CaseProject/modified_model.aadl | line 233: Couldn't resolve reference to ConnectionEnd 'cll'.
3. /CaseProject/modified_model.aadl | line 236: Couldn't resolve reference to ConnectionEnd 'door2'.
4. /CaseProject/modified_model.aadl | line 237: Couldn't resolve reference to ConnectionEnd 'door1'.
5. /CaseProject/modified_model.aadl | line 285: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@6bce4140{platform:/resource/CaseProject/modified_model.aadl#DMS.DMS_public.door_handler.imp.agree}' must be set
6. /CaseProject/modified_model.aadl | line 285: mismatched input '{' expecting RULE_ANNEXTEXT
7. /CaseProject/modified_model.aadl | line 286: mismatched input 'properties' expecting 'end'
8. /CaseProject/modified_model.aadl | line 289: Couldn't resolve reference to property definition 'Bounded_Input_DPS'. Property set name may be missing.
9. /CaseProject/modified_model.aadl | line 289: Couldn't resolve reference to property definition 'Integer'. Property set name may be missing.
10. /CaseProject/modified_model.aadl | line 289: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@10618775{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPropertyAssociation.0}' with 0 values must have at least 1 values
11. /CaseProject/modified_model.aadl | line 289: mismatched character ' ' expecting '>'
12. /CaseProject/modified_model.aadl | line 289: mismatched input ':' expecting '=>'
13. /CaseProject/modified_model.aadl | line 289: missing '=>' at '0'
14. /CaseProject/modified_model.aadl | line 291: missing EOF at '}'
