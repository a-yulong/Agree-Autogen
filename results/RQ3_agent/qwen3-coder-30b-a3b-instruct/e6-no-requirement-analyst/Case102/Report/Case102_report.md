# Case102 Refactored Experiment Report

## Summary

- Setting: E6 (No Requirement Analyst)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 421.11
- Initial validation errors: 46
- Final validation errors: 45

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 2
- AGREE errors: 43
- Warnings: 12

## Modules

- rag: True
- repair: True
- requirement_analyst: False
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 81193
- completion_tokens: 10827
- total_tokens: 92020

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
3. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
4. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
5. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
6. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
7. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
8. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
9. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
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
30. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
31. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. parsing Package_Specification, Empty packages are not allowed
2. Cannot parse AADL specifications
3. /CaseProject/modified_model.aadl | line 183: Assume statements are allowed only in component types
4. /CaseProject/modified_model.aadl | line 183: Couldn't resolve reference to 'DeOS'.
5. /CaseProject/modified_model.aadl | line 183: Couldn't resolve reference to 'EMV2'.
6. /CaseProject/modified_model.aadl | line 183: Couldn't resolve reference to 'VxWorks653'.
7. /CaseProject/modified_model.aadl | line 183: named thing must be an expression with a type
8. /CaseProject/modified_model.aadl | line 186: Couldn't resolve reference to 'C1'.
9. /CaseProject/modified_model.aadl | line 186: Couldn't resolve reference to 'acc1_input'.
10. /CaseProject/modified_model.aadl | line 186: Couldn't resolve reference to 'acc1_output'.
11. /CaseProject/modified_model.aadl | line 186: Couldn't resolve reference to 'acc_hm_pr'.
12. /CaseProject/modified_model.aadl | line 186: Couldn't resolve reference to 'acc_pr'.
13. /CaseProject/modified_model.aadl | line 186: Guarantee statements are allowed only in component types
14. /CaseProject/modified_model.aadl | line 186: named thing must be an expression with a type
15. /CaseProject/modified_model.aadl | line 189: Couldn't resolve reference to 'C2'.
16. /CaseProject/modified_model.aadl | line 189: Couldn't resolve reference to 'acc2_input'.
17. /CaseProject/modified_model.aadl | line 189: Couldn't resolve reference to 'acc2_output'.
18. /CaseProject/modified_model.aadl | line 189: Couldn't resolve reference to 'acc_hm_pr'.
19. /CaseProject/modified_model.aadl | line 189: Couldn't resolve reference to 'acc_pr'.
20. /CaseProject/modified_model.aadl | line 189: Guarantee statements are allowed only in component types
21. /CaseProject/modified_model.aadl | line 189: named thing must be an expression with a type
22. /CaseProject/modified_model.aadl | line 192: Assume statements are allowed only in component types
23. /CaseProject/modified_model.aadl | line 192: Couldn't resolve reference to 'acc_pr'.
24. /CaseProject/modified_model.aadl | line 192: Couldn't resolve reference to 'main_cpu'.
25. /CaseProject/modified_model.aadl | line 192: Couldn't resolve reference to 'part1'.
26. /CaseProject/modified_model.aadl | line 192: Expression for assume statement is of type '<error>' but must be of type 'bool'
27. /CaseProject/modified_model.aadl | line 192: named thing must be an expression with a type
28. /CaseProject/modified_model.aadl | line 195: Assume statements are allowed only in component types
29. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to 'acc_hm_pr'.
30. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to 'main_cpu'.
31. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to 'part2'.
32. /CaseProject/modified_model.aadl | line 195: Expression for assume statement is of type '<error>' but must be of type 'bool'
33. /CaseProject/modified_model.aadl | line 195: named thing must be an expression with a type
34. /CaseProject/modified_model.aadl | line 198: Assume statements are allowed only in component types
35. /CaseProject/modified_model.aadl | line 198: Couldn't resolve reference to 'ADIRUp_pr'.
36. /CaseProject/modified_model.aadl | line 198: Couldn't resolve reference to 'main_cpu'.
37. /CaseProject/modified_model.aadl | line 198: Couldn't resolve reference to 'part3'.
38. /CaseProject/modified_model.aadl | line 198: Expression for assume statement is of type '<error>' but must be of type 'bool'
39. /CaseProject/modified_model.aadl | line 198: named thing must be an expression with a type
40. /CaseProject/modified_model.aadl | line 201: Assume statements are allowed only in component types
41. /CaseProject/modified_model.aadl | line 201: Couldn't resolve reference to 'SHM_pr'.
42. /CaseProject/modified_model.aadl | line 201: Couldn't resolve reference to 'main_cpu'.
43. /CaseProject/modified_model.aadl | line 201: Couldn't resolve reference to 'part4'.
44. /CaseProject/modified_model.aadl | line 201: Expression for assume statement is of type '<error>' but must be of type 'bool'
45. /CaseProject/modified_model.aadl | line 201: named thing must be an expression with a type
