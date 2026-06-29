# Case415 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 63.07
- Initial validation errors: 33
- Final validation errors: 33

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 33
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
- completion_tokens: 3443
- total_tokens: 7121

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 197: Couldn't resolve reference to ThreadSubcomponentType 'doors_int.imp'.
2. /CaseProject/modified_model.aadl | line 233: Couldn't resolve reference to ConnectionEnd 'cll'.
3. /CaseProject/modified_model.aadl | line 236: Couldn't resolve reference to ConnectionEnd 'door2'.
4. /CaseProject/modified_model.aadl | line 237: Couldn't resolve reference to ConnectionEnd 'door1'.
5. /CaseProject/modified_model.aadl | line 282: Couldn't resolve reference to property definition 'agree'. Property set name may be missing.
6. /CaseProject/modified_model.aadl | line 282: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@2be50bba{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.3}' with 0 values must have at least 1 values
7. /CaseProject/modified_model.aadl | line 285: Couldn't resolve reference to property definition 'EngineRunningContext'. Property set name may be missing.
8. /CaseProject/modified_model.aadl | line 285: Couldn't resolve reference to property definition 'context'. Property set name may be missing.
9. /CaseProject/modified_model.aadl | line 285: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@15371de2{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.5}' with 0 values must have at least 1 values
10. /CaseProject/modified_model.aadl | line 285: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@79c4f23b{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.4}' with 0 values must have at least 1 values
11. /CaseProject/modified_model.aadl | line 285: no viable alternative at input 'EngineRunningContext'
12. /CaseProject/modified_model.aadl | line 285: no viable alternative at input 'context'
13. /CaseProject/modified_model.aadl | line 287: Couldn't resolve reference to property definition 'boolean'. Property set name may be missing.
14. /CaseProject/modified_model.aadl | line 287: Couldn't resolve reference to property definition 'engine_running'. Property set name may be missing.
15. /CaseProject/modified_model.aadl | line 287: Couldn't resolve reference to property definition 'var'. Property set name may be missing.
16. /CaseProject/modified_model.aadl | line 287: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@3350ab4{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.7}' with 0 values must have at least 1 values
17. /CaseProject/modified_model.aadl | line 287: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@5b5b53c6{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.6}' with 0 values must have at least 1 values
18. /CaseProject/modified_model.aadl | line 287: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@646cb2e{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.8}' with 0 values must have at least 1 values
19. /CaseProject/modified_model.aadl | line 287: no viable alternative at input ':'
20. /CaseProject/modified_model.aadl | line 287: no viable alternative at input ';'
21. /CaseProject/modified_model.aadl | line 287: no viable alternative at input 'engine_running'
22. /CaseProject/modified_model.aadl | line 287: no viable alternative at input 'var'
23. /CaseProject/modified_model.aadl | line 289: Couldn't resolve reference to property definition 'assume'. Property set name may be missing.
24. /CaseProject/modified_model.aadl | line 289: Couldn't resolve reference to property definition 'engine_running'. Property set name may be missing.
25. /CaseProject/modified_model.aadl | line 289: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@216328b2{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.10}' with 0 values must have at least 1 values
26. /CaseProject/modified_model.aadl | line 289: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@5315266{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.9}' with 0 values must have at least 1 values
27. /CaseProject/modified_model.aadl | line 289: mismatched character ' ' expecting '>'
28. /CaseProject/modified_model.aadl | line 289: no viable alternative at input 'engine_running'
29. /CaseProject/modified_model.aadl | line 289: no viable alternative at input 'true'
30. /CaseProject/modified_model.aadl | line 290: mismatched input ';' expecting '.'
31. /CaseProject/modified_model.aadl | line 293: mismatched character ' ' expecting '>'
32. /CaseProject/modified_model.aadl | line 293: mismatched input 'EngineRunningContext' expecting ';'
33. /CaseProject/modified_model.aadl | line 293: missing 'end' at 'assume'
