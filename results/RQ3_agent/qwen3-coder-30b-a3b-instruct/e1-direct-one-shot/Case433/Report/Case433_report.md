# Case433 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 94.57
- Initial validation errors: 36
- Final validation errors: 36

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 36
- Warnings: 0

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3680
- completion_tokens: 3160
- total_tokens: 6840

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 17: Couldn't resolve reference to ProcessSubcomponentType 'doors_process.imp'.
2. /CaseProject/modified_model.aadl | line 20: Couldn't resolve reference to ConnectionEnd 'D1_handle_position'.
3. /CaseProject/modified_model.aadl | line 21: Couldn't resolve reference to ConnectionEnd 'D1_closed'.
4. /CaseProject/modified_model.aadl | line 22: Couldn't resolve reference to ConnectionEnd 'D1_latched'.
5. /CaseProject/modified_model.aadl | line 23: Couldn't resolve reference to ConnectionEnd 'D1_locked'.
6. /CaseProject/modified_model.aadl | line 24: Couldn't resolve reference to ConnectionEnd 'D1_swivel'.
7. /CaseProject/modified_model.aadl | line 25: Couldn't resolve reference to ConnectionEnd 'D1_de_arrest'.
8. /CaseProject/modified_model.aadl | line 26: Couldn't resolve reference to ConnectionEnd 'D1_lock'.
9. /CaseProject/modified_model.aadl | line 27: Couldn't resolve reference to ConnectionEnd 'D1_warn_diff_pres'.
10. /CaseProject/modified_model.aadl | line 28: Couldn't resolve reference to ConnectionEnd 'D1_warn_slide'.
11. /CaseProject/modified_model.aadl | line 29: Couldn't resolve reference to ConnectionEnd 'D1_in_flight'.
12. /CaseProject/modified_model.aadl | line 30: Couldn't resolve reference to ConnectionEnd 'D1_on_ground'.
13. /CaseProject/modified_model.aadl | line 31: Couldn't resolve reference to ConnectionEnd 'D1_engine_running'.
14. /CaseProject/modified_model.aadl | line 32: Couldn't resolve reference to ConnectionEnd 'D1_emergency_evacuation'.
15. /CaseProject/modified_model.aadl | line 33: Couldn't resolve reference to ConnectionEnd 'D1_ecam_info'.
16. /CaseProject/modified_model.aadl | line 34: Couldn't resolve reference to ConnectionEnd 'D1_warning_info'.
17. /CaseProject/modified_model.aadl | line 36: Couldn't resolve reference to ConnectionEnd 'D1_dps'.
18. /CaseProject/modified_model.aadl | line 38: Couldn't resolve reference to ConnectionEnd 'D2_handle_position'.
19. /CaseProject/modified_model.aadl | line 39: Couldn't resolve reference to ConnectionEnd 'D2_closed'.
20. /CaseProject/modified_model.aadl | line 40: Couldn't resolve reference to ConnectionEnd 'D2_latched'.
21. /CaseProject/modified_model.aadl | line 41: Couldn't resolve reference to ConnectionEnd 'D2_locked'.
22. /CaseProject/modified_model.aadl | line 42: Couldn't resolve reference to ConnectionEnd 'D2_swivel'.
23. /CaseProject/modified_model.aadl | line 43: Couldn't resolve reference to ConnectionEnd 'D2_de_arrest'.
24. /CaseProject/modified_model.aadl | line 44: Couldn't resolve reference to ConnectionEnd 'D2_lock'.
25. /CaseProject/modified_model.aadl | line 45: Couldn't resolve reference to ConnectionEnd 'D2_warn_diff_pres'.
26. /CaseProject/modified_model.aadl | line 46: Couldn't resolve reference to ConnectionEnd 'D2_warn_slide'.
27. /CaseProject/modified_model.aadl | line 47: Couldn't resolve reference to ConnectionEnd 'D2_in_flight'.
28. /CaseProject/modified_model.aadl | line 48: Couldn't resolve reference to ConnectionEnd 'D2_on_ground'.
29. /CaseProject/modified_model.aadl | line 49: Couldn't resolve reference to ConnectionEnd 'D2_engine_running'.
30. /CaseProject/modified_model.aadl | line 50: Couldn't resolve reference to ConnectionEnd 'D2_emergency_evacuation'.
31. /CaseProject/modified_model.aadl | line 51: Couldn't resolve reference to ConnectionEnd 'D2_warning_info'.
32. /CaseProject/modified_model.aadl | line 52: Couldn't resolve reference to ConnectionEnd 'D2_ecam_info'.
33. /CaseProject/modified_model.aadl | line 54: Couldn't resolve reference to ConnectionEnd 'D2_dps'.
34. /CaseProject/modified_model.aadl | line 59: Couldn't resolve reference to ConnectionEnd 'Mix_cll'.
35. /CaseProject/modified_model.aadl | line 138: Couldn't resolve reference to property definition 'AGREE_Guard'. Property set name may be missing.
36. /CaseProject/modified_model.aadl | line 140: mismatched input '.' expecting ';'
