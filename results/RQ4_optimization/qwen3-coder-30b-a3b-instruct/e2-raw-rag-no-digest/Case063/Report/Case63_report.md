# Case63 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 339.05
- Initial validation errors: 15
- Final validation errors: 16

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 2
- AGREE errors: 14
- Warnings: 1

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 34200
- completion_tokens: 4366
- total_tokens: 38566

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 5 classified requirement item(s).
4. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
5. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
6. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
7. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
8. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
9. [validation_repair] recovered_package_block - Recovered complete AADL package block.
10. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
11. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
12. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
13. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
14. [validation_repair] recovered_package_block - Recovered complete AADL package block.
15. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
16. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
17. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
18. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
19. [validation_repair] recovered_package_block - Recovered complete AADL package block.
20. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
21. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
22. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
23. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
24. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
25. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
26. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
27. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
28. [validation_repair] recovered_package_block - Recovered complete AADL package block.
29. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.

## Final Diagnostics

1. Source_Data_Size (property association) does not point to anything
2. Cannot analyze AADL specifications
3. /CaseProject/modified_model.aadl | line 65: Couldn't resolve reference to 'Dispatch_Protocol'.
4. /CaseProject/modified_model.aadl | line 65: named thing must be an expression with a type
5. /CaseProject/modified_model.aadl | line 65: no viable alternative at input 'Sporadic'
6. /CaseProject/modified_model.aadl | line 66: Couldn't resolve reference to 'Period'.
7. /CaseProject/modified_model.aadl | line 66: extraneous input 'Ms' expecting ';'
8. /CaseProject/modified_model.aadl | line 66: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
9. /CaseProject/modified_model.aadl | line 66: named thing must be an expression with a type
10. /CaseProject/modified_model.aadl | line 67: Couldn't resolve reference to 'deadline'.
11. /CaseProject/modified_model.aadl | line 67: extraneous input 'Ms' expecting ';'
12. /CaseProject/modified_model.aadl | line 67: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
13. /CaseProject/modified_model.aadl | line 67: named thing must be an expression with a type
14. /CaseProject/modified_model.aadl | line 68: Couldn't resolve reference to 'Priority'.
15. /CaseProject/modified_model.aadl | line 68: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
16. /CaseProject/modified_model.aadl | line 68: named thing must be an expression with a type
