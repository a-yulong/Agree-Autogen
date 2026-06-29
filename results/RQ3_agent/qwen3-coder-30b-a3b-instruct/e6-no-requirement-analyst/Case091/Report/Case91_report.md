# Case91 Refactored Experiment Report

## Summary

- Setting: E6 (No Requirement Analyst)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 513.13
- Initial validation errors: 34
- Final validation errors: 34

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 34
- Warnings: 16

## Modules

- rag: True
- repair: True
- requirement_analyst: False
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 76719
- completion_tokens: 18087
- total_tokens: 94806

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
3. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
4. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
5. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
6. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
7. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
8. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
9. [validation_repair] recovered_package_block - Recovered complete AADL package block.
10. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
11. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
12. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
13. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
14. [validation_repair] recovered_package_block - Recovered complete AADL package block.
15. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
16. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
17. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
18. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
19. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
20. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
21. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
22. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
23. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
24. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
25. [validation_repair] recovered_package_block - Recovered complete AADL package block.
26. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
27. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
28. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
29. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
30. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
31. [validation_repair] recovered_package_block - Recovered complete AADL package block.
32. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 186: Assume statements are allowed only in component types
2. /CaseProject/modified_model.aadl | line 186: Couldn't resolve reference to 'impl'.
3. /CaseProject/modified_model.aadl | line 186: named thing must be an expression with a type
4. /CaseProject/modified_model.aadl | line 188: Couldn't resolve reference to 'C1'.
5. /CaseProject/modified_model.aadl | line 188: Couldn't resolve reference to 'acc1_input'.
6. /CaseProject/modified_model.aadl | line 188: Couldn't resolve reference to 'acc1_output'.
7. /CaseProject/modified_model.aadl | line 188: Couldn't resolve reference to 'acc_hm_pr'.
8. /CaseProject/modified_model.aadl | line 188: Couldn't resolve reference to 'acc_pr'.
9. /CaseProject/modified_model.aadl | line 188: Guarantee statements are allowed only in component types
10. /CaseProject/modified_model.aadl | line 188: named thing must be an expression with a type
11. /CaseProject/modified_model.aadl | line 190: Couldn't resolve reference to 'C2'.
12. /CaseProject/modified_model.aadl | line 190: Couldn't resolve reference to 'acc2_input'.
13. /CaseProject/modified_model.aadl | line 190: Couldn't resolve reference to 'acc2_output'.
14. /CaseProject/modified_model.aadl | line 190: Couldn't resolve reference to 'acc_hm_pr'.
15. /CaseProject/modified_model.aadl | line 190: Couldn't resolve reference to 'acc_pr'.
16. /CaseProject/modified_model.aadl | line 190: Guarantee statements are allowed only in component types
17. /CaseProject/modified_model.aadl | line 190: named thing must be an expression with a type
18. /CaseProject/modified_model.aadl | line 192: Assume statements are allowed only in component types
19. /CaseProject/modified_model.aadl | line 193: Couldn't resolve reference to 'acc_pr'.
20. /CaseProject/modified_model.aadl | line 193: Couldn't resolve reference to 'main_cpu'.
21. /CaseProject/modified_model.aadl | line 193: Couldn't resolve reference to 'part1'.
22. /CaseProject/modified_model.aadl | line 193: named thing must be an expression with a type
23. /CaseProject/modified_model.aadl | line 194: Couldn't resolve reference to 'acc_hm_pr'.
24. /CaseProject/modified_model.aadl | line 194: Couldn't resolve reference to 'main_cpu'.
25. /CaseProject/modified_model.aadl | line 194: Couldn't resolve reference to 'part2'.
26. /CaseProject/modified_model.aadl | line 194: named thing must be an expression with a type
27. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to 'ADIRUp_pr'.
28. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to 'main_cpu'.
29. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to 'part3'.
30. /CaseProject/modified_model.aadl | line 195: named thing must be an expression with a type
31. /CaseProject/modified_model.aadl | line 196: Couldn't resolve reference to 'SHM_pr'.
32. /CaseProject/modified_model.aadl | line 196: Couldn't resolve reference to 'main_cpu'.
33. /CaseProject/modified_model.aadl | line 196: Couldn't resolve reference to 'part4'.
34. /CaseProject/modified_model.aadl | line 196: named thing must be an expression with a type
