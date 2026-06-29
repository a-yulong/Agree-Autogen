# Case131 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 517.47
- Initial validation errors: 9
- Final validation errors: 39

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 5
- AGREE errors: 34
- Warnings: 4

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 49451
- completion_tokens: 6986
- total_tokens: 56437

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
11. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
12. [validation_repair] recovered_package_block - Recovered complete AADL package block.
13. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
14. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
15. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
16. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
17. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
18. [validation_repair] recovered_package_block - Recovered complete AADL package block.
19. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
20. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
21. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
22. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
23. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
24. [validation_repair] recovered_package_block - Recovered complete AADL package block.
25. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
26. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
27. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
28. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
29. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
30. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
31. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
32. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
33. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
34. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
35. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. Byte_Count (property association) does not point to anything
2. Byte_Count (property association) does not point to anything
3. Byte_Count (property association) does not point to anything
4. Byte_Count (property association) does not point to anything
5. Cannot analyze AADL specifications
6. /CaseProject/modified_model.aadl | line 23: Couldn't resolve reference to 'Dispatch_Protocol'.
7. /CaseProject/modified_model.aadl | line 23: Couldn't resolve reference to 'Periodic'.
8. /CaseProject/modified_model.aadl | line 23: named thing must be an expression with a type
9. /CaseProject/modified_model.aadl | line 24: Couldn't resolve reference to 'Period'.
10. /CaseProject/modified_model.aadl | line 24: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
11. /CaseProject/modified_model.aadl | line 24: named thing must be an expression with a type
12. /CaseProject/modified_model.aadl | line 25: Couldn't resolve reference to 'Compute_Execution_time'.
13. /CaseProject/modified_model.aadl | line 25: left and right sides of binary expression '<=' are of type '<error>' and 'int', but must be of the same type
14. /CaseProject/modified_model.aadl | line 25: left and right sides of binary expression '>=' are of type '<error>' and 'int', but must be of the same type
15. /CaseProject/modified_model.aadl | line 25: left side of binary expression '<=' is of type '<error>' but must be of type'int' or 'real'
16. /CaseProject/modified_model.aadl | line 25: left side of binary expression '>=' is of type '<error>' but must be of type'int' or 'real'
17. /CaseProject/modified_model.aadl | line 25: named thing must be an expression with a type
18. /CaseProject/modified_model.aadl | line 26: Couldn't resolve reference to 'Priority'.
19. /CaseProject/modified_model.aadl | line 26: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
20. /CaseProject/modified_model.aadl | line 26: named thing must be an expression with a type
21. /CaseProject/modified_model.aadl | line 41: Assume statements are allowed only in component types
22. /CaseProject/modified_model.aadl | line 41: Couldn't resolve reference to 'Dispatch_Protocol'.
23. /CaseProject/modified_model.aadl | line 41: Couldn't resolve reference to 'Periodic'.
24. /CaseProject/modified_model.aadl | line 41: named thing must be an expression with a type
25. /CaseProject/modified_model.aadl | line 42: Assume statements are allowed only in component types
26. /CaseProject/modified_model.aadl | line 42: Couldn't resolve reference to 'Period'.
27. /CaseProject/modified_model.aadl | line 42: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
28. /CaseProject/modified_model.aadl | line 42: named thing must be an expression with a type
29. /CaseProject/modified_model.aadl | line 43: Assume statements are allowed only in component types
30. /CaseProject/modified_model.aadl | line 43: Couldn't resolve reference to 'Compute_Execution_time'.
31. /CaseProject/modified_model.aadl | line 43: left and right sides of binary expression '<=' are of type '<error>' and 'int', but must be of the same type
32. /CaseProject/modified_model.aadl | line 43: left and right sides of binary expression '>=' are of type '<error>' and 'int', but must be of the same type
33. /CaseProject/modified_model.aadl | line 43: left side of binary expression '<=' is of type '<error>' but must be of type'int' or 'real'
34. /CaseProject/modified_model.aadl | line 43: left side of binary expression '>=' is of type '<error>' but must be of type'int' or 'real'
35. /CaseProject/modified_model.aadl | line 43: named thing must be an expression with a type
36. /CaseProject/modified_model.aadl | line 44: Assume statements are allowed only in component types
37. /CaseProject/modified_model.aadl | line 44: Couldn't resolve reference to 'Priority'.
38. /CaseProject/modified_model.aadl | line 44: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
39. /CaseProject/modified_model.aadl | line 44: named thing must be an expression with a type
