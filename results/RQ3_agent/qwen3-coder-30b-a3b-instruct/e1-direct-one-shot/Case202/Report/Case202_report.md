# Case202 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 62.72
- Initial validation errors: 19
- Final validation errors: 19

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 19
- Warnings: 1

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3692
- completion_tokens: 3371
- total_tokens: 7063

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to ThreadSubcomponentType 'doors_int.imp'.
2. /CaseProject/modified_model.aadl | line 231: Couldn't resolve reference to ConnectionEnd 'cll'.
3. /CaseProject/modified_model.aadl | line 234: Couldn't resolve reference to ConnectionEnd 'door2'.
4. /CaseProject/modified_model.aadl | line 235: Couldn't resolve reference to ConnectionEnd 'door1'.
5. /CaseProject/modified_model.aadl | line 283: Couldn't resolve reference to property definition 'verify'. Property set name may be missing.
6. /CaseProject/modified_model.aadl | line 283: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@79c4f23b{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.3}' with 0 values must have at least 1 values
7. /CaseProject/modified_model.aadl | line 285: Couldn't resolve reference to property definition 'D1_dps'. Property set name may be missing.
8. /CaseProject/modified_model.aadl | line 285: Couldn't resolve reference to property definition 'and'. Property set name may be missing.
9. /CaseProject/modified_model.aadl | line 285: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@15371de2{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.4}' with 0 values must have at least 1 values
10. /CaseProject/modified_model.aadl | line 285: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@3350ab4{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.6}' with 0 values must have at least 1 values
11. /CaseProject/modified_model.aadl | line 285: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@5b5b53c6{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.5}' with 0 values must have at least 1 values
12. /CaseProject/modified_model.aadl | line 285: mismatched character ' ' expecting '>'
13. /CaseProject/modified_model.aadl | line 285: mismatched character '=' expecting '-'
14. /CaseProject/modified_model.aadl | line 285: no viable alternative at character '>'
15. /CaseProject/modified_model.aadl | line 285: no viable alternative at input '0'
16. /CaseProject/modified_model.aadl | line 285: no viable alternative at input '100'
17. /CaseProject/modified_model.aadl | line 285: no viable alternative at input 'D1_dps'
18. /CaseProject/modified_model.aadl | line 286: mismatched input ';' expecting '.'
19. /CaseProject/modified_model.aadl | line 288: mismatched input '.' expecting ';'
