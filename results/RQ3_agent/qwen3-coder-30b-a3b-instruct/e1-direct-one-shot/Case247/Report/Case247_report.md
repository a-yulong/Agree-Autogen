# Case247 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 60.50
- Initial validation errors: 20
- Final validation errors: 20

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 20
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
- completion_tokens: 3363
- total_tokens: 7050

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 283: Couldn't resolve reference to property definition 'agree_nodes'. Property set name may be missing.
2. /CaseProject/modified_model.aadl | line 283: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@160c7c42{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.3}' with 0 values must have at least 1 values
3. /CaseProject/modified_model.aadl | line 284: Couldn't resolve reference to property definition 'boolean'. Property set name may be missing.
4. /CaseProject/modified_model.aadl | line 284: Couldn't resolve reference to property definition 'ecam_info'. Property set name may be missing.
5. /CaseProject/modified_model.aadl | line 284: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@2ec0ca83{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.5}' with 0 values must have at least 1 values
6. /CaseProject/modified_model.aadl | line 284: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@5503c7d{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.4}' with 0 values must have at least 1 values
7. /CaseProject/modified_model.aadl | line 284: no viable alternative at input ':'
8. /CaseProject/modified_model.aadl | line 284: no viable alternative at input ';'
9. /CaseProject/modified_model.aadl | line 284: no viable alternative at input 'ecam_info'
10. /CaseProject/modified_model.aadl | line 285: Couldn't resolve reference to property definition 'agree_annotations'. Property set name may be missing.
11. /CaseProject/modified_model.aadl | line 285: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@7827d7b{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.6}' with 0 values must have at least 1 values
12. /CaseProject/modified_model.aadl | line 286: Couldn't resolve reference to property definition 'dps'. Property set name may be missing.
13. /CaseProject/modified_model.aadl | line 286: Couldn't resolve reference to property definition 'ecam_info'. Property set name may be missing.
14. /CaseProject/modified_model.aadl | line 286: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@11cc9e1e{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.8}' with 0 values must have at least 1 values
15. /CaseProject/modified_model.aadl | line 286: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@2e7a9db7{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.7}' with 0 values must have at least 1 values
16. /CaseProject/modified_model.aadl | line 286: mismatched character ' ' expecting '>'
17. /CaseProject/modified_model.aadl | line 286: no viable alternative at character '>'
18. /CaseProject/modified_model.aadl | line 286: no viable alternative at input '('
19. /CaseProject/modified_model.aadl | line 286: no viable alternative at input '0'
20. /CaseProject/modified_model.aadl | line 286: no viable alternative at input 'ecam_info'
