# Case64 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 342.96
- Initial validation errors: 17
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

- prompt_tokens: 35122
- completion_tokens: 6176
- total_tokens: 41298

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
23. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
24. [validation_repair] recovered_package_block - Recovered complete AADL package block.
25. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
26. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
27. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
28. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
29. [validation_repair] recovered_package_block - Recovered complete AADL package block.
30. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.

## Final Diagnostics

1. Source_Data_Size (property association) does not point to anything
2. Cannot analyze AADL specifications
3. /CaseProject/modified_model.aadl | line 79: Couldn't resolve reference to 'Dispatch_Protocol'.
4. /CaseProject/modified_model.aadl | line 79: Guarantee statements are allowed only in component types
5. /CaseProject/modified_model.aadl | line 79: named thing must be an expression with a type
6. /CaseProject/modified_model.aadl | line 79: no viable alternative at input 'Sporadic'
7. /CaseProject/modified_model.aadl | line 80: Couldn't resolve reference to 'Period'.
8. /CaseProject/modified_model.aadl | line 80: Couldn't resolve reference to 'ms'.
9. /CaseProject/modified_model.aadl | line 80: Guarantee statements are allowed only in component types
10. /CaseProject/modified_model.aadl | line 80: named thing must be an expression with a type
11. /CaseProject/modified_model.aadl | line 80: no viable alternative at character 'm'
12. /CaseProject/modified_model.aadl | line 81: Couldn't resolve reference to 'deadline'.
13. /CaseProject/modified_model.aadl | line 81: Couldn't resolve reference to 'ms'.
14. /CaseProject/modified_model.aadl | line 81: Guarantee statements are allowed only in component types
15. /CaseProject/modified_model.aadl | line 81: named thing must be an expression with a type
16. /CaseProject/modified_model.aadl | line 81: no viable alternative at character 'm'
17. /CaseProject/modified_model.aadl | line 82: Couldn't resolve reference to 'Priority'.
18. /CaseProject/modified_model.aadl | line 82: Guarantee statements are allowed only in component types
19. /CaseProject/modified_model.aadl | line 82: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
20. /CaseProject/modified_model.aadl | line 82: named thing must be an expression with a type
