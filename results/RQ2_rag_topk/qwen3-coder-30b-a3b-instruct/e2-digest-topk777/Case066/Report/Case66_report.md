# Case66 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 380.30
- Initial validation errors: 6
- Final validation errors: 9

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 6
- AGREE errors: 3
- Warnings: 7

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 68549
- completion_tokens: 8803
- total_tokens: 77352

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
11. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
12. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
13. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
14. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
15. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
16. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
17. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
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
28. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
29. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
30. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
31. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
32. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
33. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
34. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
35. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. TMP (subcomponent) points to software_aocs  Telemetry_Processing (entity reference), which does not exist.
2. FDR (subcomponent) points to software_aocs  Failure_Detection_Isolation (entity reference), which does not exist.
3. FR (subcomponent) points to software_aocs  Failure_Recovery (entity reference), which does not exist.
4. Reconfig (subcomponent) points to software_aocs  Reconfigurations (entity reference), which does not exist. Possible mispelling of software_aocs  reconfigurations
5. ME (subcomponent) points to software_aocs  Manoeuvre_Execution (entity reference), which does not exist.
6. Cannot analyze AADL specifications
7. /CaseProject/modified_model.aadl | line 75: missing EOF at 'var'
8. /CaseProject/modified_model.aadl | line 117: Couldn't resolve reference to ConnectionEnd 'attitude_window'.
9. /CaseProject/modified_model.aadl | line 118: Couldn't resolve reference to ConnectionEnd 'check_thresholds'.
