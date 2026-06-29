# Case131 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 261.34
- Initial validation errors: 19
- Final validation errors: 20

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 5
- AGREE errors: 15
- Warnings: 4

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 14607
- completion_tokens: 3179
- total_tokens: 17786

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 5 classified requirement item(s).
4. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
5. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
6. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
7. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
8. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
9. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
10. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
11. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
12. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. Byte_Count (property association) does not point to anything
2. Byte_Count (property association) does not point to anything
3. Byte_Count (property association) does not point to anything
4. Byte_Count (property association) does not point to anything
5. Cannot analyze AADL specifications
6. /CaseProject/modified_model.aadl | line 23: Couldn't resolve reference to 'Period'.
7. /CaseProject/modified_model.aadl | line 23: extraneous input 'ms' expecting ';'
8. /CaseProject/modified_model.aadl | line 23: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
9. /CaseProject/modified_model.aadl | line 23: named thing must be an expression with a type
10. /CaseProject/modified_model.aadl | line 24: Couldn't resolve reference to 'Compute_Execution_time'.
11. /CaseProject/modified_model.aadl | line 24: left and right sides of binary expression '>=' are of type '<error>' and 'int', but must be of the same type
12. /CaseProject/modified_model.aadl | line 24: left side of binary expression '>=' is of type '<error>' but must be of type'int' or 'real'
13. /CaseProject/modified_model.aadl | line 24: mismatched input 'ms' expecting ';'
14. /CaseProject/modified_model.aadl | line 24: named thing must be an expression with a type
15. /CaseProject/modified_model.aadl | line 25: Couldn't resolve reference to 'Dispatch_Protocol'.
16. /CaseProject/modified_model.aadl | line 25: named thing must be an expression with a type
17. /CaseProject/modified_model.aadl | line 25: no viable alternative at input '"Periodic"'
18. /CaseProject/modified_model.aadl | line 26: Couldn't resolve reference to 'Priority'.
19. /CaseProject/modified_model.aadl | line 26: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
20. /CaseProject/modified_model.aadl | line 26: named thing must be an expression with a type
