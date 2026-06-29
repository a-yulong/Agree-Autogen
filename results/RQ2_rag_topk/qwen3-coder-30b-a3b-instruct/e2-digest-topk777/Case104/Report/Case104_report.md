# Case104 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 680.21
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
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 84802
- completion_tokens: 17640
- total_tokens: 102442

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
16. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
17. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
18. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
19. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
20. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
21. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
22. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
23. [validation_repair] recovered_package_block - Recovered complete AADL package block.
24. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
25. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
26. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
27. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
28. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
29. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
30. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
31. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
32. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
33. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
34. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
35. [validation_repair] recovered_package_block - Recovered complete AADL package block.
36. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 75: Couldn't resolve reference to 'acc1'.
2. /CaseProject/modified_model.aadl | line 75: Couldn't resolve reference to 'acc1_input'.
3. /CaseProject/modified_model.aadl | line 75: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
4. /CaseProject/modified_model.aadl | line 75: named thing must be an expression with a type
5. /CaseProject/modified_model.aadl | line 77: Couldn't resolve reference to 'acc2'.
6. /CaseProject/modified_model.aadl | line 77: Couldn't resolve reference to 'acc2_input'.
7. /CaseProject/modified_model.aadl | line 77: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
8. /CaseProject/modified_model.aadl | line 77: named thing must be an expression with a type
9. /CaseProject/modified_model.aadl | line 79: Couldn't resolve reference to 'acc3'.
10. /CaseProject/modified_model.aadl | line 79: Couldn't resolve reference to 'acc3_input'.
11. /CaseProject/modified_model.aadl | line 79: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
12. /CaseProject/modified_model.aadl | line 79: named thing must be an expression with a type
13. /CaseProject/modified_model.aadl | line 81: Couldn't resolve reference to 'acc4'.
14. /CaseProject/modified_model.aadl | line 81: Couldn't resolve reference to 'acc4_input'.
15. /CaseProject/modified_model.aadl | line 81: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
16. /CaseProject/modified_model.aadl | line 81: named thing must be an expression with a type
17. /CaseProject/modified_model.aadl | line 83: Couldn't resolve reference to 'acc5'.
18. /CaseProject/modified_model.aadl | line 83: Couldn't resolve reference to 'acc5_input'.
19. /CaseProject/modified_model.aadl | line 83: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
20. /CaseProject/modified_model.aadl | line 83: named thing must be an expression with a type
21. /CaseProject/modified_model.aadl | line 85: Couldn't resolve reference to 'acc6'.
22. /CaseProject/modified_model.aadl | line 85: Couldn't resolve reference to 'acc6_input'.
23. /CaseProject/modified_model.aadl | line 85: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
24. /CaseProject/modified_model.aadl | line 85: named thing must be an expression with a type
