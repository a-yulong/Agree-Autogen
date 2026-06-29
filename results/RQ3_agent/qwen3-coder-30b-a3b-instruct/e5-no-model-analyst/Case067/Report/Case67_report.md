# Case67 Refactored Experiment Report

## Summary

- Setting: E5 (No Model Analyst)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 463.15
- Initial validation errors: 21
- Final validation errors: 6

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 6
- AGREE errors: 0
- Warnings: 7

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: False
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 73094
- completion_tokens: 9142
- total_tokens: 82236

## Output Recovery

1. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] requirement_items_normalized - Normalized 2 classified requirement item(s).
3. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
4. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
5. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
6. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
7. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
8. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
9. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
10. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
11. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
12. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
13. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
14. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
15. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
16. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
17. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
18. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
19. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
20. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
21. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
22. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
23. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
24. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
25. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
26. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
27. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
28. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
29. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
30. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
31. [validation_repair] recovered_package_block - Recovered complete AADL package block.
32. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.

## Final Diagnostics

1. TMP (subcomponent) points to software_aocs  Telemetry_Processing (entity reference), which does not exist.
2. FDR (subcomponent) points to software_aocs  Failure_Detection_Isolation (entity reference), which does not exist.
3. FR (subcomponent) points to software_aocs  Failure_Recovery (entity reference), which does not exist.
4. Reconfig (subcomponent) points to software_aocs  Reconfigurations (entity reference), which does not exist. Possible mispelling of software_aocs  reconfigurations
5. ME (subcomponent) points to software_aocs  Manoeuvre_Execution (entity reference), which does not exist.
6. Cannot analyze AADL specifications
