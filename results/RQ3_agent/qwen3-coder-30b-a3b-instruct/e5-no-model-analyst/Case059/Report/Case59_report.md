# Case59 Refactored Experiment Report

## Summary

- Setting: E5 (No Model Analyst)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 409.95
- Initial validation errors: 12
- Final validation errors: 18

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 18
- Warnings: 0

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: False
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 81184
- completion_tokens: 11780
- total_tokens: 92964

## Output Recovery

1. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] requirement_items_normalized - Normalized 6 classified requirement item(s).
3. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
4. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
5. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
6. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
7. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
8. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
9. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
10. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
11. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
12. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
13. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
14. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
15. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
16. [validation_repair] recovered_package_block - Recovered complete AADL package block.
17. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
18. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
19. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
20. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
21. [validation_repair] recovered_package_block - Recovered complete AADL package block.
22. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
23. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
24. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
25. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
26. [validation_repair] recovered_package_block - Recovered complete AADL package block.
27. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
28. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
29. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
30. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
31. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
32. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 29: Couldn't resolve reference to 'CMD'.
2. /CaseProject/modified_model.aadl | line 29: Couldn't resolve reference to 'Fail'.
3. /CaseProject/modified_model.aadl | line 29: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
4. /CaseProject/modified_model.aadl | line 29: left side of binary expression '=>' is of type '<error>' but must be of type 'bool'
5. /CaseProject/modified_model.aadl | line 29: named thing must be an expression with a type
6. /CaseProject/modified_model.aadl | line 29: right side of unary expression 'not' is of type 'ErrorTypeDef' but must be of type 'bool'
7. /CaseProject/modified_model.aadl | line 41: Couldn't resolve reference to 'Agree_Nodes::Brake_Mode'.
8. /CaseProject/modified_model.aadl | line 44: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
9. /CaseProject/modified_model.aadl | line 44: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
10. /CaseProject/modified_model.aadl | line 62: Couldn't resolve reference to 'Agree_Nodes::Brake_Mode'.
11. /CaseProject/modified_model.aadl | line 77: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
12. /CaseProject/modified_model.aadl | line 77: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
13. /CaseProject/modified_model.aadl | line 179: Couldn't resolve reference to 'COM1.Panel'.
14. /CaseProject/modified_model.aadl | line 179: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
15. /CaseProject/modified_model.aadl | line 179: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'BSCU::PanelMsg.PanelMsgImpl'
16. /CaseProject/modified_model.aadl | line 180: Couldn't resolve reference to 'MON1.CMD_From_COM'.
17. /CaseProject/modified_model.aadl | line 180: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
18. /CaseProject/modified_model.aadl | line 180: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'int'
