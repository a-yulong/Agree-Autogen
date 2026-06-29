# Case87 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 455.04
- Initial validation errors: 6
- Final validation errors: 32

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 5
- AGREE errors: 27
- Warnings: 6

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 80021
- completion_tokens: 7741
- total_tokens: 87762

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
16. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
17. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
18. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
19. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
20. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
21. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
22. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
23. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
24. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
25. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
26. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
27. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
28. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
29. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
30. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
31. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
32. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
33. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. Source_Stack_Size (property association) does not point to anything
2. Source_Stack_Size (property association) does not point to anything
3. Source_Stack_Size (property association) does not point to anything
4. Source_Stack_Size (property association) does not point to anything
5. Cannot analyze AADL specifications
6. /CaseProject/modified_model.aadl | line 182: Couldn't resolve reference to 'acc_in_data_x'.
7. /CaseProject/modified_model.aadl | line 182: Couldn't resolve reference to 'attitude_sub'.
8. /CaseProject/modified_model.aadl | line 182: named thing must be an expression with a type
9. /CaseProject/modified_model.aadl | line 183: Couldn't resolve reference to 'acc_in_data_y'.
10. /CaseProject/modified_model.aadl | line 183: Couldn't resolve reference to 'attitude_sub'.
11. /CaseProject/modified_model.aadl | line 183: named thing must be an expression with a type
12. /CaseProject/modified_model.aadl | line 184: Couldn't resolve reference to 'acc_in_data_z'.
13. /CaseProject/modified_model.aadl | line 184: Couldn't resolve reference to 'attitude_sub'.
14. /CaseProject/modified_model.aadl | line 184: named thing must be an expression with a type
15. /CaseProject/modified_model.aadl | line 185: Couldn't resolve reference to 'attitude_sub'.
16. /CaseProject/modified_model.aadl | line 185: Couldn't resolve reference to 'mag_in_data_x'.
17. /CaseProject/modified_model.aadl | line 185: named thing must be an expression with a type
18. /CaseProject/modified_model.aadl | line 186: Couldn't resolve reference to 'attitude_sub'.
19. /CaseProject/modified_model.aadl | line 186: Couldn't resolve reference to 'mag_in_data_y'.
20. /CaseProject/modified_model.aadl | line 186: named thing must be an expression with a type
21. /CaseProject/modified_model.aadl | line 187: Couldn't resolve reference to 'attitude_sub'.
22. /CaseProject/modified_model.aadl | line 187: Couldn't resolve reference to 'mag_in_data_z'.
23. /CaseProject/modified_model.aadl | line 187: named thing must be an expression with a type
24. /CaseProject/modified_model.aadl | line 188: Couldn't resolve reference to 'attitude_sub'.
25. /CaseProject/modified_model.aadl | line 188: Couldn't resolve reference to 'gyro_in_data_x'.
26. /CaseProject/modified_model.aadl | line 188: named thing must be an expression with a type
27. /CaseProject/modified_model.aadl | line 189: Couldn't resolve reference to 'attitude_sub'.
28. /CaseProject/modified_model.aadl | line 189: Couldn't resolve reference to 'gyro_in_data_y'.
29. /CaseProject/modified_model.aadl | line 189: named thing must be an expression with a type
30. /CaseProject/modified_model.aadl | line 190: Couldn't resolve reference to 'attitude_sub'.
31. /CaseProject/modified_model.aadl | line 190: Couldn't resolve reference to 'gyro_in_data_z'.
32. /CaseProject/modified_model.aadl | line 190: named thing must be an expression with a type
