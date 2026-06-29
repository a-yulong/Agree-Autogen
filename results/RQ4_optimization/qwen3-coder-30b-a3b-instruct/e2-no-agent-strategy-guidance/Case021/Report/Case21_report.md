# Case21 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 316.26
- Initial validation errors: 19
- Final validation errors: 17

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 17
- Warnings: 1

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 28213
- completion_tokens: 3528
- total_tokens: 31741

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 4 classified requirement item(s).
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

1. /CaseProject/modified_model.aadl | line 17: missing ';' at 'cooler_on'
2. /CaseProject/modified_model.aadl | line 24: Couldn't resolve reference to 'k'.
3. /CaseProject/modified_model.aadl | line 24: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
4. /CaseProject/modified_model.aadl | line 24: named thing must be an expression with a type
5. /CaseProject/modified_model.aadl | line 25: Couldn't resolve reference to 'k'.
6. /CaseProject/modified_model.aadl | line 25: left and right sides of binary expression '+' are of type '<error>' and 'int', but must be of the same type
7. /CaseProject/modified_model.aadl | line 25: left and right sides of binary expression '-' are of type '<error>' and 'int', but must be of the same type
8. /CaseProject/modified_model.aadl | line 25: left and right sides of binary expression '<=' are of type '<error>' and 'int', but must be of the same type
9. /CaseProject/modified_model.aadl | line 25: left and right sides of binary expression '>=' are of type '<error>' and 'int', but must be of the same type
10. /CaseProject/modified_model.aadl | line 25: left side of binary expression '+' is of type '<error>' but must be of type'int' or 'real'
11. /CaseProject/modified_model.aadl | line 25: left side of binary expression '-' is of type '<error>' but must be of type'int' or 'real'
12. /CaseProject/modified_model.aadl | line 25: left side of binary expression '<=' is of type '<error>' but must be of type'int' or 'real'
13. /CaseProject/modified_model.aadl | line 25: left side of binary expression '>=' is of type '<error>' but must be of type'int' or 'real'
14. /CaseProject/modified_model.aadl | line 25: named thing must be an expression with a type
15. /CaseProject/modified_model.aadl | line 26: Couldn't resolve reference to 'k'.
16. /CaseProject/modified_model.aadl | line 26: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
17. /CaseProject/modified_model.aadl | line 26: named thing must be an expression with a type
