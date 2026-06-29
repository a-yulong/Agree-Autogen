# Case60 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 373.03
- Initial validation errors: 24
- Final validation errors: 13

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 13
- Warnings: 2

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 104885
- completion_tokens: 10474
- total_tokens: 115359

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

1. /CaseProject/modified_model.aadl | line 105: left side of binary expression '/' is of type 'int' but must be of type 'real'
2. /CaseProject/modified_model.aadl | line 105: no viable alternative at input 'as'
3. /CaseProject/modified_model.aadl | line 123: Couldn't resolve reference to 'Agree_Nodes::Brake_Mode'.
4. /CaseProject/modified_model.aadl | line 138: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
5. /CaseProject/modified_model.aadl | line 138: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
6. /CaseProject/modified_model.aadl | line 255: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
7. /CaseProject/modified_model.aadl | line 255: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
8. /CaseProject/modified_model.aadl | line 256: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
9. /CaseProject/modified_model.aadl | line 256: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
10. /CaseProject/modified_model.aadl | line 257: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
11. /CaseProject/modified_model.aadl | line 257: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
12. /CaseProject/modified_model.aadl | line 258: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
13. /CaseProject/modified_model.aadl | line 258: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
