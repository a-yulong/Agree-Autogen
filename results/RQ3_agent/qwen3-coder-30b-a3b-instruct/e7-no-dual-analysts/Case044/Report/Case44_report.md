# Case44 Refactored Experiment Report

## Summary

- Setting: E7 (No Dual Analysts)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 122.00
- Initial validation errors: 0
- Final validation errors: 6

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 6
- AGREE errors: 0
- Warnings: 0

## Modules

- rag: True
- repair: True
- requirement_analyst: False
- model_analyst: False
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 4558
- completion_tokens: 688
- total_tokens: 5246

## Output Recovery

1. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
2. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
3. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
4. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.

## Final Diagnostics

1. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy (package specification)
2. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy (package specification)
3. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy (package specification)
4. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy (package specification)
5. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy (package specification)
6. Cannot analyze AADL specifications
