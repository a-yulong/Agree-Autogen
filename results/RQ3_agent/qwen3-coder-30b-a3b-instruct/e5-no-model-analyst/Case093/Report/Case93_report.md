# Case93 Refactored Experiment Report

## Summary

- Setting: E5 (No Model Analyst)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 482.10
- Initial validation errors: 16
- Final validation errors: 16

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 16
- Warnings: 16

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: False
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 63715
- completion_tokens: 7585
- total_tokens: 71300

## Output Recovery

1. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] requirement_items_normalized - Normalized 6 classified requirement item(s).
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
25. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
26. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
27. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
28. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
29. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
30. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
31. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
32. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 192: Couldn't resolve reference to 'acc1_input'.
2. /CaseProject/modified_model.aadl | line 192: Couldn't resolve reference to 'acc1_output'.
3. /CaseProject/modified_model.aadl | line 192: Couldn't resolve reference to 'acc_hm_pr'.
4. /CaseProject/modified_model.aadl | line 192: Couldn't resolve reference to 'acc_pr'.
5. /CaseProject/modified_model.aadl | line 192: Guarantee statements are allowed only in component types
6. /CaseProject/modified_model.aadl | line 192: left side of binary expression '=>' is of type '<error>' but must be of type 'bool'
7. /CaseProject/modified_model.aadl | line 192: named thing must be an expression with a type
8. /CaseProject/modified_model.aadl | line 192: right side of binary expression '=>' is of type '<error>' but must be of type 'bool'
9. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to 'acc2_input'.
10. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to 'acc2_output'.
11. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to 'acc_hm_pr'.
12. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to 'acc_pr'.
13. /CaseProject/modified_model.aadl | line 195: Guarantee statements are allowed only in component types
14. /CaseProject/modified_model.aadl | line 195: left side of binary expression '=>' is of type '<error>' but must be of type 'bool'
15. /CaseProject/modified_model.aadl | line 195: named thing must be an expression with a type
16. /CaseProject/modified_model.aadl | line 195: right side of binary expression '=>' is of type '<error>' but must be of type 'bool'
