# Case83 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 309.75
- Initial validation errors: 16
- Final validation errors: 20

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 20
- Warnings: 0

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 45167
- completion_tokens: 6292
- total_tokens: 51459

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
17. [validation_repair] recovered_package_block - Recovered complete AADL package block.
18. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
19. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
20. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
21. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
22. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
23. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
24. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
25. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
26. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
27. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
28. [validation_repair] recovered_package_block - Recovered complete AADL package block.
29. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
30. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
31. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
32. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
33. [validation_repair] recovered_package_block - Recovered complete AADL package block.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 48: Couldn't resolve reference to 'Mix_1'.
2. /CaseProject/modified_model.aadl | line 48: Couldn't resolve reference to 'Port_1'.
3. /CaseProject/modified_model.aadl | line 48: left side of binary expression '=>' is of type '<error>' but must be of type 'bool'
4. /CaseProject/modified_model.aadl | line 48: named thing must be an expression with a type
5. /CaseProject/modified_model.aadl | line 48: right side of binary expression '=>' is of type '<error>' but must be of type 'bool'
6. /CaseProject/modified_model.aadl | line 49: Couldn't resolve reference to 'Mix_2'.
7. /CaseProject/modified_model.aadl | line 49: Couldn't resolve reference to 'Port_2'.
8. /CaseProject/modified_model.aadl | line 49: left side of binary expression '=>' is of type '<error>' but must be of type 'bool'
9. /CaseProject/modified_model.aadl | line 49: named thing must be an expression with a type
10. /CaseProject/modified_model.aadl | line 49: right side of binary expression '=>' is of type '<error>' but must be of type 'bool'
11. /CaseProject/modified_model.aadl | line 50: Couldn't resolve reference to 'Mix_1'.
12. /CaseProject/modified_model.aadl | line 50: Couldn't resolve reference to 'Port_1'.
13. /CaseProject/modified_model.aadl | line 50: left side of binary expression '=>' is of type '<error>' but must be of type 'bool'
14. /CaseProject/modified_model.aadl | line 50: named thing must be an expression with a type
15. /CaseProject/modified_model.aadl | line 50: right side of binary expression '=>' is of type '<error>' but must be of type 'bool'
16. /CaseProject/modified_model.aadl | line 51: Couldn't resolve reference to 'Mix_2'.
17. /CaseProject/modified_model.aadl | line 51: Couldn't resolve reference to 'Port_2'.
18. /CaseProject/modified_model.aadl | line 51: left side of binary expression '=>' is of type '<error>' but must be of type 'bool'
19. /CaseProject/modified_model.aadl | line 51: named thing must be an expression with a type
20. /CaseProject/modified_model.aadl | line 51: right side of binary expression '=>' is of type '<error>' but must be of type 'bool'
