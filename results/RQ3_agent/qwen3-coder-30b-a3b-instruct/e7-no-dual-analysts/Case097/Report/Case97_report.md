# Case97 Refactored Experiment Report

## Summary

- Setting: E7 (No Dual Analysts)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 432.33
- Initial validation errors: 16
- Final validation errors: 16

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 2
- AGREE errors: 14
- Warnings: 8

## Modules

- rag: True
- repair: True
- requirement_analyst: False
- model_analyst: False
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 78750
- completion_tokens: 6781
- total_tokens: 85531

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

1. parsing Package_Specification, Empty packages are not allowed
2. Cannot parse AADL specifications
3. /CaseProject/modified_model.aadl | line 359: Couldn't resolve reference to 'alarmAggregator'.
4. /CaseProject/modified_model.aadl | line 359: Couldn't resolve reference to 'arlarm_acc_in'.
5. /CaseProject/modified_model.aadl | line 359: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
6. /CaseProject/modified_model.aadl | line 359: named thing must be an expression with a type
7. /CaseProject/modified_model.aadl | line 360: Couldn't resolve reference to 'alarmAggregator'.
8. /CaseProject/modified_model.aadl | line 360: Couldn't resolve reference to 'arlarm_adirup_in'.
9. /CaseProject/modified_model.aadl | line 360: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
10. /CaseProject/modified_model.aadl | line 360: named thing must be an expression with a type
11. /CaseProject/modified_model.aadl | line 361: Couldn't resolve reference to 'acc1_output'.
12. /CaseProject/modified_model.aadl | line 361: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
13. /CaseProject/modified_model.aadl | line 361: named thing must be an expression with a type
14. /CaseProject/modified_model.aadl | line 362: Couldn't resolve reference to 'acc2_output'.
15. /CaseProject/modified_model.aadl | line 362: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
16. /CaseProject/modified_model.aadl | line 362: named thing must be an expression with a type
