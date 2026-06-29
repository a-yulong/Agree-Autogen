# Case125 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 686.83
- Initial validation errors: 3
- Final validation errors: 20

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 5
- AGREE errors: 15
- Warnings: 6

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 63584
- completion_tokens: 18831
- total_tokens: 82415

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 3 classified requirement item(s).
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
17. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
18. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
19. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
20. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
21. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
22. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
23. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
24. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
25. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
26. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
27. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
28. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
29. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
30. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
31. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
32. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
33. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
34. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
35. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
36. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
37. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. Source_Stack_Size (property association) does not point to anything
2. Source_Stack_Size (property association) does not point to anything
3. Source_Stack_Size (property association) does not point to anything
4. Source_Stack_Size (property association) does not point to anything
5. Cannot analyze AADL specifications
6. /CaseProject/modified_model.aadl | line 134: Assignment statements are allowed only in component implementations
7. /CaseProject/modified_model.aadl | line 134: Couldn't resolve reference to '"gyro_x_flow": gyro_out_data_x'.
8. /CaseProject/modified_model.aadl | line 134: Couldn't resolve reference to 'gyro_out_data_x'.
9. /CaseProject/modified_model.aadl | line 134: Couldn't resolve reference to 'gyro_sub'.
10. /CaseProject/modified_model.aadl | line 134: mismatched input '"gyro_x_flow"' expecting RULE_ID
11. /CaseProject/modified_model.aadl | line 135: Assignment statements are allowed only in component implementations
12. /CaseProject/modified_model.aadl | line 135: Couldn't resolve reference to '"gyro_y_flow": gyro_out_data_y'.
13. /CaseProject/modified_model.aadl | line 135: Couldn't resolve reference to 'gyro_out_data_y'.
14. /CaseProject/modified_model.aadl | line 135: Couldn't resolve reference to 'gyro_sub'.
15. /CaseProject/modified_model.aadl | line 135: mismatched input '"gyro_y_flow"' expecting RULE_ID
16. /CaseProject/modified_model.aadl | line 136: Assignment statements are allowed only in component implementations
17. /CaseProject/modified_model.aadl | line 136: Couldn't resolve reference to '"gyro_z_flow": gyro_out_data_z'.
18. /CaseProject/modified_model.aadl | line 136: Couldn't resolve reference to 'gyro_out_data_z'.
19. /CaseProject/modified_model.aadl | line 136: Couldn't resolve reference to 'gyro_sub'.
20. /CaseProject/modified_model.aadl | line 136: mismatched input '"gyro_z_flow"' expecting RULE_ID
