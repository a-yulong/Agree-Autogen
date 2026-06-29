# Case127 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 419.90
- Initial validation errors: 18
- Final validation errors: 23

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 5
- AGREE errors: 18
- Warnings: 6

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 79074
- completion_tokens: 10831
- total_tokens: 89905

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 9 classified requirement item(s).
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
26. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
27. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
28. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
29. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
30. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
31. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
32. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. Source_Stack_Size (property association) does not point to anything
2. Source_Stack_Size (property association) does not point to anything
3. Source_Stack_Size (property association) does not point to anything
4. Source_Stack_Size (property association) does not point to anything
5. Cannot analyze AADL specifications
6. /CaseProject/modified_model.aadl | line 204: Couldn't resolve reference to 'attitude_sub.acc_in_data_x'.
7. /CaseProject/modified_model.aadl | line 204: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
8. /CaseProject/modified_model.aadl | line 206: Couldn't resolve reference to 'attitude_sub.acc_in_data_y'.
9. /CaseProject/modified_model.aadl | line 206: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
10. /CaseProject/modified_model.aadl | line 208: Couldn't resolve reference to 'attitude_sub.acc_in_data_z'.
11. /CaseProject/modified_model.aadl | line 208: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
12. /CaseProject/modified_model.aadl | line 210: Couldn't resolve reference to 'attitude_sub.mag_in_data_x'.
13. /CaseProject/modified_model.aadl | line 210: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
14. /CaseProject/modified_model.aadl | line 212: Couldn't resolve reference to 'attitude_sub.mag_in_data_y'.
15. /CaseProject/modified_model.aadl | line 212: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
16. /CaseProject/modified_model.aadl | line 214: Couldn't resolve reference to 'attitude_sub.mag_in_data_z'.
17. /CaseProject/modified_model.aadl | line 214: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
18. /CaseProject/modified_model.aadl | line 216: Couldn't resolve reference to 'attitude_sub.gyro_in_data_x'.
19. /CaseProject/modified_model.aadl | line 216: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
20. /CaseProject/modified_model.aadl | line 218: Couldn't resolve reference to 'attitude_sub.gyro_in_data_y'.
21. /CaseProject/modified_model.aadl | line 218: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
22. /CaseProject/modified_model.aadl | line 220: Couldn't resolve reference to 'attitude_sub.gyro_in_data_z'.
23. /CaseProject/modified_model.aadl | line 220: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
