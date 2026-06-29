# Case79 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 454.91
- Initial validation errors: 16
- Final validation errors: 16

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 16
- Warnings: 0

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 88023
- completion_tokens: 10016
- total_tokens: 98039

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
12. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
13. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
14. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
15. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
16. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
17. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
18. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
19. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
20. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
21. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
22. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
23. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
24. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
25. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
26. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
27. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
28. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
29. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
30. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
31. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
32. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
33. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
34. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
35. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 285: Couldn't resolve reference to 'door1'.
2. /CaseProject/modified_model.aadl | line 285: Couldn't resolve reference to 'handle_position'.
3. /CaseProject/modified_model.aadl | line 285: named thing must be an expression with a type
4. /CaseProject/modified_model.aadl | line 285: right side of binary expression '=>' is of type '<error>' but must be of type 'bool'
5. /CaseProject/modified_model.aadl | line 286: Couldn't resolve reference to 'closed'.
6. /CaseProject/modified_model.aadl | line 286: Couldn't resolve reference to 'door1'.
7. /CaseProject/modified_model.aadl | line 286: named thing must be an expression with a type
8. /CaseProject/modified_model.aadl | line 286: right side of binary expression '=>' is of type '<error>' but must be of type 'bool'
9. /CaseProject/modified_model.aadl | line 287: Couldn't resolve reference to 'door2'.
10. /CaseProject/modified_model.aadl | line 287: Couldn't resolve reference to 'handle_position'.
11. /CaseProject/modified_model.aadl | line 287: named thing must be an expression with a type
12. /CaseProject/modified_model.aadl | line 287: right side of binary expression '=>' is of type '<error>' but must be of type 'bool'
13. /CaseProject/modified_model.aadl | line 288: Couldn't resolve reference to 'closed'.
14. /CaseProject/modified_model.aadl | line 288: Couldn't resolve reference to 'door2'.
15. /CaseProject/modified_model.aadl | line 288: named thing must be an expression with a type
16. /CaseProject/modified_model.aadl | line 288: right side of binary expression '=>' is of type '<error>' but must be of type 'bool'
