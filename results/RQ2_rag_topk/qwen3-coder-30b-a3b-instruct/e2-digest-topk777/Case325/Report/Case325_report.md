# Case325 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 139.24
- Initial validation errors: 0
- Final validation errors: 81

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 81
- AGREE errors: 0
- Warnings: 2

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 10814
- completion_tokens: 2973
- total_tokens: 13787

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 1 classified requirement item(s).
4. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
5. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
6. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
7. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.

## Final Diagnostics

1. parsing Package_Specification, token 'public' or 'private' or 'end' is expected, found with
2. parsing AADL_Declaration, not allowed in aadl v2
3. parsing AADL_Declaration, not allowed in aadl v2
4. parsing AADL_Declaration, not allowed in aadl v2
5. parsing AADL_Declaration, unexpected identifier 'clear'
6. parsing AADL_Declaration, unexpected identifier 'seconds_to_cook'
7. parsing AADL_Declaration, unexpected identifier 'door_closed'
8. parsing AADL_Declaration, unexpected identifier 'cooking_mode'
9. parsing AADL_Declaration, unexpected keyword 'end'
10. parsing AADL_Declaration, not allowed in aadl v2
11. parsing AADL_Declaration, unexpected keyword 'end'
12. parsing AADL_Declaration, not allowed in aadl v2
13. parsing AADL_Declaration, unexpected identifier 'kp_0'
14. parsing AADL_Declaration, unexpected identifier 'kp_1'
15. parsing AADL_Declaration, unexpected identifier 'kp_2'
16. parsing AADL_Declaration, unexpected identifier 'kp_3'
17. parsing AADL_Declaration, unexpected identifier 'kp_4'
18. parsing AADL_Declaration, unexpected identifier 'kp_5'
19. parsing AADL_Declaration, unexpected identifier 'kp_6'
20. parsing AADL_Declaration, unexpected identifier 'kp_7'
21. parsing AADL_Declaration, unexpected identifier 'kp_8'
22. parsing AADL_Declaration, unexpected identifier 'kp_9'
23. parsing AADL_Declaration, unexpected identifier 'cooking_mode'
24. parsing AADL_Declaration, unexpected identifier 'left_digit'
25. parsing AADL_Declaration, unexpected identifier 'middle_digit'
26. parsing AADL_Declaration, unexpected identifier 'right_digit'
27. parsing AADL_Declaration, unexpected identifier 'seconds_to_cook'
28. parsing AADL_Declaration, unexpected keyword 'end'
29. parsing AADL_Declaration, not allowed in aadl v2
30. parsing AADL_Declaration, unexpected keyword 'end'
31. parsing AADL_Declaration, not allowed in aadl v2
32. parsing AADL_Declaration, unexpected identifier 'heating_element_on'
33. parsing AADL_Declaration, unexpected keyword 'annex'
34. parsing AADL_Declaration, unexpected keyword 'end'
35. parsing AADL_Declaration, not allowed in aadl v2
36. parsing AADL_Declaration, unexpected keyword 'end'
37. parsing AADL_Declaration, not allowed in aadl v2
38. parsing AADL_Declaration, unexpected identifier 'start'
39. parsing AADL_Declaration, unexpected identifier 'kp_0'
40. parsing AADL_Declaration, unexpected identifier 'kp_1'
41. parsing AADL_Declaration, unexpected identifier 'kp_2'
42. parsing AADL_Declaration, unexpected identifier 'kp_3'
43. parsing AADL_Declaration, unexpected identifier 'kp_4'
44. parsing AADL_Declaration, unexpected identifier 'kp_5'
45. parsing AADL_Declaration, unexpected identifier 'kp_6'
46. parsing AADL_Declaration, unexpected identifier 'kp_7'
47. parsing AADL_Declaration, unexpected identifier 'kp_8'
48. parsing AADL_Declaration, unexpected identifier 'kp_9'
49. parsing AADL_Declaration, unexpected identifier 'door_closed'
50. parsing AADL_Declaration, unexpected identifier 'heating_element_on'
51. parsing AADL_Declaration, unexpected identifier 'left_digit'
52. parsing AADL_Declaration, unexpected identifier 'middle_digit'
53. parsing AADL_Declaration, unexpected identifier 'right_digit'
54. parsing AADL_Declaration, unexpected keyword 'end'
55. parsing AADL_Declaration, not allowed in aadl v2
56. parsing AADL_Declaration, unexpected identifier 'DC'
57. parsing AADL_Declaration, unexpected identifier 'OP'
58. parsing AADL_Declaration, unexpected keyword 'connections'
59. parsing AADL_Declaration, unexpected identifier 'clear_TO_DC_clear'
60. parsing AADL_Declaration, unexpected identifier 'start_TO_MC_start'
61. parsing AADL_Declaration, unexpected identifier 'kp_0_TO_DC_kp_0'
62. parsing AADL_Declaration, unexpected identifier 'kp_1_TO_DC_kp_1'
63. parsing AADL_Declaration, unexpected identifier 'kp_2_TO_DC_kp_2'
64. parsing AADL_Declaration, unexpected identifier 'kp_3_TO_DC_kp_3'
65. parsing AADL_Declaration, unexpected identifier 'kp_4_TO_DC_kp_4'
66. parsing AADL_Declaration, unexpected identifier 'kp_5_TO_DC_kp_5'
67. parsing AADL_Declaration, unexpected identifier 'kp_6_TO_DC_kp_6'
68. parsing AADL_Declaration, unexpected identifier 'kp_7_TO_DC_kp_7'
69. parsing AADL_Declaration, unexpected identifier 'kp_8_TO_DC_kp_8'
70. parsing AADL_Declaration, unexpected identifier 'kp_9_TO_DC_kp_9'
71. parsing AADL_Declaration, unexpected identifier 'door_closed_TO_MC_door_closed'
72. parsing AADL_Declaration, unexpected identifier 'DC_steps_to_cook_TO_MC_steps_to_cook'
73. parsing AADL_Declaration, unexpected identifier 'MC_cooking_mode_TO_OP_cooking_mode'
74. parsing AADL_Declaration, unexpected identifier 'MC_enable_TO_DC_enable'
75. parsing AADL_Declaration, unexpected identifier 'OP_heating_element_on_TO_heating_element_on'
76. parsing AADL_Declaration, unexpected identifier 'DC_left_digit_TO_left_digit'
77. parsing AADL_Declaration, unexpected identifier 'DC_middle_digit_TO_middle_digit'
78. parsing AADL_Declaration, unexpected identifier 'DC_right_digit_TO_right_digit'
79. parsing AADL_Declaration, unexpected keyword 'end'
80. parsing AADL_Declaration, unexpected keyword 'end'
81. Cannot parse AADL specifications
