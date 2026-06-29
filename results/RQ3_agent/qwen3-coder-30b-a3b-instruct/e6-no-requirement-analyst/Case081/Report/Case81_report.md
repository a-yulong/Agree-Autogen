# Case81 Refactored Experiment Report

## Summary

- Setting: E6 (No Requirement Analyst)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 392.16
- Initial validation errors: 24
- Final validation errors: 15

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 15
- Warnings: 0

## Modules

- rag: True
- repair: True
- requirement_analyst: False
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 45593
- completion_tokens: 6938
- total_tokens: 52531

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
14. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
15. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
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

1. /CaseProject/modified_model.aadl | line 41: Couldn't resolve reference to 'Period'.
2. /CaseProject/modified_model.aadl | line 41: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
3. /CaseProject/modified_model.aadl | line 41: named thing must be an expression with a type
4. /CaseProject/modified_model.aadl | line 42: Couldn't resolve reference to 'Deadline'.
5. /CaseProject/modified_model.aadl | line 42: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
6. /CaseProject/modified_model.aadl | line 42: named thing must be an expression with a type
7. /CaseProject/modified_model.aadl | line 43: Couldn't resolve reference to 'Compute_Execution_Time'.
8. /CaseProject/modified_model.aadl | line 43: left and right sides of binary expression '<=' are of type '<error>' and 'int', but must be of the same type
9. /CaseProject/modified_model.aadl | line 43: left and right sides of binary expression '>=' are of type '<error>' and 'int', but must be of the same type
10. /CaseProject/modified_model.aadl | line 43: left side of binary expression '<=' is of type '<error>' but must be of type'int' or 'real'
11. /CaseProject/modified_model.aadl | line 43: left side of binary expression '>=' is of type '<error>' but must be of type'int' or 'real'
12. /CaseProject/modified_model.aadl | line 43: named thing must be an expression with a type
13. /CaseProject/modified_model.aadl | line 44: Couldn't resolve reference to 'Priority'.
14. /CaseProject/modified_model.aadl | line 44: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
15. /CaseProject/modified_model.aadl | line 44: named thing must be an expression with a type
