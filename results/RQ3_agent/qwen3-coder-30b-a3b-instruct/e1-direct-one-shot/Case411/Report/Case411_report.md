# Case411 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 55.33
- Initial validation errors: 42
- Final validation errors: 42

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 42
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
- completion_tokens: 1884
- total_tokens: 6935

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 55: Couldn't resolve reference to property definition 'ARINC653::HM_Errors'.
2. /CaseProject/modified_model.aadl | line 56: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Application_Error'. For classifier references use classifier( <ref> ).
3. /CaseProject/modified_model.aadl | line 56: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Deadline_Miss'. For classifier references use classifier( <ref> ).
4. /CaseProject/modified_model.aadl | line 56: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Illegal_Request'. For classifier references use classifier( <ref> ).
5. /CaseProject/modified_model.aadl | line 56: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Numeric_Error'. For classifier references use classifier( <ref> ).
6. /CaseProject/modified_model.aadl | line 57: Couldn't resolve reference to property definition 'ARINC653::HM_Process_Recovery_actions'.
7. /CaseProject/modified_model.aadl | line 58: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Ignore'. For classifier references use classifier( <ref> ).
8. /CaseProject/modified_model.aadl | line 58: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Process_Restart'. For classifier references use classifier( <ref> ).
9. /CaseProject/modified_model.aadl | line 77: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Application_Error'. For classifier references use classifier( <ref> ).
10. /CaseProject/modified_model.aadl | line 77: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Deadline_Miss'. For classifier references use classifier( <ref> ).
11. /CaseProject/modified_model.aadl | line 77: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Illegal_Request'. For classifier references use classifier( <ref> ).
12. /CaseProject/modified_model.aadl | line 77: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Numeric_Error'. For classifier references use classifier( <ref> ).
13. /CaseProject/modified_model.aadl | line 77: Couldn't resolve reference to property definition 'ARINC653::HM_Errors'.
14. /CaseProject/modified_model.aadl | line 78: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Process_Restart'. For classifier references use classifier( <ref> ).
15. /CaseProject/modified_model.aadl | line 78: Couldn't resolve reference to property definition 'ARINC653::HM_Process_Recovery_Actions'.
16. /CaseProject/modified_model.aadl | line 96: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Application_Error'. For classifier references use classifier( <ref> ).
17. /CaseProject/modified_model.aadl | line 96: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Deadline_Miss'. For classifier references use classifier( <ref> ).
18. /CaseProject/modified_model.aadl | line 96: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Illegal_Request'. For classifier references use classifier( <ref> ).
19. /CaseProject/modified_model.aadl | line 96: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Numeric_Error'. For classifier references use classifier( <ref> ).
20. /CaseProject/modified_model.aadl | line 96: Couldn't resolve reference to property definition 'ARINC653::HM_Errors'.
21. /CaseProject/modified_model.aadl | line 97: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Process_Restart'. For classifier references use classifier( <ref> ).
22. /CaseProject/modified_model.aadl | line 97: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Process_Stop'. For classifier references use classifier( <ref> ).
23. /CaseProject/modified_model.aadl | line 97: Couldn't resolve reference to property definition 'ARINC653::HM_Process_Recovery_Actions'.
24. /CaseProject/modified_model.aadl | line 114: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Application_Error'. For classifier references use classifier( <ref> ).
25. /CaseProject/modified_model.aadl | line 114: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Deadline_Miss'. For classifier references use classifier( <ref> ).
26. /CaseProject/modified_model.aadl | line 114: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Illegal_Request'. For classifier references use classifier( <ref> ).
27. /CaseProject/modified_model.aadl | line 114: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Numeric_Error'. For classifier references use classifier( <ref> ).
28. /CaseProject/modified_model.aadl | line 114: Couldn't resolve reference to property definition 'ARINC653::HM_Errors'.
29. /CaseProject/modified_model.aadl | line 115: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Process_Restart'. For classifier references use classifier( <ref> ).
30. /CaseProject/modified_model.aadl | line 115: Couldn't resolve reference to property definition 'ARINC653::HM_Process_Recovery_Actions'.
31. /CaseProject/modified_model.aadl | line 167: Couldn't resolve reference to property definition 'Agree_Assumptions'. Property set name may be missing.
32. /CaseProject/modified_model.aadl | line 181: Couldn't resolve reference to UnitLiteral 'ms'.
33. /CaseProject/modified_model.aadl | line 181: Couldn't resolve reference to property definition 'ARINC653::Partition_Slots'.
34. /CaseProject/modified_model.aadl | line 182: Couldn't resolve reference to property definition 'ARINC653::Slots_Allocation'.
35. /CaseProject/modified_model.aadl | line 183: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Power_Fail'. For classifier references use classifier( <ref> ).
36. /CaseProject/modified_model.aadl | line 183: Couldn't resolve reference to property definition 'ARINC653::HM_Errors'.
37. /CaseProject/modified_model.aadl | line 184: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Reset'. For classifier references use classifier( <ref> ).
38. /CaseProject/modified_model.aadl | line 184: Couldn't resolve reference to property definition 'ARINC653::HM_Module_Recovery_Actions'.
39. /CaseProject/modified_model.aadl | line 190: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Code_Memory'. For classifier references use classifier( <ref> ).
40. /CaseProject/modified_model.aadl | line 190: Couldn't resolve reference to property definition 'ARINC653::Memory_Type'.
41. /CaseProject/modified_model.aadl | line 196: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Code_Memory'. For classifier references use classifier( <ref> ).
42. /CaseProject/modified_model.aadl | line 196: Couldn't resolve reference to property definition 'ARINC653::Memory_Type'.
