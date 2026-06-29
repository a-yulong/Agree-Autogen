# Case07 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 348.92
- Initial validation errors: 8
- Final validation errors: 8

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 8
- Warnings: 5

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 44898
- completion_tokens: 4648
- total_tokens: 49546

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 5 classified requirement item(s).
4. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
5. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
6. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
7. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
8. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
9. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
10. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
11. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
12. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
13. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
14. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
15. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
16. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
17. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
18. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
19. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
20. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
21. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
22. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
23. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
24. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
25. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
26. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
27. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 100: mismatched input '(' expecting ':'
2. /CaseProject/modified_model.aadl | line 100: mismatched input ')' expecting ';'
3. /CaseProject/modified_model.aadl | line 101: mismatched input '(' expecting ':'
4. /CaseProject/modified_model.aadl | line 101: mismatched input ')' expecting ';'
5. /CaseProject/modified_model.aadl | line 102: left and right sides of binary expression '=' are of type 'real' and '<error>', but must be of the same type
6. /CaseProject/modified_model.aadl | line 103: left and right sides of binary expression '=' are of type 'bool' and '<error>', but must be of the same type
7. /CaseProject/modified_model.aadl | line 104: left and right sides of binary expression '=' are of type 'bool' and '<error>', but must be of the same type
8. /CaseProject/modified_model.aadl | line 105: left and right sides of binary expression '=' are of type 'bool' and '<error>', but must be of the same type
