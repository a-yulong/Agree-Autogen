# Case60 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 404.16
- Initial validation errors: 20
- Final validation errors: 67

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 67
- Warnings: 2

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 137296
- completion_tokens: 18685
- total_tokens: 155981

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 4 classified requirement item(s).
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
17. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
18. [validation_repair] recovered_package_block - Recovered complete AADL package block.
19. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
20. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
21. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
22. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
23. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
24. [validation_repair] recovered_package_block - Recovered complete AADL package block.
25. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
26. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
27. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
28. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
29. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
30. [validation_repair] recovered_package_block - Recovered complete AADL package block.
31. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
32. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
33. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
34. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
35. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
36. [validation_repair] recovered_package_block - Recovered complete AADL package block.
37. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 105: Argument 0 of function call 'Latch' is of type 'ErrorTypeDef' but must be of type 'BoolTypeDef'
2. /CaseProject/modified_model.aadl | line 105: Couldn't resolve reference to 'FailCOM1'.
3. /CaseProject/modified_model.aadl | line 105: named thing must be an expression with a type
4. /CaseProject/modified_model.aadl | line 106: Argument 0 of function call 'Latch' is of type 'ErrorTypeDef' but must be of type 'BoolTypeDef'
5. /CaseProject/modified_model.aadl | line 106: Couldn't resolve reference to 'FailCOM2'.
6. /CaseProject/modified_model.aadl | line 106: named thing must be an expression with a type
7. /CaseProject/modified_model.aadl | line 107: Argument 0 of function call 'Latch' is of type 'ErrorTypeDef' but must be of type 'BoolTypeDef'
8. /CaseProject/modified_model.aadl | line 107: Couldn't resolve reference to 'FailMON1'.
9. /CaseProject/modified_model.aadl | line 107: named thing must be an expression with a type
10. /CaseProject/modified_model.aadl | line 108: Argument 0 of function call 'Latch' is of type 'ErrorTypeDef' but must be of type 'BoolTypeDef'
11. /CaseProject/modified_model.aadl | line 108: Couldn't resolve reference to 'FailMON2'.
12. /CaseProject/modified_model.aadl | line 108: named thing must be an expression with a type
13. /CaseProject/modified_model.aadl | line 139: Couldn't resolve reference to 'CH1'.
14. /CaseProject/modified_model.aadl | line 139: Couldn't resolve reference to 'CH2'.
15. /CaseProject/modified_model.aadl | line 139: Couldn't resolve reference to 'Error'.
16. /CaseProject/modified_model.aadl | line 139: left side of binary expression 'or' is of type '<error>' but must be of type 'bool'
17. /CaseProject/modified_model.aadl | line 139: named thing must be an expression with a type
18. /CaseProject/modified_model.aadl | line 139: right side of binary expression 'or' is of type '<error>' but must be of type 'bool'
19. /CaseProject/modified_model.aadl | line 139: right side of unary expression 'not' is of type 'ErrorTypeDef' but must be of type 'bool'
20. /CaseProject/modified_model.aadl | line 145: Couldn't resolve reference to 'CH1'.
21. /CaseProject/modified_model.aadl | line 145: Couldn't resolve reference to 'CH2'.
22. /CaseProject/modified_model.aadl | line 145: Couldn't resolve reference to 'Error'.
23. /CaseProject/modified_model.aadl | line 145: left side of binary expression 'or' is of type '<error>' but must be of type 'bool'
24. /CaseProject/modified_model.aadl | line 145: named thing must be an expression with a type
25. /CaseProject/modified_model.aadl | line 145: right side of binary expression 'or' is of type '<error>' but must be of type 'bool'
26. /CaseProject/modified_model.aadl | line 145: right side of unary expression 'not' is of type 'ErrorTypeDef' but must be of type 'bool'
27. /CaseProject/modified_model.aadl | line 151: Couldn't resolve reference to 'Active'.
28. /CaseProject/modified_model.aadl | line 151: Couldn't resolve reference to 'CH1'.
29. /CaseProject/modified_model.aadl | line 151: Couldn't resolve reference to 'CH2'.
30. /CaseProject/modified_model.aadl | line 151: left side of binary expression 'or' is of type '<error>' but must be of type 'bool'
31. /CaseProject/modified_model.aadl | line 151: named thing must be an expression with a type
32. /CaseProject/modified_model.aadl | line 151: right side of binary expression 'or' is of type '<error>' but must be of type 'bool'
33. /CaseProject/modified_model.aadl | line 157: Couldn't resolve reference to 'Active'.
34. /CaseProject/modified_model.aadl | line 157: Couldn't resolve reference to 'CH1'.
35. /CaseProject/modified_model.aadl | line 157: Couldn't resolve reference to 'CH2'.
36. /CaseProject/modified_model.aadl | line 157: left side of binary expression 'or' is of type '<error>' but must be of type 'bool'
37. /CaseProject/modified_model.aadl | line 157: named thing must be an expression with a type
38. /CaseProject/modified_model.aadl | line 157: right side of binary expression 'or' is of type '<error>' but must be of type 'bool'
39. /CaseProject/modified_model.aadl | line 163: Couldn't resolve reference to 'Active'.
40. /CaseProject/modified_model.aadl | line 163: Couldn't resolve reference to 'CH1'.
41. /CaseProject/modified_model.aadl | line 163: Couldn't resolve reference to 'CH2'.
42. /CaseProject/modified_model.aadl | line 163: named thing must be an expression with a type
43. /CaseProject/modified_model.aadl | line 163: right side of binary expression 'and' is of type '<error>' but must be of type 'bool'
44. /CaseProject/modified_model.aadl | line 169: Couldn't resolve reference to 'Active'.
45. /CaseProject/modified_model.aadl | line 169: Couldn't resolve reference to 'CH1'.
46. /CaseProject/modified_model.aadl | line 169: Couldn't resolve reference to 'CH2'.
47. /CaseProject/modified_model.aadl | line 169: named thing must be an expression with a type
48. /CaseProject/modified_model.aadl | line 169: right side of binary expression 'and' is of type '<error>' but must be of type 'bool'
49. /CaseProject/modified_model.aadl | line 187: Couldn't resolve reference to 'Agree_Nodes::Brake_Mode'.
50. /CaseProject/modified_model.aadl | line 202: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
51. /CaseProject/modified_model.aadl | line 202: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
52. /CaseProject/modified_model.aadl | line 319: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
53. /CaseProject/modified_model.aadl | line 319: Couldn't resolve reference to 'Mode'.
54. /CaseProject/modified_model.aadl | line 319: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
55. /CaseProject/modified_model.aadl | line 320: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
56. /CaseProject/modified_model.aadl | line 320: Couldn't resolve reference to 'Mode'.
57. /CaseProject/modified_model.aadl | line 320: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
58. /CaseProject/modified_model.aadl | line 321: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
59. /CaseProject/modified_model.aadl | line 321: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
60. /CaseProject/modified_model.aadl | line 322: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
61. /CaseProject/modified_model.aadl | line 322: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
62. /CaseProject/modified_model.aadl | line 324: Couldn't resolve reference to 'Mode'.
63. /CaseProject/modified_model.aadl | line 324: left and right sides of binary expression '!=' are of type 'int' and '<error>', but must be of the same type
64. /CaseProject/modified_model.aadl | line 324: named thing must be an expression with a type
65. /CaseProject/modified_model.aadl | line 325: Couldn't resolve reference to 'Mode'.
66. /CaseProject/modified_model.aadl | line 325: left and right sides of binary expression '!=' are of type 'int' and '<error>', but must be of the same type
67. /CaseProject/modified_model.aadl | line 325: named thing must be an expression with a type
