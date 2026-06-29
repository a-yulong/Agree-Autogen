# Case97 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 364.96
- Initial validation errors: 2
- Final validation errors: 8

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 2
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

- prompt_tokens: 58815
- completion_tokens: 15930
- total_tokens: 74745

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
11. [validation_repair] recovered_package_block - Recovered complete AADL package block.
12. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
13. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
14. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
15. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
16. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
17. [validation_repair] recovered_package_block - Recovered complete AADL package block.
18. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
19. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
20. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
21. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
22. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
23. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
24. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
25. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
26. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
27. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.

## Final Diagnostics

1. parsing Package_Specification, Empty packages are not allowed
2. Cannot parse AADL specifications
3. /CaseProject/modified_model.aadl | line 402: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@5a566922{platform:/resource/CaseProject/modified_model.aadl#partitions.partitions_public.systemHM_process.impl.agree}' must be set
4. /CaseProject/modified_model.aadl | line 402: mismatched input '{' expecting RULE_ANNEXTEXT
5. /CaseProject/modified_model.aadl | line 404: mismatched character ' ' expecting '>'
6. /CaseProject/modified_model.aadl | line 405: mismatched character ' ' expecting '>'
7. /CaseProject/modified_model.aadl | line 408: mismatched character ' ' expecting '>'
8. /CaseProject/modified_model.aadl | line 409: mismatched character ' ' expecting '>'
