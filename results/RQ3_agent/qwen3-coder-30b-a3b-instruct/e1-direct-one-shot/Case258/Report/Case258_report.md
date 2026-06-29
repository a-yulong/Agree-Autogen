# Case258 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 63.62
- Initial validation errors: 27
- Final validation errors: 27

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 27
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
- completion_tokens: 3476
- total_tokens: 7154

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 285: Couldn't resolve reference to property definition 'agree_body'. Property set name may be missing.
2. /CaseProject/modified_model.aadl | line 285: The required feature 'ownedValue' of 'org.osate.aadl2.impl.ModalPropertyValueImpl@598f6c93{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.3/@ownedValue.0}' must be set
3. /CaseProject/modified_model.aadl | line 288: Couldn't resolve reference to property definition 'assume'. Property set name may be missing.
4. /CaseProject/modified_model.aadl | line 288: Couldn't resolve reference to property definition 'engine_running'. Property set name may be missing.
5. /CaseProject/modified_model.aadl | line 288: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@2ec0ca83{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.5}' with 0 values must have at least 1 values
6. /CaseProject/modified_model.aadl | line 288: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@5503c7d{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.4}' with 0 values must have at least 1 values
7. /CaseProject/modified_model.aadl | line 288: mismatched character ' ' expecting '>'
8. /CaseProject/modified_model.aadl | line 288: no viable alternative at input '"engine_running_is_true"'
9. /CaseProject/modified_model.aadl | line 288: no viable alternative at input 'true'
10. /CaseProject/modified_model.aadl | line 292: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'latched'. For classifier references use classifier( <ref> ).
11. /CaseProject/modified_model.aadl | line 292: Couldn't resolve reference to property definition 'guarantee'. Property set name may be missing.
12. /CaseProject/modified_model.aadl | line 292: Couldn't resolve reference to property definition 'lock'. Property set name may be missing.
13. /CaseProject/modified_model.aadl | line 292: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@7827d7b{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.6}' with 0 values must have at least 1 values
14. /CaseProject/modified_model.aadl | line 292: no viable alternative at input '"lock_only_when_latched"'
15. /CaseProject/modified_model.aadl | line 293: Couldn't resolve reference to property definition 'guarantee'. Property set name may be missing.
16. /CaseProject/modified_model.aadl | line 293: Couldn't resolve reference to property definition 'latched'. Property set name may be missing.
17. /CaseProject/modified_model.aadl | line 293: Couldn't resolve reference to property definition 'locked'. Property set name may be missing.
18. /CaseProject/modified_model.aadl | line 293: Couldn't resolve reference to property definition 'not'. Property set name may be missing.
19. /CaseProject/modified_model.aadl | line 293: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@19f497aa{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.8}' with 0 values must have at least 1 values
20. /CaseProject/modified_model.aadl | line 293: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@4a453f8d{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.11}' with 0 values must have at least 1 values
21. /CaseProject/modified_model.aadl | line 293: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@53525379{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.12}' with 0 values must have at least 1 values
22. /CaseProject/modified_model.aadl | line 293: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@78e387d6{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.9}' with 0 values must have at least 1 values
23. /CaseProject/modified_model.aadl | line 293: The required feature 'ownedValue' of 'org.osate.aadl2.impl.ModalPropertyValueImpl@365291bd{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.17/@ownedPropertyAssociation.10/@ownedValue.0}' must be set
24. /CaseProject/modified_model.aadl | line 293: no viable alternative at input '"unlock_only_when_locked"'
25. /CaseProject/modified_model.aadl | line 293: no viable alternative at input ';'
26. /CaseProject/modified_model.aadl | line 293: no viable alternative at input 'latched'
27. /CaseProject/modified_model.aadl | line 293: no viable alternative at input 'locked'
