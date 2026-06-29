# Case81 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 284.73
- Initial validation errors: 24
- Final validation errors: 24

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 24
- Warnings: 0

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 30471
- completion_tokens: 3588
- total_tokens: 34059

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 5 classified requirement item(s).
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

1. /CaseProject/modified_model.aadl | line 46: Couldn't resolve reference to 'Dispatch_Protocol'.
2. /CaseProject/modified_model.aadl | line 46: Couldn't resolve reference to 'impl'.
3. /CaseProject/modified_model.aadl | line 46: named thing must be an expression with a type
4. /CaseProject/modified_model.aadl | line 46: no viable alternative at input '"periodic"'
5. /CaseProject/modified_model.aadl | line 47: Couldn't resolve reference to 'Period'.
6. /CaseProject/modified_model.aadl | line 47: Couldn't resolve reference to 'impl'.
7. /CaseProject/modified_model.aadl | line 47: extraneous input 'ms' expecting ';'
8. /CaseProject/modified_model.aadl | line 47: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
9. /CaseProject/modified_model.aadl | line 47: named thing must be an expression with a type
10. /CaseProject/modified_model.aadl | line 48: Couldn't resolve reference to 'Deadline'.
11. /CaseProject/modified_model.aadl | line 48: Couldn't resolve reference to 'impl'.
12. /CaseProject/modified_model.aadl | line 48: extraneous input 'ms' expecting ';'
13. /CaseProject/modified_model.aadl | line 48: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
14. /CaseProject/modified_model.aadl | line 48: named thing must be an expression with a type
15. /CaseProject/modified_model.aadl | line 49: Couldn't resolve reference to 'Compute_Execution_Time'.
16. /CaseProject/modified_model.aadl | line 49: Couldn't resolve reference to 'impl'.
17. /CaseProject/modified_model.aadl | line 49: left and right sides of binary expression '>=' are of type '<error>' and 'int', but must be of the same type
18. /CaseProject/modified_model.aadl | line 49: left side of binary expression '>=' is of type '<error>' but must be of type'int' or 'real'
19. /CaseProject/modified_model.aadl | line 49: mismatched input 'ms' expecting ';'
20. /CaseProject/modified_model.aadl | line 49: named thing must be an expression with a type
21. /CaseProject/modified_model.aadl | line 50: Couldn't resolve reference to 'Priority'.
22. /CaseProject/modified_model.aadl | line 50: Couldn't resolve reference to 'impl'.
23. /CaseProject/modified_model.aadl | line 50: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
24. /CaseProject/modified_model.aadl | line 50: named thing must be an expression with a type
