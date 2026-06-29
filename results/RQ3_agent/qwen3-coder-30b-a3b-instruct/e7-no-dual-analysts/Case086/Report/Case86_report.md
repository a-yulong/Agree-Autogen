# Case86 Refactored Experiment Report

## Summary

- Setting: E7 (No Dual Analysts)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 435.45
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
- requirement_analyst: False
- model_analyst: False
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 68286
- completion_tokens: 6175
- total_tokens: 74461

## Output Recovery

1. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
2. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
3. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
4. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
5. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
6. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
7. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
8. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
9. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
10. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
11. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
12. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
13. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
14. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
15. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
16. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
17. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
18. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
19. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
20. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
21. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
22. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
23. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
24. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
25. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
26. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
27. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
28. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
29. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

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
