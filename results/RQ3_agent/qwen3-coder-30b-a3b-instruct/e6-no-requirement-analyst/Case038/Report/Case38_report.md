# Case38 Refactored Experiment Report

## Summary

- Setting: E6 (No Requirement Analyst)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 322.22
- Initial validation errors: 10
- Final validation errors: 7

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 5
- AGREE errors: 2
- Warnings: 4

## Modules

- rag: True
- repair: True
- requirement_analyst: False
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 32754
- completion_tokens: 4980
- total_tokens: 37734

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
3. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
4. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
5. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
6. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
7. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
8. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
9. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
10. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
11. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
12. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
13. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
14. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
15. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
16. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
17. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
18. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
19. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
20. [validation_repair] recovered_package_block - Recovered complete AADL package block.
21. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
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

1. State_Out (port spec) points to Types  state_sig.impl (entity reference), which is not of an adequate kind
2. State_Out (port spec) does not point to anything or to something unreachable
3. State_Out (port spec) points to Types  state_sig.impl (entity reference), which is not of an adequate kind
4. State_Out (port spec) does not point to anything or to something unreachable
5. Cannot analyze AADL specifications
6. /CaseProject/modified_model.aadl | line 17: extraneous input '' + I * integrate((Target - Actual), 0.0);\r\n\r\n\t\teq e : real = Target - Actual;\r\n\t\teq e_dot : real = (Target - Actual)'' expecting ';'
7. /CaseProject/modified_model.aadl | line 21: Couldn't resolve reference to 'integrate'.
