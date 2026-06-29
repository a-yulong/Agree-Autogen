# Case409 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 383.65
- Initial validation errors: 46
- Final validation errors: 97

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 51
- AGREE errors: 46
- Warnings: 12

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 99807
- completion_tokens: 5565
- total_tokens: 105372

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 1 classified requirement item(s).
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
21. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
22. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
23. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
24. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
25. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
26. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
27. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
28. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
29. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
30. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
31. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
32. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. Source_Stack_Size (property association) does not point to anything
2. ARINC653  HM_Errors (property association) does not point to anything
3. (property term) does not point to anything or to something unreachable
4. (property term) does not point to anything or to something unreachable
5. (property term) does not point to anything or to something unreachable
6. (property term) does not point to anything or to something unreachable
7. ARINC653  HM_Process_Recovery_actions (property association) does not point to anything
8. (property term) does not point to anything or to something unreachable
9. (property term) does not point to anything or to something unreachable
10. (property term) does not point to anything or to something unreachable
11. (property term) does not point to anything or to something unreachable
12. Source_Stack_Size (property association) does not point to anything
13. ARINC653  HM_Errors (property association) does not point to anything
14. (property term) does not point to anything or to something unreachable
15. (property term) does not point to anything or to something unreachable
16. (property term) does not point to anything or to something unreachable
17. (property term) does not point to anything or to something unreachable
18. ARINC653  HM_Process_Recovery_Actions (property association) does not point to anything
19. (property term) does not point to anything or to something unreachable
20. (property term) does not point to anything or to something unreachable
21. (property term) does not point to anything or to something unreachable
22. (property term) does not point to anything or to something unreachable
23. Source_Stack_Size (property association) does not point to anything
24. ARINC653  HM_Errors (property association) does not point to anything
25. (property term) does not point to anything or to something unreachable
26. (property term) does not point to anything or to something unreachable
27. (property term) does not point to anything or to something unreachable
28. (property term) does not point to anything or to something unreachable
29. ARINC653  HM_Process_Recovery_Actions (property association) does not point to anything
30. (property term) does not point to anything or to something unreachable
31. (property term) does not point to anything or to something unreachable
32. (property term) does not point to anything or to something unreachable
33. (property term) does not point to anything or to something unreachable
34. Source_Stack_Size (property association) does not point to anything
35. ARINC653  HM_Errors (property association) does not point to anything
36. (property term) does not point to anything or to something unreachable
37. (property term) does not point to anything or to something unreachable
38. (property term) does not point to anything or to something unreachable
39. (property term) does not point to anything or to something unreachable
40. ARINC653  HM_Process_Recovery_Actions (property association) does not point to anything
41. (property term) does not point to anything or to something unreachable
42. (property term) does not point to anything or to something unreachable
43. (property term) does not point to anything or to something unreachable
44. (property term) does not point to anything or to something unreachable
45. ARINC653  Partition_Slots (property association) does not point to anything
46. ARINC653  Slots_Allocation (property association) does not point to anything
47. ARINC653  HM_Errors (property association) does not point to anything
48. (property term) does not point to anything or to something unreachable
49. ARINC653  HM_Module_Recovery_Actions (property association) does not point to anything
50. (property term) does not point to anything or to something unreachable
51. Cannot analyze AADL specifications
52. /CaseProject/modified_model.aadl | line 111: Couldn't resolve reference to property definition 'ARINC653::HM_Errors'.
53. /CaseProject/modified_model.aadl | line 112: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Application_Error'. For classifier references use classifier( <ref> ).
54. /CaseProject/modified_model.aadl | line 112: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Deadline_Miss'. For classifier references use classifier( <ref> ).
55. /CaseProject/modified_model.aadl | line 112: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Illegal_Request'. For classifier references use classifier( <ref> ).
56. /CaseProject/modified_model.aadl | line 112: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Numeric_Error'. For classifier references use classifier( <ref> ).
57. /CaseProject/modified_model.aadl | line 113: Couldn't resolve reference to property definition 'ARINC653::HM_Process_Recovery_actions'.
58. /CaseProject/modified_model.aadl | line 114: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Ignore'. For classifier references use classifier( <ref> ).
59. /CaseProject/modified_model.aadl | line 114: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Process_Restart'. For classifier references use classifier( <ref> ).
60. /CaseProject/modified_model.aadl | line 133: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Application_Error'. For classifier references use classifier( <ref> ).
61. /CaseProject/modified_model.aadl | line 133: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Deadline_Miss'. For classifier references use classifier( <ref> ).
62. /CaseProject/modified_model.aadl | line 133: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Illegal_Request'. For classifier references use classifier( <ref> ).
63. /CaseProject/modified_model.aadl | line 133: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Numeric_Error'. For classifier references use classifier( <ref> ).
64. /CaseProject/modified_model.aadl | line 133: Couldn't resolve reference to property definition 'ARINC653::HM_Errors'.
65. /CaseProject/modified_model.aadl | line 134: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Process_Restart'. For classifier references use classifier( <ref> ).
66. /CaseProject/modified_model.aadl | line 134: Couldn't resolve reference to property definition 'ARINC653::HM_Process_Recovery_Actions'.
67. /CaseProject/modified_model.aadl | line 156: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Application_Error'. For classifier references use classifier( <ref> ).
68. /CaseProject/modified_model.aadl | line 156: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Deadline_Miss'. For classifier references use classifier( <ref> ).
69. /CaseProject/modified_model.aadl | line 156: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Illegal_Request'. For classifier references use classifier( <ref> ).
70. /CaseProject/modified_model.aadl | line 156: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Numeric_Error'. For classifier references use classifier( <ref> ).
71. /CaseProject/modified_model.aadl | line 156: Couldn't resolve reference to property definition 'ARINC653::HM_Errors'.
72. /CaseProject/modified_model.aadl | line 157: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Process_Restart'. For classifier references use classifier( <ref> ).
73. /CaseProject/modified_model.aadl | line 157: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Process_Stop'. For classifier references use classifier( <ref> ).
74. /CaseProject/modified_model.aadl | line 157: Couldn't resolve reference to property definition 'ARINC653::HM_Process_Recovery_Actions'.
75. /CaseProject/modified_model.aadl | line 159: left and right sides of binary expression '<=' are of type '<error>' and 'int', but must be of the same type
76. /CaseProject/modified_model.aadl | line 159: left and right sides of binary expression '<=' are of type 'int' and '<error>', but must be of the same type
77. /CaseProject/modified_model.aadl | line 159: left side of binary expression '<=' is of type '<error>' but must be of type'int' or 'real'
78. /CaseProject/modified_model.aadl | line 159: named thing must be an expression with a type
79. /CaseProject/modified_model.aadl | line 159: right side of binary expression '<=' is of type '<error>' but must be of type'int' or 'real'
80. /CaseProject/modified_model.aadl | line 177: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Application_Error'. For classifier references use classifier( <ref> ).
81. /CaseProject/modified_model.aadl | line 177: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Deadline_Miss'. For classifier references use classifier( <ref> ).
82. /CaseProject/modified_model.aadl | line 177: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Illegal_Request'. For classifier references use classifier( <ref> ).
83. /CaseProject/modified_model.aadl | line 177: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Numeric_Error'. For classifier references use classifier( <ref> ).
84. /CaseProject/modified_model.aadl | line 177: Couldn't resolve reference to property definition 'ARINC653::HM_Errors'.
85. /CaseProject/modified_model.aadl | line 178: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Process_Restart'. For classifier references use classifier( <ref> ).
86. /CaseProject/modified_model.aadl | line 178: Couldn't resolve reference to property definition 'ARINC653::HM_Process_Recovery_Actions'.
87. /CaseProject/modified_model.aadl | line 257: Couldn't resolve reference to UnitLiteral 'ms'.
88. /CaseProject/modified_model.aadl | line 257: Couldn't resolve reference to property definition 'ARINC653::Partition_Slots'.
89. /CaseProject/modified_model.aadl | line 258: Couldn't resolve reference to property definition 'ARINC653::Slots_Allocation'.
90. /CaseProject/modified_model.aadl | line 259: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Power_Fail'. For classifier references use classifier( <ref> ).
91. /CaseProject/modified_model.aadl | line 259: Couldn't resolve reference to property definition 'ARINC653::HM_Errors'.
92. /CaseProject/modified_model.aadl | line 260: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Reset'. For classifier references use classifier( <ref> ).
93. /CaseProject/modified_model.aadl | line 260: Couldn't resolve reference to property definition 'ARINC653::HM_Module_Recovery_Actions'.
94. /CaseProject/modified_model.aadl | line 267: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Code_Memory'. For classifier references use classifier( <ref> ).
95. /CaseProject/modified_model.aadl | line 267: Couldn't resolve reference to property definition 'ARINC653::Memory_Type'.
96. /CaseProject/modified_model.aadl | line 273: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Code_Memory'. For classifier references use classifier( <ref> ).
97. /CaseProject/modified_model.aadl | line 273: Couldn't resolve reference to property definition 'ARINC653::Memory_Type'.
