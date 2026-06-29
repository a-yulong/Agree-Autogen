# Case121 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 387.97
- Initial validation errors: 4
- Final validation errors: 20

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 5
- AGREE errors: 15
- Warnings: 6

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 56724
- completion_tokens: 12352
- total_tokens: 69076

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 2 classified requirement item(s).
4. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
5. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
6. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
7. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
8. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
9. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
10. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
11. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
12. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
13. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
14. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
15. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
16. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
17. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
18. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
19. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
20. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
21. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
22. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
23. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
24. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
25. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
26. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
27. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
28. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
29. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. Source_Stack_Size (property association) does not point to anything
2. Source_Stack_Size (property association) does not point to anything
3. Source_Stack_Size (property association) does not point to anything
4. Source_Stack_Size (property association) does not point to anything
5. Cannot analyze AADL specifications
6. /CaseProject/modified_model.aadl | line 36: Assignment statements are allowed only in component implementations
7. /CaseProject/modified_model.aadl | line 36: Couldn't resolve reference to '"output_x_dependency": acc_out_data_x'.
8. /CaseProject/modified_model.aadl | line 36: Couldn't resolve reference to 'acc_out_data_x'.
9. /CaseProject/modified_model.aadl | line 36: Couldn't resolve reference to 'accelero_sub'.
10. /CaseProject/modified_model.aadl | line 36: mismatched input '"output_x_dependency"' expecting RULE_ID
11. /CaseProject/modified_model.aadl | line 37: Assignment statements are allowed only in component implementations
12. /CaseProject/modified_model.aadl | line 37: Couldn't resolve reference to '"output_y_dependency": acc_out_data_y'.
13. /CaseProject/modified_model.aadl | line 37: Couldn't resolve reference to 'acc_out_data_y'.
14. /CaseProject/modified_model.aadl | line 37: Couldn't resolve reference to 'accelero_sub'.
15. /CaseProject/modified_model.aadl | line 37: mismatched input '"output_y_dependency"' expecting RULE_ID
16. /CaseProject/modified_model.aadl | line 38: Assignment statements are allowed only in component implementations
17. /CaseProject/modified_model.aadl | line 38: Couldn't resolve reference to '"output_z_dependency": acc_out_data_z'.
18. /CaseProject/modified_model.aadl | line 38: Couldn't resolve reference to 'acc_out_data_z'.
19. /CaseProject/modified_model.aadl | line 38: Couldn't resolve reference to 'accelero_sub'.
20. /CaseProject/modified_model.aadl | line 38: mismatched input '"output_z_dependency"' expecting RULE_ID
