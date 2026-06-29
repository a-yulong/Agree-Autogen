# Case60 Refactored Experiment Report

## Summary

- Setting: E7 (No Dual Analysts)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 471.99
- Initial validation errors: 23
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
- requirement_analyst: False
- model_analyst: False
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 105079
- completion_tokens: 10234
- total_tokens: 115313

## Output Recovery

1. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
2. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
3. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
4. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
5. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
6. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
7. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
8. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
9. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
10. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
11. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
12. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
13. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
14. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
15. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
16. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
17. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
18. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
19. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
20. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
21. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
22. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
23. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
24. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
25. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
26. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
27. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
28. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
29. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
30. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
31. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 105: left and right sides of binary expression '*' are of type 'int' and 'real', but must be of the same type
2. /CaseProject/modified_model.aadl | line 105: left side of binary expression '/' is of type 'int' but must be of type 'real'
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
