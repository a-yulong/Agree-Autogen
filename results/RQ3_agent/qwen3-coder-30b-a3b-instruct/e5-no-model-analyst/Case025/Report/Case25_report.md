# Case25 Refactored Experiment Report

## Summary

- Setting: E5 (No Model Analyst)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 411.14
- Initial validation errors: 11
- Final validation errors: 21

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 21
- Warnings: 1

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: False
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 57547
- completion_tokens: 7999
- total_tokens: 65546

## Output Recovery

1. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] requirement_items_normalized - Normalized 2 classified requirement item(s).
3. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
4. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
5. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
6. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
7. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
8. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
9. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
10. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
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
28. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
29. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
30. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
31. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
32. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
33. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
34. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
35. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
36. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 56: Couldn't resolve reference to 'tempin1'.
2. /CaseProject/modified_model.aadl | line 56: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
3. /CaseProject/modified_model.aadl | line 56: named thing must be an expression with a type
4. /CaseProject/modified_model.aadl | line 57: Couldn't resolve reference to 'tempin2'.
5. /CaseProject/modified_model.aadl | line 57: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
6. /CaseProject/modified_model.aadl | line 57: named thing must be an expression with a type
7. /CaseProject/modified_model.aadl | line 58: Couldn't resolve reference to 'tempin1'.
8. /CaseProject/modified_model.aadl | line 58: Couldn't resolve reference to 'tempin2'.
9. /CaseProject/modified_model.aadl | line 58: Couldn't resolve reference to 'tempout'.
10. /CaseProject/modified_model.aadl | line 58: named thing must be an expression with a type
11. /CaseProject/modified_model.aadl | line 58: right side of binary expression 'and' is of type '<error>' but must be of type 'bool'
12. /CaseProject/modified_model.aadl | line 83: Couldn't resolve reference to 'temp1'.
13. /CaseProject/modified_model.aadl | line 83: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
14. /CaseProject/modified_model.aadl | line 83: named thing must be an expression with a type
15. /CaseProject/modified_model.aadl | line 84: Couldn't resolve reference to 'temp2'.
16. /CaseProject/modified_model.aadl | line 84: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
17. /CaseProject/modified_model.aadl | line 84: named thing must be an expression with a type
18. /CaseProject/modified_model.aadl | line 85: right side of binary expression 'and' is of type 'int' but must be of type 'bool'
19. /CaseProject/modified_model.aadl | line 91: Assume statements are allowed only in component types
20. /CaseProject/modified_model.aadl | line 92: Assume statements are allowed only in component types
21. /CaseProject/modified_model.aadl | line 93: Guarantee statements are allowed only in component types
