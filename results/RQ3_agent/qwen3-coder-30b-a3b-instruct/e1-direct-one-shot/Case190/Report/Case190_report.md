# Case190 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 184.48
- Initial validation errors: 21
- Final validation errors: 21

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 21
- Warnings: 1

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3692
- completion_tokens: 3365
- total_tokens: 7057

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to ThreadSubcomponentType 'doors_int.imp'.
2. /CaseProject/modified_model.aadl | line 231: Couldn't resolve reference to ConnectionEnd 'cll'.
3. /CaseProject/modified_model.aadl | line 234: Couldn't resolve reference to ConnectionEnd 'door2'.
4. /CaseProject/modified_model.aadl | line 235: Couldn't resolve reference to ConnectionEnd 'door1'.
5. /CaseProject/modified_model.aadl | line 282: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@282c4da0{platform:/resource/CaseProject/modified_model.aadl#DMS.DMS_public.door_handler.imp.agree}' must be set
6. /CaseProject/modified_model.aadl | line 282: mismatched input '{' expecting RULE_ANNEXTEXT
7. /CaseProject/modified_model.aadl | line 283: mismatched input 'properties' expecting 'end'
8. /CaseProject/modified_model.aadl | line 284: Couldn't resolve reference to property definition 'Bounded_Input'. Property set name may be missing.
9. /CaseProject/modified_model.aadl | line 284: Couldn't resolve reference to property definition 'D1_dps'. Property set name may be missing.
10. /CaseProject/modified_model.aadl | line 284: Couldn't resolve reference to property definition 'and'. Property set name may be missing.
11. /CaseProject/modified_model.aadl | line 284: The required feature 'ownedValue' of 'org.osate.aadl2.impl.ModalPropertyValueImpl@3eb6d7a9{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPropertyAssociation.2/@ownedValue.0}' must be set
12. /CaseProject/modified_model.aadl | line 284: The required feature 'ownedValue' of 'org.osate.aadl2.impl.ModalPropertyValueImpl@54af9cce{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPropertyAssociation.0/@ownedValue.0}' must be set
13. /CaseProject/modified_model.aadl | line 284: The required feature 'ownedValue' of 'org.osate.aadl2.impl.ModalPropertyValueImpl@683218c8{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPropertyAssociation.1/@ownedValue.0}' must be set
14. /CaseProject/modified_model.aadl | line 284: mismatched character ' ' expecting '>'
15. /CaseProject/modified_model.aadl | line 284: mismatched character '=' expecting '-'
16. /CaseProject/modified_model.aadl | line 284: missing '=>' at '0'
17. /CaseProject/modified_model.aadl | line 284: missing '=>' at '100'
18. /CaseProject/modified_model.aadl | line 284: missing '=>' at 'D1_dps'
19. /CaseProject/modified_model.aadl | line 284: no viable alternative at character '>'
20. /CaseProject/modified_model.aadl | line 284: no viable alternative at input '0'
21. /CaseProject/modified_model.aadl | line 285: mismatched input '}' expecting 'end'
