# Case234 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 59.69
- Initial validation errors: 19
- Final validation errors: 19

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 19
- Warnings: 0

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3678
- completion_tokens: 3387
- total_tokens: 7065

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 283: Couldn't resolve reference to property definition 'agree_contract'. Property set name may be missing.
2. /CaseProject/modified_model.aadl | line 283: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@79c4f23b{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.3}' with 0 values must have at least 1 values
3. /CaseProject/modified_model.aadl | line 286: Couldn't resolve reference to property definition 'boolean'. Property set name may be missing.
4. /CaseProject/modified_model.aadl | line 286: Couldn't resolve reference to property definition 'context'. Property set name may be missing.
5. /CaseProject/modified_model.aadl | line 286: Couldn't resolve reference to property definition 'engine_running'. Property set name may be missing.
6. /CaseProject/modified_model.aadl | line 286: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@15371de2{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.4}' with 0 values must have at least 1 values
7. /CaseProject/modified_model.aadl | line 286: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@3350ab4{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.6}' with 0 values must have at least 1 values
8. /CaseProject/modified_model.aadl | line 286: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@5b5b53c6{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.5}' with 0 values must have at least 1 values
9. /CaseProject/modified_model.aadl | line 286: no viable alternative at input ':'
10. /CaseProject/modified_model.aadl | line 286: no viable alternative at input ';'
11. /CaseProject/modified_model.aadl | line 286: no viable alternative at input 'context'
12. /CaseProject/modified_model.aadl | line 286: no viable alternative at input 'engine_running'
13. /CaseProject/modified_model.aadl | line 287: Couldn't resolve reference to property definition 'assume'. Property set name may be missing.
14. /CaseProject/modified_model.aadl | line 287: Couldn't resolve reference to property definition 'engine_running'. Property set name may be missing.
15. /CaseProject/modified_model.aadl | line 287: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@5315266{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.8}' with 0 values must have at least 1 values
16. /CaseProject/modified_model.aadl | line 287: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@646cb2e{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.7}' with 0 values must have at least 1 values
17. /CaseProject/modified_model.aadl | line 287: mismatched character ' ' expecting '>'
18. /CaseProject/modified_model.aadl | line 287: no viable alternative at input 'engine_running'
19. /CaseProject/modified_model.aadl | line 287: no viable alternative at input 'true'
