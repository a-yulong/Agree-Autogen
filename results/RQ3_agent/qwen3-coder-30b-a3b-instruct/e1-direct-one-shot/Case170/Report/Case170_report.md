# Case170 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 75.79
- Initial validation errors: 5
- Final validation errors: 5

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 5
- Warnings: 2

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 1774
- completion_tokens: 1617
- total_tokens: 3391

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 225: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexLibraryImpl@49b89425{platform:/resource/CaseProject/modified_model.aadl#Ardupilot_Software.Ardupilot_Software_public.agree}' must be set
2. /CaseProject/modified_model.aadl | line 225: mismatched input '{' expecting RULE_ANNEXTEXT
3. /CaseProject/modified_model.aadl | line 229: Couldn't resolve reference to property definition 'Always_Valid'. Property set name may be missing.
4. /CaseProject/modified_model.aadl | line 229: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@760f1081{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPropertyAssociation.0}' with 0 values must have at least 1 values
5. /CaseProject/modified_model.aadl | line 229: mismatched input ':' expecting '=>'
