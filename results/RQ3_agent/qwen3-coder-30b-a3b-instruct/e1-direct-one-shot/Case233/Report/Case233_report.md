# Case233 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 147.36
- Initial validation errors: 38
- Final validation errors: 38

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 38
- Warnings: 0

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3686
- completion_tokens: 3435
- total_tokens: 7121

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 284: Couldn't resolve reference to property definition 'agree'. Property set name may be missing.
2. /CaseProject/modified_model.aadl | line 284: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@5b5b53c6{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.3}' with 0 values must have at least 1 values
3. /CaseProject/modified_model.aadl | line 287: Couldn't resolve reference to property definition 'assume'. Property set name may be missing.
4. /CaseProject/modified_model.aadl | line 287: Couldn't resolve reference to property definition 'bounded_dps_input'. Property set name may be missing.
5. /CaseProject/modified_model.aadl | line 287: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@3350ab4{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.4}' with 0 values must have at least 1 values
6. /CaseProject/modified_model.aadl | line 287: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@646cb2e{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.5}' with 0 values must have at least 1 values
7. /CaseProject/modified_model.aadl | line 287: no viable alternative at input ':'
8. /CaseProject/modified_model.aadl | line 287: no viable alternative at input 'assume'
9. /CaseProject/modified_model.aadl | line 287: no viable alternative at input 'bounded_dps_input'
10. /CaseProject/modified_model.aadl | line 288: Couldn't resolve reference to property definition 'for'. Property set name may be missing.
11. /CaseProject/modified_model.aadl | line 288: Couldn't resolve reference to property definition 'ms'. Property set name may be missing.
12. /CaseProject/modified_model.aadl | line 288: Couldn't resolve reference to property definition 't'. Property set name may be missing.
13. /CaseProject/modified_model.aadl | line 288: Couldn't resolve reference to property definition 'time'. Property set name may be missing.
14. /CaseProject/modified_model.aadl | line 288: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@19f497aa{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.9}' with 0 values must have at least 1 values
15. /CaseProject/modified_model.aadl | line 288: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@216328b2{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.7}' with 0 values must have at least 1 values
16. /CaseProject/modified_model.aadl | line 288: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@5315266{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.6}' with 0 values must have at least 1 values
17. /CaseProject/modified_model.aadl | line 288: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@54234569{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.8}' with 0 values must have at least 1 values
18. /CaseProject/modified_model.aadl | line 288: no viable alternative at input ':'
19. /CaseProject/modified_model.aadl | line 288: no viable alternative at input ']'
20. /CaseProject/modified_model.aadl | line 288: no viable alternative at input 'all'
21. /CaseProject/modified_model.aadl | line 288: no viable alternative at input 'in'
22. /CaseProject/modified_model.aadl | line 288: required (...)+ loop did not match anything at character '.'
23. /CaseProject/modified_model.aadl | line 289: Couldn't resolve reference to property definition 'and'. Property set name may be missing.
24. /CaseProject/modified_model.aadl | line 289: Couldn't resolve reference to property definition 'dps'. Property set name may be missing.
25. /CaseProject/modified_model.aadl | line 289: Couldn't resolve reference to property definition 'implies'. Property set name may be missing.
26. /CaseProject/modified_model.aadl | line 289: Couldn't resolve reference to property definition 't'. Property set name may be missing.
27. /CaseProject/modified_model.aadl | line 289: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@3460e4ed{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.11}' with 0 values must have at least 1 values
28. /CaseProject/modified_model.aadl | line 289: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@4a453f8d{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.12}' with 0 values must have at least 1 values
29. /CaseProject/modified_model.aadl | line 289: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@53525379{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.13}' with 0 values must have at least 1 values
30. /CaseProject/modified_model.aadl | line 289: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@6de33fde{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.15}' with 0 values must have at least 1 values
31. /CaseProject/modified_model.aadl | line 289: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@78b9155e{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.14}' with 0 values must have at least 1 values
32. /CaseProject/modified_model.aadl | line 289: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@78e387d6{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.10}' with 0 values must have at least 1 values
33. /CaseProject/modified_model.aadl | line 289: mismatched character ' ' expecting '>'
34. /CaseProject/modified_model.aadl | line 289: mismatched character '=' expecting '-'
35. /CaseProject/modified_model.aadl | line 289: no viable alternative at character '>'
36. /CaseProject/modified_model.aadl | line 289: no viable alternative at input '('
37. /CaseProject/modified_model.aadl | line 289: no viable alternative at input ')'
38. /CaseProject/modified_model.aadl | line 289: no viable alternative at input 'dps'
