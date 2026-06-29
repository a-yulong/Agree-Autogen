# Case235 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 81.91
- Initial validation errors: 11
- Final validation errors: 11

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 11
- Warnings: 0

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3687
- completion_tokens: 3417
- total_tokens: 7104

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 285: Couldn't resolve reference to property definition 'agree'. Property set name may be missing.
2. /CaseProject/modified_model.aadl | line 285: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@5503c7d{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.3}' with 0 values must have at least 1 values
3. /CaseProject/modified_model.aadl | line 288: Couldn't resolve reference to property definition 'dps'. Property set name may be missing.
4. /CaseProject/modified_model.aadl | line 288: Couldn't resolve reference to property definition 'ecam_info'. Property set name may be missing.
5. /CaseProject/modified_model.aadl | line 288: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@2ec0ca83{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.4}' with 0 values must have at least 1 values
6. /CaseProject/modified_model.aadl | line 288: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@7827d7b{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.5}' with 0 values must have at least 1 values
7. /CaseProject/modified_model.aadl | line 288: mismatched character ' ' expecting '>'
8. /CaseProject/modified_model.aadl | line 288: no viable alternative at character '>'
9. /CaseProject/modified_model.aadl | line 288: no viable alternative at input '0'
10. /CaseProject/modified_model.aadl | line 288: no viable alternative at input 'dps'
11. /CaseProject/modified_model.aadl | line 288: no viable alternative at input 'ecam_info'
