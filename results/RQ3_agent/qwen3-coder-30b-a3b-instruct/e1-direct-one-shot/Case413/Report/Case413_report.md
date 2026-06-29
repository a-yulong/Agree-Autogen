# Case413 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 41.20
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

- prompt_tokens: 2785
- completion_tokens: 110
- total_tokens: 2895

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 14: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@e26a3df{platform:/resource/CaseProject/modified_model.aadl#BA_example2.BA_example2_public.speed.i.agree}' must be set
2. /CaseProject/modified_model.aadl | line 14: mismatched input '{' expecting RULE_ANNEXTEXT
3. /CaseProject/modified_model.aadl | line 15: mismatched input 'properties' expecting 'end'
4. /CaseProject/modified_model.aadl | line 16: Couldn't resolve reference to property definition 'Contract'. Property set name may be missing.
5. /CaseProject/modified_model.aadl | line 18: missing EOF at '}'
