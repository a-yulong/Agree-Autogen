# Case11 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 308.07
- Initial validation errors: 15
- Final validation errors: 16

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 16
- Warnings: 1

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 33917
- completion_tokens: 3868
- total_tokens: 37785

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 5 classified requirement item(s).
4. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
5. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
6. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
7. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
8. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
9. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
10. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
11. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
12. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
13. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
14. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
15. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
16. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
17. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
18. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
19. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
20. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
21. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
22. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
23. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
24. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
25. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
26. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
27. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 26: mismatched input '=' expecting ':'
2. /CaseProject/modified_model.aadl | line 27: mismatched input '=' expecting ':'
3. /CaseProject/modified_model.aadl | line 28: mismatched input '=' expecting ':'
4. /CaseProject/modified_model.aadl | line 30: left and right sides of binary expression '=' are of type '<error>' and 'real', but must be of the same type
5. /CaseProject/modified_model.aadl | line 30: named thing must be an expression with a type
6. /CaseProject/modified_model.aadl | line 31: left and right sides of binary expression '=' are of type '<error>' and 'real', but must be of the same type
7. /CaseProject/modified_model.aadl | line 31: named thing must be an expression with a type
8. /CaseProject/modified_model.aadl | line 32: left and right sides of binary expression '=' are of type '<error>' and 'real', but must be of the same type
9. /CaseProject/modified_model.aadl | line 32: named thing must be an expression with a type
10. /CaseProject/modified_model.aadl | line 34: Couldn't resolve reference to 'altitudeFromGround'.
11. /CaseProject/modified_model.aadl | line 34: Couldn't resolve reference to 'height'.
12. /CaseProject/modified_model.aadl | line 34: named thing must be an expression with a type
13. /CaseProject/modified_model.aadl | line 36: Couldn't resolve reference to 'altitudeFromGround'.
14. /CaseProject/modified_model.aadl | line 36: left and right sides of binary expression '<=' are of type '<error>' and 'real', but must be of the same type
15. /CaseProject/modified_model.aadl | line 36: left side of binary expression '<=' is of type '<error>' but must be of type'int' or 'real'
16. /CaseProject/modified_model.aadl | line 36: named thing must be an expression with a type
