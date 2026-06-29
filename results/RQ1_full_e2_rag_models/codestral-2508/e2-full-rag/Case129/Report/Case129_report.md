# Case129 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 306.65
- Initial validation errors: 19
- Final validation errors: 4

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 3
- AGREE errors: 1
- Warnings: 1

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 40021
- completion_tokens: 5966
- total_tokens: 45987

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 4 classified requirement item(s).
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
21. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
22. [validation_repair] recovered_package_block - Recovered complete AADL package block.
23. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
24. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
25. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
26. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
27. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
28. [validation_repair] recovered_package_block - Recovered complete AADL package block.
29. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
30. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
31. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
32. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
33. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.

## Final Diagnostics

1. Byte_Count (property association) does not point to anything
2. Byte_Count (property association) points to segment1 (identifier) that is not a valid subcomponent
3. Cannot analyze AADL specifications
4. /CaseProject/modified_model.aadl | line 97: Could not find path element segment1 in subcomponent segment1
