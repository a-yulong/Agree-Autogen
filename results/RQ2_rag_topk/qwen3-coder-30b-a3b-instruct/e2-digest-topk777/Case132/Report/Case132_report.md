# Case132 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 423.34
- Initial validation errors: 18
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

- prompt_tokens: 52132
- completion_tokens: 8345
- total_tokens: 60477

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

1. Byte_Count (property association) does not point to anything
2. Byte_Count (property association) does not point to anything
3. Byte_Count (property association) does not point to anything
4. Byte_Count (property association) does not point to anything
5. Cannot analyze AADL specifications
6. /CaseProject/modified_model.aadl | line 116: Couldn't resolve reference to 'cpu_rm'.
7. /CaseProject/modified_model.aadl | line 116: Couldn't resolve reference to 'impl'.
8. /CaseProject/modified_model.aadl | line 116: Couldn't resolve reference to 'p0'.
9. /CaseProject/modified_model.aadl | line 116: named thing must be an expression with a type
10. /CaseProject/modified_model.aadl | line 117: Couldn't resolve reference to 'impl'.
11. /CaseProject/modified_model.aadl | line 117: Couldn't resolve reference to 'mem'.
12. /CaseProject/modified_model.aadl | line 117: Couldn't resolve reference to 'segment1'.
13. /CaseProject/modified_model.aadl | line 117: named thing must be an expression with a type
14. /CaseProject/modified_model.aadl | line 118: Couldn't resolve reference to 'cpu_rm'.
15. /CaseProject/modified_model.aadl | line 118: Couldn't resolve reference to 'impl'.
16. /CaseProject/modified_model.aadl | line 118: Couldn't resolve reference to 'node_b'.
17. /CaseProject/modified_model.aadl | line 118: Couldn't resolve reference to 'p1'.
18. /CaseProject/modified_model.aadl | line 118: named thing must be an expression with a type
19. /CaseProject/modified_model.aadl | line 119: Couldn't resolve reference to 'Node_b'.
20. /CaseProject/modified_model.aadl | line 119: Couldn't resolve reference to 'impl'.
21. /CaseProject/modified_model.aadl | line 119: Couldn't resolve reference to 'mem'.
22. /CaseProject/modified_model.aadl | line 119: Couldn't resolve reference to 'segment2'.
23. /CaseProject/modified_model.aadl | line 119: named thing must be an expression with a type
