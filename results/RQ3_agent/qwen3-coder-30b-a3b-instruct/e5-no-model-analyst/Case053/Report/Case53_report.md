# Case53 Refactored Experiment Report

## Summary

- Setting: E5 (No Model Analyst)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 102.72
- Initial validation errors: 0
- Final validation errors: 9

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 9
- AGREE errors: 0
- Warnings: 0

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: False
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 5423
- completion_tokens: 789
- total_tokens: 6212

## Output Recovery

1. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] requirement_items_normalized - Normalized 2 classified requirement item(s).
3. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
4. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
5. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
6. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.

## Final Diagnostics

1. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy_Extended (package specification)
2. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy_Extended (package specification)
3. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy_Extended (package specification)
4. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy_Extended (package specification)
5. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy_Extended (package specification)
6. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy_Extended (package specification)
7. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy_Extended (package specification)
8. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy_Extended (package specification)
9. Cannot analyze AADL specifications
