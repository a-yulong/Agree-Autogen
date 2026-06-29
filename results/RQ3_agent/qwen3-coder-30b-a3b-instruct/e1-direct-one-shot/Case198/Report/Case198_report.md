# Case198 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 62.29
- Initial validation errors: 25
- Final validation errors: 25

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 25
- Warnings: 1

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3678
- completion_tokens: 3394
- total_tokens: 7072

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 197: Couldn't resolve reference to ThreadSubcomponentType 'doors_int.imp'.
2. /CaseProject/modified_model.aadl | line 233: Couldn't resolve reference to ConnectionEnd 'cll'.
3. /CaseProject/modified_model.aadl | line 236: Couldn't resolve reference to ConnectionEnd 'door2'.
4. /CaseProject/modified_model.aadl | line 237: Couldn't resolve reference to ConnectionEnd 'door1'.
5. /CaseProject/modified_model.aadl | line 283: Couldn't resolve reference to property definition 'agree'. Property set name may be missing.
6. /CaseProject/modified_model.aadl | line 283: Couldn't resolve reference to property definition 'contracts'. Property set name may be missing.
7. /CaseProject/modified_model.aadl | line 283: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@2b9d4b0{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.3}' with 0 values must have at least 1 values
8. /CaseProject/modified_model.aadl | line 283: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@2be50bba{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.4}' with 0 values must have at least 1 values
9. /CaseProject/modified_model.aadl | line 283: no viable alternative at input 'contracts'
10. /CaseProject/modified_model.aadl | line 286: Couldn't resolve reference to property definition 'context'. Property set name may be missing.
11. /CaseProject/modified_model.aadl | line 286: Couldn't resolve reference to property definition 'engine_running_is_true'. Property set name may be missing.
12. /CaseProject/modified_model.aadl | line 286: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@15371de2{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.6}' with 0 values must have at least 1 values
13. /CaseProject/modified_model.aadl | line 286: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@79c4f23b{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.5}' with 0 values must have at least 1 values
14. /CaseProject/modified_model.aadl | line 286: no viable alternative at input 'context'
15. /CaseProject/modified_model.aadl | line 286: no viable alternative at input 'engine_running_is_true'
16. /CaseProject/modified_model.aadl | line 287: Couldn't resolve reference to property definition 'assume'. Property set name may be missing.
17. /CaseProject/modified_model.aadl | line 287: Couldn't resolve reference to property definition 'engine_running'. Property set name may be missing.
18. /CaseProject/modified_model.aadl | line 287: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@3350ab4{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.8}' with 0 values must have at least 1 values
19. /CaseProject/modified_model.aadl | line 287: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@5b5b53c6{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.7}' with 0 values must have at least 1 values
20. /CaseProject/modified_model.aadl | line 287: mismatched character ' ' expecting '>'
21. /CaseProject/modified_model.aadl | line 287: no viable alternative at input 'assume'
22. /CaseProject/modified_model.aadl | line 287: no viable alternative at input 'engine_running'
23. /CaseProject/modified_model.aadl | line 287: no viable alternative at input 'true'
24. /CaseProject/modified_model.aadl | line 288: mismatched input ';' expecting '.'
25. /CaseProject/modified_model.aadl | line 289: mismatched input '.' expecting ';'
