# Case22 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 37.90
- Initial validation errors: 17
- Final validation errors: 17

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 17
- Warnings: 2

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 1049
- completion_tokens: 887
- total_tokens: 1936

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 59: Couldn't resolve reference to SystemSubcomponentType 'heater.impl'.
2. /CaseProject/modified_model.aadl | line 60: Couldn't resolve reference to SystemSubcomponentType 'cooler.impl'.
3. /CaseProject/modified_model.aadl | line 67: Couldn't resolve reference to ConnectionEnd 'enabled'.
4. /CaseProject/modified_model.aadl | line 68: Couldn't resolve reference to ConnectionEnd 'enabled'.
5. /CaseProject/modified_model.aadl | line 92: Couldn't resolve reference to property definition 'AGREE::Node'.
6. /CaseProject/modified_model.aadl | line 92: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@21abda60{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.13/@ownedPropertyAssociation.0}' with 0 values must have at least 1 values
7. /CaseProject/modified_model.aadl | line 92: mismatched character ' ' expecting '>'
8. /CaseProject/modified_model.aadl | line 92: no viable alternative at input ':'
9. /CaseProject/modified_model.aadl | line 93: mismatched input '::' expecting '.'
10. /CaseProject/modified_model.aadl | line 96: missing 'end' at 'variables'
11. /CaseProject/modified_model.aadl | line 97: mismatched input 'heating_request' expecting ';'
12. /CaseProject/modified_model.aadl | line 103: mismatched character ' ' expecting '>'
13. /CaseProject/modified_model.aadl | line 104: mismatched character ' ' expecting '>'
14. /CaseProject/modified_model.aadl | line 109: mismatched character ' ' expecting '>'
15. /CaseProject/modified_model.aadl | line 109: mismatched character '=' expecting '-'
16. /CaseProject/modified_model.aadl | line 110: mismatched character ' ' expecting '>'
17. /CaseProject/modified_model.aadl | line 110: no viable alternative at character '>'
