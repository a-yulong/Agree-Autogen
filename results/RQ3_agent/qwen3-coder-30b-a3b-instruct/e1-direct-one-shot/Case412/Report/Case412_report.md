# Case412 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 50.53
- Initial validation errors: 44
- Final validation errors: 44

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 44
- Warnings: 12

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 5051
- completion_tokens: 1944
- total_tokens: 6995

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 59: Couldn't resolve reference to property definition 'ARINC653::HM_Errors'.
2. /CaseProject/modified_model.aadl | line 60: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Application_Error'. For classifier references use classifier( <ref> ).
3. /CaseProject/modified_model.aadl | line 60: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Deadline_Miss'. For classifier references use classifier( <ref> ).
4. /CaseProject/modified_model.aadl | line 60: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Illegal_Request'. For classifier references use classifier( <ref> ).
5. /CaseProject/modified_model.aadl | line 60: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Numeric_Error'. For classifier references use classifier( <ref> ).
6. /CaseProject/modified_model.aadl | line 61: Couldn't resolve reference to property definition 'ARINC653::HM_Process_Recovery_actions'.
7. /CaseProject/modified_model.aadl | line 62: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Ignore'. For classifier references use classifier( <ref> ).
8. /CaseProject/modified_model.aadl | line 62: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Process_Restart'. For classifier references use classifier( <ref> ).
9. /CaseProject/modified_model.aadl | line 67: Couldn't resolve reference to property definition 'AGREE_Bounds'. Property set name may be missing.
10. /CaseProject/modified_model.aadl | line 67: mismatched input '=>' expecting ';'
11. /CaseProject/modified_model.aadl | line 67: no viable alternative at input '=>'
12. /CaseProject/modified_model.aadl | line 83: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Application_Error'. For classifier references use classifier( <ref> ).
13. /CaseProject/modified_model.aadl | line 83: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Deadline_Miss'. For classifier references use classifier( <ref> ).
14. /CaseProject/modified_model.aadl | line 83: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Illegal_Request'. For classifier references use classifier( <ref> ).
15. /CaseProject/modified_model.aadl | line 83: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Numeric_Error'. For classifier references use classifier( <ref> ).
16. /CaseProject/modified_model.aadl | line 83: Couldn't resolve reference to property definition 'ARINC653::HM_Errors'.
17. /CaseProject/modified_model.aadl | line 84: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Process_Restart'. For classifier references use classifier( <ref> ).
18. /CaseProject/modified_model.aadl | line 84: Couldn't resolve reference to property definition 'ARINC653::HM_Process_Recovery_Actions'.
19. /CaseProject/modified_model.aadl | line 106: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Application_Error'. For classifier references use classifier( <ref> ).
20. /CaseProject/modified_model.aadl | line 106: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Deadline_Miss'. For classifier references use classifier( <ref> ).
21. /CaseProject/modified_model.aadl | line 106: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Illegal_Request'. For classifier references use classifier( <ref> ).
22. /CaseProject/modified_model.aadl | line 106: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Numeric_Error'. For classifier references use classifier( <ref> ).
23. /CaseProject/modified_model.aadl | line 106: Couldn't resolve reference to property definition 'ARINC653::HM_Errors'.
24. /CaseProject/modified_model.aadl | line 107: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Process_Restart'. For classifier references use classifier( <ref> ).
25. /CaseProject/modified_model.aadl | line 107: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Process_Stop'. For classifier references use classifier( <ref> ).
26. /CaseProject/modified_model.aadl | line 107: Couldn't resolve reference to property definition 'ARINC653::HM_Process_Recovery_Actions'.
27. /CaseProject/modified_model.aadl | line 124: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Application_Error'. For classifier references use classifier( <ref> ).
28. /CaseProject/modified_model.aadl | line 124: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Deadline_Miss'. For classifier references use classifier( <ref> ).
29. /CaseProject/modified_model.aadl | line 124: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Illegal_Request'. For classifier references use classifier( <ref> ).
30. /CaseProject/modified_model.aadl | line 124: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Numeric_Error'. For classifier references use classifier( <ref> ).
31. /CaseProject/modified_model.aadl | line 124: Couldn't resolve reference to property definition 'ARINC653::HM_Errors'.
32. /CaseProject/modified_model.aadl | line 125: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Process_Restart'. For classifier references use classifier( <ref> ).
33. /CaseProject/modified_model.aadl | line 125: Couldn't resolve reference to property definition 'ARINC653::HM_Process_Recovery_Actions'.
34. /CaseProject/modified_model.aadl | line 190: Couldn't resolve reference to UnitLiteral 'ms'.
35. /CaseProject/modified_model.aadl | line 190: Couldn't resolve reference to property definition 'ARINC653::Partition_Slots'.
36. /CaseProject/modified_model.aadl | line 191: Couldn't resolve reference to property definition 'ARINC653::Slots_Allocation'.
37. /CaseProject/modified_model.aadl | line 192: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Power_Fail'. For classifier references use classifier( <ref> ).
38. /CaseProject/modified_model.aadl | line 192: Couldn't resolve reference to property definition 'ARINC653::HM_Errors'.
39. /CaseProject/modified_model.aadl | line 193: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Reset'. For classifier references use classifier( <ref> ).
40. /CaseProject/modified_model.aadl | line 193: Couldn't resolve reference to property definition 'ARINC653::HM_Module_Recovery_Actions'.
41. /CaseProject/modified_model.aadl | line 200: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Code_Memory'. For classifier references use classifier( <ref> ).
42. /CaseProject/modified_model.aadl | line 200: Couldn't resolve reference to property definition 'ARINC653::Memory_Type'.
43. /CaseProject/modified_model.aadl | line 206: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Code_Memory'. For classifier references use classifier( <ref> ).
44. /CaseProject/modified_model.aadl | line 206: Couldn't resolve reference to property definition 'ARINC653::Memory_Type'.
