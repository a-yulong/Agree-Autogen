# Case65 Refactored Experiment Report

## Summary

- Setting: E2 (Full AGREE-AutoGen)
- Final status: Fail
- Repair rounds: 5
- Runtime seconds: 328.69
- Initial validation errors: 6
- Final validation errors: 26

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 6
- AGREE errors: 20
- Warnings: 7

## Modules

- rag: True
- repair: True
- requirement_analyst: True
- model_analyst: True
- agree_generator: True
- model_fusion: True

## Token Usage

- prompt_tokens: 40452
- completion_tokens: 5644
- total_tokens: 46096

## Output Recovery

1. [model_analyst] extracted_json_object - Recovered first balanced JSON object.
2. [requirement_analyst] extracted_json_object - Recovered first balanced JSON object.
3. [requirement_analyst] requirement_items_normalized - Normalized 2 classified requirement item(s).
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
25. [validation_repair] recovered_annex_blocks - Recovered AGREE annex block(s) without full package.
26. [validation_repair] repair_annexes_merged_locally - Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.

## Final Diagnostics

1. TMP (subcomponent) points to software_aocs  Telemetry_Processing (entity reference), which does not exist.
2. FDR (subcomponent) points to software_aocs  Failure_Detection_Isolation (entity reference), which does not exist.
3. FR (subcomponent) points to software_aocs  Failure_Recovery (entity reference), which does not exist.
4. Reconfig (subcomponent) points to software_aocs  Reconfigurations (entity reference), which does not exist. Possible mispelling of software_aocs  reconfigurations
5. ME (subcomponent) points to software_aocs  Manoeuvre_Execution (entity reference), which does not exist.
6. Cannot analyze AADL specifications
7. /CaseProject/modified_model.aadl | line 72: Couldn't resolve reference to 'TCP'.
8. /CaseProject/modified_model.aadl | line 72: Couldn't resolve reference to 'nominal_attitude'.
9. /CaseProject/modified_model.aadl | line 72: left and right sides of binary expression '=' are of type 'real' and '<error>', but must be of the same type
10. /CaseProject/modified_model.aadl | line 72: left side of binary expression '=>' is of type '<error>' but must be of type 'bool'
11. /CaseProject/modified_model.aadl | line 72: named thing must be an expression with a type
12. /CaseProject/modified_model.aadl | line 75: Couldn't resolve reference to 'TCP'.
13. /CaseProject/modified_model.aadl | line 75: Couldn't resolve reference to 'nominal_orbit'.
14. /CaseProject/modified_model.aadl | line 75: left and right sides of binary expression '=' are of type 'real' and '<error>', but must be of the same type
15. /CaseProject/modified_model.aadl | line 75: left side of binary expression '=>' is of type '<error>' but must be of type 'bool'
16. /CaseProject/modified_model.aadl | line 75: named thing must be an expression with a type
17. /CaseProject/modified_model.aadl | line 78: Couldn't resolve reference to 'TCP'.
18. /CaseProject/modified_model.aadl | line 78: Couldn't resolve reference to 'nominal_attitude'.
19. /CaseProject/modified_model.aadl | line 78: left and right sides of binary expression '=' are of type 'real' and '<error>', but must be of the same type
20. /CaseProject/modified_model.aadl | line 78: named thing must be an expression with a type
21. /CaseProject/modified_model.aadl | line 81: Couldn't resolve reference to 'TCP'.
22. /CaseProject/modified_model.aadl | line 81: Couldn't resolve reference to 'nominal_orbit'.
23. /CaseProject/modified_model.aadl | line 81: left and right sides of binary expression '=' are of type 'real' and '<error>', but must be of the same type
24. /CaseProject/modified_model.aadl | line 81: named thing must be an expression with a type
25. /CaseProject/modified_model.aadl | line 103: Couldn't resolve reference to ConnectionEnd 'attitude_window'.
26. /CaseProject/modified_model.aadl | line 104: Couldn't resolve reference to ConnectionEnd 'check_thresholds'.
