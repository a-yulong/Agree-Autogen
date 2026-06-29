# Case38 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 307.76
- Initial validation errors: 5
- Final validation errors: 14

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 11
- AGREE errors: 3
- Warnings: 4

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 31631
- completion_tokens: 3753
- total_tokens: 35384

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 4 classified requirement item(s).
4. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
5. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
6. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
7. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
8. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
9. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
10. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
11. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
12. [validation_repair] normalized_text_or_annex_delimiters - Normalized code fence or annex delimiter formatting.
13. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
14. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
15. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
16. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
17. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
18. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
19. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
20. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
21. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
22. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
23. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
24. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
25. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
26. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

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
12. /CaseProject/modified_model.aadl | line 13: The variable 'e' on the left side of equation is of type 'real' but must be of type 'Types::speed.speed_impl'
13. /CaseProject/modified_model.aadl | line 13: left side of binary expression '-' is of type 'Types::speed.speed_impl' but must be of type'int' or 'real'
14. /CaseProject/modified_model.aadl | line 13: right side of binary expression '-' is of type 'Types::speed.speed_impl' but must be of type'int' or 'real'
