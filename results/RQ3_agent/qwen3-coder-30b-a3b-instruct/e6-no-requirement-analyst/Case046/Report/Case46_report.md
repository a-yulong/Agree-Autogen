# Case46 Refactored Experiment Report

## Summary

- Setting: E6 (No Requirement Analyst)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 549.27
- Initial validation errors: 63
- Final validation errors: 41

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 6
- AGREE errors: 35
- Warnings: 0

## Modules

- rag: True
- repair: True
- requirement_analyst: False
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 71467
- completion_tokens: 10687
- total_tokens: 82154

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
24. [validation_repair] recovered_package_block - Recovered complete AADL package block.
25. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
26. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
27. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
28. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
29. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
30. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy (package specification)
2. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy (package specification)
3. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy (package specification)
4. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy (package specification)
5. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy (package specification)
6. Cannot analyze AADL specifications
7. /CaseProject/modified_model.aadl | line 30: Couldn't resolve reference to 'mode'.
8. /CaseProject/modified_model.aadl | line 30: left and right sides of binary expression '>=' are of type '<error>' and 'int', but must be of the same type
9. /CaseProject/modified_model.aadl | line 30: left side of binary expression '>=' is of type '<error>' but must be of type'int' or 'real'
10. /CaseProject/modified_model.aadl | line 30: named thing must be an expression with a type
11. /CaseProject/modified_model.aadl | line 49: Assume statements are allowed only in component types
12. /CaseProject/modified_model.aadl | line 51: Couldn't resolve reference to 'mode'.
13. /CaseProject/modified_model.aadl | line 51: Guarantee statements are allowed only in component types
14. /CaseProject/modified_model.aadl | line 51: left and right sides of binary expression '>=' are of type '<error>' and 'int', but must be of the same type
15. /CaseProject/modified_model.aadl | line 51: left side of binary expression '>=' is of type '<error>' but must be of type'int' or 'real'
16. /CaseProject/modified_model.aadl | line 51: named thing must be an expression with a type
17. /CaseProject/modified_model.aadl | line 53: Guarantee statements are allowed only in component types
18. /CaseProject/modified_model.aadl | line 55: Couldn't resolve reference to '"input_forward": A_sub.Input'.
19. /CaseProject/modified_model.aadl | line 55: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
20. /CaseProject/modified_model.aadl | line 55: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'int'
21. /CaseProject/modified_model.aadl | line 55: mismatched input '"input_forward"' expecting RULE_ID
22. /CaseProject/modified_model.aadl | line 57: Couldn't resolve reference to '"a_to_b_c": B_sub.Input'.
23. /CaseProject/modified_model.aadl | line 57: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
24. /CaseProject/modified_model.aadl | line 57: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'int'
25. /CaseProject/modified_model.aadl | line 57: mismatched input '"a_to_b_c"' expecting RULE_ID
26. /CaseProject/modified_model.aadl | line 59: Couldn't resolve reference to '"a_to_c": C_sub.Input_1'.
27. /CaseProject/modified_model.aadl | line 59: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
28. /CaseProject/modified_model.aadl | line 59: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'int'
29. /CaseProject/modified_model.aadl | line 59: mismatched input '"a_to_c"' expecting RULE_ID
30. /CaseProject/modified_model.aadl | line 61: Couldn't resolve reference to '"b_to_c": C_sub.Input_2'.
31. /CaseProject/modified_model.aadl | line 61: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
32. /CaseProject/modified_model.aadl | line 61: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'int'
33. /CaseProject/modified_model.aadl | line 61: mismatched input '"b_to_c"' expecting RULE_ID
34. /CaseProject/modified_model.aadl | line 63: Couldn't resolve reference to '"c_to_output": Output'.
35. /CaseProject/modified_model.aadl | line 63: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
36. /CaseProject/modified_model.aadl | line 63: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'int'
37. /CaseProject/modified_model.aadl | line 63: mismatched input '"c_to_output"' expecting RULE_ID
38. /CaseProject/modified_model.aadl | line 65: Couldn't resolve reference to '"mode_assignment": mode'.
39. /CaseProject/modified_model.aadl | line 65: Couldn't resolve reference to 'mode'.
40. /CaseProject/modified_model.aadl | line 65: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
41. /CaseProject/modified_model.aadl | line 65: mismatched input '"mode_assignment"' expecting RULE_ID
