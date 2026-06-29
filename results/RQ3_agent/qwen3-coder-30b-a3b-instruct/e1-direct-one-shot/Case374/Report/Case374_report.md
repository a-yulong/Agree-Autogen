# Case374 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 63.82
- Initial validation errors: 15
- Final validation errors: 15

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 15
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
- completion_tokens: 2887
- total_tokens: 7453

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 259: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexLibraryImpl@8f2e3e6{platform:/resource/CaseProject/modified_model.aadl#flyByWire_soft.flyByWire_soft_public.agree}' must be set
2. /CaseProject/modified_model.aadl | line 259: mismatched input '{' expecting RULE_ANNEXTEXT
3. /CaseProject/modified_model.aadl | line 261: Couldn't resolve reference to property definition 'Cde_AileronR_Output_Bounded'. Property set name may be missing.
4. /CaseProject/modified_model.aadl | line 261: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@32ba5c65{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPropertyAssociation.0}' with 0 values must have at least 1 values
5. /CaseProject/modified_model.aadl | line 261: mismatched character ' ' expecting '>'
6. /CaseProject/modified_model.aadl | line 261: mismatched input ':' expecting '=>'
7. /CaseProject/modified_model.aadl | line 262: Couldn't resolve reference to property definition 'Cde_AileronR_Output_Lower_Bound'. Property set name may be missing.
8. /CaseProject/modified_model.aadl | line 262: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@780129bc{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPropertyAssociation.1}' with 0 values must have at least 1 values
9. /CaseProject/modified_model.aadl | line 262: mismatched character ' ' expecting '>'
10. /CaseProject/modified_model.aadl | line 262: mismatched input ':' expecting '=>'
11. /CaseProject/modified_model.aadl | line 263: Couldn't resolve reference to property definition 'Cde_AileronR_Output_Upper_Bound'. Property set name may be missing.
12. /CaseProject/modified_model.aadl | line 263: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@44de8e00{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPropertyAssociation.2}' with 0 values must have at least 1 values
13. /CaseProject/modified_model.aadl | line 263: mismatched character ' ' expecting '>'
14. /CaseProject/modified_model.aadl | line 263: mismatched input ':' expecting '=>'
15. /CaseProject/modified_model.aadl | line 265: missing EOF at '}'
