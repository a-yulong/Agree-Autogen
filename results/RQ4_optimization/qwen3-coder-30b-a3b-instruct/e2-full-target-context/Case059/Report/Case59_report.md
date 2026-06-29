# Case59 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 531.99
- Initial validation errors: 36
- Final validation errors: 31

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 31
- Warnings: 2

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 144389
- completion_tokens: 15306
- total_tokens: 159695

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 6 classified requirement item(s).
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
22. [validation_repair] recovered_package_block - Recovered complete AADL package block.
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

1. /CaseProject/modified_model.aadl | line 29: Couldn't resolve reference to 'Fail'.
2. /CaseProject/modified_model.aadl | line 29: left side of binary expression '=>' is of type '<error>' but must be of type 'bool'
3. /CaseProject/modified_model.aadl | line 29: named thing must be an expression with a type
4. /CaseProject/modified_model.aadl | line 29: right side of unary expression 'not' is of type 'ErrorTypeDef' but must be of type 'bool'
5. /CaseProject/modified_model.aadl | line 41: Couldn't resolve reference to 'Agree_Nodes::Brake_Mode'.
6. /CaseProject/modified_model.aadl | line 44: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
7. /CaseProject/modified_model.aadl | line 44: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
8. /CaseProject/modified_model.aadl | line 62: Couldn't resolve reference to 'Agree_Nodes::Brake_Mode'.
9. /CaseProject/modified_model.aadl | line 77: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
10. /CaseProject/modified_model.aadl | line 77: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
11. /CaseProject/modified_model.aadl | line 187: Couldn't resolve reference to 'Initializing'.
12. /CaseProject/modified_model.aadl | line 187: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
13. /CaseProject/modified_model.aadl | line 187: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
14. /CaseProject/modified_model.aadl | line 194: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
15. /CaseProject/modified_model.aadl | line 194: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
16. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
17. /CaseProject/modified_model.aadl | line 195: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
18. /CaseProject/modified_model.aadl | line 196: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
19. /CaseProject/modified_model.aadl | line 196: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
20. /CaseProject/modified_model.aadl | line 197: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
21. /CaseProject/modified_model.aadl | line 197: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
22. /CaseProject/modified_model.aadl | line 205: Couldn't resolve reference to 'COM1Failed'.
23. /CaseProject/modified_model.aadl | line 205: Couldn't resolve reference to 'MON1Failed'.
24. /CaseProject/modified_model.aadl | line 205: left side of binary expression 'or' is of type '<error>' but must be of type 'bool'
25. /CaseProject/modified_model.aadl | line 205: named thing must be an expression with a type
26. /CaseProject/modified_model.aadl | line 205: right side of binary expression 'or' is of type '<error>' but must be of type 'bool'
27. /CaseProject/modified_model.aadl | line 206: Couldn't resolve reference to 'COM2Failed'.
28. /CaseProject/modified_model.aadl | line 206: Couldn't resolve reference to 'MON2Failed'.
29. /CaseProject/modified_model.aadl | line 206: left side of binary expression 'or' is of type '<error>' but must be of type 'bool'
30. /CaseProject/modified_model.aadl | line 206: named thing must be an expression with a type
31. /CaseProject/modified_model.aadl | line 206: right side of binary expression 'or' is of type '<error>' but must be of type 'bool'
