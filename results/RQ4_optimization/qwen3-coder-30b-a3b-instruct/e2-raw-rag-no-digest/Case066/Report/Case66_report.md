# Case66 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 330.70
- Initial validation errors: 12
- Final validation errors: 16

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 6
- AGREE errors: 10
- Warnings: 7

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 57297
- completion_tokens: 6128
- total_tokens: 63425

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 2 classified requirement item(s).
4. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
5. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
6. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
7. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
8. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
9. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
10. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
11. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
12. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
13. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
14. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
15. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
16. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
17. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
18. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
19. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
20. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
21. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
22. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
23. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
24. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
25. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
26. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
27. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. TMP (subcomponent) points to software_aocs  Telemetry_Processing (entity reference), which does not exist.
2. FDR (subcomponent) points to software_aocs  Failure_Detection_Isolation (entity reference), which does not exist.
3. FR (subcomponent) points to software_aocs  Failure_Recovery (entity reference), which does not exist.
4. Reconfig (subcomponent) points to software_aocs  Reconfigurations (entity reference), which does not exist. Possible mispelling of software_aocs  reconfigurations
5. ME (subcomponent) points to software_aocs  Manoeuvre_Execution (entity reference), which does not exist.
6. Cannot analyze AADL specifications
7. /CaseProject/modified_model.aadl | line 73: Couldn't resolve reference to 'ACF'.
8. /CaseProject/modified_model.aadl | line 73: Couldn't resolve reference to 'TCP'.
9. /CaseProject/modified_model.aadl | line 73: Couldn't resolve reference to 'nominal_attitude'.
10. /CaseProject/modified_model.aadl | line 73: named thing must be an expression with a type
11. /CaseProject/modified_model.aadl | line 79: Couldn't resolve reference to 'OCF'.
12. /CaseProject/modified_model.aadl | line 79: Couldn't resolve reference to 'TCP'.
13. /CaseProject/modified_model.aadl | line 79: Couldn't resolve reference to 'nominal_orbit'.
14. /CaseProject/modified_model.aadl | line 79: named thing must be an expression with a type
15. /CaseProject/modified_model.aadl | line 127: Couldn't resolve reference to ConnectionEnd 'attitude_window'.
16. /CaseProject/modified_model.aadl | line 128: Couldn't resolve reference to ConnectionEnd 'check_thresholds'.
