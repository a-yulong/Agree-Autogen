# Case38 Refactored Experiment Report

## Summary

- Setting: E7 (No Dual Analysts)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 413.49
- Initial validation errors: 22
- Final validation errors: 29

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 11
- AGREE errors: 18
- Warnings: 5

## Modules

- rag: True
- repair: True
- requirement_analyst: False
- model_analyst: False
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 47480
- completion_tokens: 7160
- total_tokens: 54640

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

1. Target (port spec) points to Types  speed.speed_impl (entity reference), which is not of an adequate kind
2. Target (port spec) does not point to anything or to something unreachable
3. Actual (port spec) points to Types  speed.speed_impl (entity reference), which is not of an adequate kind
4. Actual (port spec) does not point to anything or to something unreachable
5. Actual (port spec) points to Types  speed.speed_impl (entity reference), which is not of an adequate kind
6. Actual (port spec) does not point to anything or to something unreachable
7. State_Out (port spec) points to Types  state_sig.impl (entity reference), which is not of an adequate kind
8. State_Out (port spec) does not point to anything or to something unreachable
9. State_Out (port spec) points to Types  state_sig.impl (entity reference), which is not of an adequate kind
10. State_Out (port spec) does not point to anything or to something unreachable
11. Cannot analyze AADL specifications
12. /CaseProject/modified_model.aadl | line 13: Couldn't resolve reference to 'e'.
13. /CaseProject/modified_model.aadl | line 13: Couldn't resolve reference to 'value'.
14. /CaseProject/modified_model.aadl | line 13: left side of binary expression '-' is of type '<error>' but must be of type'int' or 'real'
15. /CaseProject/modified_model.aadl | line 13: named thing must be an expression with a type
16. /CaseProject/modified_model.aadl | line 13: right side of binary expression '-' is of type '<error>' but must be of type'int' or 'real'
17. /CaseProject/modified_model.aadl | line 14: Couldn't resolve reference to 'D'.
18. /CaseProject/modified_model.aadl | line 14: Couldn't resolve reference to 'I'.
19. /CaseProject/modified_model.aadl | line 14: Couldn't resolve reference to 'P'.
20. /CaseProject/modified_model.aadl | line 14: Couldn't resolve reference to 'e'.
21. /CaseProject/modified_model.aadl | line 14: Couldn't resolve reference to 'e_dot'.
22. /CaseProject/modified_model.aadl | line 14: Couldn't resolve reference to 'e_int'.
23. /CaseProject/modified_model.aadl | line 14: left and right sides of binary expression '=' are of type 'real' and '<error>', but must be of the same type
24. /CaseProject/modified_model.aadl | line 14: left side of binary expression '*' is of type '<error>' but must be of type'int' or 'real'
25. /CaseProject/modified_model.aadl | line 14: left side of binary expression '+' is of type '<error>' but must be of type'int' or 'real'
26. /CaseProject/modified_model.aadl | line 14: named thing must be an expression with a type
27. /CaseProject/modified_model.aadl | line 14: right side of binary expression '*' is of type '<error>' but must be of type'int' or 'real'
28. /CaseProject/modified_model.aadl | line 14: right side of binary expression '+' is of type '<error>' but must be of type'int' or 'real'
29. /CaseProject/modified_model.aadl | line 15: missing EOF at 'constant'
