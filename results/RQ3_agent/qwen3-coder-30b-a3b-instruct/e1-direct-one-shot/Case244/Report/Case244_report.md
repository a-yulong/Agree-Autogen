# Case244 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 66.30
- Initial validation errors: 58
- Final validation errors: 58

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 58
- Warnings: 2

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3678
- completion_tokens: 2920
- total_tokens: 6598

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 12: Couldn't resolve reference to DeviceSubcomponentType 'LGS.imp'.
2. /CaseProject/modified_model.aadl | line 13: Couldn't resolve reference to DeviceSubcomponentType 'DPS.imp'.
3. /CaseProject/modified_model.aadl | line 14: Couldn't resolve reference to DeviceSubcomponentType 'OCU.imp'.
4. /CaseProject/modified_model.aadl | line 15: Couldn't resolve reference to DeviceSubcomponentType 'FWS.imp'.
5. /CaseProject/modified_model.aadl | line 16: Couldn't resolve reference to DeviceSubcomponentType 'ECAM.imp'.
6. /CaseProject/modified_model.aadl | line 17: Couldn't resolve reference to ProcessSubcomponentType 'doors_process.imp'.
7. /CaseProject/modified_model.aadl | line 20: Couldn't resolve reference to ConnectionEnd 'D1_handle_position'.
8. /CaseProject/modified_model.aadl | line 21: Couldn't resolve reference to ConnectionEnd 'D1_closed'.
9. /CaseProject/modified_model.aadl | line 22: Couldn't resolve reference to ConnectionEnd 'D1_latched'.
10. /CaseProject/modified_model.aadl | line 23: Couldn't resolve reference to ConnectionEnd 'D1_locked'.
11. /CaseProject/modified_model.aadl | line 24: Couldn't resolve reference to ConnectionEnd 'D1_swivel'.
12. /CaseProject/modified_model.aadl | line 25: Couldn't resolve reference to ConnectionEnd 'D1_de_arrest'.
13. /CaseProject/modified_model.aadl | line 26: Couldn't resolve reference to ConnectionEnd 'D1_lock'.
14. /CaseProject/modified_model.aadl | line 27: Couldn't resolve reference to ConnectionEnd 'D1_warn_diff_pres'.
15. /CaseProject/modified_model.aadl | line 28: Couldn't resolve reference to ConnectionEnd 'D1_warn_slide'.
16. /CaseProject/modified_model.aadl | line 29: Couldn't resolve reference to ConnectionEnd 'D1_in_flight'.
17. /CaseProject/modified_model.aadl | line 29: Couldn't resolve reference to ConnectionEnd 'in_flight1'.
18. /CaseProject/modified_model.aadl | line 30: Couldn't resolve reference to ConnectionEnd 'D1_on_ground'.
19. /CaseProject/modified_model.aadl | line 30: Couldn't resolve reference to ConnectionEnd 'on_ground1'.
20. /CaseProject/modified_model.aadl | line 31: Couldn't resolve reference to ConnectionEnd 'D1_engine_running'.
21. /CaseProject/modified_model.aadl | line 31: Couldn't resolve reference to ConnectionEnd 'engine_running1'.
22. /CaseProject/modified_model.aadl | line 32: Couldn't resolve reference to ConnectionEnd 'D1_emergency_evacuation'.
23. /CaseProject/modified_model.aadl | line 32: Couldn't resolve reference to ConnectionEnd 'emergency_evacuation1'.
24. /CaseProject/modified_model.aadl | line 33: Couldn't resolve reference to ConnectionEnd 'D1_ecam_info'.
25. /CaseProject/modified_model.aadl | line 33: Couldn't resolve reference to ConnectionEnd 'info_door1'.
26. /CaseProject/modified_model.aadl | line 34: Couldn't resolve reference to ConnectionEnd 'D1_warning_info'.
27. /CaseProject/modified_model.aadl | line 34: Couldn't resolve reference to ConnectionEnd 'wrn_door1'.
28. /CaseProject/modified_model.aadl | line 36: Couldn't resolve reference to ConnectionEnd 'D1_dps'.
29. /CaseProject/modified_model.aadl | line 36: Couldn't resolve reference to ConnectionEnd 'dps1'.
30. /CaseProject/modified_model.aadl | line 38: Couldn't resolve reference to ConnectionEnd 'D2_handle_position'.
31. /CaseProject/modified_model.aadl | line 39: Couldn't resolve reference to ConnectionEnd 'D2_closed'.
32. /CaseProject/modified_model.aadl | line 40: Couldn't resolve reference to ConnectionEnd 'D2_latched'.
33. /CaseProject/modified_model.aadl | line 41: Couldn't resolve reference to ConnectionEnd 'D2_locked'.
34. /CaseProject/modified_model.aadl | line 42: Couldn't resolve reference to ConnectionEnd 'D2_swivel'.
35. /CaseProject/modified_model.aadl | line 43: Couldn't resolve reference to ConnectionEnd 'D2_de_arrest'.
36. /CaseProject/modified_model.aadl | line 44: Couldn't resolve reference to ConnectionEnd 'D2_lock'.
37. /CaseProject/modified_model.aadl | line 45: Couldn't resolve reference to ConnectionEnd 'D2_warn_diff_pres'.
38. /CaseProject/modified_model.aadl | line 46: Couldn't resolve reference to ConnectionEnd 'D2_warn_slide'.
39. /CaseProject/modified_model.aadl | line 47: Couldn't resolve reference to ConnectionEnd 'D2_in_flight'.
40. /CaseProject/modified_model.aadl | line 47: Couldn't resolve reference to ConnectionEnd 'in_flight2'.
41. /CaseProject/modified_model.aadl | line 48: Couldn't resolve reference to ConnectionEnd 'D2_on_ground'.
42. /CaseProject/modified_model.aadl | line 48: Couldn't resolve reference to ConnectionEnd 'on_ground2'.
43. /CaseProject/modified_model.aadl | line 49: Couldn't resolve reference to ConnectionEnd 'D2_engine_running'.
44. /CaseProject/modified_model.aadl | line 49: Couldn't resolve reference to ConnectionEnd 'engine_running2'.
45. /CaseProject/modified_model.aadl | line 50: Couldn't resolve reference to ConnectionEnd 'D2_emergency_evacuation'.
46. /CaseProject/modified_model.aadl | line 50: Couldn't resolve reference to ConnectionEnd 'emergency_evacuation2'.
47. /CaseProject/modified_model.aadl | line 51: Couldn't resolve reference to ConnectionEnd 'D2_warning_info'.
48. /CaseProject/modified_model.aadl | line 51: Couldn't resolve reference to ConnectionEnd 'wrn_door2'.
49. /CaseProject/modified_model.aadl | line 52: Couldn't resolve reference to ConnectionEnd 'D2_ecam_info'.
50. /CaseProject/modified_model.aadl | line 52: Couldn't resolve reference to ConnectionEnd 'info_door2'.
51. /CaseProject/modified_model.aadl | line 54: Couldn't resolve reference to ConnectionEnd 'D2_dps'.
52. /CaseProject/modified_model.aadl | line 54: Couldn't resolve reference to ConnectionEnd 'dps2'.
53. /CaseProject/modified_model.aadl | line 59: Couldn't resolve reference to ConnectionEnd 'Mix_cll'.
54. /CaseProject/modified_model.aadl | line 59: Couldn't resolve reference to ConnectionEnd 'cll'.
55. /CaseProject/modified_model.aadl | line 95: Couldn't resolve reference to property definition 'AGREE_Guarded'. Property set name may be missing.
56. /CaseProject/modified_model.aadl | line 96: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@2ec85a25{platform:/resource/CaseProject/modified_model.aadl#DMS.DMS_public.door.imp.agree}' must be set
57. /CaseProject/modified_model.aadl | line 96: mismatched input '{' expecting RULE_ANNEXTEXT
58. /CaseProject/modified_model.aadl | line 229: mismatched input '<EOF>' expecting 'end'
