# Case91 Refactored Experiment Report

## Summary

- Setting: E7 (No Dual Analysts)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 405.65
- Initial validation errors: 39
- Final validation errors: 38

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 38
- Warnings: 16

## Modules

- rag: True
- repair: True
- requirement_analyst: False
- model_analyst: False
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 72738
- completion_tokens: 8369
- total_tokens: 81107

## Output Recovery

1. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
2. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
3. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
4. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
5. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
6. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
7. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
8. [validation_repair] recovered_package_block - Recovered complete AADL package block.
9. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
10. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
11. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
12. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
13. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
14. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
15. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
16. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
17. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
18. [validation_repair] recovered_package_block - Recovered complete AADL package block.
19. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
20. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
21. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
22. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
23. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
24. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
25. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
26. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
27. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
28. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
29. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 187: Assume statements are allowed only in component types
2. /CaseProject/modified_model.aadl | line 187: Couldn't resolve reference to 'DeOS'.
3. /CaseProject/modified_model.aadl | line 187: Couldn't resolve reference to 'EMV2'.
4. /CaseProject/modified_model.aadl | line 187: Couldn't resolve reference to 'VxWorks653'.
5. /CaseProject/modified_model.aadl | line 187: named thing must be an expression with a type
6. /CaseProject/modified_model.aadl | line 191: Couldn't resolve reference to 'acc1_input'.
7. /CaseProject/modified_model.aadl | line 191: Couldn't resolve reference to 'acc1_output'.
8. /CaseProject/modified_model.aadl | line 191: Couldn't resolve reference to 'acc_hm_pr'.
9. /CaseProject/modified_model.aadl | line 191: Couldn't resolve reference to 'acc_pr'.
10. /CaseProject/modified_model.aadl | line 191: Guarantee statements are allowed only in component types
11. /CaseProject/modified_model.aadl | line 191: left side of binary expression '=>' is of type '<error>' but must be of type 'bool'
12. /CaseProject/modified_model.aadl | line 191: named thing must be an expression with a type
13. /CaseProject/modified_model.aadl | line 191: right side of binary expression '=>' is of type '<error>' but must be of type 'bool'
14. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to 'acc2_input'.
15. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to 'acc2_output'.
16. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to 'acc_hm_pr'.
17. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to 'acc_pr'.
18. /CaseProject/modified_model.aadl | line 195: Guarantee statements are allowed only in component types
19. /CaseProject/modified_model.aadl | line 195: left side of binary expression '=>' is of type '<error>' but must be of type 'bool'
20. /CaseProject/modified_model.aadl | line 195: named thing must be an expression with a type
21. /CaseProject/modified_model.aadl | line 195: right side of binary expression '=>' is of type '<error>' but must be of type 'bool'
22. /CaseProject/modified_model.aadl | line 199: Assume statements are allowed only in component types
23. /CaseProject/modified_model.aadl | line 202: Couldn't resolve reference to 'acc_pr'.
24. /CaseProject/modified_model.aadl | line 202: Couldn't resolve reference to 'main_cpu'.
25. /CaseProject/modified_model.aadl | line 202: Couldn't resolve reference to 'part1'.
26. /CaseProject/modified_model.aadl | line 202: named thing must be an expression with a type
27. /CaseProject/modified_model.aadl | line 205: Couldn't resolve reference to 'acc_hm_pr'.
28. /CaseProject/modified_model.aadl | line 205: Couldn't resolve reference to 'main_cpu'.
29. /CaseProject/modified_model.aadl | line 205: Couldn't resolve reference to 'part2'.
30. /CaseProject/modified_model.aadl | line 205: named thing must be an expression with a type
31. /CaseProject/modified_model.aadl | line 208: Couldn't resolve reference to 'ADIRUp_pr'.
32. /CaseProject/modified_model.aadl | line 208: Couldn't resolve reference to 'main_cpu'.
33. /CaseProject/modified_model.aadl | line 208: Couldn't resolve reference to 'part3'.
34. /CaseProject/modified_model.aadl | line 208: named thing must be an expression with a type
35. /CaseProject/modified_model.aadl | line 211: Couldn't resolve reference to 'SHM_pr'.
36. /CaseProject/modified_model.aadl | line 211: Couldn't resolve reference to 'main_cpu'.
37. /CaseProject/modified_model.aadl | line 211: Couldn't resolve reference to 'part4'.
38. /CaseProject/modified_model.aadl | line 211: named thing must be an expression with a type
