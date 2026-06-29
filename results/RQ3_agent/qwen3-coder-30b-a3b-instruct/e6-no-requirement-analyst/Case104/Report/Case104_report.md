# Case104 Refactored Experiment Report

## Summary

- Setting: E6 (No Requirement Analyst)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 419.76
- Initial validation errors: 8
- Final validation errors: 24

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 24
- Warnings: 6

## Modules

- rag: True
- repair: True
- requirement_analyst: False
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 72205
- completion_tokens: 15821
- total_tokens: 88026

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
3. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
4. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
5. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
6. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
7. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
8. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
9. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
10. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
11. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
12. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
13. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
14. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
15. [validation_repair] recovered_package_block - Recovered complete AADL package block.
16. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
17. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
18. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
19. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
20. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
21. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
22. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
23. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
24. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
25. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
26. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
27. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
28. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
29. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
30. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
31. [validation_repair] recovered_package_block - Recovered complete AADL package block.
32. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 75: Couldn't resolve reference to 'acc1'.
2. /CaseProject/modified_model.aadl | line 75: Couldn't resolve reference to 'acc1_input'.
3. /CaseProject/modified_model.aadl | line 75: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
4. /CaseProject/modified_model.aadl | line 75: named thing must be an expression with a type
5. /CaseProject/modified_model.aadl | line 76: Couldn't resolve reference to 'acc2'.
6. /CaseProject/modified_model.aadl | line 76: Couldn't resolve reference to 'acc2_input'.
7. /CaseProject/modified_model.aadl | line 76: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
8. /CaseProject/modified_model.aadl | line 76: named thing must be an expression with a type
9. /CaseProject/modified_model.aadl | line 77: Couldn't resolve reference to 'acc3'.
10. /CaseProject/modified_model.aadl | line 77: Couldn't resolve reference to 'acc3_input'.
11. /CaseProject/modified_model.aadl | line 77: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
12. /CaseProject/modified_model.aadl | line 77: named thing must be an expression with a type
13. /CaseProject/modified_model.aadl | line 78: Couldn't resolve reference to 'acc4'.
14. /CaseProject/modified_model.aadl | line 78: Couldn't resolve reference to 'acc4_input'.
15. /CaseProject/modified_model.aadl | line 78: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
16. /CaseProject/modified_model.aadl | line 78: named thing must be an expression with a type
17. /CaseProject/modified_model.aadl | line 79: Couldn't resolve reference to 'acc5'.
18. /CaseProject/modified_model.aadl | line 79: Couldn't resolve reference to 'acc5_input'.
19. /CaseProject/modified_model.aadl | line 79: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
20. /CaseProject/modified_model.aadl | line 79: named thing must be an expression with a type
21. /CaseProject/modified_model.aadl | line 80: Couldn't resolve reference to 'acc6'.
22. /CaseProject/modified_model.aadl | line 80: Couldn't resolve reference to 'acc6_input'.
23. /CaseProject/modified_model.aadl | line 80: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
24. /CaseProject/modified_model.aadl | line 80: named thing must be an expression with a type
