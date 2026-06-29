# Case244 Refactored Experiment Report

## Summary

- Setting: E6 (No Requirement Analyst)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 404.31
- Initial validation errors: 7
- Final validation errors: 8

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 8
- Warnings: 0

## Modules

- rag: True
- repair: True
- requirement_analyst: False
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 70723
- completion_tokens: 9334
- total_tokens: 80057

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
30. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
31. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 95: Assume statements are allowed only in component types
2. /CaseProject/modified_model.aadl | line 96: Guarantee statements are allowed only in component types
3. /CaseProject/modified_model.aadl | line 97: Guarantee statements are allowed only in component types
4. /CaseProject/modified_model.aadl | line 98: Guarantee statements are allowed only in component types
5. /CaseProject/modified_model.aadl | line 99: Guarantee statements are allowed only in component types
6. /CaseProject/modified_model.aadl | line 100: Guarantee statements are allowed only in component types
7. /CaseProject/modified_model.aadl | line 101: Guarantee statements are allowed only in component types
8. /CaseProject/modified_model.aadl | line 102: Guarantee statements are allowed only in component types
