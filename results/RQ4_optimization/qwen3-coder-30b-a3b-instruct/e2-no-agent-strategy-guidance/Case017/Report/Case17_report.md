# Case17 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 344.23
- Initial validation errors: 12
- Final validation errors: 12

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 12
- Warnings: 1

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 37388
- completion_tokens: 5994
- total_tokens: 43382

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 5 classified requirement item(s).
4. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
5. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
6. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
7. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
8. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
9. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
10. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
11. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
12. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
13. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
14. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
15. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
16. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
17. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
18. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
19. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
20. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
21. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
22. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
23. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
24. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
25. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
26. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
27. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 100: mismatched input ':' expecting ';'
2. /CaseProject/modified_model.aadl | line 112: Couldn't resolve reference to 'numberServicesTrue'.
3. /CaseProject/modified_model.aadl | line 112: left and right sides of binary expression '=' are of type '<error>' and 'int', but must be of the same type
4. /CaseProject/modified_model.aadl | line 112: named thing must be an expression with a type
5. /CaseProject/modified_model.aadl | line 125: Couldn't resolve reference to 'numberServicesTrue'.
6. /CaseProject/modified_model.aadl | line 125: left and right sides of binary expression '<' are of type '<error>' and 'int', but must be of the same type
7. /CaseProject/modified_model.aadl | line 125: left side of binary expression '<' is of type '<error>' but must be of type'int' or 'real'
8. /CaseProject/modified_model.aadl | line 125: named thing must be an expression with a type
9. /CaseProject/modified_model.aadl | line 127: Equation assigns 0 variables, but right side returns 1 values
10. /CaseProject/modified_model.aadl | line 127: mismatched input '"numberServicesTrue_init"' expecting RULE_ID
11. /CaseProject/modified_model.aadl | line 130: Equation assigns 0 variables, but right side returns 1 values
12. /CaseProject/modified_model.aadl | line 130: mismatched input '"numberServicesTrue_update"' expecting RULE_ID
