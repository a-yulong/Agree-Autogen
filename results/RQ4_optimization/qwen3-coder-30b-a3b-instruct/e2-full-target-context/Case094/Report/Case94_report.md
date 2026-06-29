# Case94 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 476.42
- Initial validation errors: 24
- Final validation errors: 6

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 6
- Warnings: 8

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 136169
- completion_tokens: 20404
- total_tokens: 156573

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
12. [validation_repair] recovered_package_block - Recovered complete AADL package block.
13. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
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
28. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
29. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
30. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
31. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
32. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
33. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
34. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 125: Assume statements are allowed only in component types
2. /CaseProject/modified_model.aadl | line 126: Assume statements are allowed only in component types
3. /CaseProject/modified_model.aadl | line 127: Assume statements are allowed only in component types
4. /CaseProject/modified_model.aadl | line 128: Assume statements are allowed only in component types
5. /CaseProject/modified_model.aadl | line 129: Assume statements are allowed only in component types
6. /CaseProject/modified_model.aadl | line 130: Assume statements are allowed only in component types
