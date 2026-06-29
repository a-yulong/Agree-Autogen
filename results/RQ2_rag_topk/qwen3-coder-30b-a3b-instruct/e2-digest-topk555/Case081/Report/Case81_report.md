# Case81 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 407.16
- Initial validation errors: 23
- Final validation errors: 24

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 24
- Warnings: 0

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 54521
- completion_tokens: 8573
- total_tokens: 63094

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 5 classified requirement item(s).
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
16. [validation_repair] recovered_package_block - Recovered complete AADL package block.
17. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
18. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
19. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
20. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
21. [validation_repair] recovered_package_block - Recovered complete AADL package block.
22. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
23. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
24. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
25. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
26. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
27. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
28. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
29. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
30. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
31. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
32. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 41: Couldn't resolve reference to 'Dispatch_Protocol'.
2. /CaseProject/modified_model.aadl | line 41: Couldn't resolve reference to 'impl'.
3. /CaseProject/modified_model.aadl | line 41: Couldn't resolve reference to 'periodic'.
4. /CaseProject/modified_model.aadl | line 41: named thing must be an expression with a type
5. /CaseProject/modified_model.aadl | line 42: Couldn't resolve reference to 'Period'.
6. /CaseProject/modified_model.aadl | line 42: Couldn't resolve reference to 'impl'.
7. /CaseProject/modified_model.aadl | line 42: extraneous input 'ms' expecting ';'
8. /CaseProject/modified_model.aadl | line 42: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
9. /CaseProject/modified_model.aadl | line 42: named thing must be an expression with a type
10. /CaseProject/modified_model.aadl | line 43: Couldn't resolve reference to 'Deadline'.
11. /CaseProject/modified_model.aadl | line 43: Couldn't resolve reference to 'impl'.
12. /CaseProject/modified_model.aadl | line 43: extraneous input 'ms' expecting ';'
13. /CaseProject/modified_model.aadl | line 43: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
14. /CaseProject/modified_model.aadl | line 43: named thing must be an expression with a type
15. /CaseProject/modified_model.aadl | line 44: Couldn't resolve reference to 'Compute_Execution_Time'.
16. /CaseProject/modified_model.aadl | line 44: Couldn't resolve reference to 'impl'.
17. /CaseProject/modified_model.aadl | line 44: left and right sides of binary expression '>=' are of type '<error>' and 'int', but must be of the same type
18. /CaseProject/modified_model.aadl | line 44: left side of binary expression '>=' is of type '<error>' but must be of type'int' or 'real'
19. /CaseProject/modified_model.aadl | line 44: mismatched input 'ms' expecting ';'
20. /CaseProject/modified_model.aadl | line 44: named thing must be an expression with a type
21. /CaseProject/modified_model.aadl | line 45: Couldn't resolve reference to 'Priority'.
22. /CaseProject/modified_model.aadl | line 45: Couldn't resolve reference to 'impl'.
23. /CaseProject/modified_model.aadl | line 45: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
24. /CaseProject/modified_model.aadl | line 45: named thing must be an expression with a type
