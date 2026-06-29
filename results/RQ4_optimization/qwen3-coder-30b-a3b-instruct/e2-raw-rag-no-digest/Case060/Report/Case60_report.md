# Case60 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 410.95
- Initial validation errors: 22
- Final validation errors: 22

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 22
- Warnings: 2

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 106414
- completion_tokens: 9729
- total_tokens: 116143

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
20. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
21. [validation_repair] recovered_package_block - Recovered complete AADL package block.
22. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
23. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
24. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
25. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
26. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 106: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
2. /CaseProject/modified_model.aadl | line 106: Couldn't resolve reference to 'Mode'.
3. /CaseProject/modified_model.aadl | line 106: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
4. /CaseProject/modified_model.aadl | line 124: Couldn't resolve reference to 'Agree_Nodes::Brake_Mode'.
5. /CaseProject/modified_model.aadl | line 139: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
6. /CaseProject/modified_model.aadl | line 139: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
7. /CaseProject/modified_model.aadl | line 256: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
8. /CaseProject/modified_model.aadl | line 256: Couldn't resolve reference to 'Mode'.
9. /CaseProject/modified_model.aadl | line 256: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
10. /CaseProject/modified_model.aadl | line 257: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
11. /CaseProject/modified_model.aadl | line 257: Couldn't resolve reference to 'Mode'.
12. /CaseProject/modified_model.aadl | line 257: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
13. /CaseProject/modified_model.aadl | line 258: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
14. /CaseProject/modified_model.aadl | line 258: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
15. /CaseProject/modified_model.aadl | line 259: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
16. /CaseProject/modified_model.aadl | line 259: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
17. /CaseProject/modified_model.aadl | line 261: Couldn't resolve reference to 'Mode'.
18. /CaseProject/modified_model.aadl | line 261: left and right sides of binary expression '!=' are of type 'int' and '<error>', but must be of the same type
19. /CaseProject/modified_model.aadl | line 261: named thing must be an expression with a type
20. /CaseProject/modified_model.aadl | line 262: Couldn't resolve reference to 'Mode'.
21. /CaseProject/modified_model.aadl | line 262: left and right sides of binary expression '!=' are of type 'int' and '<error>', but must be of the same type
22. /CaseProject/modified_model.aadl | line 262: named thing must be an expression with a type
