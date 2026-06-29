# Case39 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 296.38
- Initial validation errors: 5
- Final validation errors: 13

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 11
- AGREE errors: 2
- Warnings: 4

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 22088
- completion_tokens: 2935
- total_tokens: 25023

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 3 classified requirement item(s).
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

1. Target (port spec) points to Types  speed.speed_impl (entity reference), which is not of an adequate kind
2. Target (port spec) does not point to anything or to something unreachable
3. Actual (port spec) points to Types  speed.speed_impl (entity reference), which is not of an adequate kind
4. Actual (port spec) does not point to anything or to something unreachable
5. Actual (port spec) points to Types  speed.speed_impl (entity reference), which is not of an adequate kind
6. Actual (port spec) does not point to anything or to something unreachable
7. State_Out (port spec) points to Types  state_sig.impl (entity reference), which is not of an adequate kind
8. State_Out (port spec) does not point to anything or to something unreachable
9. State_Out (port spec) points to Types  state_sig.impl (entity reference), which is not of an adequate kind
10. State_Out (port spec) does not point to anything or to something unreachable
11. Cannot analyze AADL specifications
12. /CaseProject/modified_model.aadl | line 22: left and right sides of binary expression '+' are of type 'Types::speed.speed_impl' and 'real', but must be of the same type
13. /CaseProject/modified_model.aadl | line 22: left side of binary expression '+' is of type 'Types::speed.speed_impl' but must be of type'int' or 'real'
