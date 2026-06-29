# Case23 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 61.48
- Initial validation errors: 28
- Final validation errors: 28

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 28
- Warnings: 1

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 1042
- completion_tokens: 888
- total_tokens: 1930

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 92: Couldn't resolve reference to property definition 'AGREE::Node'.
2. /CaseProject/modified_model.aadl | line 92: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@7e1d8d41{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.13/@ownedPropertyAssociation.0}' with 0 values must have at least 1 values
3. /CaseProject/modified_model.aadl | line 92: mismatched character ' ' expecting '>'
4. /CaseProject/modified_model.aadl | line 92: no viable alternative at input ':'
5. /CaseProject/modified_model.aadl | line 93: Couldn't resolve reference to property definition 'AGREE::Var'.
6. /CaseProject/modified_model.aadl | line 93: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@4809c771{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.13/@ownedPropertyAssociation.1}' with 0 values must have at least 1 values
7. /CaseProject/modified_model.aadl | line 93: mismatched character ' ' expecting '>'
8. /CaseProject/modified_model.aadl | line 93: no viable alternative at input ':'
9. /CaseProject/modified_model.aadl | line 94: Couldn't resolve reference to property definition 'AGREE::Var'.
10. /CaseProject/modified_model.aadl | line 94: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@6f4e39b3{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.13/@ownedPropertyAssociation.2}' with 0 values must have at least 1 values
11. /CaseProject/modified_model.aadl | line 94: mismatched character ' ' expecting '>'
12. /CaseProject/modified_model.aadl | line 94: no viable alternative at input ':'
13. /CaseProject/modified_model.aadl | line 95: Couldn't resolve reference to property definition 'AGREE::Guarantee'.
14. /CaseProject/modified_model.aadl | line 95: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@750e2d33{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.13/@ownedPropertyAssociation.3}' with 0 values must have at least 1 values
15. /CaseProject/modified_model.aadl | line 95: mismatched character ' ' expecting '>'
16. /CaseProject/modified_model.aadl | line 95: no viable alternative at input ':'
17. /CaseProject/modified_model.aadl | line 96: Couldn't resolve reference to property definition 'AGREE::Guarantee'.
18. /CaseProject/modified_model.aadl | line 96: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@7ea91c39{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.13/@ownedPropertyAssociation.4}' with 0 values must have at least 1 values
19. /CaseProject/modified_model.aadl | line 96: mismatched character ' ' expecting '>'
20. /CaseProject/modified_model.aadl | line 96: no viable alternative at input ':'
21. /CaseProject/modified_model.aadl | line 97: Couldn't resolve reference to property definition 'AGREE::Guarantee'.
22. /CaseProject/modified_model.aadl | line 97: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@55d35f7a{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.13/@ownedPropertyAssociation.5}' with 0 values must have at least 1 values
23. /CaseProject/modified_model.aadl | line 97: mismatched character ' ' expecting '>'
24. /CaseProject/modified_model.aadl | line 97: no viable alternative at input ':'
25. /CaseProject/modified_model.aadl | line 98: Couldn't resolve reference to property definition 'AGREE::Guarantee'.
26. /CaseProject/modified_model.aadl | line 98: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@12ef7db5{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.13/@ownedPropertyAssociation.6}' with 0 values must have at least 1 values
27. /CaseProject/modified_model.aadl | line 98: mismatched character ' ' expecting '>'
28. /CaseProject/modified_model.aadl | line 98: no viable alternative at input ':'
