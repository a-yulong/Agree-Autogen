# Case131 Refactored Experiment Report

## Summary

- Setting: E6 (No Requirement Analyst)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 377.48
- Initial validation errors: 19
- Final validation errors: 6

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 5
- AGREE errors: 1
- Warnings: 4

## Modules

- rag: True
- repair: True
- requirement_analyst: False
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 36003
- completion_tokens: 6088
- total_tokens: 42091

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
3. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
4. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
5. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
6. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
7. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
8. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
9. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
10. [validation_repair] recovered_package_block - Recovered complete AADL package block.
11. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
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
26. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
27. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
28. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
29. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
30. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
31. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
32. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. Byte_Count (property association) does not point to anything
2. Byte_Count (property association) does not point to anything
3. Byte_Count (property association) does not point to anything
4. Byte_Count (property association) does not point to anything
5. Cannot analyze AADL specifications
6. /CaseProject/modified_model.aadl | line 23: missing EOF at 'constant'
