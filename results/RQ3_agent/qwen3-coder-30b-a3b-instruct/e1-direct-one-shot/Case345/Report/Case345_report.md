# Case345 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 113.72
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
- completion_tokens: 2967
- total_tokens: 7533

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 259: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexLibraryImpl@3b170235{platform:/resource/CaseProject/modified_model.aadl#flyByWire_soft.flyByWire_soft_public.agree}' must be set
2. /CaseProject/modified_model.aadl | line 259: mismatched input '{' expecting RULE_ANNEXTEXT
3. /CaseProject/modified_model.aadl | line 261: Couldn't resolve reference to property definition 'Bound_Cde_AileronL_Output'. Property set name may be missing.
4. /CaseProject/modified_model.aadl | line 261: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@10166230{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPropertyAssociation.0}' with 0 values must have at least 1 values
5. /CaseProject/modified_model.aadl | line 261: mismatched character ' ' expecting '>'
6. /CaseProject/modified_model.aadl | line 261: mismatched input ':' expecting '=>'
7. /CaseProject/modified_model.aadl | line 264: missing EOF at 'property'
8. /CaseProject/modified_model.aadl | line 269: mismatched character ' ' expecting '>'
9. /CaseProject/modified_model.aadl | line 269: mismatched character '=' expecting '-'
10. /CaseProject/modified_model.aadl | line 269: no viable alternative at character '>'
