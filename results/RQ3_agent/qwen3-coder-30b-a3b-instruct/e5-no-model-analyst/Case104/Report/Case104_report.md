# Case104 Refactored Experiment Report

## Summary

- Setting: E5 (No Model Analyst)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 429.27
- Initial validation errors: 8
- Final validation errors: 6

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 6
- Warnings: 6

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: False
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 77373
- completion_tokens: 10324
- total_tokens: 87697

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
15. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
16. [validation_repair] recovered_package_block - Recovered complete AADL package block.
17. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
18. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
19. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
20. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
21. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
22. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
23. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
24. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
25. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
26. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
27. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
28. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
29. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
30. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
31. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
32. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
33. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
34. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 100: Assume statements are allowed only in component types
2. /CaseProject/modified_model.aadl | line 101: Assume statements are allowed only in component types
3. /CaseProject/modified_model.aadl | line 102: Assume statements are allowed only in component types
4. /CaseProject/modified_model.aadl | line 103: Assume statements are allowed only in component types
5. /CaseProject/modified_model.aadl | line 104: Assume statements are allowed only in component types
6. /CaseProject/modified_model.aadl | line 105: Assume statements are allowed only in component types
