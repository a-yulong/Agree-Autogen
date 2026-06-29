# Case36 Refactored Experiment Report

## Summary

- Setting: E5 (No Model Analyst)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 406.24
- Initial validation errors: 13
- Final validation errors: 20

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 20
- Warnings: 7

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: False
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 51288
- completion_tokens: 6958
- total_tokens: 58246

## Output Recovery

1. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] requirement_items_normalized - Normalized 4 classified requirement item(s).
3. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
4. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
5. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
6. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
7. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
8. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
9. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
10. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
11. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
12. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
13. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
14. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
15. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
16. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
17. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
18. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
19. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
20. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
21. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
22. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
23. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
24. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
25. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
26. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
27. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
28. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
29. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
30. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
31. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
32. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
33. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
34. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 14: left and right sides of binary expression '>=' are of type 'Types::speed.speed_impl' and 'real', but must be of the same type
2. /CaseProject/modified_model.aadl | line 14: left side of binary expression '>=' is of type 'Types::speed.speed_impl' but must be of type'int' or 'real'
3. /CaseProject/modified_model.aadl | line 15: left and right sides of binary expression '<' are of type 'Types::speed.speed_impl' and 'real', but must be of the same type
4. /CaseProject/modified_model.aadl | line 15: left side of binary expression '<' is of type 'Types::speed.speed_impl' but must be of type'int' or 'real'
5. /CaseProject/modified_model.aadl | line 18: left side of binary expression '<=' is of type 'Types::speed.speed_impl' but must be of type'int' or 'real'
6. /CaseProject/modified_model.aadl | line 18: right side of binary expression '<=' is of type 'Types::speed.speed_impl' but must be of type'int' or 'real'
7. /CaseProject/modified_model.aadl | line 19: Expression for guarantee statement is of type '<error>' but must be of type 'bool'
8. /CaseProject/modified_model.aadl | line 19: left and right sides of binary expression '-' are of type '<error>' and 'Types::speed.speed_impl', but must be of the same type
9. /CaseProject/modified_model.aadl | line 19: left and right sides of binary expression '-' are of type 'bool' and 'Types::speed.speed_impl', but must be of the same type
10. /CaseProject/modified_model.aadl | line 19: left side of binary expression '-' is of type '<error>' but must be of type'int' or 'real'
11. /CaseProject/modified_model.aadl | line 19: left side of binary expression '-' is of type 'bool' but must be of type'int' or 'real'
12. /CaseProject/modified_model.aadl | line 19: left side of binary expression '>' is of type 'Types::speed.speed_impl' but must be of type'int' or 'real'
13. /CaseProject/modified_model.aadl | line 19: mismatched input ')' expecting ';'
14. /CaseProject/modified_model.aadl | line 19: mismatched input ',' expecting ')'
15. /CaseProject/modified_model.aadl | line 19: mismatched input ',' expecting 'then'
16. /CaseProject/modified_model.aadl | line 19: right side of binary expression '-' is of type 'Types::speed.speed_impl' but must be of type'int' or 'real'
17. /CaseProject/modified_model.aadl | line 19: right side of binary expression '>' is of type 'Types::speed.speed_impl' but must be of type'int' or 'real'
18. /CaseProject/modified_model.aadl | line 33: 'Actual' and 'Actual_Speed' have incompatible classifiers.
19. /CaseProject/modified_model.aadl | line 35: The types of 'Target_Speed' and 'Target' do not match.
20. /CaseProject/modified_model.aadl | line 40: 'State_Out' and 'State_Signal' have incompatible classifiers.
