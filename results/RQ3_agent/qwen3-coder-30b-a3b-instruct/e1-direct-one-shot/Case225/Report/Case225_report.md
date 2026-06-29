# Case225 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 178.38
- Initial validation errors: 17
- Final validation errors: 17

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 17
- Warnings: 1

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3681
- completion_tokens: 3380
- total_tokens: 7061

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 197: Couldn't resolve reference to ThreadSubcomponentType 'doors_int.imp'.
2. /CaseProject/modified_model.aadl | line 233: Couldn't resolve reference to ConnectionEnd 'cll'.
3. /CaseProject/modified_model.aadl | line 236: Couldn't resolve reference to ConnectionEnd 'door2'.
4. /CaseProject/modified_model.aadl | line 237: Couldn't resolve reference to ConnectionEnd 'door1'.
5. /CaseProject/modified_model.aadl | line 285: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@6ef4cbe1{platform:/resource/CaseProject/modified_model.aadl#DMS.DMS_public.door_handler.imp.agree}' must be set
6. /CaseProject/modified_model.aadl | line 285: mismatched input '{' expecting RULE_ANNEXTEXT
7. /CaseProject/modified_model.aadl | line 286: mismatched input 'properties' expecting 'end'
8. /CaseProject/modified_model.aadl | line 287: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'in_flight'. For classifier references use classifier( <ref> ).
9. /CaseProject/modified_model.aadl | line 287: Couldn't resolve reference to property definition 'Assert'. Property set name may be missing.
10. /CaseProject/modified_model.aadl | line 287: Couldn't resolve reference to property definition 'ecam_info'. Property set name may be missing.
11. /CaseProject/modified_model.aadl | line 287: Couldn't resolve reference to property definition 'whenever'. Property set name may be missing.
12. /CaseProject/modified_model.aadl | line 287: The required feature 'ownedValue' of 'org.osate.aadl2.impl.ModalPropertyValueImpl@441d3ddf{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPropertyAssociation.1/@ownedValue.0}' must be set
13. /CaseProject/modified_model.aadl | line 287: The required feature 'ownedValue' of 'org.osate.aadl2.impl.ModalPropertyValueImpl@65689000{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPropertyAssociation.0/@ownedValue.0}' must be set
14. /CaseProject/modified_model.aadl | line 287: missing '=>' at 'ecam_info'
15. /CaseProject/modified_model.aadl | line 287: missing '=>' at 'in_flight'
16. /CaseProject/modified_model.aadl | line 287: missing '=>' at 'whenever'
17. /CaseProject/modified_model.aadl | line 288: mismatched input '}' expecting 'end'
