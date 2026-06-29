# Case97 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 1673.30
- Initial validation errors: 3
- Final validation errors: 143

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 142
- AGREE errors: 1
- Warnings: 8

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 62502
- completion_tokens: 16113
- total_tokens: 78615

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
17. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
18. [validation_repair] recovered_package_block - Recovered complete AADL package block.
19. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
20. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
21. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
22. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
23. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
24. [validation_repair] recovered_package_block - Recovered complete AADL package block.
25. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
26. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
27. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.

## Final Diagnostics

1. parsing Package_Specification, token 'public' or 'private' or 'end' is expected, found with
2. parsing AADL_Declaration, not allowed in aadl v2
3. parsing AADL_Declaration, not allowed in aadl v2
4. parsing AADL_Declaration, unexpected identifier 'acc2_output'
5. parsing AADL_Declaration, unexpected identifier 'acc3_output'
6. parsing AADL_Declaration, unexpected identifier 'acc4_output'
7. parsing AADL_Declaration, unexpected identifier 'acc5_output'
8. parsing AADL_Declaration, unexpected identifier 'acc6_output'
9. parsing AADL_Declaration, unexpected identifier 'acc1_event_in'
10. parsing AADL_Declaration, unexpected identifier 'acc2_event_in'
11. parsing AADL_Declaration, unexpected identifier 'acc3_event_in'
12. parsing AADL_Declaration, unexpected identifier 'acc4_event_in'
13. parsing AADL_Declaration, unexpected identifier 'acc5_event_in'
14. parsing AADL_Declaration, unexpected identifier 'acc6_event_in'
15. parsing AADL_Declaration, unexpected keyword 'end'
16. parsing AADL_Declaration, not allowed in aadl v2
17. parsing AADL_Declaration, unexpected identifier 'acc2'
18. parsing AADL_Declaration, unexpected identifier 'acc3'
19. parsing AADL_Declaration, unexpected identifier 'acc4'
20. parsing AADL_Declaration, unexpected identifier 'acc5'
21. parsing AADL_Declaration, unexpected identifier 'acc6'
22. parsing AADL_Declaration, unexpected keyword 'connections'
23. parsing AADL_Declaration, unexpected identifier 'C2'
24. parsing AADL_Declaration, unexpected identifier 'C3'
25. parsing AADL_Declaration, unexpected identifier 'C4'
26. parsing AADL_Declaration, unexpected identifier 'C5'
27. parsing AADL_Declaration, unexpected identifier 'C6'
28. parsing AADL_Declaration, unexpected identifier 'C7'
29. parsing AADL_Declaration, unexpected identifier 'C8'
30. parsing AADL_Declaration, unexpected identifier 'C9'
31. parsing AADL_Declaration, unexpected identifier 'C10'
32. parsing AADL_Declaration, unexpected identifier 'C11'
33. parsing AADL_Declaration, unexpected identifier 'C12'
34. parsing AADL_Declaration, unexpected keyword 'end'
35. parsing AADL_Declaration, not allowed in aadl v2
36. parsing AADL_Declaration, unexpected identifier 'acc2_input'
37. parsing AADL_Declaration, unexpected identifier 'acc3_input'
38. parsing AADL_Declaration, unexpected identifier 'acc4_input'
39. parsing AADL_Declaration, unexpected identifier 'acc5_input'
40. parsing AADL_Declaration, unexpected identifier 'acc6_input'
41. parsing AADL_Declaration, unexpected keyword 'end'
42. parsing AADL_Declaration, not allowed in aadl v2
43. parsing AADL_Declaration, unexpected identifier 'acc2'
44. parsing AADL_Declaration, unexpected identifier 'acc3'
45. parsing AADL_Declaration, unexpected identifier 'acc4'
46. parsing AADL_Declaration, unexpected identifier 'acc5'
47. parsing AADL_Declaration, unexpected identifier 'acc6'
48. parsing AADL_Declaration, unexpected keyword 'connections'
49. parsing AADL_Declaration, unexpected identifier 'C22'
50. parsing AADL_Declaration, unexpected identifier 'C23'
51. parsing AADL_Declaration, unexpected identifier 'C24'
52. parsing AADL_Declaration, unexpected identifier 'C25'
53. parsing AADL_Declaration, unexpected identifier 'C26'
54. parsing AADL_Declaration, unexpected keyword 'annex'
55. parsing AADL_Declaration, unexpected keyword 'end'
56. parsing AADL_Declaration, not allowed in aadl v2
57. parsing AADL_Declaration, unexpected keyword 'end'
58. parsing AADL_Declaration, not allowed in aadl v2
59. parsing AADL_Declaration, not allowed in aadl v2
60. parsing AADL_Declaration, unexpected identifier 'acc2_input'
61. parsing AADL_Declaration, unexpected identifier 'acc3_input'
62. parsing AADL_Declaration, unexpected identifier 'acc4_input'
63. parsing AADL_Declaration, unexpected identifier 'acc5_input'
64. parsing AADL_Declaration, unexpected identifier 'acc6_input'
65. parsing AADL_Declaration, unexpected identifier 'acc_error_out'
66. parsing AADL_Declaration, unexpected identifier 'acc_error_action'
67. parsing AADL_Declaration, unexpected identifier 'event2acc1'
68. parsing AADL_Declaration, unexpected identifier 'event2acc2'
69. parsing AADL_Declaration, unexpected identifier 'event2acc3'
70. parsing AADL_Declaration, unexpected identifier 'event2acc4'
71. parsing AADL_Declaration, unexpected identifier 'event2acc5'
72. parsing AADL_Declaration, unexpected identifier 'event2acc6'
73. parsing AADL_Declaration, unexpected keyword 'end'
74. parsing AADL_Declaration, not allowed in aadl v2
75. parsing AADL_Declaration, unexpected keyword 'connections'
76. parsing AADL_Declaration, unexpected identifier 'C2'
77. parsing AADL_Declaration, unexpected identifier 'C3'
78. parsing AADL_Declaration, unexpected identifier 'C4'
79. parsing AADL_Declaration, unexpected identifier 'C5'
80. parsing AADL_Declaration, unexpected identifier 'C6'
81. parsing AADL_Declaration, unexpected identifier 'C7'
82. parsing AADL_Declaration, unexpected identifier 'C8'
83. parsing AADL_Declaration, unexpected identifier 'C9'
84. parsing AADL_Declaration, unexpected identifier 'C10'
85. parsing AADL_Declaration, unexpected identifier 'C11'
86. parsing AADL_Declaration, unexpected identifier 'C12'
87. parsing AADL_Declaration, unexpected identifier 'C13'
88. parsing AADL_Declaration, unexpected identifier 'C14'
89. parsing AADL_Declaration, unexpected keyword 'annex'
90. parsing AADL_Declaration, unexpected keyword 'end'
91. parsing AADL_Declaration, not allowed in aadl v2
92. parsing AADL_Declaration, unexpected keyword 'end'
93. parsing AADL_Declaration, not allowed in aadl v2
94. parsing AADL_Declaration, not allowed in aadl v2
95. parsing AADL_Declaration, unexpected identifier 'acc2_input'
96. parsing AADL_Declaration, unexpected identifier 'acc3_input'
97. parsing AADL_Declaration, unexpected identifier 'acc4_input'
98. parsing AADL_Declaration, unexpected identifier 'acc5_input'
99. parsing AADL_Declaration, unexpected identifier 'acc6_input'
100. parsing AADL_Declaration, unexpected identifier 'ADIRUp_error_out'
101. parsing AADL_Declaration, unexpected identifier 'ADIRUp_error_action'
102. parsing AADL_Declaration, unexpected keyword 'end'
103. parsing AADL_Declaration, not allowed in aadl v2
104. parsing AADL_Declaration, unexpected identifier 'HM_th'
105. parsing AADL_Declaration, unexpected keyword 'connections'
106. parsing AADL_Declaration, unexpected identifier 'C2'
107. parsing AADL_Declaration, unexpected identifier 'C3'
108. parsing AADL_Declaration, unexpected identifier 'C4'
109. parsing AADL_Declaration, unexpected identifier 'C5'
110. parsing AADL_Declaration, unexpected identifier 'C6'
111. parsing AADL_Declaration, unexpected identifier 'C7'
112. parsing AADL_Declaration, unexpected identifier 'C8'
113. parsing AADL_Declaration, unexpected identifier 'C9'
114. parsing AADL_Declaration, unexpected identifier 'C10'
115. parsing AADL_Declaration, unexpected identifier 'C11'
116. parsing AADL_Declaration, unexpected identifier 'C12'
117. parsing AADL_Declaration, unexpected identifier 'C13'
118. parsing AADL_Declaration, unexpected identifier 'C14'
119. parsing AADL_Declaration, unexpected keyword 'annex'
120. parsing AADL_Declaration, unexpected keyword 'end'
121. parsing AADL_Declaration, not allowed in aadl v2
122. parsing AADL_Declaration, unexpected keyword 'end'
123. parsing AADL_Declaration, not allowed in aadl v2
124. parsing AADL_Declaration, not allowed in aadl v2
125. parsing AADL_Declaration, unexpected identifier 'arlarm_adirup_in'
126. parsing AADL_Declaration, unexpected identifier 'systemHM_action_acc_hm'
127. parsing AADL_Declaration, unexpected identifier 'systemHM_action_adirup'
128. parsing AADL_Declaration, unexpected keyword 'annex'
129. parsing AADL_Declaration, unexpected keyword 'end'
130. parsing AADL_Declaration, not allowed in aadl v2
131. parsing AADL_Declaration, unexpected identifier 'diagnosisEngine'
132. parsing AADL_Declaration, unexpected identifier 'mitigationActor'
133. parsing AADL_Declaration, unexpected keyword 'connections'
134. parsing AADL_Declaration, unexpected identifier 'C2'
135. parsing AADL_Declaration, unexpected identifier 'C31'
136. parsing AADL_Declaration, unexpected identifier 'C32'
137. parsing AADL_Declaration, unexpected identifier 'C4'
138. parsing AADL_Declaration, unexpected identifier 'C5'
139. parsing AADL_Declaration, unexpected keyword 'end'
140. parsing AADL_Declaration, unexpected keyword 'end'
141. parsing Package_Specification, Empty packages are not allowed
142. Cannot parse AADL specifications
143. /CaseProject/modified_model.aadl | line 3: no viable alternative at input 'with'
