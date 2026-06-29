# Case62 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 447.95
- Initial validation errors: 20
- Final validation errors: 20

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 2
- AGREE errors: 18
- Warnings: 1

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 47738
- completion_tokens: 8448
- total_tokens: 56186

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
27. [validation_repair] recovered_package_block - Recovered complete AADL package block.
28. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
29. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
30. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
31. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
32. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
33. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. Source_Data_Size (property association) does not point to anything
2. Cannot analyze AADL specifications
3. /CaseProject/modified_model.aadl | line 65: Couldn't resolve reference to 'Dispatch_Protocol'.
4. /CaseProject/modified_model.aadl | line 65: Couldn't resolve reference to 'Impl'.
5. /CaseProject/modified_model.aadl | line 65: named thing must be an expression with a type
6. /CaseProject/modified_model.aadl | line 65: no viable alternative at input 'Sporadic'
7. /CaseProject/modified_model.aadl | line 66: Couldn't resolve reference to 'Impl'.
8. /CaseProject/modified_model.aadl | line 66: Couldn't resolve reference to 'Period'.
9. /CaseProject/modified_model.aadl | line 66: extraneous input 'Ms' expecting ';'
10. /CaseProject/modified_model.aadl | line 66: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
11. /CaseProject/modified_model.aadl | line 66: named thing must be an expression with a type
12. /CaseProject/modified_model.aadl | line 67: Couldn't resolve reference to 'Deadline'.
13. /CaseProject/modified_model.aadl | line 67: Couldn't resolve reference to 'Impl'.
14. /CaseProject/modified_model.aadl | line 67: extraneous input 'Ms' expecting ';'
15. /CaseProject/modified_model.aadl | line 67: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
16. /CaseProject/modified_model.aadl | line 67: named thing must be an expression with a type
17. /CaseProject/modified_model.aadl | line 68: Couldn't resolve reference to 'Impl'.
18. /CaseProject/modified_model.aadl | line 68: Couldn't resolve reference to 'Priority'.
19. /CaseProject/modified_model.aadl | line 68: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
20. /CaseProject/modified_model.aadl | line 68: named thing must be an expression with a type
