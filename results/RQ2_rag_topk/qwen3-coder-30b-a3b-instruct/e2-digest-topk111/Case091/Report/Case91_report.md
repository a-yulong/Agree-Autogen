# Case91 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 513.89
- Initial validation errors: 36
- Final validation errors: 36

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 36
- Warnings: 16

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 77673
- completion_tokens: 16496
- total_tokens: 94169

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 6 classified requirement item(s).
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

1. /CaseProject/modified_model.aadl | line 192: Couldn't resolve reference to 'acc1_input'.
2. /CaseProject/modified_model.aadl | line 192: Couldn't resolve reference to 'acc1_output'.
3. /CaseProject/modified_model.aadl | line 192: Couldn't resolve reference to 'acc_hm_pr'.
4. /CaseProject/modified_model.aadl | line 192: Couldn't resolve reference to 'acc_pr'.
5. /CaseProject/modified_model.aadl | line 192: Guarantee statements are allowed only in component types
6. /CaseProject/modified_model.aadl | line 192: left side of binary expression '=>' is of type '<error>' but must be of type 'bool'
7. /CaseProject/modified_model.aadl | line 192: named thing must be an expression with a type
8. /CaseProject/modified_model.aadl | line 192: right side of binary expression '=>' is of type '<error>' but must be of type 'bool'
9. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to 'acc2_input'.
10. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to 'acc2_output'.
11. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to 'acc_hm_pr'.
12. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to 'acc_pr'.
13. /CaseProject/modified_model.aadl | line 195: Guarantee statements are allowed only in component types
14. /CaseProject/modified_model.aadl | line 195: left side of binary expression '=>' is of type '<error>' but must be of type 'bool'
15. /CaseProject/modified_model.aadl | line 195: named thing must be an expression with a type
16. /CaseProject/modified_model.aadl | line 195: right side of binary expression '=>' is of type '<error>' but must be of type 'bool'
17. /CaseProject/modified_model.aadl | line 198: Assume statements are allowed only in component types
18. /CaseProject/modified_model.aadl | line 198: Couldn't resolve reference to 'acc_pr'.
19. /CaseProject/modified_model.aadl | line 198: Couldn't resolve reference to 'main_cpu'.
20. /CaseProject/modified_model.aadl | line 198: Couldn't resolve reference to 'part1'.
21. /CaseProject/modified_model.aadl | line 198: named thing must be an expression with a type
22. /CaseProject/modified_model.aadl | line 201: Assume statements are allowed only in component types
23. /CaseProject/modified_model.aadl | line 201: Couldn't resolve reference to 'acc_hm_pr'.
24. /CaseProject/modified_model.aadl | line 201: Couldn't resolve reference to 'main_cpu'.
25. /CaseProject/modified_model.aadl | line 201: Couldn't resolve reference to 'part2'.
26. /CaseProject/modified_model.aadl | line 201: named thing must be an expression with a type
27. /CaseProject/modified_model.aadl | line 204: Assume statements are allowed only in component types
28. /CaseProject/modified_model.aadl | line 204: Couldn't resolve reference to 'ADIRUp_pr'.
29. /CaseProject/modified_model.aadl | line 204: Couldn't resolve reference to 'main_cpu'.
30. /CaseProject/modified_model.aadl | line 204: Couldn't resolve reference to 'part3'.
31. /CaseProject/modified_model.aadl | line 204: named thing must be an expression with a type
32. /CaseProject/modified_model.aadl | line 207: Assume statements are allowed only in component types
33. /CaseProject/modified_model.aadl | line 207: Couldn't resolve reference to 'SHM_pr'.
34. /CaseProject/modified_model.aadl | line 207: Couldn't resolve reference to 'main_cpu'.
35. /CaseProject/modified_model.aadl | line 207: Couldn't resolve reference to 'part4'.
36. /CaseProject/modified_model.aadl | line 207: named thing must be an expression with a type
