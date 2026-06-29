# Case103 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 388.55
- Initial validation errors: 4
- Final validation errors: 16

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 16
- Warnings: 10

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 65918
- completion_tokens: 8197
- total_tokens: 74115

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 5 classified requirement item(s).
4. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
5. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
6. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
7. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
8. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
9. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
10. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
11. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
12. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
13. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
14. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
15. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
16. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
17. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
18. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
19. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
20. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
21. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
22. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
23. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
24. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
25. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
26. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
27. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
28. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
29. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
30. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
31. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
32. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
33. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 37: left and right sides of binary expression '=' are of type 'int' and 'real', but must be of the same type
2. /CaseProject/modified_model.aadl | line 37: left side of binary expression '/' is of type 'int' but must be of type 'real'
3. /CaseProject/modified_model.aadl | line 37: no viable alternative at input '='
4. /CaseProject/modified_model.aadl | line 37: right side of binary expression '/' is of type '<error>' but must be of type 'real'
5. /CaseProject/modified_model.aadl | line 38: left and right sides of binary expression '=' are of type 'int' and 'real', but must be of the same type
6. /CaseProject/modified_model.aadl | line 38: left side of binary expression '/' is of type 'int' but must be of type 'real'
7. /CaseProject/modified_model.aadl | line 38: no viable alternative at input '='
8. /CaseProject/modified_model.aadl | line 38: right side of binary expression '/' is of type '<error>' but must be of type 'real'
9. /CaseProject/modified_model.aadl | line 39: left and right sides of binary expression '=' are of type 'int' and 'real', but must be of the same type
10. /CaseProject/modified_model.aadl | line 39: left side of binary expression '/' is of type 'int' but must be of type 'real'
11. /CaseProject/modified_model.aadl | line 39: no viable alternative at input '='
12. /CaseProject/modified_model.aadl | line 39: right side of binary expression '/' is of type '<error>' but must be of type 'real'
13. /CaseProject/modified_model.aadl | line 40: left and right sides of binary expression '=' are of type 'int' and 'real', but must be of the same type
14. /CaseProject/modified_model.aadl | line 40: left side of binary expression '/' is of type 'int' but must be of type 'real'
15. /CaseProject/modified_model.aadl | line 40: no viable alternative at input '='
16. /CaseProject/modified_model.aadl | line 40: right side of binary expression '/' is of type '<error>' but must be of type 'real'
