# Case25 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 385.98
- Initial validation errors: 12
- Final validation errors: 20

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 20
- Warnings: 1

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 57690
- completion_tokens: 8200
- total_tokens: 65890

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 2 classified requirement item(s).
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
16. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
17. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
18. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
19. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
20. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
21. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
22. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
23. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
24. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
25. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
26. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
27. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
28. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
29. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
30. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
31. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
32. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
33. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
34. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
35. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 56: Couldn't resolve reference to 'tempin1'.
2. /CaseProject/modified_model.aadl | line 56: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
3. /CaseProject/modified_model.aadl | line 56: named thing must be an expression with a type
4. /CaseProject/modified_model.aadl | line 57: Couldn't resolve reference to 'tempin2'.
5. /CaseProject/modified_model.aadl | line 57: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
6. /CaseProject/modified_model.aadl | line 57: named thing must be an expression with a type
7. /CaseProject/modified_model.aadl | line 58: Couldn't resolve reference to 'c0'.
8. /CaseProject/modified_model.aadl | line 58: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
9. /CaseProject/modified_model.aadl | line 58: named thing must be an expression with a type
10. /CaseProject/modified_model.aadl | line 59: Couldn't resolve reference to 'c1'.
11. /CaseProject/modified_model.aadl | line 59: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
12. /CaseProject/modified_model.aadl | line 59: named thing must be an expression with a type
13. /CaseProject/modified_model.aadl | line 84: Couldn't resolve reference to 'temp1'.
14. /CaseProject/modified_model.aadl | line 84: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
15. /CaseProject/modified_model.aadl | line 84: named thing must be an expression with a type
16. /CaseProject/modified_model.aadl | line 85: Couldn't resolve reference to 'temp2'.
17. /CaseProject/modified_model.aadl | line 85: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
18. /CaseProject/modified_model.aadl | line 85: named thing must be an expression with a type
19. /CaseProject/modified_model.aadl | line 91: Assume statements are allowed only in component types
20. /CaseProject/modified_model.aadl | line 92: Assume statements are allowed only in component types
