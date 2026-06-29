# Case91 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 727.22
- Initial validation errors: 50
- Final validation errors: 50

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 50
- Warnings: 16

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 86497
- completion_tokens: 13137
- total_tokens: 99634

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 6 classified requirement item(s).
4. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
5. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
6. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
7. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
8. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
9. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
10. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
11. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
12. [validation_repair] recovered_package_block - Recovered complete AADL package block.
13. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
14. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
15. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
16. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
17. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
18. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
19. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
20. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
21. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
22. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
23. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
24. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
25. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
26. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
27. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
28. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
29. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
30. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
31. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
32. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
33. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
34. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 187: Assume statements are allowed only in component types
2. /CaseProject/modified_model.aadl | line 187: Couldn't resolve reference to 'C1'.
3. /CaseProject/modified_model.aadl | line 187: Couldn't resolve reference to 'acc1_input'.
4. /CaseProject/modified_model.aadl | line 187: Couldn't resolve reference to 'acc1_output'.
5. /CaseProject/modified_model.aadl | line 187: Couldn't resolve reference to 'acc_hm_pr'.
6. /CaseProject/modified_model.aadl | line 187: Couldn't resolve reference to 'acc_pr'.
7. /CaseProject/modified_model.aadl | line 187: left side of binary expression '=>' is of type '<error>' but must be of type 'bool'
8. /CaseProject/modified_model.aadl | line 187: left side of binary expression 'and' is of type '<error>' but must be of type 'bool'
9. /CaseProject/modified_model.aadl | line 187: named thing must be an expression with a type
10. /CaseProject/modified_model.aadl | line 187: right side of binary expression '=>' is of type '<error>' but must be of type 'bool'
11. /CaseProject/modified_model.aadl | line 187: right side of binary expression 'and' is of type '<error>' but must be of type 'bool'
12. /CaseProject/modified_model.aadl | line 190: Assume statements are allowed only in component types
13. /CaseProject/modified_model.aadl | line 190: Couldn't resolve reference to 'C2'.
14. /CaseProject/modified_model.aadl | line 190: Couldn't resolve reference to 'acc2_input'.
15. /CaseProject/modified_model.aadl | line 190: Couldn't resolve reference to 'acc2_output'.
16. /CaseProject/modified_model.aadl | line 190: Couldn't resolve reference to 'acc_hm_pr'.
17. /CaseProject/modified_model.aadl | line 190: Couldn't resolve reference to 'acc_pr'.
18. /CaseProject/modified_model.aadl | line 190: left side of binary expression '=>' is of type '<error>' but must be of type 'bool'
19. /CaseProject/modified_model.aadl | line 190: left side of binary expression 'and' is of type '<error>' but must be of type 'bool'
20. /CaseProject/modified_model.aadl | line 190: named thing must be an expression with a type
21. /CaseProject/modified_model.aadl | line 190: right side of binary expression '=>' is of type '<error>' but must be of type 'bool'
22. /CaseProject/modified_model.aadl | line 190: right side of binary expression 'and' is of type '<error>' but must be of type 'bool'
23. /CaseProject/modified_model.aadl | line 193: Assume statements are allowed only in component types
24. /CaseProject/modified_model.aadl | line 193: Couldn't resolve reference to 'acc_pr'.
25. /CaseProject/modified_model.aadl | line 193: Couldn't resolve reference to 'main_cpu'.
26. /CaseProject/modified_model.aadl | line 193: Couldn't resolve reference to 'part1'.
27. /CaseProject/modified_model.aadl | line 193: left side of binary expression '=>' is of type '<error>' but must be of type 'bool'
28. /CaseProject/modified_model.aadl | line 193: named thing must be an expression with a type
29. /CaseProject/modified_model.aadl | line 193: right side of binary expression '=>' is of type '<error>' but must be of type 'bool'
30. /CaseProject/modified_model.aadl | line 196: Assume statements are allowed only in component types
31. /CaseProject/modified_model.aadl | line 196: Couldn't resolve reference to 'acc_hm_pr'.
32. /CaseProject/modified_model.aadl | line 196: Couldn't resolve reference to 'main_cpu'.
33. /CaseProject/modified_model.aadl | line 196: Couldn't resolve reference to 'part2'.
34. /CaseProject/modified_model.aadl | line 196: left side of binary expression '=>' is of type '<error>' but must be of type 'bool'
35. /CaseProject/modified_model.aadl | line 196: named thing must be an expression with a type
36. /CaseProject/modified_model.aadl | line 196: right side of binary expression '=>' is of type '<error>' but must be of type 'bool'
37. /CaseProject/modified_model.aadl | line 199: Assume statements are allowed only in component types
38. /CaseProject/modified_model.aadl | line 199: Couldn't resolve reference to 'ADIRUp_pr'.
39. /CaseProject/modified_model.aadl | line 199: Couldn't resolve reference to 'main_cpu'.
40. /CaseProject/modified_model.aadl | line 199: Couldn't resolve reference to 'part3'.
41. /CaseProject/modified_model.aadl | line 199: left side of binary expression '=>' is of type '<error>' but must be of type 'bool'
42. /CaseProject/modified_model.aadl | line 199: named thing must be an expression with a type
43. /CaseProject/modified_model.aadl | line 199: right side of binary expression '=>' is of type '<error>' but must be of type 'bool'
44. /CaseProject/modified_model.aadl | line 202: Assume statements are allowed only in component types
45. /CaseProject/modified_model.aadl | line 202: Couldn't resolve reference to 'SHM_pr'.
46. /CaseProject/modified_model.aadl | line 202: Couldn't resolve reference to 'main_cpu'.
47. /CaseProject/modified_model.aadl | line 202: Couldn't resolve reference to 'part4'.
48. /CaseProject/modified_model.aadl | line 202: left side of binary expression '=>' is of type '<error>' but must be of type 'bool'
49. /CaseProject/modified_model.aadl | line 202: named thing must be an expression with a type
50. /CaseProject/modified_model.aadl | line 202: right side of binary expression '=>' is of type '<error>' but must be of type 'bool'
