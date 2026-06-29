# Case186 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 64.13
- Initial validation errors: 45
- Final validation errors: 45

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 45
- Warnings: 19

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3678
- completion_tokens: 3535
- total_tokens: 7213

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 115: Duplicate Element 'DPS' in PublicPackageSection 'DMS_public'
2. /CaseProject/modified_model.aadl | line 197: Couldn't resolve reference to ThreadSubcomponentType 'doors_int.imp'.
3. /CaseProject/modified_model.aadl | line 233: Couldn't resolve reference to ConnectionEnd 'cll'.
4. /CaseProject/modified_model.aadl | line 236: Couldn't resolve reference to ConnectionEnd 'door2'.
5. /CaseProject/modified_model.aadl | line 237: Couldn't resolve reference to ConnectionEnd 'door1'.
6. /CaseProject/modified_model.aadl | line 283: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@b506ed0{platform:/resource/CaseProject/modified_model.aadl#DMS.DMS_public.door_handler.imp.agree}' must be set
7. /CaseProject/modified_model.aadl | line 283: mismatched input '{' expecting RULE_ANNEXTEXT
8. /CaseProject/modified_model.aadl | line 288: mismatched input ':' expecting 'end'
9. /CaseProject/modified_model.aadl | line 288: mismatched input 'feature' expecting 'end'
10. /CaseProject/modified_model.aadl | line 288: missing 'group' at 'in_flight'
11. /CaseProject/modified_model.aadl | line 289: mismatched input ':' expecting 'end'
12. /CaseProject/modified_model.aadl | line 289: missing 'group' at 'on_ground'
13. /CaseProject/modified_model.aadl | line 290: mismatched input ':' expecting 'end'
14. /CaseProject/modified_model.aadl | line 290: missing 'group' at 'engine_running'
15. /CaseProject/modified_model.aadl | line 291: mismatched input ':' expecting 'end'
16. /CaseProject/modified_model.aadl | line 291: missing 'group' at 'emergency_evacuation'
17. /CaseProject/modified_model.aadl | line 292: mismatched input ':' expecting 'end'
18. /CaseProject/modified_model.aadl | line 292: missing 'group' at 'handle_position'
19. /CaseProject/modified_model.aadl | line 293: mismatched input ':' expecting 'end'
20. /CaseProject/modified_model.aadl | line 293: missing 'group' at 'closed'
21. /CaseProject/modified_model.aadl | line 294: mismatched input ':' expecting 'end'
22. /CaseProject/modified_model.aadl | line 294: missing 'group' at 'latched'
23. /CaseProject/modified_model.aadl | line 295: mismatched input ':' expecting 'end'
24. /CaseProject/modified_model.aadl | line 295: missing 'group' at 'locked'
25. /CaseProject/modified_model.aadl | line 296: Duplicate Element 'dps' in PublicPackageSection 'DMS_public'
26. /CaseProject/modified_model.aadl | line 296: mismatched input ':' expecting 'end'
27. /CaseProject/modified_model.aadl | line 296: missing 'group' at 'dps'
28. /CaseProject/modified_model.aadl | line 299: mismatched input ':' expecting 'end'
29. /CaseProject/modified_model.aadl | line 299: missing 'group' at 'swivel'
30. /CaseProject/modified_model.aadl | line 300: mismatched input ':' expecting 'end'
31. /CaseProject/modified_model.aadl | line 300: missing 'group' at 'de_arrest'
32. /CaseProject/modified_model.aadl | line 301: mismatched input ':' expecting 'end'
33. /CaseProject/modified_model.aadl | line 301: missing 'group' at 'lock'
34. /CaseProject/modified_model.aadl | line 302: mismatched input ':' expecting 'end'
35. /CaseProject/modified_model.aadl | line 302: missing 'group' at 'warn_diff_pres'
36. /CaseProject/modified_model.aadl | line 303: mismatched input ':' expecting 'end'
37. /CaseProject/modified_model.aadl | line 303: missing 'group' at 'warn_slide'
38. /CaseProject/modified_model.aadl | line 304: mismatched input ':' expecting 'end'
39. /CaseProject/modified_model.aadl | line 304: missing 'group' at 'door_locked'
40. /CaseProject/modified_model.aadl | line 305: mismatched input ':' expecting 'end'
41. /CaseProject/modified_model.aadl | line 305: missing 'group' at 'warning_info'
42. /CaseProject/modified_model.aadl | line 306: mismatched input ':' expecting 'end'
43. /CaseProject/modified_model.aadl | line 306: missing 'group' at 'ecam_info'
44. /CaseProject/modified_model.aadl | line 309: mismatched character ' ' expecting '>'
45. /CaseProject/modified_model.aadl | line 311: missing EOF at '}'
