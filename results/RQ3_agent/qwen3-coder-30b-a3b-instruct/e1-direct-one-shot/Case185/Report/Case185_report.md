# Case185 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 111.48
- Initial validation errors: 18
- Final validation errors: 18

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 18
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
- completion_tokens: 3392
- total_tokens: 7078

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 285: Couldn't resolve reference to property definition 'agree'. Property set name may be missing.
2. /CaseProject/modified_model.aadl | line 285: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@5503c7d{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.3}' with 0 values must have at least 1 values
3. /CaseProject/modified_model.aadl | line 287: Couldn't resolve reference to property definition 'and'. Property set name may be missing.
4. /CaseProject/modified_model.aadl | line 287: Couldn't resolve reference to property definition 'assume'. Property set name may be missing.
5. /CaseProject/modified_model.aadl | line 287: Couldn't resolve reference to property definition 'dps'. Property set name may be missing.
6. /CaseProject/modified_model.aadl | line 287: Couldn't resolve reference to property definition 'dps_bounded'. Property set name may be missing.
7. /CaseProject/modified_model.aadl | line 287: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@11cc9e1e{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.7}' with 0 values must have at least 1 values
8. /CaseProject/modified_model.aadl | line 287: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@2e7a9db7{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.6}' with 0 values must have at least 1 values
9. /CaseProject/modified_model.aadl | line 287: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@2ec0ca83{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.4}' with 0 values must have at least 1 values
10. /CaseProject/modified_model.aadl | line 287: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@5b0e9e0c{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.8}' with 0 values must have at least 1 values
11. /CaseProject/modified_model.aadl | line 287: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@7827d7b{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.5}' with 0 values must have at least 1 values
12. /CaseProject/modified_model.aadl | line 287: mismatched character '=' expecting '-'
13. /CaseProject/modified_model.aadl | line 287: no viable alternative at input '100'
14. /CaseProject/modified_model.aadl | line 287: no viable alternative at input ':'
15. /CaseProject/modified_model.aadl | line 287: no viable alternative at input 'and'
16. /CaseProject/modified_model.aadl | line 287: no viable alternative at input 'assume'
17. /CaseProject/modified_model.aadl | line 287: no viable alternative at input 'dps'
18. /CaseProject/modified_model.aadl | line 287: no viable alternative at input 'dps_bounded'
