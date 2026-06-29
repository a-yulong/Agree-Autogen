# Case71 Refactored Experiment Report

## Summary

- Setting: E6 (No Requirement Analyst)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 351.82
- Initial validation errors: 8
- Final validation errors: 26

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 26
- Warnings: 2

## Modules

- rag: True
- repair: True
- requirement_analyst: False
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 48838
- completion_tokens: 6874
- total_tokens: 55712

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [rag_digest_agree_generator] extracted_json_object - Recovered first balanced JSON object.
3. [rag_digest_model_fusion] extracted_json_object - Recovered first balanced JSON object.
4. [model_fusion_target] extracted_json_object - Recovered first balanced JSON object.
5. [model_fusion_plan] extracted_json_object - Recovered first balanced JSON object.
6. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
7. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
8. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
9. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
10. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
11. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
12. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
13. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
14. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
15. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.
16. [rag_digest_validation_repair] extracted_json_object - Recovered first balanced JSON object.
17. [validation_repair_plan] extracted_json_object - Recovered first balanced JSON object.
18. [validation_repair] missing_repaired_aadl_tag - Recovered AADL artifact without the requested section tag.
19. [validation_repair] recovered_package_block - Recovered complete AADL package block.
20. [validation_repair] complete_aadl_repair_used - Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.
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

1. /CaseProject/modified_model.aadl | line 107: Assignment statements are allowed only in component implementations
2. /CaseProject/modified_model.aadl | line 107: Couldn't resolve reference to '"signal_routing_gps_pos": pspg.gps_pos'.
3. /CaseProject/modified_model.aadl | line 107: mismatched input '"signal_routing_gps_pos"' expecting RULE_ID
4. /CaseProject/modified_model.aadl | line 108: Assignment statements are allowed only in component implementations
5. /CaseProject/modified_model.aadl | line 108: Couldn't resolve reference to '"signal_routing_speed": speed'.
6. /CaseProject/modified_model.aadl | line 108: Couldn't resolve reference to 'pspg'.
7. /CaseProject/modified_model.aadl | line 108: Couldn't resolve reference to 'speed'.
8. /CaseProject/modified_model.aadl | line 108: mismatched input '"signal_routing_speed"' expecting RULE_ID
9. /CaseProject/modified_model.aadl | line 109: Assignment statements are allowed only in component implementations
10. /CaseProject/modified_model.aadl | line 109: Couldn't resolve reference to '"signal_routing_angle": angle'.
11. /CaseProject/modified_model.aadl | line 109: Couldn't resolve reference to 'angle'.
12. /CaseProject/modified_model.aadl | line 109: Couldn't resolve reference to 'pspg'.
13. /CaseProject/modified_model.aadl | line 109: mismatched input '"signal_routing_angle"' expecting RULE_ID
14. /CaseProject/modified_model.aadl | line 123: Couldn't resolve reference to '"signal_routing_gps_pos": gps_pos'.
15. /CaseProject/modified_model.aadl | line 123: Couldn't resolve reference to 'gps_pos'.
16. /CaseProject/modified_model.aadl | line 123: Couldn't resolve reference to 'pspg'.
17. /CaseProject/modified_model.aadl | line 123: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
18. /CaseProject/modified_model.aadl | line 123: mismatched input '"signal_routing_gps_pos"' expecting RULE_ID
19. /CaseProject/modified_model.aadl | line 124: Couldn't resolve reference to '"signal_routing_speed": pspg.speed'.
20. /CaseProject/modified_model.aadl | line 124: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
21. /CaseProject/modified_model.aadl | line 124: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'int'
22. /CaseProject/modified_model.aadl | line 124: mismatched input '"signal_routing_speed"' expecting RULE_ID
23. /CaseProject/modified_model.aadl | line 125: Couldn't resolve reference to '"signal_routing_angle": pspg.angle'.
24. /CaseProject/modified_model.aadl | line 125: LHS of assignment must be an AGREE 'eq' variable or an output port of this component
25. /CaseProject/modified_model.aadl | line 125: The left hand side of the assignment statement is of type '<error>' but the right hand side is of type 'int'
26. /CaseProject/modified_model.aadl | line 125: mismatched input '"signal_routing_angle"' expecting RULE_ID
