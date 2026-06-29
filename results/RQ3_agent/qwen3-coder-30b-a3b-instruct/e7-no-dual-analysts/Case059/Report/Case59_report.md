# Case59 Refactored Experiment Report

## Summary

- Setting: E7 (No Dual Analysts)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 543.15
- Initial validation errors: 36
- Final validation errors: 83

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 83
- Warnings: 2

## Modules

- rag: True
- repair: True
- requirement_analyst: False
- model_analyst: False
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 127824
- completion_tokens: 10867
- total_tokens: 138691

## Output Recovery

1. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
2. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
3. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
4. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
5. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
6. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
7. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
8. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
9. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
10. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
11. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
12. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
13. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
14. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
15. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
16. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
17. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
18. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
19. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
20. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
21. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
22. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
23. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
24. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
25. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
26. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
27. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
28. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
29. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 28: Couldn't resolve reference to 'COM1'.
2. /CaseProject/modified_model.aadl | line 29: Couldn't resolve reference to 'COM2'.
3. /CaseProject/modified_model.aadl | line 30: Couldn't resolve reference to 'MON1'.
4. /CaseProject/modified_model.aadl | line 31: Couldn't resolve reference to 'MON2'.
5. /CaseProject/modified_model.aadl | line 33: Assignment statements are allowed only in component implementations
6. /CaseProject/modified_model.aadl | line 33: Couldn't resolve reference to 'Initializing'.
7. /CaseProject/modified_model.aadl | line 35: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
8. /CaseProject/modified_model.aadl | line 35: Couldn't resolve reference to 'CMD'.
9. /CaseProject/modified_model.aadl | line 35: Couldn't resolve reference to 'COM1'.
10. /CaseProject/modified_model.aadl | line 35: Couldn't resolve reference to 'Mode'.
11. /CaseProject/modified_model.aadl | line 35: Lemma statements are allowed only in component implementations and nodes
12. /CaseProject/modified_model.aadl | line 35: named thing must be an expression with a type
13. /CaseProject/modified_model.aadl | line 36: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
14. /CaseProject/modified_model.aadl | line 36: Couldn't resolve reference to 'CMD'.
15. /CaseProject/modified_model.aadl | line 36: Couldn't resolve reference to 'COM2'.
16. /CaseProject/modified_model.aadl | line 36: Couldn't resolve reference to 'Mode'.
17. /CaseProject/modified_model.aadl | line 36: Lemma statements are allowed only in component implementations and nodes
18. /CaseProject/modified_model.aadl | line 36: named thing must be an expression with a type
19. /CaseProject/modified_model.aadl | line 37: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
20. /CaseProject/modified_model.aadl | line 37: Couldn't resolve reference to 'Cmd'.
21. /CaseProject/modified_model.aadl | line 37: Couldn't resolve reference to 'MON1'.
22. /CaseProject/modified_model.aadl | line 37: Couldn't resolve reference to 'Mode'.
23. /CaseProject/modified_model.aadl | line 37: Couldn't resolve reference to 'Status'.
24. /CaseProject/modified_model.aadl | line 37: Lemma statements are allowed only in component implementations and nodes
25. /CaseProject/modified_model.aadl | line 37: named thing must be an expression with a type
26. /CaseProject/modified_model.aadl | line 38: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
27. /CaseProject/modified_model.aadl | line 38: Couldn't resolve reference to 'Cmd'.
28. /CaseProject/modified_model.aadl | line 38: Couldn't resolve reference to 'MON2'.
29. /CaseProject/modified_model.aadl | line 38: Couldn't resolve reference to 'Mode'.
30. /CaseProject/modified_model.aadl | line 38: Couldn't resolve reference to 'Status'.
31. /CaseProject/modified_model.aadl | line 38: Lemma statements are allowed only in component implementations and nodes
32. /CaseProject/modified_model.aadl | line 38: named thing must be an expression with a type
33. /CaseProject/modified_model.aadl | line 40: Couldn't resolve reference to 'COM1'.
34. /CaseProject/modified_model.aadl | line 40: Couldn't resolve reference to 'MON1'.
35. /CaseProject/modified_model.aadl | line 40: Couldn't resolve reference to 'Mode'.
36. /CaseProject/modified_model.aadl | line 40: Lemma statements are allowed only in component implementations and nodes
37. /CaseProject/modified_model.aadl | line 40: named thing must be an expression with a type
38. /CaseProject/modified_model.aadl | line 41: Couldn't resolve reference to 'COM2'.
39. /CaseProject/modified_model.aadl | line 41: Couldn't resolve reference to 'MON2'.
40. /CaseProject/modified_model.aadl | line 41: Couldn't resolve reference to 'Mode'.
41. /CaseProject/modified_model.aadl | line 41: Lemma statements are allowed only in component implementations and nodes
42. /CaseProject/modified_model.aadl | line 41: named thing must be an expression with a type
43. /CaseProject/modified_model.aadl | line 42: Couldn't resolve reference to 'COM1'.
44. /CaseProject/modified_model.aadl | line 42: Lemma statements are allowed only in component implementations and nodes
45. /CaseProject/modified_model.aadl | line 43: Couldn't resolve reference to 'MON1'.
46. /CaseProject/modified_model.aadl | line 43: Lemma statements are allowed only in component implementations and nodes
47. /CaseProject/modified_model.aadl | line 44: Couldn't resolve reference to 'COM2'.
48. /CaseProject/modified_model.aadl | line 44: Lemma statements are allowed only in component implementations and nodes
49. /CaseProject/modified_model.aadl | line 45: Couldn't resolve reference to 'MON2'.
50. /CaseProject/modified_model.aadl | line 45: Lemma statements are allowed only in component implementations and nodes
51. /CaseProject/modified_model.aadl | line 46: Lemma statements are allowed only in component implementations and nodes
52. /CaseProject/modified_model.aadl | line 47: Lemma statements are allowed only in component implementations and nodes
53. /CaseProject/modified_model.aadl | line 59: Couldn't resolve reference to 'Agree_Nodes::Brake_Mode'.
54. /CaseProject/modified_model.aadl | line 62: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
55. /CaseProject/modified_model.aadl | line 62: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
56. /CaseProject/modified_model.aadl | line 80: Couldn't resolve reference to 'Agree_Nodes::Brake_Mode'.
57. /CaseProject/modified_model.aadl | line 95: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
58. /CaseProject/modified_model.aadl | line 95: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
59. /CaseProject/modified_model.aadl | line 200: COM1_Running already defined in component type contract
60. /CaseProject/modified_model.aadl | line 201: COM2_Running already defined in component type contract
61. /CaseProject/modified_model.aadl | line 202: MON1_Running already defined in component type contract
62. /CaseProject/modified_model.aadl | line 203: MON2_Running already defined in component type contract
63. /CaseProject/modified_model.aadl | line 205: Couldn't resolve reference to 'Initializing'.
64. /CaseProject/modified_model.aadl | line 205: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
65. /CaseProject/modified_model.aadl | line 205: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
66. /CaseProject/modified_model.aadl | line 212: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
67. /CaseProject/modified_model.aadl | line 212: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
68. /CaseProject/modified_model.aadl | line 213: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
69. /CaseProject/modified_model.aadl | line 213: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
70. /CaseProject/modified_model.aadl | line 214: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
71. /CaseProject/modified_model.aadl | line 214: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
72. /CaseProject/modified_model.aadl | line 215: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
73. /CaseProject/modified_model.aadl | line 215: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
74. /CaseProject/modified_model.aadl | line 223: Couldn't resolve reference to 'COM1Failed'.
75. /CaseProject/modified_model.aadl | line 223: Couldn't resolve reference to 'MON1Failed'.
76. /CaseProject/modified_model.aadl | line 223: left side of binary expression 'or' is of type '<error>' but must be of type 'bool'
77. /CaseProject/modified_model.aadl | line 223: named thing must be an expression with a type
78. /CaseProject/modified_model.aadl | line 223: right side of binary expression 'or' is of type '<error>' but must be of type 'bool'
79. /CaseProject/modified_model.aadl | line 224: Couldn't resolve reference to 'COM2Failed'.
80. /CaseProject/modified_model.aadl | line 224: Couldn't resolve reference to 'MON2Failed'.
81. /CaseProject/modified_model.aadl | line 224: left side of binary expression 'or' is of type '<error>' but must be of type 'bool'
82. /CaseProject/modified_model.aadl | line 224: named thing must be an expression with a type
83. /CaseProject/modified_model.aadl | line 224: right side of binary expression 'or' is of type '<error>' but must be of type 'bool'
