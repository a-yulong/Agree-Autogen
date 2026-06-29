# Case24 Refactored Experiment Report

## Summary

- Setting: E7 (No Dual Analysts)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 454.31
- Initial validation errors: 14
- Final validation errors: 46

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 46
- Warnings: 1

## Modules

- rag: True
- repair: True
- requirement_analyst: False
- model_analyst: False
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 62773
- completion_tokens: 9727
- total_tokens: 72500

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
13. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
14. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
15. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
16. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
17. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
18. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
19. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
20. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
21. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
22. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
23. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
24. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
25. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
26. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
27. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
28. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
29. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
30. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
31. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
32. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
33. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 57: Couldn't resolve reference to 'tempin1'.
2. /CaseProject/modified_model.aadl | line 57: Couldn't resolve reference to 'tempin2'.
3. /CaseProject/modified_model.aadl | line 57: Couldn't resolve reference to 'tempout'.
4. /CaseProject/modified_model.aadl | line 57: named thing must be an expression with a type
5. /CaseProject/modified_model.aadl | line 60: Couldn't resolve reference to 'tempin1'.
6. /CaseProject/modified_model.aadl | line 60: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
7. /CaseProject/modified_model.aadl | line 60: named thing must be an expression with a type
8. /CaseProject/modified_model.aadl | line 63: Couldn't resolve reference to 'tempin2'.
9. /CaseProject/modified_model.aadl | line 63: left and right sides of binary expression '=' are of type 'int' and '<error>', but must be of the same type
10. /CaseProject/modified_model.aadl | line 63: named thing must be an expression with a type
11. /CaseProject/modified_model.aadl | line 66: Couldn't resolve reference to 'tempin1'.
12. /CaseProject/modified_model.aadl | line 66: Couldn't resolve reference to 'tempin2'.
13. /CaseProject/modified_model.aadl | line 66: Couldn't resolve reference to 'tempout'.
14. /CaseProject/modified_model.aadl | line 66: named thing must be an expression with a type
15. /CaseProject/modified_model.aadl | line 92: Couldn't resolve reference to 'tempin1'.
16. /CaseProject/modified_model.aadl | line 92: Couldn't resolve reference to 'tempin2'.
17. /CaseProject/modified_model.aadl | line 92: Couldn't resolve reference to 'tempout'.
18. /CaseProject/modified_model.aadl | line 92: named thing must be an expression with a type
19. /CaseProject/modified_model.aadl | line 95: Couldn't resolve reference to 'temp1'.
20. /CaseProject/modified_model.aadl | line 95: Couldn't resolve reference to 'tempin1'.
21. /CaseProject/modified_model.aadl | line 95: named thing must be an expression with a type
22. /CaseProject/modified_model.aadl | line 98: Couldn't resolve reference to 'temp2'.
23. /CaseProject/modified_model.aadl | line 98: Couldn't resolve reference to 'tempin2'.
24. /CaseProject/modified_model.aadl | line 98: named thing must be an expression with a type
25. /CaseProject/modified_model.aadl | line 101: Couldn't resolve reference to 'tempin1'.
26. /CaseProject/modified_model.aadl | line 101: Couldn't resolve reference to 'tempin2'.
27. /CaseProject/modified_model.aadl | line 101: Couldn't resolve reference to 'tempout'.
28. /CaseProject/modified_model.aadl | line 101: named thing must be an expression with a type
29. /CaseProject/modified_model.aadl | line 107: Assume statements are allowed only in component types
30. /CaseProject/modified_model.aadl | line 108: Couldn't resolve reference to 'tempin1'.
31. /CaseProject/modified_model.aadl | line 108: Couldn't resolve reference to 'tempin2'.
32. /CaseProject/modified_model.aadl | line 108: Couldn't resolve reference to 'tempout'.
33. /CaseProject/modified_model.aadl | line 108: named thing must be an expression with a type
34. /CaseProject/modified_model.aadl | line 110: Guarantee statements are allowed only in component types
35. /CaseProject/modified_model.aadl | line 111: Couldn't resolve reference to 'temp1'.
36. /CaseProject/modified_model.aadl | line 111: Couldn't resolve reference to 'tempin1'.
37. /CaseProject/modified_model.aadl | line 111: named thing must be an expression with a type
38. /CaseProject/modified_model.aadl | line 113: Guarantee statements are allowed only in component types
39. /CaseProject/modified_model.aadl | line 114: Couldn't resolve reference to 'temp2'.
40. /CaseProject/modified_model.aadl | line 114: Couldn't resolve reference to 'tempin2'.
41. /CaseProject/modified_model.aadl | line 114: named thing must be an expression with a type
42. /CaseProject/modified_model.aadl | line 116: Guarantee statements are allowed only in component types
43. /CaseProject/modified_model.aadl | line 117: Couldn't resolve reference to 'tempin1'.
44. /CaseProject/modified_model.aadl | line 117: Couldn't resolve reference to 'tempin2'.
45. /CaseProject/modified_model.aadl | line 117: Couldn't resolve reference to 'tempout'.
46. /CaseProject/modified_model.aadl | line 117: named thing must be an expression with a type
