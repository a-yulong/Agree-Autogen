# Case431 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 63.67
- Initial validation errors: 59
- Final validation errors: 59

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 59
- Warnings: 2

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3687
- completion_tokens: 3421
- total_tokens: 7108

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 14: Couldn't resolve reference to DeviceSubcomponentType 'OCU.imp'.
2. /CaseProject/modified_model.aadl | line 15: Couldn't resolve reference to DeviceSubcomponentType 'FWS.imp'.
3. /CaseProject/modified_model.aadl | line 16: Couldn't resolve reference to DeviceSubcomponentType 'ECAM.imp'.
4. /CaseProject/modified_model.aadl | line 17: Couldn't resolve reference to ProcessSubcomponentType 'doors_process.imp'.
5. /CaseProject/modified_model.aadl | line 20: Couldn't resolve reference to ConnectionEnd 'D1_handle_position'.
6. /CaseProject/modified_model.aadl | line 21: Couldn't resolve reference to ConnectionEnd 'D1_closed'.
7. /CaseProject/modified_model.aadl | line 22: Couldn't resolve reference to ConnectionEnd 'D1_latched'.
8. /CaseProject/modified_model.aadl | line 23: Couldn't resolve reference to ConnectionEnd 'D1_locked'.
9. /CaseProject/modified_model.aadl | line 24: Couldn't resolve reference to ConnectionEnd 'D1_swivel'.
10. /CaseProject/modified_model.aadl | line 25: Couldn't resolve reference to ConnectionEnd 'D1_de_arrest'.
11. /CaseProject/modified_model.aadl | line 26: Couldn't resolve reference to ConnectionEnd 'D1_lock'.
12. /CaseProject/modified_model.aadl | line 27: Couldn't resolve reference to ConnectionEnd 'D1_warn_diff_pres'.
13. /CaseProject/modified_model.aadl | line 28: Couldn't resolve reference to ConnectionEnd 'D1_warn_slide'.
14. /CaseProject/modified_model.aadl | line 29: Couldn't resolve reference to ConnectionEnd 'D1_in_flight'.
15. /CaseProject/modified_model.aadl | line 30: Couldn't resolve reference to ConnectionEnd 'D1_on_ground'.
16. /CaseProject/modified_model.aadl | line 31: Couldn't resolve reference to ConnectionEnd 'D1_engine_running'.
17. /CaseProject/modified_model.aadl | line 32: Couldn't resolve reference to ConnectionEnd 'D1_emergency_evacuation'.
18. /CaseProject/modified_model.aadl | line 33: Couldn't resolve reference to ConnectionEnd 'D1_ecam_info'.
19. /CaseProject/modified_model.aadl | line 33: Couldn't resolve reference to ConnectionEnd 'info_door1'.
20. /CaseProject/modified_model.aadl | line 34: Couldn't resolve reference to ConnectionEnd 'D1_warning_info'.
21. /CaseProject/modified_model.aadl | line 34: Couldn't resolve reference to ConnectionEnd 'wrn_door1'.
22. /CaseProject/modified_model.aadl | line 36: Couldn't resolve reference to ConnectionEnd 'D1_dps'.
23. /CaseProject/modified_model.aadl | line 38: Couldn't resolve reference to ConnectionEnd 'D2_handle_position'.
24. /CaseProject/modified_model.aadl | line 39: Couldn't resolve reference to ConnectionEnd 'D2_closed'.
25. /CaseProject/modified_model.aadl | line 40: Couldn't resolve reference to ConnectionEnd 'D2_latched'.
26. /CaseProject/modified_model.aadl | line 41: Couldn't resolve reference to ConnectionEnd 'D2_locked'.
27. /CaseProject/modified_model.aadl | line 42: Couldn't resolve reference to ConnectionEnd 'D2_swivel'.
28. /CaseProject/modified_model.aadl | line 43: Couldn't resolve reference to ConnectionEnd 'D2_de_arrest'.
29. /CaseProject/modified_model.aadl | line 44: Couldn't resolve reference to ConnectionEnd 'D2_lock'.
30. /CaseProject/modified_model.aadl | line 45: Couldn't resolve reference to ConnectionEnd 'D2_warn_diff_pres'.
31. /CaseProject/modified_model.aadl | line 46: Couldn't resolve reference to ConnectionEnd 'D2_warn_slide'.
32. /CaseProject/modified_model.aadl | line 47: Couldn't resolve reference to ConnectionEnd 'D2_in_flight'.
33. /CaseProject/modified_model.aadl | line 48: Couldn't resolve reference to ConnectionEnd 'D2_on_ground'.
34. /CaseProject/modified_model.aadl | line 49: Couldn't resolve reference to ConnectionEnd 'D2_engine_running'.
35. /CaseProject/modified_model.aadl | line 50: Couldn't resolve reference to ConnectionEnd 'D2_emergency_evacuation'.
36. /CaseProject/modified_model.aadl | line 51: Couldn't resolve reference to ConnectionEnd 'D2_warning_info'.
37. /CaseProject/modified_model.aadl | line 51: Couldn't resolve reference to ConnectionEnd 'wrn_door2'.
38. /CaseProject/modified_model.aadl | line 52: Couldn't resolve reference to ConnectionEnd 'D2_ecam_info'.
39. /CaseProject/modified_model.aadl | line 52: Couldn't resolve reference to ConnectionEnd 'info_door2'.
40. /CaseProject/modified_model.aadl | line 54: Couldn't resolve reference to ConnectionEnd 'D2_dps'.
41. /CaseProject/modified_model.aadl | line 59: Couldn't resolve reference to ConnectionEnd 'Mix_cll'.
42. /CaseProject/modified_model.aadl | line 59: Couldn't resolve reference to ConnectionEnd 'cll'.
43. /CaseProject/modified_model.aadl | line 123: Couldn't resolve reference to property definition 'AGREE_Bounds'. Property set name may be missing.
44. /CaseProject/modified_model.aadl | line 124: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@230232b0{platform:/resource/CaseProject/modified_model.aadl#DMS.DMS_public.DPS.imp.agree}' must be set
45. /CaseProject/modified_model.aadl | line 124: mismatched input '{' expecting RULE_ANNEXTEXT
46. /CaseProject/modified_model.aadl | line 125: mismatched input 'properties' expecting 'end'
47. /CaseProject/modified_model.aadl | line 126: Couldn't resolve reference to property definition 'bounds'. Property set name may be missing.
48. /CaseProject/modified_model.aadl | line 126: Couldn't resolve reference to property definition 'integer'. Property set name may be missing.
49. /CaseProject/modified_model.aadl | line 126: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@8f57e4c{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPropertyAssociation.0}' with 0 values must have at least 1 values
50. /CaseProject/modified_model.aadl | line 126: mismatched character ' ' expecting '>'
51. /CaseProject/modified_model.aadl | line 126: mismatched input ':' expecting '=>'
52. /CaseProject/modified_model.aadl | line 126: missing '=>' at '100'
53. /CaseProject/modified_model.aadl | line 127: Couldn't resolve reference to property definition 'bound_dps1'. Property set name may be missing.
54. /CaseProject/modified_model.aadl | line 127: Couldn't resolve reference to property definition 'integer'. Property set name may be missing.
55. /CaseProject/modified_model.aadl | line 127: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@15e5246{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPropertyAssociation.2}' with 0 values must have at least 1 values
56. /CaseProject/modified_model.aadl | line 127: mismatched character ' ' expecting '>'
57. /CaseProject/modified_model.aadl | line 127: mismatched input ':' expecting '=>'
58. /CaseProject/modified_model.aadl | line 127: missing '=>' at '0'
59. /CaseProject/modified_model.aadl | line 129: missing EOF at '}'
