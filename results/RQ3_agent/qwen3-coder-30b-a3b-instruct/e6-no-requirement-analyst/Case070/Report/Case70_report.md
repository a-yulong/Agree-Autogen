# Case70 Refactored Experiment Report

## Summary

- Setting: E6 (No Requirement Analyst)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 505.77
- Initial validation errors: 2
- Final validation errors: 30

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 30
- Warnings: 3

## Modules

- rag: True
- repair: True
- requirement_analyst: False
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 82820
- completion_tokens: 12981
- total_tokens: 95801

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
3. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
4. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
5. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
6. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
7. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
8. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
9. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
10. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
11. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
12. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
13. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
14. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
15. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
16. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
17. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
18. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
19. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
20. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
21. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
22. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
23. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
24. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
25. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
26. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
27. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
28. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
29. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
30. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
31. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 58: left and right sides of binary expression '=' are of type '<error>' and 'real', but must be of the same type
2. /CaseProject/modified_model.aadl | line 59: left and right sides of binary expression '=' are of type '<error>' and 'bool', but must be of the same type
3. /CaseProject/modified_model.aadl | line 60: left and right sides of binary expression '=' are of type '<error>' and 'bool', but must be of the same type
4. /CaseProject/modified_model.aadl | line 61: left and right sides of binary expression '=' are of type '<error>' and 'bool', but must be of the same type
5. /CaseProject/modified_model.aadl | line 62: left and right sides of binary expression '=' are of type '<error>' and 'bool', but must be of the same type
6. /CaseProject/modified_model.aadl | line 63: left and right sides of binary expression '=' are of type '<error>' and 'bool', but must be of the same type
7. /CaseProject/modified_model.aadl | line 64: left and right sides of binary expression '=' are of type '<error>' and 'bool', but must be of the same type
8. /CaseProject/modified_model.aadl | line 64: left and right sides of binary expression '=' are of type '<error>' and 'real', but must be of the same type
9. /CaseProject/modified_model.aadl | line 65: left and right sides of binary expression '=' are of type '<error>' and 'real', but must be of the same type
10. /CaseProject/modified_model.aadl | line 66: left and right sides of binary expression '=' are of type '<error>' and 'bool', but must be of the same type
11. /CaseProject/modified_model.aadl | line 66: mismatched input ';' expecting ','
12. /CaseProject/modified_model.aadl | line 71: left and right sides of binary expression '=' are of type '<error>' and 'real', but must be of the same type
13. /CaseProject/modified_model.aadl | line 72: left and right sides of binary expression '=' are of type '<error>' and 'real', but must be of the same type
14. /CaseProject/modified_model.aadl | line 73: left and right sides of binary expression '=' are of type '<error>' and 'bool', but must be of the same type
15. /CaseProject/modified_model.aadl | line 74: left and right sides of binary expression '=' are of type '<error>' and 'bool', but must be of the same type
16. /CaseProject/modified_model.aadl | line 75: left and right sides of binary expression '=' are of type '<error>' and 'bool', but must be of the same type
17. /CaseProject/modified_model.aadl | line 76: left and right sides of binary expression '=' are of type '<error>' and 'bool', but must be of the same type
18. /CaseProject/modified_model.aadl | line 77: left and right sides of binary expression '=' are of type '<error>' and 'bool', but must be of the same type
19. /CaseProject/modified_model.aadl | line 78: left and right sides of binary expression '=' are of type '<error>' and 'bool', but must be of the same type
20. /CaseProject/modified_model.aadl | line 79: left and right sides of binary expression '=' are of type '<error>' and 'bool', but must be of the same type
21. /CaseProject/modified_model.aadl | line 80: left and right sides of binary expression '=' are of type '<error>' and 'bool', but must be of the same type
22. /CaseProject/modified_model.aadl | line 81: left and right sides of binary expression '=' are of type '<error>' and 'bool', but must be of the same type
23. /CaseProject/modified_model.aadl | line 82: left and right sides of binary expression '=' are of type '<error>' and 'bool', but must be of the same type
24. /CaseProject/modified_model.aadl | line 83: left and right sides of binary expression '=' are of type '<error>' and 'bool', but must be of the same type
25. /CaseProject/modified_model.aadl | line 84: left and right sides of binary expression '=' are of type '<error>' and 'real', but must be of the same type
26. /CaseProject/modified_model.aadl | line 85: left and right sides of binary expression '=' are of type '<error>' and 'real', but must be of the same type
27. /CaseProject/modified_model.aadl | line 86: left and right sides of binary expression '=' are of type '<error>' and 'real', but must be of the same type
28. /CaseProject/modified_model.aadl | line 87: left and right sides of binary expression '=' are of type '<error>' and 'bool', but must be of the same type
29. /CaseProject/modified_model.aadl | line 88: left and right sides of binary expression '=' are of type '<error>' and 'bool', but must be of the same type
30. /CaseProject/modified_model.aadl | line 88: mismatched input ';' expecting ','
