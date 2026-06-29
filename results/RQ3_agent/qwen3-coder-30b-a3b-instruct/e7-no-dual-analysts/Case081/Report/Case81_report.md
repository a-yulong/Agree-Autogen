# Case81 Refactored Experiment Report

## Summary

- Setting: E7 (No Dual Analysts)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 386.69
- Initial validation errors: 18
- Final validation errors: 21

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 21
- Warnings: 0

## Modules

- rag: True
- repair: True
- requirement_analyst: False
- model_analyst: False
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 39358
- completion_tokens: 5908
- total_tokens: 45266

## Output Recovery

1. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
2. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
3. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
4. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
5. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
6. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
7. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
8. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
9. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
10. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
11. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
12. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
13. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
14. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
15. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
16. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
17. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
18. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
19. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
20. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
21. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
22. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
23. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
24. [validation_repair] recovered_package_block - Recovered complete AADL package block.
25. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
26. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
27. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
28. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
29. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
30. [validation_repair] recovered_package_block - Recovered complete AADL package block.
31. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 41: Couldn't resolve reference to 'Period'.
2. /CaseProject/modified_model.aadl | line 41: extraneous input 'ms' expecting ';'
3. /CaseProject/modified_model.aadl | line 41: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
4. /CaseProject/modified_model.aadl | line 41: named thing must be an expression with a type
5. /CaseProject/modified_model.aadl | line 42: Couldn't resolve reference to 'Period'.
6. /CaseProject/modified_model.aadl | line 42: extraneous input 'ms' expecting ';'
7. /CaseProject/modified_model.aadl | line 42: left and right sides of binary expression '<=' are of type '<error>' and 'int', but must be of the same type
8. /CaseProject/modified_model.aadl | line 42: left side of binary expression '<=' is of type '<error>' but must be of type'int' or 'real'
9. /CaseProject/modified_model.aadl | line 42: named thing must be an expression with a type
10. /CaseProject/modified_model.aadl | line 43: Couldn't resolve reference to 'Compute_Execution_Time'.
11. /CaseProject/modified_model.aadl | line 43: left and right sides of binary expression '>=' are of type '<error>' and 'int', but must be of the same type
12. /CaseProject/modified_model.aadl | line 43: left side of binary expression '>=' is of type '<error>' but must be of type'int' or 'real'
13. /CaseProject/modified_model.aadl | line 43: mismatched input 'ms' expecting ';'
14. /CaseProject/modified_model.aadl | line 43: named thing must be an expression with a type
15. /CaseProject/modified_model.aadl | line 44: Couldn't resolve reference to 'Priority'.
16. /CaseProject/modified_model.aadl | line 44: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
17. /CaseProject/modified_model.aadl | line 44: named thing must be an expression with a type
18. /CaseProject/modified_model.aadl | line 45: Couldn't resolve reference to 'Period'.
19. /CaseProject/modified_model.aadl | line 45: extraneous input 'ms' expecting ';'
20. /CaseProject/modified_model.aadl | line 45: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
21. /CaseProject/modified_model.aadl | line 45: named thing must be an expression with a type
