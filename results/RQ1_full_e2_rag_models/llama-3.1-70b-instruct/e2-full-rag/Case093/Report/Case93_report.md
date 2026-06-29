# Case93 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 634.10
- Initial validation errors: 34
- Final validation errors: 33

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 33
- Warnings: 17

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 74889
- completion_tokens: 13569
- total_tokens: 88458

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
12. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
13. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
14. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
15. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
16. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
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
28. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
29. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
30. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
31. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
32. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
33. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
34. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 184: mismatched input '::' expecting 'end'
2. /CaseProject/modified_model.aadl | line 189: Assume statements are allowed only in component types
3. /CaseProject/modified_model.aadl | line 189: Couldn't resolve reference to 'C1'.
4. /CaseProject/modified_model.aadl | line 189: Couldn't resolve reference to 'acc1_input'.
5. /CaseProject/modified_model.aadl | line 189: Couldn't resolve reference to 'acc1_output'.
6. /CaseProject/modified_model.aadl | line 189: Couldn't resolve reference to 'acc_hm_pr'.
7. /CaseProject/modified_model.aadl | line 189: left side of binary expression '=>' is of type '<error>' but must be of type 'bool'
8. /CaseProject/modified_model.aadl | line 189: left side of binary expression 'and' is of type '<error>' but must be of type 'bool'
9. /CaseProject/modified_model.aadl | line 189: named thing must be an expression with a type
10. /CaseProject/modified_model.aadl | line 189: right side of binary expression '=>' is of type '<error>' but must be of type 'bool'
11. /CaseProject/modified_model.aadl | line 189: right side of binary expression 'and' is of type '<error>' but must be of type 'bool'
12. /CaseProject/modified_model.aadl | line 192: Assume statements are allowed only in component types
13. /CaseProject/modified_model.aadl | line 192: Couldn't resolve reference to 'C2'.
14. /CaseProject/modified_model.aadl | line 192: Couldn't resolve reference to 'acc2_input'.
15. /CaseProject/modified_model.aadl | line 192: Couldn't resolve reference to 'acc2_output'.
16. /CaseProject/modified_model.aadl | line 192: Couldn't resolve reference to 'acc_hm_pr'.
17. /CaseProject/modified_model.aadl | line 192: left side of binary expression '=>' is of type '<error>' but must be of type 'bool'
18. /CaseProject/modified_model.aadl | line 192: left side of binary expression 'and' is of type '<error>' but must be of type 'bool'
19. /CaseProject/modified_model.aadl | line 192: named thing must be an expression with a type
20. /CaseProject/modified_model.aadl | line 192: right side of binary expression '=>' is of type '<error>' but must be of type 'bool'
21. /CaseProject/modified_model.aadl | line 192: right side of binary expression 'and' is of type '<error>' but must be of type 'bool'
22. /CaseProject/modified_model.aadl | line 195: Assume statements are allowed only in component types
23. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to 'acc_pr_bound_to_main_cpu_part1'.
24. /CaseProject/modified_model.aadl | line 195: Expression for assume statement is of type '<error>' but must be of type 'bool'
25. /CaseProject/modified_model.aadl | line 198: Assume statements are allowed only in component types
26. /CaseProject/modified_model.aadl | line 198: Couldn't resolve reference to 'acc_hm_pr_bound_to_main_cpu_part2'.
27. /CaseProject/modified_model.aadl | line 198: Expression for assume statement is of type '<error>' but must be of type 'bool'
28. /CaseProject/modified_model.aadl | line 201: Assume statements are allowed only in component types
29. /CaseProject/modified_model.aadl | line 201: Couldn't resolve reference to 'ADIRUp_pr_bound_to_main_cpu_part3'.
30. /CaseProject/modified_model.aadl | line 201: Expression for assume statement is of type '<error>' but must be of type 'bool'
31. /CaseProject/modified_model.aadl | line 204: Assume statements are allowed only in component types
32. /CaseProject/modified_model.aadl | line 204: Couldn't resolve reference to 'SHM_pr_bound_to_main_cpu_part4'.
33. /CaseProject/modified_model.aadl | line 204: Expression for assume statement is of type '<error>' but must be of type 'bool'
