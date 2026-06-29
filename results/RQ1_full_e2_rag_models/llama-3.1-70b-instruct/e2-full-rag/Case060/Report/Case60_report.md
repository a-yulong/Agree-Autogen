# Case60 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 619.40
- Initial validation errors: 19
- Final validation errors: 63

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 63
- Warnings: 2

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 102394
- completion_tokens: 10680
- total_tokens: 113074

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 3 classified requirement item(s).
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
27. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
28. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
29. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
30. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
31. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
32. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
33. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
34. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 105: Couldn't resolve reference to 'CMD_From_COM'.
2. /CaseProject/modified_model.aadl | line 105: Couldn't resolve reference to 'Cmd'.
3. /CaseProject/modified_model.aadl | line 105: Couldn't resolve reference to 'Status'.
4. /CaseProject/modified_model.aadl | line 105: named thing must be an expression with a type
5. /CaseProject/modified_model.aadl | line 106: The variable 'Active' on the left side of equation is of type 'bool' but must be of type '<error>'
6. /CaseProject/modified_model.aadl | line 108: Couldn't resolve reference to 'Active'.
7. /CaseProject/modified_model.aadl | line 108: Couldn't resolve reference to 'Sync_From'.
8. /CaseProject/modified_model.aadl | line 108: left and right sides of binary expression '->' are of type '<error>' and 'bool', but must be of the same type
9. /CaseProject/modified_model.aadl | line 108: named thing must be an expression with a type
10. /CaseProject/modified_model.aadl | line 108: right side of unary expression 'not' is of type 'ErrorTypeDef' but must be of type 'bool'
11. /CaseProject/modified_model.aadl | line 112: Couldn't resolve reference to 'Active'.
12. /CaseProject/modified_model.aadl | line 112: Couldn't resolve reference to 'Error'.
13. /CaseProject/modified_model.aadl | line 112: Couldn't resolve reference to 'Sync_From'.
14. /CaseProject/modified_model.aadl | line 112: named thing must be an expression with a type
15. /CaseProject/modified_model.aadl | line 112: right side of binary expression 'and' is of type '<error>' but must be of type 'bool'
16. /CaseProject/modified_model.aadl | line 112: right side of unary expression 'not' is of type 'ErrorTypeDef' but must be of type 'bool'
17. /CaseProject/modified_model.aadl | line 114: Couldn't resolve reference to 'Active'.
18. /CaseProject/modified_model.aadl | line 114: Couldn't resolve reference to 'Error'.
19. /CaseProject/modified_model.aadl | line 114: Couldn't resolve reference to 'Sync_From'.
20. /CaseProject/modified_model.aadl | line 114: left side of binary expression 'or' is of type '<error>' but must be of type 'bool'
21. /CaseProject/modified_model.aadl | line 114: named thing must be an expression with a type
22. /CaseProject/modified_model.aadl | line 114: right side of binary expression 'or' is of type '<error>' but must be of type 'bool'
23. /CaseProject/modified_model.aadl | line 114: right side of unary expression 'not' is of type 'ErrorTypeDef' but must be of type 'bool'
24. /CaseProject/modified_model.aadl | line 119: Couldn't resolve reference to 'Cmd'.
25. /CaseProject/modified_model.aadl | line 119: Couldn't resolve reference to 'Status'.
26. /CaseProject/modified_model.aadl | line 119: mismatched input ')' expecting ';'
27. /CaseProject/modified_model.aadl | line 119: named thing must be an expression with a type
28. /CaseProject/modified_model.aadl | line 119: no viable alternative at input 'int'
29. /CaseProject/modified_model.aadl | line 121: Couldn't resolve reference to 'Error'.
30. /CaseProject/modified_model.aadl | line 121: Couldn't resolve reference to 'Status'.
31. /CaseProject/modified_model.aadl | line 121: left and right sides of binary expression '=' are of type '<error>' and 'bool', but must be of the same type
32. /CaseProject/modified_model.aadl | line 121: named thing must be an expression with a type
33. /CaseProject/modified_model.aadl | line 122: Couldn't resolve reference to 'Error'.
34. /CaseProject/modified_model.aadl | line 122: Couldn't resolve reference to 'Sync_To'.
35. /CaseProject/modified_model.aadl | line 122: left and right sides of binary expression '=' are of type '<error>' and 'bool', but must be of the same type
36. /CaseProject/modified_model.aadl | line 122: named thing must be an expression with a type
37. /CaseProject/modified_model.aadl | line 124: Couldn't resolve reference to 'Active'.
38. /CaseProject/modified_model.aadl | line 124: Couldn't resolve reference to 'Status'.
39. /CaseProject/modified_model.aadl | line 124: left and right sides of binary expression '=' are of type '<error>' and 'bool', but must be of the same type
40. /CaseProject/modified_model.aadl | line 124: named thing must be an expression with a type
41. /CaseProject/modified_model.aadl | line 125: Couldn't resolve reference to 'Active'.
42. /CaseProject/modified_model.aadl | line 125: Couldn't resolve reference to 'Sync_To'.
43. /CaseProject/modified_model.aadl | line 125: left and right sides of binary expression '=' are of type '<error>' and 'bool', but must be of the same type
44. /CaseProject/modified_model.aadl | line 125: named thing must be an expression with a type
45. /CaseProject/modified_model.aadl | line 143: Couldn't resolve reference to 'Agree_Nodes::Brake_Mode'.
46. /CaseProject/modified_model.aadl | line 158: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
47. /CaseProject/modified_model.aadl | line 158: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
48. /CaseProject/modified_model.aadl | line 275: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
49. /CaseProject/modified_model.aadl | line 275: Couldn't resolve reference to 'Mode'.
50. /CaseProject/modified_model.aadl | line 275: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
51. /CaseProject/modified_model.aadl | line 276: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
52. /CaseProject/modified_model.aadl | line 276: Couldn't resolve reference to 'Mode'.
53. /CaseProject/modified_model.aadl | line 276: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
54. /CaseProject/modified_model.aadl | line 277: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
55. /CaseProject/modified_model.aadl | line 277: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
56. /CaseProject/modified_model.aadl | line 278: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
57. /CaseProject/modified_model.aadl | line 278: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
58. /CaseProject/modified_model.aadl | line 280: Couldn't resolve reference to 'Mode'.
59. /CaseProject/modified_model.aadl | line 280: left and right sides of binary expression '!=' are of type 'int' and '<error>', but must be of the same type
60. /CaseProject/modified_model.aadl | line 280: named thing must be an expression with a type
61. /CaseProject/modified_model.aadl | line 281: Couldn't resolve reference to 'Mode'.
62. /CaseProject/modified_model.aadl | line 281: left and right sides of binary expression '!=' are of type 'int' and '<error>', but must be of the same type
63. /CaseProject/modified_model.aadl | line 281: named thing must be an expression with a type
