# Case93 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 424.45
- Initial validation errors: 34
- Final validation errors: 34

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 34
- Warnings: 16

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 67825
- completion_tokens: 9934
- total_tokens: 77759

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
11. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
12. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
13. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
14. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
15. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
16. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
17. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
18. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
19. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
20. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
21. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
22. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
23. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
24. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
25. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
26. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
27. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
28. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
29. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 192: Assume statements are allowed only in component types
2. /CaseProject/modified_model.aadl | line 192: Couldn't resolve reference to 'acc_pr'.
3. /CaseProject/modified_model.aadl | line 192: Couldn't resolve reference to 'main_cpu'.
4. /CaseProject/modified_model.aadl | line 192: Couldn't resolve reference to 'part1'.
5. /CaseProject/modified_model.aadl | line 192: named thing must be an expression with a type
6. /CaseProject/modified_model.aadl | line 196: Assume statements are allowed only in component types
7. /CaseProject/modified_model.aadl | line 196: Couldn't resolve reference to 'acc_hm_pr'.
8. /CaseProject/modified_model.aadl | line 196: Couldn't resolve reference to 'main_cpu'.
9. /CaseProject/modified_model.aadl | line 196: Couldn't resolve reference to 'part2'.
10. /CaseProject/modified_model.aadl | line 196: named thing must be an expression with a type
11. /CaseProject/modified_model.aadl | line 200: Assume statements are allowed only in component types
12. /CaseProject/modified_model.aadl | line 200: Couldn't resolve reference to 'ADIRUp_pr'.
13. /CaseProject/modified_model.aadl | line 200: Couldn't resolve reference to 'main_cpu'.
14. /CaseProject/modified_model.aadl | line 200: Couldn't resolve reference to 'part3'.
15. /CaseProject/modified_model.aadl | line 200: named thing must be an expression with a type
16. /CaseProject/modified_model.aadl | line 204: Assume statements are allowed only in component types
17. /CaseProject/modified_model.aadl | line 204: Couldn't resolve reference to 'SHM_pr'.
18. /CaseProject/modified_model.aadl | line 204: Couldn't resolve reference to 'main_cpu'.
19. /CaseProject/modified_model.aadl | line 204: Couldn't resolve reference to 'part4'.
20. /CaseProject/modified_model.aadl | line 204: named thing must be an expression with a type
21. /CaseProject/modified_model.aadl | line 208: Couldn't resolve reference to 'C1'.
22. /CaseProject/modified_model.aadl | line 208: Couldn't resolve reference to 'acc1_input'.
23. /CaseProject/modified_model.aadl | line 208: Couldn't resolve reference to 'acc1_output'.
24. /CaseProject/modified_model.aadl | line 208: Couldn't resolve reference to 'acc_hm_pr'.
25. /CaseProject/modified_model.aadl | line 208: Couldn't resolve reference to 'acc_pr'.
26. /CaseProject/modified_model.aadl | line 208: Guarantee statements are allowed only in component types
27. /CaseProject/modified_model.aadl | line 208: named thing must be an expression with a type
28. /CaseProject/modified_model.aadl | line 212: Couldn't resolve reference to 'C2'.
29. /CaseProject/modified_model.aadl | line 212: Couldn't resolve reference to 'acc2_input'.
30. /CaseProject/modified_model.aadl | line 212: Couldn't resolve reference to 'acc2_output'.
31. /CaseProject/modified_model.aadl | line 212: Couldn't resolve reference to 'acc_hm_pr'.
32. /CaseProject/modified_model.aadl | line 212: Couldn't resolve reference to 'acc_pr'.
33. /CaseProject/modified_model.aadl | line 212: Guarantee statements are allowed only in component types
34. /CaseProject/modified_model.aadl | line 212: named thing must be an expression with a type
