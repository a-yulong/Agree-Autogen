# Case53 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 47.26
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

- prompt_tokens: 690
- completion_tokens: 505
- total_tokens: 1195

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 41: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@4c24f3a2{platform:/resource/CaseProject/modified_model.aadl#Integer_Toy_Extended.Integer_Toy_Extended_public.top_level.Impl.agree}' must be set
2. /CaseProject/modified_model.aadl | line 41: mismatched input '{' expecting RULE_ANNEXTEXT
3. /CaseProject/modified_model.aadl | line 42: mismatched input 'properties' expecting 'end'
4. /CaseProject/modified_model.aadl | line 43: Couldn't resolve reference to property definition 'Input'. Property set name may be missing.
5. /CaseProject/modified_model.aadl | line 43: Couldn't resolve reference to property definition 'assume'. Property set name may be missing.
6. /CaseProject/modified_model.aadl | line 43: mismatched character ' ' expecting '-'
7. /CaseProject/modified_model.aadl | line 43: mismatched input ':' expecting ';'
8. /CaseProject/modified_model.aadl | line 43: missing '=>' at '"Input_assume"'
9. /CaseProject/modified_model.aadl | line 43: missing '=>' at '10'
10. /CaseProject/modified_model.aadl | line 44: Couldn't resolve reference to property definition 'Output'. Property set name may be missing.
11. /CaseProject/modified_model.aadl | line 44: Couldn't resolve reference to property definition 'guarantee'. Property set name may be missing.
12. /CaseProject/modified_model.aadl | line 44: mismatched character ' ' expecting '-'
13. /CaseProject/modified_model.aadl | line 44: mismatched input ':' expecting ';'
14. /CaseProject/modified_model.aadl | line 44: missing '=>' at '"Output_guarantee"'
15. /CaseProject/modified_model.aadl | line 44: missing '=>' at '50'
16. /CaseProject/modified_model.aadl | line 45: mismatched input 'properties' expecting RULE_ID
17. /CaseProject/modified_model.aadl | line 46: missing EOF at '}'
