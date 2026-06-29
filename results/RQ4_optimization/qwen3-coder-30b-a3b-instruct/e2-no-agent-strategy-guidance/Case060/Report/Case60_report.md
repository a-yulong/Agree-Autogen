# Case60 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 320.04
- Initial validation errors: 21
- Final validation errors: 14

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 14
- Warnings: 2

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 53756
- completion_tokens: 3460
- total_tokens: 57216

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 4 classified requirement item(s).
4. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
5. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
6. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
7. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
8. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
9. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
10. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
11. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
12. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
13. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
14. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
15. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
16. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
17. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
18. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
19. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
20. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
21. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
22. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
23. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
24. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
25. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 104: Couldn't resolve reference to 'Agree_Nodes::Brake_Mode'.
2. /CaseProject/modified_model.aadl | line 107: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
3. /CaseProject/modified_model.aadl | line 107: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
4. /CaseProject/modified_model.aadl | line 125: Couldn't resolve reference to 'Agree_Nodes::Brake_Mode'.
5. /CaseProject/modified_model.aadl | line 140: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
6. /CaseProject/modified_model.aadl | line 140: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
7. /CaseProject/modified_model.aadl | line 257: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
8. /CaseProject/modified_model.aadl | line 257: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
9. /CaseProject/modified_model.aadl | line 258: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
10. /CaseProject/modified_model.aadl | line 258: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
11. /CaseProject/modified_model.aadl | line 259: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
12. /CaseProject/modified_model.aadl | line 259: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
13. /CaseProject/modified_model.aadl | line 260: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
14. /CaseProject/modified_model.aadl | line 260: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
