# Case54 Refactored Experiment Report

## Summary

- Setting: E7 (No Dual Analysts)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 325.93
- Initial validation errors: 8
- Final validation errors: 25

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 9
- AGREE errors: 16
- Warnings: 0

## Modules

- rag: True
- repair: True
- requirement_analyst: False
- model_analyst: False
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 37082
- completion_tokens: 3628
- total_tokens: 40710

## Output Recovery

1. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
2. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
3. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
4. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
5. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
6. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
7. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
8. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
9. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
10. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
11. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
12. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
13. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
14. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
15. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
16. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
17. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
18. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
19. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
20. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
21. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
22. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
23. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
24. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
25. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
26. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
27. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
28. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
29. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
30. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy_Extended (package specification)
2. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy_Extended (package specification)
3. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy_Extended (package specification)
4. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy_Extended (package specification)
5. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy_Extended (package specification)
6. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy_Extended (package specification)
7. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy_Extended (package specification)
8. Communication_Properties (identifier) qualified reference name not found in 'with' statements of Integer_Toy_Extended (package specification)
9. Cannot analyze AADL specifications
10. /CaseProject/modified_model.aadl | line 23: Couldn't resolve reference to 'Input'.
11. /CaseProject/modified_model.aadl | line 23: left and right sides of binary expression '<' are of type '<error>' and 'int', but must be of the same type
12. /CaseProject/modified_model.aadl | line 23: left side of binary expression '<' is of type '<error>' but must be of type'int' or 'real'
13. /CaseProject/modified_model.aadl | line 23: named thing must be an expression with a type
14. /CaseProject/modified_model.aadl | line 24: Couldn't resolve reference to 'Input'.
15. /CaseProject/modified_model.aadl | line 24: left and right sides of binary expression '<' are of type '<error>' and 'int', but must be of the same type
16. /CaseProject/modified_model.aadl | line 24: left side of binary expression '<' is of type '<error>' but must be of type'int' or 'real'
17. /CaseProject/modified_model.aadl | line 24: named thing must be an expression with a type
18. /CaseProject/modified_model.aadl | line 34: Couldn't resolve reference to 'Input1'.
19. /CaseProject/modified_model.aadl | line 34: left and right sides of binary expression '<' are of type '<error>' and 'int', but must be of the same type
20. /CaseProject/modified_model.aadl | line 34: left side of binary expression '<' is of type '<error>' but must be of type'int' or 'real'
21. /CaseProject/modified_model.aadl | line 34: named thing must be an expression with a type
22. /CaseProject/modified_model.aadl | line 35: Couldn't resolve reference to 'Input2'.
23. /CaseProject/modified_model.aadl | line 35: left and right sides of binary expression '<' are of type '<error>' and 'int', but must be of the same type
24. /CaseProject/modified_model.aadl | line 35: left side of binary expression '<' is of type '<error>' but must be of type'int' or 'real'
25. /CaseProject/modified_model.aadl | line 35: named thing must be an expression with a type
