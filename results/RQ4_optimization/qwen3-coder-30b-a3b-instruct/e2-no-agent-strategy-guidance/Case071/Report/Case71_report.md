# Case71 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 347.13
- Initial validation errors: 8
- Final validation errors: 12

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 12
- Warnings: 2

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 29224
- completion_tokens: 3292
- total_tokens: 32516

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 2 classified requirement item(s).
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

1. /CaseProject/modified_model.aadl | line 107: Couldn't resolve reference to 'gps_pos'.
2. /CaseProject/modified_model.aadl | line 107: Couldn't resolve reference to 'pspg'.
3. /CaseProject/modified_model.aadl | line 107: left and right sides of binary expression '=' are of type 'Ardupilot_Software::GPS_Position.i' and '<error>', but must be of the same type
4. /CaseProject/modified_model.aadl | line 107: named thing must be an expression with a type
5. /CaseProject/modified_model.aadl | line 108: Couldn't resolve reference to 'pspg'.
6. /CaseProject/modified_model.aadl | line 108: Couldn't resolve reference to 'speed'.
7. /CaseProject/modified_model.aadl | line 108: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
8. /CaseProject/modified_model.aadl | line 108: named thing must be an expression with a type
9. /CaseProject/modified_model.aadl | line 109: Couldn't resolve reference to 'angle'.
10. /CaseProject/modified_model.aadl | line 109: Couldn't resolve reference to 'pspg'.
11. /CaseProject/modified_model.aadl | line 109: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
12. /CaseProject/modified_model.aadl | line 109: named thing must be an expression with a type
