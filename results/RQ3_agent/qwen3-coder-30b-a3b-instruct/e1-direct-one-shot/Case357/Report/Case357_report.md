# Case357 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 65.26
- Initial validation errors: 10
- Final validation errors: 10

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 10
- Warnings: 3

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 4566
- completion_tokens: 2855
- total_tokens: 7421

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 259: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexLibraryImpl@6c8efde4{platform:/resource/CaseProject/modified_model.aadl#flyByWire_soft.flyByWire_soft_public.agree}' must be set
2. /CaseProject/modified_model.aadl | line 259: mismatched input '{' expecting RULE_ANNEXTEXT
3. /CaseProject/modified_model.aadl | line 261: Couldn't resolve reference to property definition 'Bounds_Cde_AileronL_Output'. Property set name may be missing.
4. /CaseProject/modified_model.aadl | line 261: Couldn't resolve reference to property definition 'Integer_16'. Property set name may be missing.
5. /CaseProject/modified_model.aadl | line 261: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@44de8e00{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPropertyAssociation.1}' with 0 values must have at least 1 values
6. /CaseProject/modified_model.aadl | line 261: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@47797401{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPropertyAssociation.0}' with 0 values must have at least 1 values
7. /CaseProject/modified_model.aadl | line 261: mismatched character ' ' expecting '>'
8. /CaseProject/modified_model.aadl | line 261: mismatched input ':' expecting '=>'
9. /CaseProject/modified_model.aadl | line 261: required (...)+ loop did not match anything at character '.'
10. /CaseProject/modified_model.aadl | line 263: missing EOF at '}'
