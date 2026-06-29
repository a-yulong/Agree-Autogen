# Case45 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 290.02
- Initial validation errors: 11
- Final validation errors: 17

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 6
- AGREE errors: 11
- Warnings: 0

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 25682
- completion_tokens: 3314
- total_tokens: 28996

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 3 classified requirement item(s).
4. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
5. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
6. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
7. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
8. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
9. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
10. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
11. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
12. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
13. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
14. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
15. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
16. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
17. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
18. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
19. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
20. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
21. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
22. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
23. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
24. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
25. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
26. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
27. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
28. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy (package specification)
2. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy (package specification)
3. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy (package specification)
4. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy (package specification)
5. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy (package specification)
6. Cannot analyze AADL specifications
7. /CaseProject/modified_model.aadl | line 25: The 'then' and 'else' expressions are of non-matching types 'IntTypeDef' and 'ErrorTypeDef'
8. /CaseProject/modified_model.aadl | line 25: The first and second arguments of the 'prev' function are of non-matching types 'IntTypeDef' and 'ErrorTypeDef'
9. /CaseProject/modified_model.aadl | line 25: extraneous input ')' expecting ';'
10. /CaseProject/modified_model.aadl | line 25: left and right sides of binary expression '+' are of type '<error>' and 'int', but must be of the same type
11. /CaseProject/modified_model.aadl | line 25: left and right sides of binary expression '=' are of type 'real' and 'int', but must be of the same type
12. /CaseProject/modified_model.aadl | line 25: left side of binary expression '+' is of type '<error>' but must be of type'int' or 'real'
13. /CaseProject/modified_model.aadl | line 25: mismatched input ')' expecting ','
14. /CaseProject/modified_model.aadl | line 29: The first and second arguments of the 'prev' function are of non-matching types 'IntTypeDef' and 'ErrorTypeDef'
15. /CaseProject/modified_model.aadl | line 29: left and right sides of binary expression '>' are of type 'int' and '<error>', but must be of the same type
16. /CaseProject/modified_model.aadl | line 29: mismatched input ')' expecting ','
17. /CaseProject/modified_model.aadl | line 29: right side of binary expression '>' is of type '<error>' but must be of type'int' or 'real'
