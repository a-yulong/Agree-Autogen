# Case246 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 62.98
- Initial validation errors: 35
- Final validation errors: 35

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 35
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
- completion_tokens: 3409
- total_tokens: 7087

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 197: Couldn't resolve reference to ThreadSubcomponentType 'doors_int.imp'.
2. /CaseProject/modified_model.aadl | line 233: Couldn't resolve reference to ConnectionEnd 'cll'.
3. /CaseProject/modified_model.aadl | line 236: Couldn't resolve reference to ConnectionEnd 'door2'.
4. /CaseProject/modified_model.aadl | line 237: Couldn't resolve reference to ConnectionEnd 'door1'.
5. /CaseProject/modified_model.aadl | line 283: Couldn't resolve reference to property definition 'agree'. Property set name may be missing.
6. /CaseProject/modified_model.aadl | line 283: Couldn't resolve reference to property definition 'contracts'. Property set name may be missing.
7. /CaseProject/modified_model.aadl | line 283: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@160c7c42{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.4}' with 0 values must have at least 1 values
8. /CaseProject/modified_model.aadl | line 283: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@3514ac7d{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.3}' with 0 values must have at least 1 values
9. /CaseProject/modified_model.aadl | line 283: no viable alternative at input 'contracts'
10. /CaseProject/modified_model.aadl | line 284: Couldn't resolve reference to property definition 'context'. Property set name may be missing.
11. /CaseProject/modified_model.aadl | line 284: Couldn't resolve reference to property definition 'door_handler_context'. Property set name may be missing.
12. /CaseProject/modified_model.aadl | line 284: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@2ec0ca83{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.6}' with 0 values must have at least 1 values
13. /CaseProject/modified_model.aadl | line 284: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@5503c7d{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.5}' with 0 values must have at least 1 values
14. /CaseProject/modified_model.aadl | line 284: no viable alternative at input 'context'
15. /CaseProject/modified_model.aadl | line 284: no viable alternative at input 'door_handler_context'
16. /CaseProject/modified_model.aadl | line 287: Couldn't resolve reference to property definition 'ENGINE_RUNNING_TRUE'. Property set name may be missing.
17. /CaseProject/modified_model.aadl | line 287: Couldn't resolve reference to property definition 'boolean'. Property set name may be missing.
18. /CaseProject/modified_model.aadl | line 287: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@2e7a9db7{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.8}' with 0 values must have at least 1 values
19. /CaseProject/modified_model.aadl | line 287: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@7827d7b{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.7}' with 0 values must have at least 1 values
20. /CaseProject/modified_model.aadl | line 287: mismatched character ' ' expecting '>'
21. /CaseProject/modified_model.aadl | line 287: no viable alternative at input ':'
22. /CaseProject/modified_model.aadl | line 287: no viable alternative at input 'constant'
23. /CaseProject/modified_model.aadl | line 287: no viable alternative at input 'true'
24. /CaseProject/modified_model.aadl | line 288: Couldn't resolve reference to property definition 'ENGINE_RUNNING_TRUE'. Property set name may be missing.
25. /CaseProject/modified_model.aadl | line 288: Couldn't resolve reference to property definition 'engine_running'. Property set name may be missing.
26. /CaseProject/modified_model.aadl | line 288: Couldn't resolve reference to property definition 'engine_running_is_true'. Property set name may be missing.
27. /CaseProject/modified_model.aadl | line 288: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@11cc9e1e{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.9}' with 0 values must have at least 1 values
28. /CaseProject/modified_model.aadl | line 288: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@21ea1d9d{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.11}' with 0 values must have at least 1 values
29. /CaseProject/modified_model.aadl | line 288: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@5b0e9e0c{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.10}' with 0 values must have at least 1 values
30. /CaseProject/modified_model.aadl | line 288: mismatched character ' ' expecting '>'
31. /CaseProject/modified_model.aadl | line 288: no viable alternative at input ':'
32. /CaseProject/modified_model.aadl | line 288: no viable alternative at input ';'
33. /CaseProject/modified_model.aadl | line 288: no viable alternative at input 'ENGINE_RUNNING_TRUE'
34. /CaseProject/modified_model.aadl | line 289: mismatched input ';' expecting '.'
35. /CaseProject/modified_model.aadl | line 290: mismatched input '.' expecting ';'
