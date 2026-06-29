# Case288 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 55.33
- Initial validation errors: 21
- Final validation errors: 21

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 21
- Warnings: 2

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 4589
- completion_tokens: 2865
- total_tokens: 7454

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 275: Couldn't resolve reference to property definition 'AGREE::property"P_Inputboundedbyenvironment":'.
2. /CaseProject/modified_model.aadl | line 275: Couldn't resolve reference to property definition 'P_Input'. Property set name may be missing.
3. /CaseProject/modified_model.aadl | line 275: Couldn't resolve reference to property definition 'always'. Property set name may be missing.
4. /CaseProject/modified_model.aadl | line 275: Couldn't resolve reference to property definition 'and'. Property set name may be missing.
5. /CaseProject/modified_model.aadl | line 275: Couldn't resolve reference to property definition 'assert'. Property set name may be missing.
6. /CaseProject/modified_model.aadl | line 275: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@10a0a1e{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.25/@ownedPropertyAssociation.5}' with 0 values must have at least 1 values
7. /CaseProject/modified_model.aadl | line 275: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@13ee97af{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.25/@ownedPropertyAssociation.2}' with 0 values must have at least 1 values
8. /CaseProject/modified_model.aadl | line 275: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@341ccfd1{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.25/@ownedPropertyAssociation.3}' with 0 values must have at least 1 values
9. /CaseProject/modified_model.aadl | line 275: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@3cead673{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.25/@ownedPropertyAssociation.4}' with 0 values must have at least 1 values
10. /CaseProject/modified_model.aadl | line 275: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@4345fd45{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.25/@ownedPropertyAssociation.6}' with 0 values must have at least 1 values
11. /CaseProject/modified_model.aadl | line 275: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@5a7e81{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.25/@ownedPropertyAssociation.1}' with 0 values must have at least 1 values
12. /CaseProject/modified_model.aadl | line 275: mismatched character ' ' expecting '>'
13. /CaseProject/modified_model.aadl | line 275: mismatched character '=' expecting '-'
14. /CaseProject/modified_model.aadl | line 275: mismatched input 'property' expecting RULE_ID
15. /CaseProject/modified_model.aadl | line 275: no viable alternative at character '>'
16. /CaseProject/modified_model.aadl | line 275: no viable alternative at input '('
17. /CaseProject/modified_model.aadl | line 275: no viable alternative at input '0.0'
18. /CaseProject/modified_model.aadl | line 275: no viable alternative at input '100.0'
19. /CaseProject/modified_model.aadl | line 275: no viable alternative at input 'P_Input'
20. /CaseProject/modified_model.aadl | line 275: no viable alternative at input 'always'
21. /CaseProject/modified_model.aadl | line 275: no viable alternative at input 'assert'
