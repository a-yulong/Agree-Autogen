# Case07 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 395.88
- Initial validation errors: 8
- Final validation errors: 11

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 11
- Warnings: 5

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 30066
- completion_tokens: 4606
- total_tokens: 34672

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
13. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
14. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
15. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
16. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
17. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
18. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 101: Couldn't resolve reference to 'x'.
2. /CaseProject/modified_model.aadl | line 101: Equation assigns 2 variables, but right side returns 1 values
3. /CaseProject/modified_model.aadl | line 101: extraneous input ')' expecting ':'
4. /CaseProject/modified_model.aadl | line 101: left and right sides of binary expression '<' are of type '<error>' and 'bool', but must be of the same type
5. /CaseProject/modified_model.aadl | line 101: left side of binary expression '<' is of type '<error>' but must be of type'int' or 'real'
6. /CaseProject/modified_model.aadl | line 101: mismatched input '(' expecting ':'
7. /CaseProject/modified_model.aadl | line 101: named thing must be an expression with a type
8. /CaseProject/modified_model.aadl | line 101: right side of binary expression '<' is of type 'bool' but must be of type'int' or 'real'
9. /CaseProject/modified_model.aadl | line 103: left and right sides of binary expression '=' are of type 'bool' and '<error>', but must be of the same type
10. /CaseProject/modified_model.aadl | line 104: left and right sides of binary expression '=' are of type 'bool' and '<error>', but must be of the same type
11. /CaseProject/modified_model.aadl | line 105: left and right sides of binary expression '=' are of type 'bool' and '<error>', but must be of the same type
