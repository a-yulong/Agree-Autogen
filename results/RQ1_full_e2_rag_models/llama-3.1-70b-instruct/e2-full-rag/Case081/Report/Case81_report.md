# Case81 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 388.37
- Initial validation errors: 11
- Final validation errors: 15

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 15
- Warnings: 0

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 45983
- completion_tokens: 5596
- total_tokens: 51579

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 5 classified requirement item(s).
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

1. /CaseProject/modified_model.aadl | line 46: Couldn't resolve reference to 'periodic'.
2. /CaseProject/modified_model.aadl | line 46: named thing must be an expression with a type
3. /CaseProject/modified_model.aadl | line 46: no viable alternative at input 'Dispatch_Protocol'
4. /CaseProject/modified_model.aadl | line 47: extraneous input 'ms' expecting ';'
5. /CaseProject/modified_model.aadl | line 47: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
6. /CaseProject/modified_model.aadl | line 47: no viable alternative at input 'Period'
7. /CaseProject/modified_model.aadl | line 48: extraneous input 'ms' expecting ';'
8. /CaseProject/modified_model.aadl | line 48: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
9. /CaseProject/modified_model.aadl | line 48: no viable alternative at input 'Deadline'
10. /CaseProject/modified_model.aadl | line 49: left and right sides of binary expression '>=' are of type '<error>' and 'int', but must be of the same type
11. /CaseProject/modified_model.aadl | line 49: left side of binary expression '>=' is of type '<error>' but must be of type'int' or 'real'
12. /CaseProject/modified_model.aadl | line 49: mismatched input 'ms' expecting ';'
13. /CaseProject/modified_model.aadl | line 49: no viable alternative at input 'Compute_Execution_Time'
14. /CaseProject/modified_model.aadl | line 50: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
15. /CaseProject/modified_model.aadl | line 50: no viable alternative at input 'Priority'
