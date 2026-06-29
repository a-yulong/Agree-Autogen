# Case59 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 320.89
- Initial validation errors: 29
- Final validation errors: 29

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 29
- Warnings: 2

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 62868
- completion_tokens: 5624
- total_tokens: 68492

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 6 classified requirement item(s).
4. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
5. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
6. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
7. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
8. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
9. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
10. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
11. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
12. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
13. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
14. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
15. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
16. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
17. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
18. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
19. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
20. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
21. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
22. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
23. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
24. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
25. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 26: left and right sides of binary expression '=' are of type 'int' and 'bool', but must be of the same type
2. /CaseProject/modified_model.aadl | line 30: left and right sides of binary expression '=' are of type 'int' and 'bool', but must be of the same type
3. /CaseProject/modified_model.aadl | line 45: Couldn't resolve reference to 'Agree_Nodes::Brake_Mode'.
4. /CaseProject/modified_model.aadl | line 48: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
5. /CaseProject/modified_model.aadl | line 48: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
6. /CaseProject/modified_model.aadl | line 66: Couldn't resolve reference to 'Agree_Nodes::Brake_Mode'.
7. /CaseProject/modified_model.aadl | line 81: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
8. /CaseProject/modified_model.aadl | line 81: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
9. /CaseProject/modified_model.aadl | line 191: Couldn't resolve reference to 'Initializing'.
10. /CaseProject/modified_model.aadl | line 191: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
11. /CaseProject/modified_model.aadl | line 191: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
12. /CaseProject/modified_model.aadl | line 198: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
13. /CaseProject/modified_model.aadl | line 198: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
14. /CaseProject/modified_model.aadl | line 199: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
15. /CaseProject/modified_model.aadl | line 199: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
16. /CaseProject/modified_model.aadl | line 200: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
17. /CaseProject/modified_model.aadl | line 200: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
18. /CaseProject/modified_model.aadl | line 201: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
19. /CaseProject/modified_model.aadl | line 201: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
20. /CaseProject/modified_model.aadl | line 209: Couldn't resolve reference to 'COM1Failed'.
21. /CaseProject/modified_model.aadl | line 209: Couldn't resolve reference to 'MON1Failed'.
22. /CaseProject/modified_model.aadl | line 209: left side of binary expression 'or' is of type '<error>' but must be of type 'bool'
23. /CaseProject/modified_model.aadl | line 209: named thing must be an expression with a type
24. /CaseProject/modified_model.aadl | line 209: right side of binary expression 'or' is of type '<error>' but must be of type 'bool'
25. /CaseProject/modified_model.aadl | line 210: Couldn't resolve reference to 'COM2Failed'.
26. /CaseProject/modified_model.aadl | line 210: Couldn't resolve reference to 'MON2Failed'.
27. /CaseProject/modified_model.aadl | line 210: left side of binary expression 'or' is of type '<error>' but must be of type 'bool'
28. /CaseProject/modified_model.aadl | line 210: named thing must be an expression with a type
29. /CaseProject/modified_model.aadl | line 210: right side of binary expression 'or' is of type '<error>' but must be of type 'bool'
