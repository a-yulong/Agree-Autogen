# Case93 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 601.65
- Initial validation errors: 36
- Final validation errors: 20

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 20
- Warnings: 16

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 67538
- completion_tokens: 12943
- total_tokens: 80481

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 6 classified requirement item(s).
4. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
5. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
6. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
7. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
8. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
9. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
10. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
11. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
12. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
13. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
14. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
15. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
16. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
17. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
18. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
19. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
20. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
21. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
22. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
23. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
24. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
25. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
26. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
27. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 192: Assume statements are allowed only in component types
2. /CaseProject/modified_model.aadl | line 192: Couldn't resolve reference to 'acc_pr'.
3. /CaseProject/modified_model.aadl | line 192: Couldn't resolve reference to 'main_cpu'.
4. /CaseProject/modified_model.aadl | line 192: Couldn't resolve reference to 'part1'.
5. /CaseProject/modified_model.aadl | line 192: named thing must be an expression with a type
6. /CaseProject/modified_model.aadl | line 195: Assume statements are allowed only in component types
7. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to 'acc_hm_pr'.
8. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to 'main_cpu'.
9. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to 'part2'.
10. /CaseProject/modified_model.aadl | line 195: named thing must be an expression with a type
11. /CaseProject/modified_model.aadl | line 198: Assume statements are allowed only in component types
12. /CaseProject/modified_model.aadl | line 198: Couldn't resolve reference to 'ADIRUp_pr'.
13. /CaseProject/modified_model.aadl | line 198: Couldn't resolve reference to 'main_cpu'.
14. /CaseProject/modified_model.aadl | line 198: Couldn't resolve reference to 'part3'.
15. /CaseProject/modified_model.aadl | line 198: named thing must be an expression with a type
16. /CaseProject/modified_model.aadl | line 201: Assume statements are allowed only in component types
17. /CaseProject/modified_model.aadl | line 201: Couldn't resolve reference to 'SHM_pr'.
18. /CaseProject/modified_model.aadl | line 201: Couldn't resolve reference to 'main_cpu'.
19. /CaseProject/modified_model.aadl | line 201: Couldn't resolve reference to 'part4'.
20. /CaseProject/modified_model.aadl | line 201: named thing must be an expression with a type
