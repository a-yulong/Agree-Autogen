# Case131 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 421.53
- Initial validation errors: 19
- Final validation errors: 24

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 5
- AGREE errors: 19
- Warnings: 4

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 53022
- completion_tokens: 8309
- total_tokens: 61331

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
16. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
17. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
18. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
19. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
20. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
21. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
22. [validation_repair] recovered_package_block - Recovered complete AADL package block.
23. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
24. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
25. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
26. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
27. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
28. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
29. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
30. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
31. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
32. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
33. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. Byte_Count (property association) does not point to anything
2. Byte_Count (property association) does not point to anything
3. Byte_Count (property association) does not point to anything
4. Byte_Count (property association) does not point to anything
5. Cannot analyze AADL specifications
6. /CaseProject/modified_model.aadl | line 35: Couldn't resolve reference to 'Period'.
7. /CaseProject/modified_model.aadl | line 35: Guarantee statements are allowed only in component types
8. /CaseProject/modified_model.aadl | line 35: extraneous input 'ms' expecting ';'
9. /CaseProject/modified_model.aadl | line 35: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
10. /CaseProject/modified_model.aadl | line 35: named thing must be an expression with a type
11. /CaseProject/modified_model.aadl | line 36: Couldn't resolve reference to 'Compute_Execution_time'.
12. /CaseProject/modified_model.aadl | line 36: Guarantee statements are allowed only in component types
13. /CaseProject/modified_model.aadl | line 36: left and right sides of binary expression '>=' are of type '<error>' and 'int', but must be of the same type
14. /CaseProject/modified_model.aadl | line 36: left side of binary expression '>=' is of type '<error>' but must be of type'int' or 'real'
15. /CaseProject/modified_model.aadl | line 36: mismatched input 'ms' expecting ';'
16. /CaseProject/modified_model.aadl | line 36: named thing must be an expression with a type
17. /CaseProject/modified_model.aadl | line 37: Couldn't resolve reference to 'Dispatch_Protocol'.
18. /CaseProject/modified_model.aadl | line 37: Couldn't resolve reference to 'Periodic'.
19. /CaseProject/modified_model.aadl | line 37: Guarantee statements are allowed only in component types
20. /CaseProject/modified_model.aadl | line 37: named thing must be an expression with a type
21. /CaseProject/modified_model.aadl | line 38: Assume statements are allowed only in component types
22. /CaseProject/modified_model.aadl | line 38: Couldn't resolve reference to 'Priority'.
23. /CaseProject/modified_model.aadl | line 38: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
24. /CaseProject/modified_model.aadl | line 38: named thing must be an expression with a type
