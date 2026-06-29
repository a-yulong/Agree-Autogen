# Case158 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 43.21
- Initial validation errors: 13
- Final validation errors: 13

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 13
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
- completion_tokens: 1601
- total_tokens: 3375

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 225: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexLibraryImpl@14457a95{platform:/resource/CaseProject/modified_model.aadl#Ardupilot_Software.Ardupilot_Software_public.agree}' must be set
2. /CaseProject/modified_model.aadl | line 225: mismatched input '{' expecting RULE_ANNEXTEXT
3. /CaseProject/modified_model.aadl | line 228: Couldn't resolve reference to property definition 'and'. Property set name may be missing.
4. /CaseProject/modified_model.aadl | line 228: Couldn't resolve reference to property definition 'angle'. Property set name may be missing.
5. /CaseProject/modified_model.aadl | line 228: The required feature 'ownedValue' of 'org.osate.aadl2.impl.ModalPropertyValueImpl@123a21ad{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPropertyAssociation.1/@ownedValue.0}' must be set
6. /CaseProject/modified_model.aadl | line 228: The required feature 'ownedValue' of 'org.osate.aadl2.impl.ModalPropertyValueImpl@7a4c1a6c{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPropertyAssociation.0/@ownedValue.0}' must be set
7. /CaseProject/modified_model.aadl | line 228: mismatched character ' ' expecting '>'
8. /CaseProject/modified_model.aadl | line 228: mismatched character '=' expecting '-'
9. /CaseProject/modified_model.aadl | line 228: missing '=>' at '0'
10. /CaseProject/modified_model.aadl | line 228: missing '=>' at '100'
11. /CaseProject/modified_model.aadl | line 228: missing '=>' at 'angle'
12. /CaseProject/modified_model.aadl | line 228: no viable alternative at character '>'
13. /CaseProject/modified_model.aadl | line 229: mismatched input '}' expecting 'end'
