# Case129 Refactored Experiment Report

## Summary

- Setting: E5 (No Model Analyst)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 394.26
- Initial validation errors: 17
- Final validation errors: 18

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 4
- AGREE errors: 14
- Warnings: 3

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: False
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 35761
- completion_tokens: 4637
- total_tokens: 40398

## Output Recovery

1. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] requirement_items_normalized - Normalized 5 classified requirement item(s).
3. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
4. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
5. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
6. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
7. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
8. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
9. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
10. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
11. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
12. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
13. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
14. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
15. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
16. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
17. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
18. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
19. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
20. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
21. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
22. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
23. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
24. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
25. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
26. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
27. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
28. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
29. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
30. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
31. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. Byte_Count (property association) does not point to anything
2. Byte_Count (property association) does not point to anything
3. Byte_Count (property association) does not point to anything
4. Cannot analyze AADL specifications
5. /CaseProject/modified_model.aadl | line 23: Couldn't resolve reference to 'Period'.
6. /CaseProject/modified_model.aadl | line 23: Couldn't resolve reference to 'impl_1'.
7. /CaseProject/modified_model.aadl | line 23: extraneous input 'ms' expecting ';'
8. /CaseProject/modified_model.aadl | line 23: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
9. /CaseProject/modified_model.aadl | line 23: named thing must be an expression with a type
10. /CaseProject/modified_model.aadl | line 24: Couldn't resolve reference to 'Compute_Execution_time'.
11. /CaseProject/modified_model.aadl | line 24: Couldn't resolve reference to 'impl_1'.
12. /CaseProject/modified_model.aadl | line 24: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
13. /CaseProject/modified_model.aadl | line 24: mismatched input 'ms' expecting ';'
14. /CaseProject/modified_model.aadl | line 24: named thing must be an expression with a type
15. /CaseProject/modified_model.aadl | line 25: Couldn't resolve reference to 'Priority'.
16. /CaseProject/modified_model.aadl | line 25: Couldn't resolve reference to 'impl_1'.
17. /CaseProject/modified_model.aadl | line 25: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
18. /CaseProject/modified_model.aadl | line 25: named thing must be an expression with a type
