# Case103 Refactored Experiment Report

## Summary

- Setting: E6 (No Requirement Analyst)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 379.33
- Initial validation errors: 6
- Final validation errors: 30

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 30
- Warnings: 12

## Modules

- rag: True
- repair: True
- requirement_analyst: False
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 59191
- completion_tokens: 8723
- total_tokens: 67914

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
3. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
4. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
5. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
6. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
7. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
8. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
9. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
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
25. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
26. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
27. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
28. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
29. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
30. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
31. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 41: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
2. /CaseProject/modified_model.aadl | line 41: left side of binary expression '/' is of type '<error>' but must be of type 'real'
3. /CaseProject/modified_model.aadl | line 41: no viable alternative at input '/'
4. /CaseProject/modified_model.aadl | line 41: no viable alternative at input '='
5. /CaseProject/modified_model.aadl | line 41: right side of binary expression '/' is of type '<error>' but must be of type 'real'
6. /CaseProject/modified_model.aadl | line 44: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
7. /CaseProject/modified_model.aadl | line 44: left side of binary expression '/' is of type '<error>' but must be of type 'real'
8. /CaseProject/modified_model.aadl | line 44: no viable alternative at input '/'
9. /CaseProject/modified_model.aadl | line 44: no viable alternative at input '='
10. /CaseProject/modified_model.aadl | line 44: right side of binary expression '/' is of type '<error>' but must be of type 'real'
11. /CaseProject/modified_model.aadl | line 47: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
12. /CaseProject/modified_model.aadl | line 47: left side of binary expression '/' is of type '<error>' but must be of type 'real'
13. /CaseProject/modified_model.aadl | line 47: no viable alternative at input '/'
14. /CaseProject/modified_model.aadl | line 47: no viable alternative at input '='
15. /CaseProject/modified_model.aadl | line 47: right side of binary expression '/' is of type '<error>' but must be of type 'real'
16. /CaseProject/modified_model.aadl | line 50: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
17. /CaseProject/modified_model.aadl | line 50: left side of binary expression '/' is of type '<error>' but must be of type 'real'
18. /CaseProject/modified_model.aadl | line 50: no viable alternative at input '/'
19. /CaseProject/modified_model.aadl | line 50: no viable alternative at input '='
20. /CaseProject/modified_model.aadl | line 50: right side of binary expression '/' is of type '<error>' but must be of type 'real'
21. /CaseProject/modified_model.aadl | line 53: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
22. /CaseProject/modified_model.aadl | line 53: left side of binary expression '/' is of type '<error>' but must be of type 'real'
23. /CaseProject/modified_model.aadl | line 53: no viable alternative at input '/'
24. /CaseProject/modified_model.aadl | line 53: no viable alternative at input '='
25. /CaseProject/modified_model.aadl | line 53: right side of binary expression '/' is of type '<error>' but must be of type 'real'
26. /CaseProject/modified_model.aadl | line 56: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
27. /CaseProject/modified_model.aadl | line 56: left side of binary expression '/' is of type '<error>' but must be of type 'real'
28. /CaseProject/modified_model.aadl | line 56: no viable alternative at input '/'
29. /CaseProject/modified_model.aadl | line 56: no viable alternative at input '='
30. /CaseProject/modified_model.aadl | line 56: right side of binary expression '/' is of type '<error>' but must be of type 'real'
