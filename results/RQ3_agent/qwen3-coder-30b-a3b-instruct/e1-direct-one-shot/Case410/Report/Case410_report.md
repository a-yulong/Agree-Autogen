# Case410 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 68.87
- Initial validation errors: 41
- Final validation errors: 41

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 41
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
- completion_tokens: 1849
- total_tokens: 6900

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
31. /CaseProject/modified_model.aadl | line 176: Couldn't resolve reference to UnitLiteral 'ms'.
32. /CaseProject/modified_model.aadl | line 176: Couldn't resolve reference to property definition 'ARINC653::Partition_Slots'.
33. /CaseProject/modified_model.aadl | line 177: Couldn't resolve reference to property definition 'ARINC653::Slots_Allocation'.
34. /CaseProject/modified_model.aadl | line 178: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Power_Fail'. For classifier references use classifier( <ref> ).
35. /CaseProject/modified_model.aadl | line 178: Couldn't resolve reference to property definition 'ARINC653::HM_Errors'.
36. /CaseProject/modified_model.aadl | line 179: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Reset'. For classifier references use classifier( <ref> ).
37. /CaseProject/modified_model.aadl | line 179: Couldn't resolve reference to property definition 'ARINC653::HM_Module_Recovery_Actions'.
38. /CaseProject/modified_model.aadl | line 185: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Code_Memory'. For classifier references use classifier( <ref> ).
39. /CaseProject/modified_model.aadl | line 185: Couldn't resolve reference to property definition 'ARINC653::Memory_Type'.
40. /CaseProject/modified_model.aadl | line 191: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'Code_Memory'. For classifier references use classifier( <ref> ).
41. /CaseProject/modified_model.aadl | line 191: Couldn't resolve reference to property definition 'ARINC653::Memory_Type'.
