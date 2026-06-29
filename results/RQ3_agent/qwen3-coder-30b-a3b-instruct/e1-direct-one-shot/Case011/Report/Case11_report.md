# Case11 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 61.23
- Initial validation errors: 8
- Final validation errors: 8

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 8
- Warnings: 1

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 2074
- completion_tokens: 1898
- total_tokens: 3972

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 24: Element of the same name ('gcasRequested') in AGREE Annex in 'GCAS_Monitor.GCAS_Monitor_impl'
2. /CaseProject/modified_model.aadl | line 29: mismatched input '=' expecting ':'
3. /CaseProject/modified_model.aadl | line 30: mismatched input '=' expecting ':'
4. /CaseProject/modified_model.aadl | line 31: mismatched input '=' expecting ':'
5. /CaseProject/modified_model.aadl | line 37: Feature of the same name ('gcasRequested') in component type
6. /CaseProject/modified_model.aadl | line 37: Guarantee statements are allowed only in component types
7. /CaseProject/modified_model.aadl | line 37: mismatched input '=' expecting RULE_STRING
8. /CaseProject/modified_model.aadl | line 39: missing ';' at 'end'
