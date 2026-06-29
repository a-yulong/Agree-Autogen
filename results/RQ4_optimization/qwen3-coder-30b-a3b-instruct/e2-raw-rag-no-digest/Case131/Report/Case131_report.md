# Case131 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 302.12
- Initial validation errors: 19
- Final validation errors: 23

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 5
- AGREE errors: 18
- Warnings: 4

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 32873
- completion_tokens: 2970
- total_tokens: 35843

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 4 classified requirement item(s).
4. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
5. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
6. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
7. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
8. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
9. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
10. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
11. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
12. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
13. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
14. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
15. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
16. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
17. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
18. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
19. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
20. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
21. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
22. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
23. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
24. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
25. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. Byte_Count (property association) does not point to anything
2. Byte_Count (property association) does not point to anything
3. Byte_Count (property association) does not point to anything
4. Byte_Count (property association) does not point to anything
5. Cannot analyze AADL specifications
6. /CaseProject/modified_model.aadl | line 23: Couldn't resolve reference to 'Period'.
7. /CaseProject/modified_model.aadl | line 23: Couldn't resolve reference to 'impl_1'.
8. /CaseProject/modified_model.aadl | line 23: extraneous input 'ms' expecting ';'
9. /CaseProject/modified_model.aadl | line 23: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
10. /CaseProject/modified_model.aadl | line 23: named thing must be an expression with a type
11. /CaseProject/modified_model.aadl | line 24: Couldn't resolve reference to 'Compute_Execution_time'.
12. /CaseProject/modified_model.aadl | line 24: Couldn't resolve reference to 'impl_1'.
13. /CaseProject/modified_model.aadl | line 24: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
14. /CaseProject/modified_model.aadl | line 24: mismatched input 'ms' expecting ';'
15. /CaseProject/modified_model.aadl | line 24: named thing must be an expression with a type
16. /CaseProject/modified_model.aadl | line 25: Couldn't resolve reference to 'Dispatch_Protocol'.
17. /CaseProject/modified_model.aadl | line 25: Couldn't resolve reference to 'Periodic'.
18. /CaseProject/modified_model.aadl | line 25: Couldn't resolve reference to 'impl_1'.
19. /CaseProject/modified_model.aadl | line 25: named thing must be an expression with a type
20. /CaseProject/modified_model.aadl | line 26: Couldn't resolve reference to 'Priority'.
21. /CaseProject/modified_model.aadl | line 26: Couldn't resolve reference to 'impl_1'.
22. /CaseProject/modified_model.aadl | line 26: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
23. /CaseProject/modified_model.aadl | line 26: named thing must be an expression with a type
