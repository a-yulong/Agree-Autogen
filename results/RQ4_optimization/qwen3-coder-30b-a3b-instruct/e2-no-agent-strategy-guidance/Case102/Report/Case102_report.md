# Case102 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 385.35
- Initial validation errors: 36
- Final validation errors: 38

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 2
- AGREE errors: 36
- Warnings: 12

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 44984
- completion_tokens: 8712
- total_tokens: 53696

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

1. parsing Package_Specification, Empty packages are not allowed
2. Cannot parse AADL specifications
3. /CaseProject/modified_model.aadl | line 183: Couldn't resolve reference to 'acc1_input'.
4. /CaseProject/modified_model.aadl | line 183: Couldn't resolve reference to 'acc1_output'.
5. /CaseProject/modified_model.aadl | line 183: Couldn't resolve reference to 'acc_hm_pr'.
6. /CaseProject/modified_model.aadl | line 183: Couldn't resolve reference to 'acc_pr'.
7. /CaseProject/modified_model.aadl | line 183: Guarantee statements are allowed only in component types
8. /CaseProject/modified_model.aadl | line 183: left side of binary expression '=>' is of type '<error>' but must be of type 'bool'
9. /CaseProject/modified_model.aadl | line 183: named thing must be an expression with a type
10. /CaseProject/modified_model.aadl | line 183: right side of binary expression '=>' is of type '<error>' but must be of type 'bool'
11. /CaseProject/modified_model.aadl | line 186: Couldn't resolve reference to 'acc2_input'.
12. /CaseProject/modified_model.aadl | line 186: Couldn't resolve reference to 'acc2_output'.
13. /CaseProject/modified_model.aadl | line 186: Couldn't resolve reference to 'acc_hm_pr'.
14. /CaseProject/modified_model.aadl | line 186: Couldn't resolve reference to 'acc_pr'.
15. /CaseProject/modified_model.aadl | line 186: Guarantee statements are allowed only in component types
16. /CaseProject/modified_model.aadl | line 186: left side of binary expression '=>' is of type '<error>' but must be of type 'bool'
17. /CaseProject/modified_model.aadl | line 186: named thing must be an expression with a type
18. /CaseProject/modified_model.aadl | line 186: right side of binary expression '=>' is of type '<error>' but must be of type 'bool'
19. /CaseProject/modified_model.aadl | line 189: Couldn't resolve reference to 'acc_pr'.
20. /CaseProject/modified_model.aadl | line 189: Couldn't resolve reference to 'main_cpu'.
21. /CaseProject/modified_model.aadl | line 189: Couldn't resolve reference to 'part1'.
22. /CaseProject/modified_model.aadl | line 189: Guarantee statements are allowed only in component types
23. /CaseProject/modified_model.aadl | line 189: named thing must be an expression with a type
24. /CaseProject/modified_model.aadl | line 192: Couldn't resolve reference to 'acc_hm_pr'.
25. /CaseProject/modified_model.aadl | line 192: Couldn't resolve reference to 'main_cpu'.
26. /CaseProject/modified_model.aadl | line 192: Couldn't resolve reference to 'part2'.
27. /CaseProject/modified_model.aadl | line 192: Guarantee statements are allowed only in component types
28. /CaseProject/modified_model.aadl | line 192: named thing must be an expression with a type
29. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to 'ADIRUp_pr'.
30. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to 'main_cpu'.
31. /CaseProject/modified_model.aadl | line 195: Couldn't resolve reference to 'part3'.
32. /CaseProject/modified_model.aadl | line 195: Guarantee statements are allowed only in component types
33. /CaseProject/modified_model.aadl | line 195: named thing must be an expression with a type
34. /CaseProject/modified_model.aadl | line 198: Couldn't resolve reference to 'SHM_pr'.
35. /CaseProject/modified_model.aadl | line 198: Couldn't resolve reference to 'main_cpu'.
36. /CaseProject/modified_model.aadl | line 198: Couldn't resolve reference to 'part4'.
37. /CaseProject/modified_model.aadl | line 198: Guarantee statements are allowed only in component types
38. /CaseProject/modified_model.aadl | line 198: named thing must be an expression with a type
