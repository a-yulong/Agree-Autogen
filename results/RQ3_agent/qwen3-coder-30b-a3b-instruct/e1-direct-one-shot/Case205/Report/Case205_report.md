# Case205 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 61.44
- Initial validation errors: 20
- Final validation errors: 20

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 20
- Warnings: 1

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3699
- completion_tokens: 3439
- total_tokens: 7138

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to ThreadSubcomponentType 'doors_int.imp'.
2. /CaseProject/modified_model.aadl | line 231: Couldn't resolve reference to ConnectionEnd 'cll'.
3. /CaseProject/modified_model.aadl | line 234: Couldn't resolve reference to ConnectionEnd 'door2'.
4. /CaseProject/modified_model.aadl | line 235: Couldn't resolve reference to ConnectionEnd 'door1'.
5. /CaseProject/modified_model.aadl | line 283: Couldn't resolve reference to property definition 'agree'. Property set name may be missing.
6. /CaseProject/modified_model.aadl | line 283: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@4f541e67{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.3}' with 0 values must have at least 1 values
7. /CaseProject/modified_model.aadl | line 286: Couldn't resolve reference to property definition 'D1_ecam_info_eq_D1_dps_gt_0'. Property set name may be missing.
8. /CaseProject/modified_model.aadl | line 286: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@3514ac7d{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.4}' with 0 values must have at least 1 values
9. /CaseProject/modified_model.aadl | line 286: no viable alternative at input 'is'
10. /CaseProject/modified_model.aadl | line 286: no viable alternative at input 'property'
11. /CaseProject/modified_model.aadl | line 287: Couldn't resolve reference to property definition 'D1_dps'. Property set name may be missing.
12. /CaseProject/modified_model.aadl | line 287: Couldn't resolve reference to property definition 'D1_ecam_info'. Property set name may be missing.
13. /CaseProject/modified_model.aadl | line 287: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@160c7c42{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.5}' with 0 values must have at least 1 values
14. /CaseProject/modified_model.aadl | line 287: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@5503c7d{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.6}' with 0 values must have at least 1 values
15. /CaseProject/modified_model.aadl | line 287: mismatched character ' ' expecting '>'
16. /CaseProject/modified_model.aadl | line 287: no viable alternative at character '>'
17. /CaseProject/modified_model.aadl | line 287: no viable alternative at input '('
18. /CaseProject/modified_model.aadl | line 287: no viable alternative at input '0'
19. /CaseProject/modified_model.aadl | line 288: mismatched input ';' expecting '.'
20. /CaseProject/modified_model.aadl | line 289: mismatched input '.' expecting ';'
