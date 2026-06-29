# Case64 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 362.84
- Initial validation errors: 15
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

- prompt_tokens: 49135
- completion_tokens: 8736
- total_tokens: 57871

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
11. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
12. [validation_repair] recovered_package_block - Recovered complete AADL package block.
13. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
14. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
15. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
16. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
17. [validation_repair] recovered_package_block - Recovered complete AADL package block.
18. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
19. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
20. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
21. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
22. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
23. [validation_repair] recovered_package_block - Recovered complete AADL package block.
24. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
25. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
26. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
27. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
28. [validation_repair] recovered_package_block - Recovered complete AADL package block.
29. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
30. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
31. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
32. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
33. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
34. [validation_repair] recovered_package_block - Recovered complete AADL package block.
35. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.

## Final Diagnostics

1. Source_Data_Size (property association) does not point to anything
2. Cannot analyze AADL specifications
3. /CaseProject/modified_model.aadl | line 82: Couldn't resolve reference to 'Dispatch_Protocol'.
4. /CaseProject/modified_model.aadl | line 82: Guarantee statements are allowed only in component types
5. /CaseProject/modified_model.aadl | line 82: named thing must be an expression with a type
6. /CaseProject/modified_model.aadl | line 82: no viable alternative at input 'Sporadic'
7. /CaseProject/modified_model.aadl | line 83: Couldn't resolve reference to 'Period'.
8. /CaseProject/modified_model.aadl | line 83: Guarantee statements are allowed only in component types
9. /CaseProject/modified_model.aadl | line 83: extraneous input 'Ms' expecting ';'
10. /CaseProject/modified_model.aadl | line 83: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
11. /CaseProject/modified_model.aadl | line 83: named thing must be an expression with a type
12. /CaseProject/modified_model.aadl | line 84: Couldn't resolve reference to 'deadline'.
13. /CaseProject/modified_model.aadl | line 84: Guarantee statements are allowed only in component types
14. /CaseProject/modified_model.aadl | line 84: extraneous input 'Ms' expecting ';'
15. /CaseProject/modified_model.aadl | line 84: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
16. /CaseProject/modified_model.aadl | line 84: named thing must be an expression with a type
17. /CaseProject/modified_model.aadl | line 85: Couldn't resolve reference to 'Priority'.
18. /CaseProject/modified_model.aadl | line 85: Guarantee statements are allowed only in component types
19. /CaseProject/modified_model.aadl | line 85: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
20. /CaseProject/modified_model.aadl | line 85: named thing must be an expression with a type
