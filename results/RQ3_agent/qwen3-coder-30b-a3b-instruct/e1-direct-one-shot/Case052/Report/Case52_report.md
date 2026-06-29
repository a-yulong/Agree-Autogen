# Case52 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 39.41
- Initial validation errors: 16
- Final validation errors: 16

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 16
- Warnings: 1

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 673
- completion_tokens: 484
- total_tokens: 1157

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 22: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@783b3aa0{platform:/resource/CaseProject/modified_model.aadl#Integer_Toy_Extended.Integer_Toy_Extended_public.C.agree}' must be set
2. /CaseProject/modified_model.aadl | line 22: mismatched input '{' expecting RULE_ANNEXTEXT
3. /CaseProject/modified_model.aadl | line 23: mismatched input 'properties' expecting 'end'
4. /CaseProject/modified_model.aadl | line 24: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Input2'. For classifier references use classifier( <ref> ).
5. /CaseProject/modified_model.aadl | line 24: Couldn't resolve reference to property definition 'Guarantee'. Property set name may be missing.
6. /CaseProject/modified_model.aadl | line 24: Couldn't resolve reference to property definition 'Input1'. Property set name may be missing.
7. /CaseProject/modified_model.aadl | line 24: Couldn't resolve reference to property definition 'Output'. Property set name may be missing.
8. /CaseProject/modified_model.aadl | line 24: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@427308f8{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPropertyAssociation.0}' with 0 values must have at least 1 values
9. /CaseProject/modified_model.aadl | line 24: The required feature 'maximum' of 'org.osate.aadl2.impl.RangeValueImpl@4af70b83{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPropertyAssociation.2/@ownedValue.0/@ownedValue}' must be set
10. /CaseProject/modified_model.aadl | line 24: The required feature 'ownedValue' of 'org.osate.aadl2.impl.ModalPropertyValueImpl@47e89fed{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPropertyAssociation.1/@ownedValue.0}' must be set
11. /CaseProject/modified_model.aadl | line 24: mismatched character ' ' expecting '>'
12. /CaseProject/modified_model.aadl | line 24: mismatched input ':' expecting '=>'
13. /CaseProject/modified_model.aadl | line 24: mismatched input ';' expecting '..'
14. /CaseProject/modified_model.aadl | line 24: missing '=>' at '+'
15. /CaseProject/modified_model.aadl | line 24: missing '=>' at 'Input1'
16. /CaseProject/modified_model.aadl | line 25: mismatched input '}' expecting 'end'
