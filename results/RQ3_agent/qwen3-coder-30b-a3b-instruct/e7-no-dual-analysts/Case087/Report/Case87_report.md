# Case87 Refactored Experiment Report

## Summary

- Setting: E7 (No Dual Analysts)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 575.55
- Initial validation errors: 14
- Final validation errors: 65

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 5
- AGREE errors: 60
- Warnings: 6

## Modules

- rag: True
- repair: True
- requirement_analyst: False
- model_analyst: False
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 98671
- completion_tokens: 8756
- total_tokens: 107427

## Output Recovery

1. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
2. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
3. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
4. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
5. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
6. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
7. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
8. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
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
24. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
25. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
26. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
27. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
28. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
29. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
30. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. Source_Stack_Size (property association) does not point to anything
2. Source_Stack_Size (property association) does not point to anything
3. Source_Stack_Size (property association) does not point to anything
4. Source_Stack_Size (property association) does not point to anything
5. Cannot analyze AADL specifications
6. /CaseProject/modified_model.aadl | line 182: Couldn't resolve reference to 'acc_in_data_x'.
7. /CaseProject/modified_model.aadl | line 182: Couldn't resolve reference to 'attitude_sub'.
8. /CaseProject/modified_model.aadl | line 182: named thing must be an expression with a type
9. /CaseProject/modified_model.aadl | line 183: Couldn't resolve reference to 'acc_in_data_y'.
10. /CaseProject/modified_model.aadl | line 183: Couldn't resolve reference to 'attitude_sub'.
11. /CaseProject/modified_model.aadl | line 183: named thing must be an expression with a type
12. /CaseProject/modified_model.aadl | line 184: Couldn't resolve reference to 'attitude_sub'.
13. /CaseProject/modified_model.aadl | line 184: Couldn't resolve reference to 'mag_in_data_x'.
14. /CaseProject/modified_model.aadl | line 184: named thing must be an expression with a type
15. /CaseProject/modified_model.aadl | line 185: Couldn't resolve reference to 'attitude_sub'.
16. /CaseProject/modified_model.aadl | line 185: Couldn't resolve reference to 'mag_in_data_y'.
17. /CaseProject/modified_model.aadl | line 185: named thing must be an expression with a type
18. /CaseProject/modified_model.aadl | line 186: Couldn't resolve reference to 'attitude_sub'.
19. /CaseProject/modified_model.aadl | line 186: Couldn't resolve reference to 'mag_in_data_z'.
20. /CaseProject/modified_model.aadl | line 186: named thing must be an expression with a type
21. /CaseProject/modified_model.aadl | line 187: Couldn't resolve reference to 'attitude_sub'.
22. /CaseProject/modified_model.aadl | line 187: Couldn't resolve reference to 'gyro_in_data_x'.
23. /CaseProject/modified_model.aadl | line 187: named thing must be an expression with a type
24. /CaseProject/modified_model.aadl | line 188: Couldn't resolve reference to 'attitude_sub'.
25. /CaseProject/modified_model.aadl | line 188: Couldn't resolve reference to 'gyro_in_data_y'.
26. /CaseProject/modified_model.aadl | line 188: named thing must be an expression with a type
27. /CaseProject/modified_model.aadl | line 189: Couldn't resolve reference to 'attitude_sub'.
28. /CaseProject/modified_model.aadl | line 189: Couldn't resolve reference to 'gyro_in_data_z'.
29. /CaseProject/modified_model.aadl | line 189: named thing must be an expression with a type
30. /CaseProject/modified_model.aadl | line 190: Couldn't resolve reference to 'acc_in_data_x'.
31. /CaseProject/modified_model.aadl | line 190: Couldn't resolve reference to 'attitude_sub'.
32. /CaseProject/modified_model.aadl | line 190: Expression for guarantee statement is of type '<error>' but must be of type 'bool'
33. /CaseProject/modified_model.aadl | line 190: named thing must be an expression with a type
34. /CaseProject/modified_model.aadl | line 191: Couldn't resolve reference to 'acc_in_data_y'.
35. /CaseProject/modified_model.aadl | line 191: Couldn't resolve reference to 'attitude_sub'.
36. /CaseProject/modified_model.aadl | line 191: Expression for guarantee statement is of type '<error>' but must be of type 'bool'
37. /CaseProject/modified_model.aadl | line 191: named thing must be an expression with a type
38. /CaseProject/modified_model.aadl | line 192: Couldn't resolve reference to 'acc_in_data_z'.
39. /CaseProject/modified_model.aadl | line 192: Couldn't resolve reference to 'attitude_sub'.
40. /CaseProject/modified_model.aadl | line 192: Expression for guarantee statement is of type '<error>' but must be of type 'bool'
41. /CaseProject/modified_model.aadl | line 192: named thing must be an expression with a type
42. /CaseProject/modified_model.aadl | line 193: Couldn't resolve reference to 'attitude_sub'.
43. /CaseProject/modified_model.aadl | line 193: Couldn't resolve reference to 'mag_in_data_x'.
44. /CaseProject/modified_model.aadl | line 193: Expression for guarantee statement is of type '<error>' but must be of type 'bool'
45. /CaseProject/modified_model.aadl | line 193: named thing must be an expression with a type
46. /CaseProject/modified_model.aadl | line 194: Couldn't resolve reference to 'attitude_sub'.
47. /CaseProject/modified_model.aadl | line 194: Couldn't resolve reference to 'mag_in_data_y'.
48. /CaseProject/modified_model.aadl | line 194: Expression for guarantee statement is of type '<error>' but must be of type 'bool'
49. /CaseProject/modified_model.aadl | line 194: named thing must be an expression with a type
50. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to 'attitude_sub'.
51. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to 'mag_in_data_z'.
52. /CaseProject/modified_model.aadl | line 195: Expression for guarantee statement is of type '<error>' but must be of type 'bool'
53. /CaseProject/modified_model.aadl | line 195: named thing must be an expression with a type
54. /CaseProject/modified_model.aadl | line 196: Couldn't resolve reference to 'attitude_sub'.
55. /CaseProject/modified_model.aadl | line 196: Couldn't resolve reference to 'gyro_in_data_x'.
56. /CaseProject/modified_model.aadl | line 196: Expression for guarantee statement is of type '<error>' but must be of type 'bool'
57. /CaseProject/modified_model.aadl | line 196: named thing must be an expression with a type
58. /CaseProject/modified_model.aadl | line 197: Couldn't resolve reference to 'attitude_sub'.
59. /CaseProject/modified_model.aadl | line 197: Couldn't resolve reference to 'gyro_in_data_y'.
60. /CaseProject/modified_model.aadl | line 197: Expression for guarantee statement is of type '<error>' but must be of type 'bool'
61. /CaseProject/modified_model.aadl | line 197: named thing must be an expression with a type
62. /CaseProject/modified_model.aadl | line 198: Couldn't resolve reference to 'attitude_sub'.
63. /CaseProject/modified_model.aadl | line 198: Couldn't resolve reference to 'gyro_in_data_z'.
64. /CaseProject/modified_model.aadl | line 198: Expression for guarantee statement is of type '<error>' but must be of type 'bool'
65. /CaseProject/modified_model.aadl | line 198: named thing must be an expression with a type
