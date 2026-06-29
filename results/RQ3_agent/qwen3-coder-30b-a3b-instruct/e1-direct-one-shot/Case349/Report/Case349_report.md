# Case349 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 112.79
- Initial validation errors: 7
- Final validation errors: 7

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 7
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
- completion_tokens: 2844
- total_tokens: 7410

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 259: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexLibraryImpl@2e362407{platform:/resource/CaseProject/modified_model.aadl#flyByWire_soft.flyByWire_soft_public.agree}' must be set
2. /CaseProject/modified_model.aadl | line 259: mismatched input '{' expecting RULE_ANNEXTEXT
3. /CaseProject/modified_model.aadl | line 261: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Cde_AileronL_Output'. For classifier references use classifier( <ref> ).
4. /CaseProject/modified_model.aadl | line 261: Couldn't resolve reference to property definition 'Bound'. Property set name may be missing.
5. /CaseProject/modified_model.aadl | line 261: missing '=>' at '('
6. /CaseProject/modified_model.aadl | line 262: mismatched input 'properties' expecting RULE_ID
7. /CaseProject/modified_model.aadl | line 263: missing EOF at '}'
