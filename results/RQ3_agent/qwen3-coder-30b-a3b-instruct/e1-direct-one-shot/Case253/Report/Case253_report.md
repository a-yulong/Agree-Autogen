# Case253 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 94.74
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

- prompt_tokens: 3699
- completion_tokens: 3406
- total_tokens: 7105

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 283: Couldn't resolve reference to property definition 'agree'. Property set name may be missing.
2. /CaseProject/modified_model.aadl | line 283: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@160c7c42{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.3}' with 0 values must have at least 1 values
3. /CaseProject/modified_model.aadl | line 285: Couldn't resolve reference to property definition 'D1_dps'. Property set name may be missing.
4. /CaseProject/modified_model.aadl | line 285: Couldn't resolve reference to property definition 'D1_ecam_info'. Property set name may be missing.
5. /CaseProject/modified_model.aadl | line 285: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@2ec0ca83{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.5}' with 0 values must have at least 1 values
6. /CaseProject/modified_model.aadl | line 285: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@5503c7d{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.4}' with 0 values must have at least 1 values
7. /CaseProject/modified_model.aadl | line 285: mismatched character ' ' expecting '>'
8. /CaseProject/modified_model.aadl | line 285: no viable alternative at character '>'
9. /CaseProject/modified_model.aadl | line 285: no viable alternative at input '('
10. /CaseProject/modified_model.aadl | line 285: no viable alternative at input '0'
11. /CaseProject/modified_model.aadl | line 285: no viable alternative at input 'D1_ecam_info'
