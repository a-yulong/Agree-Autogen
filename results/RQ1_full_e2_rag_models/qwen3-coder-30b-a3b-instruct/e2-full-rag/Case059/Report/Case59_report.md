# Case59 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 316.48
- Initial validation errors: 36
- Final validation errors: 36

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 36
- Warnings: 2

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 41856
- completion_tokens: 6459
- total_tokens: 48315

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
11. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
12. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
13. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
14. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
15. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
16. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 26: Couldn't resolve reference to 'COM1'.
2. /CaseProject/modified_model.aadl | line 26: Couldn't resolve reference to 'Panel'.
3. /CaseProject/modified_model.aadl | line 26: left and right sides of binary expression '=' are of type 'BSCU::PanelMsg.PanelMsgImpl' and '<error>', but must be of the same type
4. /CaseProject/modified_model.aadl | line 26: named thing must be an expression with a type
5. /CaseProject/modified_model.aadl | line 27: Couldn't resolve reference to 'CMD'.
6. /CaseProject/modified_model.aadl | line 27: Couldn't resolve reference to 'CMD_From_COM'.
7. /CaseProject/modified_model.aadl | line 27: Couldn't resolve reference to 'COM1'.
8. /CaseProject/modified_model.aadl | line 27: Couldn't resolve reference to 'MON1'.
9. /CaseProject/modified_model.aadl | line 27: named thing must be an expression with a type
10. /CaseProject/modified_model.aadl | line 43: Couldn't resolve reference to 'Agree_Nodes::Brake_Mode'.
11. /CaseProject/modified_model.aadl | line 46: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
12. /CaseProject/modified_model.aadl | line 46: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
13. /CaseProject/modified_model.aadl | line 64: Couldn't resolve reference to 'Agree_Nodes::Brake_Mode'.
14. /CaseProject/modified_model.aadl | line 79: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
15. /CaseProject/modified_model.aadl | line 79: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
16. /CaseProject/modified_model.aadl | line 189: Couldn't resolve reference to 'Initializing'.
17. /CaseProject/modified_model.aadl | line 189: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
18. /CaseProject/modified_model.aadl | line 189: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'bool'
19. /CaseProject/modified_model.aadl | line 196: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
20. /CaseProject/modified_model.aadl | line 196: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
21. /CaseProject/modified_model.aadl | line 197: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
22. /CaseProject/modified_model.aadl | line 197: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
23. /CaseProject/modified_model.aadl | line 198: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
24. /CaseProject/modified_model.aadl | line 198: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
25. /CaseProject/modified_model.aadl | line 199: Couldn't resolve reference to 'Agree_Nodes::Brake_Cmd'.
26. /CaseProject/modified_model.aadl | line 199: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
27. /CaseProject/modified_model.aadl | line 207: Couldn't resolve reference to 'COM1Failed'.
28. /CaseProject/modified_model.aadl | line 207: Couldn't resolve reference to 'MON1Failed'.
29. /CaseProject/modified_model.aadl | line 207: left side of binary expression 'or' is of type '<error>' but must be of type 'bool'
30. /CaseProject/modified_model.aadl | line 207: named thing must be an expression with a type
31. /CaseProject/modified_model.aadl | line 207: right side of binary expression 'or' is of type '<error>' but must be of type 'bool'
32. /CaseProject/modified_model.aadl | line 208: Couldn't resolve reference to 'COM2Failed'.
33. /CaseProject/modified_model.aadl | line 208: Couldn't resolve reference to 'MON2Failed'.
34. /CaseProject/modified_model.aadl | line 208: left side of binary expression 'or' is of type '<error>' but must be of type 'bool'
35. /CaseProject/modified_model.aadl | line 208: named thing must be an expression with a type
36. /CaseProject/modified_model.aadl | line 208: right side of binary expression 'or' is of type '<error>' but must be of type 'bool'
