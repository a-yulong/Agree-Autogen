# Case200 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 60.56
- Initial validation errors: 19
- Final validation errors: 19

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 19
- Warnings: 1

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3682
- completion_tokens: 3429
- total_tokens: 7111

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 197: Couldn't resolve reference to ThreadSubcomponentType 'doors_int.imp'.
2. /CaseProject/modified_model.aadl | line 233: Couldn't resolve reference to ConnectionEnd 'cll'.
3. /CaseProject/modified_model.aadl | line 236: Couldn't resolve reference to ConnectionEnd 'door2'.
4. /CaseProject/modified_model.aadl | line 237: Couldn't resolve reference to ConnectionEnd 'door1'.
5. /CaseProject/modified_model.aadl | line 285: Couldn't resolve reference to property definition 'agree'. Property set name may be missing.
6. /CaseProject/modified_model.aadl | line 285: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@2b9d4b0{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.3}' with 0 values must have at least 1 values
7. /CaseProject/modified_model.aadl | line 288: Couldn't resolve reference to property definition 'ecam_info_propagation'. Property set name may be missing.
8. /CaseProject/modified_model.aadl | line 288: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@2be50bba{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.4}' with 0 values must have at least 1 values
9. /CaseProject/modified_model.aadl | line 288: no viable alternative at input 'is'
10. /CaseProject/modified_model.aadl | line 288: no viable alternative at input 'property'
11. /CaseProject/modified_model.aadl | line 289: Couldn't resolve reference to property definition 'ecam_info'. Property set name may be missing.
12. /CaseProject/modified_model.aadl | line 289: Couldn't resolve reference to property definition 'engine_running'. Property set name may be missing.
13. /CaseProject/modified_model.aadl | line 289: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@15371de2{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.6}' with 0 values must have at least 1 values
14. /CaseProject/modified_model.aadl | line 289: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@79c4f23b{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.5}' with 0 values must have at least 1 values
15. /CaseProject/modified_model.aadl | line 289: mismatched character ' ' expecting '>'
16. /CaseProject/modified_model.aadl | line 289: no viable alternative at input ';'
17. /CaseProject/modified_model.aadl | line 289: no viable alternative at input 'engine_running'
18. /CaseProject/modified_model.aadl | line 290: mismatched input ';' expecting '.'
19. /CaseProject/modified_model.aadl | line 291: mismatched input '.' expecting ';'
