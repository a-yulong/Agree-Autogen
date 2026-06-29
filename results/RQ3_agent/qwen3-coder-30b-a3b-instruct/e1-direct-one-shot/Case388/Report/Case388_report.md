# Case388 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 60.50
- Initial validation errors: 13
- Final validation errors: 13

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 13
- Warnings: 8

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3842
- completion_tokens: 1366
- total_tokens: 5208

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 93: Couldn't resolve reference to property definition 'agree_property'. Property set name may be missing.
2. /CaseProject/modified_model.aadl | line 93: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@4b50c21{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.8/@ownedPropertyAssociation.4}' with 0 values must have at least 1 values
3. /CaseProject/modified_model.aadl | line 94: Couldn't resolve reference to property definition 'Data_In'. Property set name may be missing.
4. /CaseProject/modified_model.aadl | line 94: Couldn't resolve reference to property definition 'and'. Property set name may be missing.
5. /CaseProject/modified_model.aadl | line 94: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@5dacf18d{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.8/@ownedPropertyAssociation.5}' with 0 values must have at least 1 values
6. /CaseProject/modified_model.aadl | line 94: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@5f33e6d{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.8/@ownedPropertyAssociation.7}' with 0 values must have at least 1 values
7. /CaseProject/modified_model.aadl | line 94: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@6f52a229{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.8/@ownedPropertyAssociation.6}' with 0 values must have at least 1 values
8. /CaseProject/modified_model.aadl | line 94: mismatched character ' ' expecting '>'
9. /CaseProject/modified_model.aadl | line 94: mismatched character '=' expecting '-'
10. /CaseProject/modified_model.aadl | line 94: no viable alternative at character '>'
11. /CaseProject/modified_model.aadl | line 94: no viable alternative at input '0'
12. /CaseProject/modified_model.aadl | line 94: no viable alternative at input '100'
13. /CaseProject/modified_model.aadl | line 94: no viable alternative at input 'Data_In'
