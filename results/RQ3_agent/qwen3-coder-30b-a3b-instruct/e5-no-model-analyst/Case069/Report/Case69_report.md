# Case69 Refactored Experiment Report

## Summary

- Setting: E5 (No Model Analyst)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 417.12
- Initial validation errors: 3
- Final validation errors: 21

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 21
- Warnings: 3

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: False
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 60482
- completion_tokens: 6620
- total_tokens: 67102

## Output Recovery

1. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] requirement_items_normalized - Normalized 3 classified requirement item(s).
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
20. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
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

1. /CaseProject/modified_model.aadl | line 55: Couldn't resolve reference to 'ms'.
2. /CaseProject/modified_model.aadl | line 55: extraneous input ')' expecting ';'
3. /CaseProject/modified_model.aadl | line 55: left and right sides of binary expression '<=' are of type '<error>' and 'real', but must be of the same type
4. /CaseProject/modified_model.aadl | line 55: left and right sides of binary expression '<=' are of type 'real' and '<error>', but must be of the same type
5. /CaseProject/modified_model.aadl | line 55: left side of binary expression '<=' is of type '<error>' but must be of type'int' or 'real'
6. /CaseProject/modified_model.aadl | line 55: missing ')' at '<='
7. /CaseProject/modified_model.aadl | line 55: missing ',' at 'ms'
8. /CaseProject/modified_model.aadl | line 55: missing 'in' at '('
9. /CaseProject/modified_model.aadl | line 55: named thing must be an expression with a type
10. /CaseProject/modified_model.aadl | line 55: no viable alternative at input 'ms'
11. /CaseProject/modified_model.aadl | line 55: right side of binary expression '<=' is of type '<error>' but must be of type'int' or 'real'
12. /CaseProject/modified_model.aadl | line 56: left side of binary expression '=>' is of type '<error>' but must be of type 'bool'
13. /CaseProject/modified_model.aadl | line 56: left side of binary expression 'and' is of type '<error>' but must be of type 'bool'
14. /CaseProject/modified_model.aadl | line 56: mismatched input ';' expecting ','
15. /CaseProject/modified_model.aadl | line 56: missing 'in' at '('
16. /CaseProject/modified_model.aadl | line 56: right side of binary expression 'and' is of type '<error>' but must be of type 'bool'
17. /CaseProject/modified_model.aadl | line 57: left side of binary expression '=>' is of type '<error>' but must be of type 'bool'
18. /CaseProject/modified_model.aadl | line 57: left side of binary expression 'or' is of type '<error>' but must be of type 'bool'
19. /CaseProject/modified_model.aadl | line 57: mismatched input ';' expecting ','
20. /CaseProject/modified_model.aadl | line 57: missing 'in' at '('
21. /CaseProject/modified_model.aadl | line 57: right side of binary expression 'or' is of type '<error>' but must be of type 'bool'
