# Case81 Refactored Experiment Report

## Summary

- Setting: E5 (No Model Analyst)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 478.92
- Initial validation errors: 20
- Final validation errors: 18

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 18
- Warnings: 0

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: False
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 47561
- completion_tokens: 8198
- total_tokens: 55759

## Output Recovery

1. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] requirement_items_normalized - Normalized 5 classified requirement item(s).
3. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
4. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
5. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
6. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
7. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
8. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
9. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
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
25. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
26. [validation_repair] recovered_package_block - Recovered complete AADL package block.
27. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
28. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
29. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
30. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
31. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
32. [validation_repair] recovered_package_block - Recovered complete AADL package block.
33. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 41: Couldn't resolve reference to 'period'.
2. /CaseProject/modified_model.aadl | line 41: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
3. /CaseProject/modified_model.aadl | line 41: named thing must be an expression with a type
4. /CaseProject/modified_model.aadl | line 42: Couldn't resolve reference to 'deadline'.
5. /CaseProject/modified_model.aadl | line 42: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
6. /CaseProject/modified_model.aadl | line 42: named thing must be an expression with a type
7. /CaseProject/modified_model.aadl | line 43: Couldn't resolve reference to 'compute_time'.
8. /CaseProject/modified_model.aadl | line 43: left and right sides of binary expression '<=' are of type '<error>' and 'int', but must be of the same type
9. /CaseProject/modified_model.aadl | line 43: left and right sides of binary expression '<=' are of type 'int' and '<error>', but must be of the same type
10. /CaseProject/modified_model.aadl | line 43: left side of binary expression '<=' is of type '<error>' but must be of type'int' or 'real'
11. /CaseProject/modified_model.aadl | line 43: named thing must be an expression with a type
12. /CaseProject/modified_model.aadl | line 43: right side of binary expression '<=' is of type '<error>' but must be of type'int' or 'real'
13. /CaseProject/modified_model.aadl | line 44: Couldn't resolve reference to 'priority'.
14. /CaseProject/modified_model.aadl | line 44: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
15. /CaseProject/modified_model.aadl | line 44: named thing must be an expression with a type
16. /CaseProject/modified_model.aadl | line 45: Couldn't resolve reference to 'dispatch_protocol'.
17. /CaseProject/modified_model.aadl | line 45: Couldn't resolve reference to 'periodic'.
18. /CaseProject/modified_model.aadl | line 45: named thing must be an expression with a type
