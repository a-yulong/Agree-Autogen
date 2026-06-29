# Case213 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 195.47
- Initial validation errors: 15
- Final validation errors: 15

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 15
- Warnings: 0

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3681
- completion_tokens: 3412
- total_tokens: 7093

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 285: Couldn't resolve reference to property definition 'agree'. Property set name may be missing.
2. /CaseProject/modified_model.aadl | line 285: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@319aa9ee{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.3}' with 0 values must have at least 1 values
3. /CaseProject/modified_model.aadl | line 288: Couldn't resolve reference to property definition 'assert'. Property set name may be missing.
4. /CaseProject/modified_model.aadl | line 288: Couldn't resolve reference to property definition 'ecam_info'. Property set name may be missing.
5. /CaseProject/modified_model.aadl | line 288: Couldn't resolve reference to property definition 'in_flight'. Property set name may be missing.
6. /CaseProject/modified_model.aadl | line 288: Couldn't resolve reference to property definition 'whenever'. Property set name may be missing.
7. /CaseProject/modified_model.aadl | line 288: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@15371de2{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.7}' with 0 values must have at least 1 values
8. /CaseProject/modified_model.aadl | line 288: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@2b9d4b0{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.4}' with 0 values must have at least 1 values
9. /CaseProject/modified_model.aadl | line 288: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@2be50bba{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.5}' with 0 values must have at least 1 values
10. /CaseProject/modified_model.aadl | line 288: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@79c4f23b{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.6}' with 0 values must have at least 1 values
11. /CaseProject/modified_model.aadl | line 288: no viable alternative at input ';'
12. /CaseProject/modified_model.aadl | line 288: no viable alternative at input 'assert'
13. /CaseProject/modified_model.aadl | line 288: no viable alternative at input 'ecam_info'
14. /CaseProject/modified_model.aadl | line 288: no viable alternative at input 'in_flight'
15. /CaseProject/modified_model.aadl | line 288: no viable alternative at input 'whenever'
