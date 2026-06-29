# Case95 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 319.36
- Initial validation errors: 10
- Final validation errors: 20

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 2
- AGREE errors: 18
- Warnings: 8

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 81947
- completion_tokens: 8361
- total_tokens: 90308

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
21. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
22. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
23. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
24. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
25. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
26. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
27. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
28. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
29. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
30. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. parsing Package_Specification, Empty packages are not allowed
2. Cannot parse AADL specifications
3. /CaseProject/modified_model.aadl | line 163: Assignment statements are allowed only in component implementations
4. /CaseProject/modified_model.aadl | line 163: Couldn't resolve reference to 'acc1_validated_dataout'.
5. /CaseProject/modified_model.aadl | line 163: Couldn't resolve reference to 'acc_HM'.
6. /CaseProject/modified_model.aadl | line 164: Assignment statements are allowed only in component implementations
7. /CaseProject/modified_model.aadl | line 164: Couldn't resolve reference to 'acc2_validated_dataout'.
8. /CaseProject/modified_model.aadl | line 164: Couldn't resolve reference to 'acc_HM'.
9. /CaseProject/modified_model.aadl | line 165: Assignment statements are allowed only in component implementations
10. /CaseProject/modified_model.aadl | line 165: Couldn't resolve reference to 'acc3_validated_dataout'.
11. /CaseProject/modified_model.aadl | line 165: Couldn't resolve reference to 'acc_HM'.
12. /CaseProject/modified_model.aadl | line 166: Assignment statements are allowed only in component implementations
13. /CaseProject/modified_model.aadl | line 166: Couldn't resolve reference to 'acc4_validated_dataout'.
14. /CaseProject/modified_model.aadl | line 166: Couldn't resolve reference to 'acc_HM'.
15. /CaseProject/modified_model.aadl | line 167: Assignment statements are allowed only in component implementations
16. /CaseProject/modified_model.aadl | line 167: Couldn't resolve reference to 'acc5_validated_dataout'.
17. /CaseProject/modified_model.aadl | line 167: Couldn't resolve reference to 'acc_HM'.
18. /CaseProject/modified_model.aadl | line 168: Assignment statements are allowed only in component implementations
19. /CaseProject/modified_model.aadl | line 168: Couldn't resolve reference to 'acc6_validated_dataout'.
20. /CaseProject/modified_model.aadl | line 168: Couldn't resolve reference to 'acc_HM'.
