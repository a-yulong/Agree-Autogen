# Case91 Refactored Experiment Report

## Summary

- Setting: E5 (No Model Analyst)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 463.90
- Initial validation errors: 36
- Final validation errors: 20

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 20
- Warnings: 16

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: False
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 69181
- completion_tokens: 9283
- total_tokens: 78464

## Output Recovery

1. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] requirement_items_normalized - Normalized 6 classified requirement item(s).
3. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
4. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
5. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
6. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
7. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
8. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
9. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
10. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
11. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
12. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
13. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
14. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
15. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
16. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
17. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
18. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
19. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
20. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
21. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
22. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
23. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
24. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
25. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
26. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
27. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
28. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
29. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
30. [validation_repair] recovered_package_block - Recovered complete AADL package block.
31. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 15: Assume statements are allowed only in component types
2. /CaseProject/modified_model.aadl | line 15: Couldn't resolve reference to 'acc_pr'.
3. /CaseProject/modified_model.aadl | line 15: Couldn't resolve reference to 'main_cpu'.
4. /CaseProject/modified_model.aadl | line 15: Couldn't resolve reference to 'part1'.
5. /CaseProject/modified_model.aadl | line 15: named thing must be an expression with a type
6. /CaseProject/modified_model.aadl | line 16: Assume statements are allowed only in component types
7. /CaseProject/modified_model.aadl | line 16: Couldn't resolve reference to 'acc_hm_pr'.
8. /CaseProject/modified_model.aadl | line 16: Couldn't resolve reference to 'main_cpu'.
9. /CaseProject/modified_model.aadl | line 16: Couldn't resolve reference to 'part2'.
10. /CaseProject/modified_model.aadl | line 16: named thing must be an expression with a type
11. /CaseProject/modified_model.aadl | line 17: Assume statements are allowed only in component types
12. /CaseProject/modified_model.aadl | line 17: Couldn't resolve reference to 'ADIRUp_pr'.
13. /CaseProject/modified_model.aadl | line 17: Couldn't resolve reference to 'main_cpu'.
14. /CaseProject/modified_model.aadl | line 17: Couldn't resolve reference to 'part3'.
15. /CaseProject/modified_model.aadl | line 17: named thing must be an expression with a type
16. /CaseProject/modified_model.aadl | line 18: Assume statements are allowed only in component types
17. /CaseProject/modified_model.aadl | line 18: Couldn't resolve reference to 'SHM_pr'.
18. /CaseProject/modified_model.aadl | line 18: Couldn't resolve reference to 'main_cpu'.
19. /CaseProject/modified_model.aadl | line 18: Couldn't resolve reference to 'part4'.
20. /CaseProject/modified_model.aadl | line 18: named thing must be an expression with a type
