# Case118 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 212.76
- Initial validation errors: 4
- Final validation errors: 4

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 4
- Warnings: 4

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 14695
- completion_tokens: 3338
- total_tokens: 18033

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 2 classified requirement item(s).
4. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
5. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
6. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
7. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 428: left side of binary expression '=>' is of type 'int' but must be of type 'bool'
2. /CaseProject/modified_model.aadl | line 428: right side of binary expression '=>' is of type 'int' but must be of type 'bool'
3. /CaseProject/modified_model.aadl | line 429: left side of binary expression '=>' is of type 'int' but must be of type 'bool'
4. /CaseProject/modified_model.aadl | line 429: right side of binary expression '=>' is of type 'int' but must be of type 'bool'
