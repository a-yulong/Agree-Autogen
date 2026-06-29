# Case77 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 592.76
- Initial validation errors: 8
- Final validation errors: 132

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 132
- Warnings: 0

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 147385
- completion_tokens: 18644
- total_tokens: 166029

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
22. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
23. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
24. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
25. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
26. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
27. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
28. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
29. [validation_repair] recovered_package_block - Recovered complete AADL package block.
30. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
31. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
32. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
33. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
34. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
35. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
36. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 325: Couldn't resolve reference to '"D1_handle_position routing": D1_handle_position'.
2. /CaseProject/modified_model.aadl | line 325: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
3. /CaseProject/modified_model.aadl | line 325: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
4. /CaseProject/modified_model.aadl | line 325: mismatched input '"D1_handle_position routing"' expecting RULE_ID
5. /CaseProject/modified_model.aadl | line 326: Couldn't resolve reference to '"D1_closed routing": D1_closed'.
6. /CaseProject/modified_model.aadl | line 326: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
7. /CaseProject/modified_model.aadl | line 326: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
8. /CaseProject/modified_model.aadl | line 326: mismatched input '"D1_closed routing"' expecting RULE_ID
9. /CaseProject/modified_model.aadl | line 327: Couldn't resolve reference to '"D1_latched routing": D1_latched'.
10. /CaseProject/modified_model.aadl | line 327: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
11. /CaseProject/modified_model.aadl | line 327: mismatched input '"D1_latched routing"' expecting RULE_ID
12. /CaseProject/modified_model.aadl | line 327: no viable alternative at input 'latched'
13. /CaseProject/modified_model.aadl | line 328: Couldn't resolve reference to '"D1_locked routing": D1_locked'.
14. /CaseProject/modified_model.aadl | line 328: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
15. /CaseProject/modified_model.aadl | line 328: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
16. /CaseProject/modified_model.aadl | line 328: mismatched input '"D1_locked routing"' expecting RULE_ID
17. /CaseProject/modified_model.aadl | line 329: Couldn't resolve reference to '"D1_swivel routing": D1_swivel'.
18. /CaseProject/modified_model.aadl | line 329: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
19. /CaseProject/modified_model.aadl | line 329: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
20. /CaseProject/modified_model.aadl | line 329: mismatched input '"D1_swivel routing"' expecting RULE_ID
21. /CaseProject/modified_model.aadl | line 330: Couldn't resolve reference to '"D1_de_arrest routing": D1_de_arrest'.
22. /CaseProject/modified_model.aadl | line 330: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
23. /CaseProject/modified_model.aadl | line 330: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
24. /CaseProject/modified_model.aadl | line 330: mismatched input '"D1_de_arrest routing"' expecting RULE_ID
25. /CaseProject/modified_model.aadl | line 331: Couldn't resolve reference to '"D1_lock routing": D1_lock'.
26. /CaseProject/modified_model.aadl | line 331: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
27. /CaseProject/modified_model.aadl | line 331: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
28. /CaseProject/modified_model.aadl | line 331: mismatched input '"D1_lock routing"' expecting RULE_ID
29. /CaseProject/modified_model.aadl | line 332: Couldn't resolve reference to '"D1_warn_diff_pres routing": D1_warn_diff_pres'.
30. /CaseProject/modified_model.aadl | line 332: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
31. /CaseProject/modified_model.aadl | line 332: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
32. /CaseProject/modified_model.aadl | line 332: mismatched input '"D1_warn_diff_pres routing"' expecting RULE_ID
33. /CaseProject/modified_model.aadl | line 333: Couldn't resolve reference to '"D1_warn_slide routing": D1_warn_slide'.
34. /CaseProject/modified_model.aadl | line 333: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
35. /CaseProject/modified_model.aadl | line 333: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
36. /CaseProject/modified_model.aadl | line 333: mismatched input '"D1_warn_slide routing"' expecting RULE_ID
37. /CaseProject/modified_model.aadl | line 334: Couldn't resolve reference to '"D1_in_flight routing": D1_in_flight'.
38. /CaseProject/modified_model.aadl | line 334: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
39. /CaseProject/modified_model.aadl | line 334: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
40. /CaseProject/modified_model.aadl | line 334: mismatched input '"D1_in_flight routing"' expecting RULE_ID
41. /CaseProject/modified_model.aadl | line 335: Couldn't resolve reference to '"D1_on_ground routing": D1_on_ground'.
42. /CaseProject/modified_model.aadl | line 335: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
43. /CaseProject/modified_model.aadl | line 335: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
44. /CaseProject/modified_model.aadl | line 335: mismatched input '"D1_on_ground routing"' expecting RULE_ID
45. /CaseProject/modified_model.aadl | line 336: Couldn't resolve reference to '"D1_engine_running routing": D1_engine_running'.
46. /CaseProject/modified_model.aadl | line 336: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
47. /CaseProject/modified_model.aadl | line 336: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
48. /CaseProject/modified_model.aadl | line 336: mismatched input '"D1_engine_running routing"' expecting RULE_ID
49. /CaseProject/modified_model.aadl | line 337: Couldn't resolve reference to '"D1_emergency_evacuation routing": D1_emergency_evacuation'.
50. /CaseProject/modified_model.aadl | line 337: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
51. /CaseProject/modified_model.aadl | line 337: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
52. /CaseProject/modified_model.aadl | line 337: mismatched input '"D1_emergency_evacuation routing"' expecting RULE_ID
53. /CaseProject/modified_model.aadl | line 338: Couldn't resolve reference to '"D1_dps routing": D1_dps'.
54. /CaseProject/modified_model.aadl | line 338: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
55. /CaseProject/modified_model.aadl | line 338: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'int'
56. /CaseProject/modified_model.aadl | line 338: mismatched input '"D1_dps routing"' expecting RULE_ID
57. /CaseProject/modified_model.aadl | line 339: Couldn't resolve reference to '"D1_warning_info routing": D1_warning_info'.
58. /CaseProject/modified_model.aadl | line 339: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
59. /CaseProject/modified_model.aadl | line 339: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
60. /CaseProject/modified_model.aadl | line 339: mismatched input '"D1_warning_info routing"' expecting RULE_ID
61. /CaseProject/modified_model.aadl | line 340: Couldn't resolve reference to '"D1_ecam_info routing": D1_ecam_info'.
62. /CaseProject/modified_model.aadl | line 340: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
63. /CaseProject/modified_model.aadl | line 340: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
64. /CaseProject/modified_model.aadl | line 340: mismatched input '"D1_ecam_info routing"' expecting RULE_ID
65. /CaseProject/modified_model.aadl | line 341: Couldn't resolve reference to '"D2_handle_position routing": D2_handle_position'.
66. /CaseProject/modified_model.aadl | line 341: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
67. /CaseProject/modified_model.aadl | line 341: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
68. /CaseProject/modified_model.aadl | line 341: mismatched input '"D2_handle_position routing"' expecting RULE_ID
69. /CaseProject/modified_model.aadl | line 342: Couldn't resolve reference to '"D2_closed routing": D2_closed'.
70. /CaseProject/modified_model.aadl | line 342: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
71. /CaseProject/modified_model.aadl | line 342: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
72. /CaseProject/modified_model.aadl | line 342: mismatched input '"D2_closed routing"' expecting RULE_ID
73. /CaseProject/modified_model.aadl | line 343: Couldn't resolve reference to '"D2_latched routing": D2_latched'.
74. /CaseProject/modified_model.aadl | line 343: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
75. /CaseProject/modified_model.aadl | line 343: mismatched input '"D2_latched routing"' expecting RULE_ID
76. /CaseProject/modified_model.aadl | line 343: no viable alternative at input 'latched'
77. /CaseProject/modified_model.aadl | line 344: Couldn't resolve reference to '"D2_locked routing": D2_locked'.
78. /CaseProject/modified_model.aadl | line 344: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
79. /CaseProject/modified_model.aadl | line 344: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
80. /CaseProject/modified_model.aadl | line 344: mismatched input '"D2_locked routing"' expecting RULE_ID
81. /CaseProject/modified_model.aadl | line 345: Couldn't resolve reference to '"D2_swivel routing": D2_swivel'.
82. /CaseProject/modified_model.aadl | line 345: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
83. /CaseProject/modified_model.aadl | line 345: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
84. /CaseProject/modified_model.aadl | line 345: mismatched input '"D2_swivel routing"' expecting RULE_ID
85. /CaseProject/modified_model.aadl | line 346: Couldn't resolve reference to '"D2_de_arrest routing": D2_de_arrest'.
86. /CaseProject/modified_model.aadl | line 346: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
87. /CaseProject/modified_model.aadl | line 346: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
88. /CaseProject/modified_model.aadl | line 346: mismatched input '"D2_de_arrest routing"' expecting RULE_ID
89. /CaseProject/modified_model.aadl | line 347: Couldn't resolve reference to '"D2_lock routing": D2_lock'.
90. /CaseProject/modified_model.aadl | line 347: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
91. /CaseProject/modified_model.aadl | line 347: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
92. /CaseProject/modified_model.aadl | line 347: mismatched input '"D2_lock routing"' expecting RULE_ID
93. /CaseProject/modified_model.aadl | line 348: Couldn't resolve reference to '"D2_warn_diff_pres routing": D2_warn_diff_pres'.
94. /CaseProject/modified_model.aadl | line 348: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
95. /CaseProject/modified_model.aadl | line 348: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
96. /CaseProject/modified_model.aadl | line 348: mismatched input '"D2_warn_diff_pres routing"' expecting RULE_ID
97. /CaseProject/modified_model.aadl | line 349: Couldn't resolve reference to '"D2_warn_slide routing": D2_warn_slide'.
98. /CaseProject/modified_model.aadl | line 349: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
99. /CaseProject/modified_model.aadl | line 349: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
100. /CaseProject/modified_model.aadl | line 349: mismatched input '"D2_warn_slide routing"' expecting RULE_ID
101. /CaseProject/modified_model.aadl | line 350: Couldn't resolve reference to '"D2_in_flight routing": D2_in_flight'.
102. /CaseProject/modified_model.aadl | line 350: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
103. /CaseProject/modified_model.aadl | line 350: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
104. /CaseProject/modified_model.aadl | line 350: mismatched input '"D2_in_flight routing"' expecting RULE_ID
105. /CaseProject/modified_model.aadl | line 351: Couldn't resolve reference to '"D2_on_ground routing": D2_on_ground'.
106. /CaseProject/modified_model.aadl | line 351: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
107. /CaseProject/modified_model.aadl | line 351: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
108. /CaseProject/modified_model.aadl | line 351: mismatched input '"D2_on_ground routing"' expecting RULE_ID
109. /CaseProject/modified_model.aadl | line 352: Couldn't resolve reference to '"D2_engine_running routing": D2_engine_running'.
110. /CaseProject/modified_model.aadl | line 352: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
111. /CaseProject/modified_model.aadl | line 352: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
112. /CaseProject/modified_model.aadl | line 352: mismatched input '"D2_engine_running routing"' expecting RULE_ID
113. /CaseProject/modified_model.aadl | line 353: Couldn't resolve reference to '"D2_emergency_evacuation routing": D2_emergency_evacuation'.
114. /CaseProject/modified_model.aadl | line 353: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
115. /CaseProject/modified_model.aadl | line 353: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
116. /CaseProject/modified_model.aadl | line 353: mismatched input '"D2_emergency_evacuation routing"' expecting RULE_ID
117. /CaseProject/modified_model.aadl | line 354: Couldn't resolve reference to '"D2_dps routing": D2_dps'.
118. /CaseProject/modified_model.aadl | line 354: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
119. /CaseProject/modified_model.aadl | line 354: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'int'
120. /CaseProject/modified_model.aadl | line 354: mismatched input '"D2_dps routing"' expecting RULE_ID
121. /CaseProject/modified_model.aadl | line 355: Couldn't resolve reference to '"D2_warning_info routing": D2_warning_info'.
122. /CaseProject/modified_model.aadl | line 355: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
123. /CaseProject/modified_model.aadl | line 355: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
124. /CaseProject/modified_model.aadl | line 355: mismatched input '"D2_warning_info routing"' expecting RULE_ID
125. /CaseProject/modified_model.aadl | line 356: Couldn't resolve reference to '"D2_ecam_info routing": D2_ecam_info'.
126. /CaseProject/modified_model.aadl | line 356: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
127. /CaseProject/modified_model.aadl | line 356: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
128. /CaseProject/modified_model.aadl | line 356: mismatched input '"D2_ecam_info routing"' expecting RULE_ID
129. /CaseProject/modified_model.aadl | line 357: Couldn't resolve reference to '"Mix_cll routing": Mix_cll'.
130. /CaseProject/modified_model.aadl | line 357: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
131. /CaseProject/modified_model.aadl | line 357: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
132. /CaseProject/modified_model.aadl | line 357: mismatched input '"Mix_cll routing"' expecting RULE_ID
