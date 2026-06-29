# Case54 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 366.50
- Initial validation errors: 4
- Final validation errors: 9

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 9
- AGREE errors: 0
- Warnings: 0

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 32912
- completion_tokens: 5531
- total_tokens: 38443

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
12. [validation_repair] recovered_package_block - Recovered complete AADL package block.
13. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
14. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
15. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
16. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
17. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
18. [validation_repair] recovered_package_block - Recovered complete AADL package block.
19. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
20. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
21. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
22. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
23. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
24. [validation_repair] recovered_package_block - Recovered complete AADL package block.
25. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
26. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
27. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
28. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
29. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
30. [validation_repair] recovered_package_block - Recovered complete AADL package block.
31. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
32. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
33. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
34. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
35. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
36. [validation_repair] recovered_package_block - Recovered complete AADL package block.
37. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy_Extended (package specification)
2. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy_Extended (package specification)
3. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy_Extended (package specification)
4. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy_Extended (package specification)
5. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy_Extended (package specification)
6. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy_Extended (package specification)
7. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy_Extended (package specification)
8. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy_Extended (package specification)
9. Cannot analyze AADL specifications
