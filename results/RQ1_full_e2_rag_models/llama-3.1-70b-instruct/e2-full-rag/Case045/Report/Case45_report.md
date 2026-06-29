# Case45 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 316.15
- Initial validation errors: 9
- Final validation errors: 13

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 6
- AGREE errors: 7
- Warnings: 0

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 26245
- completion_tokens: 5048
- total_tokens: 31293

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 4 classified requirement item(s).
4. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
5. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
6. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
7. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
8. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
9. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
10. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
11. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
12. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
13. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
14. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
15. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
16. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
17. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy (package specification)
2. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy (package specification)
3. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy (package specification)
4. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy (package specification)
5. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy (package specification)
6. Cannot analyze AADL specifications
7. /CaseProject/modified_model.aadl | line 23: Duplicate Element 'mode'
8. /CaseProject/modified_model.aadl | line 24: Duplicate Element 'mode'
9. /CaseProject/modified_model.aadl | line 24: mismatched input '': int = mode + 1;\r\n  guarantee "mode init": mode >= 0;\r\n  guarantee "mode increasing": mode'' expecting ':'
10. /CaseProject/modified_model.aadl | line 27: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
11. /CaseProject/modified_model.aadl | line 27: named thing must be an expression with a type
12. /CaseProject/modified_model.aadl | line 28: left and right sides of binary expression '!=' are of type '<error>' and 'int', but must be of the same type
13. /CaseProject/modified_model.aadl | line 28: named thing must be an expression with a type
