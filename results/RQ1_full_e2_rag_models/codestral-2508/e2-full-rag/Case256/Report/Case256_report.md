# Case256 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 392.07
- Initial validation errors: 0
- Final validation errors: 1

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 1
- AGREE errors: 0
- Warnings: 0

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 7062
- completion_tokens: 1471
- total_tokens: 8533

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 1 classified requirement item(s).
4. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
5. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
6. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
7. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.

## Final Diagnostics

1. AADL Inspector exception: Command '['E:\\AI-1.10\\bin\\AADLInspector.exe', '-a', 'C:\\Users\\25780\\Desktop\\Exp_Data\\Result_v4.0\\full_e2_rag_3models_20260608_0510\\codestral-2508\\e2-full-rag\\Case256\\Report\\aadl_inspector_input.aic', '--plugin', 'Static.parse', '--result', 'C:\\Users\\25780\\Desktop\\Exp_Data\\Result_v4.0\\full_e2_rag_3models_20260608_0510\\codestral-2508\\e2-full-rag\\Case256\\Report\\aadl_inspector_report.txt', '--show', 'false', '--aadlVersion', 'V2']' timed out after 300 seconds
