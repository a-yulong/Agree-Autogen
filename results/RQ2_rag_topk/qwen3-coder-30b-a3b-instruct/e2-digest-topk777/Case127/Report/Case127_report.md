# Case127 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 433.48
- Initial validation errors: 6
- Final validation errors: 50

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 5
- AGREE errors: 45
- Warnings: 6

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 83331
- completion_tokens: 10337
- total_tokens: 93668

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 2 classified requirement item(s).
4. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
5. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
6. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
7. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
8. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
9. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
10. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
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
21. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
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

1. Source_Stack_Size (property association) does not point to anything
2. Source_Stack_Size (property association) does not point to anything
3. Source_Stack_Size (property association) does not point to anything
4. Source_Stack_Size (property association) does not point to anything
5. Cannot analyze AADL specifications
6. /CaseProject/modified_model.aadl | line 163: Element of the same name ('acc_in_data_x') in AGREE Annex in 'ATTITUDE_CALCULATION'
7. /CaseProject/modified_model.aadl | line 164: Element of the same name ('acc_in_data_y') in AGREE Annex in 'ATTITUDE_CALCULATION'
8. /CaseProject/modified_model.aadl | line 165: Element of the same name ('acc_in_data_z') in AGREE Annex in 'ATTITUDE_CALCULATION'
9. /CaseProject/modified_model.aadl | line 167: Element of the same name ('mag_in_data_x') in AGREE Annex in 'ATTITUDE_CALCULATION'
10. /CaseProject/modified_model.aadl | line 168: Element of the same name ('mag_in_data_y') in AGREE Annex in 'ATTITUDE_CALCULATION'
11. /CaseProject/modified_model.aadl | line 169: Element of the same name ('mag_in_data_z') in AGREE Annex in 'ATTITUDE_CALCULATION'
12. /CaseProject/modified_model.aadl | line 171: Element of the same name ('gyro_in_data_x') in AGREE Annex in 'ATTITUDE_CALCULATION'
13. /CaseProject/modified_model.aadl | line 172: Element of the same name ('gyro_in_data_y') in AGREE Annex in 'ATTITUDE_CALCULATION'
14. /CaseProject/modified_model.aadl | line 173: Element of the same name ('gyro_in_data_z') in AGREE Annex in 'ATTITUDE_CALCULATION'
15. /CaseProject/modified_model.aadl | line 182: Feature of the same name ('acc_in_data_x') in component type
16. /CaseProject/modified_model.aadl | line 182: The assumed type of constant statement 'acc_in_data_x' is 'RealTypeDef' but the actual type is 'ErrorTypeDef'
17. /CaseProject/modified_model.aadl | line 182: mismatched input ';' expecting '='
18. /CaseProject/modified_model.aadl | line 183: Feature of the same name ('acc_in_data_y') in component type
19. /CaseProject/modified_model.aadl | line 183: The assumed type of constant statement 'acc_in_data_y' is 'RealTypeDef' but the actual type is 'ErrorTypeDef'
20. /CaseProject/modified_model.aadl | line 183: mismatched input ';' expecting '='
21. /CaseProject/modified_model.aadl | line 184: Feature of the same name ('acc_in_data_z') in component type
22. /CaseProject/modified_model.aadl | line 184: The assumed type of constant statement 'acc_in_data_z' is 'RealTypeDef' but the actual type is 'ErrorTypeDef'
23. /CaseProject/modified_model.aadl | line 184: mismatched input ';' expecting '='
24. /CaseProject/modified_model.aadl | line 185: Feature of the same name ('mag_in_data_x') in component type
25. /CaseProject/modified_model.aadl | line 185: The assumed type of constant statement 'mag_in_data_x' is 'RealTypeDef' but the actual type is 'ErrorTypeDef'
26. /CaseProject/modified_model.aadl | line 185: mismatched input ';' expecting '='
27. /CaseProject/modified_model.aadl | line 186: Feature of the same name ('mag_in_data_y') in component type
28. /CaseProject/modified_model.aadl | line 186: The assumed type of constant statement 'mag_in_data_y' is 'RealTypeDef' but the actual type is 'ErrorTypeDef'
29. /CaseProject/modified_model.aadl | line 186: mismatched input ';' expecting '='
30. /CaseProject/modified_model.aadl | line 187: Feature of the same name ('mag_in_data_z') in component type
31. /CaseProject/modified_model.aadl | line 187: The assumed type of constant statement 'mag_in_data_z' is 'RealTypeDef' but the actual type is 'ErrorTypeDef'
32. /CaseProject/modified_model.aadl | line 187: mismatched input ';' expecting '='
33. /CaseProject/modified_model.aadl | line 188: Feature of the same name ('gyro_in_data_x') in component type
34. /CaseProject/modified_model.aadl | line 188: The assumed type of constant statement 'gyro_in_data_x' is 'RealTypeDef' but the actual type is 'ErrorTypeDef'
35. /CaseProject/modified_model.aadl | line 188: mismatched input ';' expecting '='
36. /CaseProject/modified_model.aadl | line 189: Feature of the same name ('gyro_in_data_y') in component type
37. /CaseProject/modified_model.aadl | line 189: The assumed type of constant statement 'gyro_in_data_y' is 'RealTypeDef' but the actual type is 'ErrorTypeDef'
38. /CaseProject/modified_model.aadl | line 189: mismatched input ';' expecting '='
39. /CaseProject/modified_model.aadl | line 190: Feature of the same name ('gyro_in_data_z') in component type
40. /CaseProject/modified_model.aadl | line 190: The assumed type of constant statement 'gyro_in_data_z' is 'RealTypeDef' but the actual type is 'ErrorTypeDef'
41. /CaseProject/modified_model.aadl | line 190: mismatched input ';' expecting '='
42. /CaseProject/modified_model.aadl | line 191: named thing must be an expression with a type
43. /CaseProject/modified_model.aadl | line 192: named thing must be an expression with a type
44. /CaseProject/modified_model.aadl | line 193: named thing must be an expression with a type
45. /CaseProject/modified_model.aadl | line 194: named thing must be an expression with a type
46. /CaseProject/modified_model.aadl | line 195: named thing must be an expression with a type
47. /CaseProject/modified_model.aadl | line 196: named thing must be an expression with a type
48. /CaseProject/modified_model.aadl | line 197: named thing must be an expression with a type
49. /CaseProject/modified_model.aadl | line 198: named thing must be an expression with a type
50. /CaseProject/modified_model.aadl | line 199: named thing must be an expression with a type
