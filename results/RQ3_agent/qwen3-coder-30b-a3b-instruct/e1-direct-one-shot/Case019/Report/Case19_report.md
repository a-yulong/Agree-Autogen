# Case19 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 52.63
- Initial validation errors: 14
- Final validation errors: 14

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 14
- Warnings: 3

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 2057
- completion_tokens: 2105
- total_tokens: 4162

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 118: missing 'end' at 'agree_nodes'
2. /CaseProject/modified_model.aadl | line 120: mismatched input ':' expecting ';'
3. /CaseProject/modified_model.aadl | line 120: missing '.' at 'altitude'
4. /CaseProject/modified_model.aadl | line 142: missing EOF at 'agree_stmts'
5. /CaseProject/modified_model.aadl | line 144: mismatched character ' ' expecting '>'
6. /CaseProject/modified_model.aadl | line 144: mismatched character '=' expecting '-'
7. /CaseProject/modified_model.aadl | line 144: no viable alternative at character '>'
8. /CaseProject/modified_model.aadl | line 145: mismatched character ' ' expecting '>'
9. /CaseProject/modified_model.aadl | line 145: mismatched character '=' expecting '-'
10. /CaseProject/modified_model.aadl | line 145: no viable alternative at character '>'
11. /CaseProject/modified_model.aadl | line 148: mismatched character ' ' expecting '>'
12. /CaseProject/modified_model.aadl | line 151: no viable alternative at character '>'
13. /CaseProject/modified_model.aadl | line 154: mismatched character ' ' expecting '>'
14. /CaseProject/modified_model.aadl | line 157: no viable alternative at character '>'
