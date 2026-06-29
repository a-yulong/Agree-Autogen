# Case42 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 392.41
- Initial validation errors: 24
- Final validation errors: 24

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 24
- Warnings: 2

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 45024
- completion_tokens: 6973
- total_tokens: 51997

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 6 classified requirement item(s).
4. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
5. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
6. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
7. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
8. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
9. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
10. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
11. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
12. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
13. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
14. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
15. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
16. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
17. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
18. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
19. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
20. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
21. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
22. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
23. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
24. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
25. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 70: Couldn't resolve reference to 'clear_TO_MC_clear'.
2. /CaseProject/modified_model.aadl | line 70: named thing must be an expression with a type
3. /CaseProject/modified_model.aadl | line 70: right side of binary expression '=>' is of type '<error>' but must be of type 'bool'
4. /CaseProject/modified_model.aadl | line 71: Couldn't resolve reference to 'clear_TO_DC_clear'.
5. /CaseProject/modified_model.aadl | line 71: named thing must be an expression with a type
6. /CaseProject/modified_model.aadl | line 71: right side of binary expression '=>' is of type '<error>' but must be of type 'bool'
7. /CaseProject/modified_model.aadl | line 72: Couldn't resolve reference to 'start_TO_MC_start'.
8. /CaseProject/modified_model.aadl | line 72: named thing must be an expression with a type
9. /CaseProject/modified_model.aadl | line 72: right side of binary expression '=>' is of type '<error>' but must be of type 'bool'
10. /CaseProject/modified_model.aadl | line 73: Couldn't resolve reference to 'kp_0_TO_DC_kp_0'.
11. /CaseProject/modified_model.aadl | line 73: named thing must be an expression with a type
12. /CaseProject/modified_model.aadl | line 73: right side of binary expression '=>' is of type '<error>' but must be of type 'bool'
13. /CaseProject/modified_model.aadl | line 74: Couldn't resolve reference to 'clear_TO_MC_clear'.
14. /CaseProject/modified_model.aadl | line 74: left and right sides of binary expression '=' are of type '<error>' and 'bool', but must be of the same type
15. /CaseProject/modified_model.aadl | line 74: named thing must be an expression with a type
16. /CaseProject/modified_model.aadl | line 75: Couldn't resolve reference to 'clear_TO_DC_clear'.
17. /CaseProject/modified_model.aadl | line 75: left and right sides of binary expression '=' are of type '<error>' and 'bool', but must be of the same type
18. /CaseProject/modified_model.aadl | line 75: named thing must be an expression with a type
19. /CaseProject/modified_model.aadl | line 76: Couldn't resolve reference to 'start_TO_MC_start'.
20. /CaseProject/modified_model.aadl | line 76: left and right sides of binary expression '=' are of type '<error>' and 'bool', but must be of the same type
21. /CaseProject/modified_model.aadl | line 76: named thing must be an expression with a type
22. /CaseProject/modified_model.aadl | line 77: Couldn't resolve reference to 'kp_0_TO_DC_kp_0'.
23. /CaseProject/modified_model.aadl | line 77: left and right sides of binary expression '=' are of type '<error>' and 'bool', but must be of the same type
24. /CaseProject/modified_model.aadl | line 77: named thing must be an expression with a type
