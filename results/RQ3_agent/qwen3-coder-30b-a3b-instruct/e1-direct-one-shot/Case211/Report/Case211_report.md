# Case211 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 62.92
- Initial validation errors: 26
- Final validation errors: 26

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 26
- Warnings: 1

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3687
- completion_tokens: 3498
- total_tokens: 7185

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 197: Couldn't resolve reference to ThreadSubcomponentType 'doors_int.imp'.
2. /CaseProject/modified_model.aadl | line 233: Couldn't resolve reference to ConnectionEnd 'cll'.
3. /CaseProject/modified_model.aadl | line 236: Couldn't resolve reference to ConnectionEnd 'door2'.
4. /CaseProject/modified_model.aadl | line 237: Couldn't resolve reference to ConnectionEnd 'door1'.
5. /CaseProject/modified_model.aadl | line 286: Couldn't resolve reference to property definition 'agree_node'. Property set name may be missing.
6. /CaseProject/modified_model.aadl | line 286: Couldn't resolve reference to property definition 'ecam_info_derivation'. Property set name may be missing.
7. /CaseProject/modified_model.aadl | line 286: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@15371de2{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.3}' with 0 values must have at least 1 values
8. /CaseProject/modified_model.aadl | line 286: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@5b5b53c6{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.4}' with 0 values must have at least 1 values
9. /CaseProject/modified_model.aadl | line 286: no viable alternative at input 'ecam_info_derivation'
10. /CaseProject/modified_model.aadl | line 289: Couldn't resolve reference to property definition 'dps'. Property set name may be missing.
11. /CaseProject/modified_model.aadl | line 289: Couldn't resolve reference to property definition 'ecam_info'. Property set name may be missing.
12. /CaseProject/modified_model.aadl | line 289: Couldn't resolve reference to property definition 'let'. Property set name may be missing.
13. /CaseProject/modified_model.aadl | line 289: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@3350ab4{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.5}' with 0 values must have at least 1 values
14. /CaseProject/modified_model.aadl | line 289: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@5315266{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.7}' with 0 values must have at least 1 values
15. /CaseProject/modified_model.aadl | line 289: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@646cb2e{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.6}' with 0 values must have at least 1 values
16. /CaseProject/modified_model.aadl | line 289: mismatched character ' ' expecting '>'
17. /CaseProject/modified_model.aadl | line 289: no viable alternative at character '>'
18. /CaseProject/modified_model.aadl | line 289: no viable alternative at input '0'
19. /CaseProject/modified_model.aadl | line 289: no viable alternative at input 'dps'
20. /CaseProject/modified_model.aadl | line 289: no viable alternative at input 'ecam_info'
21. /CaseProject/modified_model.aadl | line 289: no viable alternative at input 'let'
22. /CaseProject/modified_model.aadl | line 290: mismatched input ';' expecting '.'
23. /CaseProject/modified_model.aadl | line 293: mismatched input 'ecam_info_derived' expecting ';'
24. /CaseProject/modified_model.aadl | line 293: missing 'end' at 'agree_property'
25. /CaseProject/modified_model.aadl | line 295: mismatched character ' ' expecting '>'
26. /CaseProject/modified_model.aadl | line 295: no viable alternative at character '>'
