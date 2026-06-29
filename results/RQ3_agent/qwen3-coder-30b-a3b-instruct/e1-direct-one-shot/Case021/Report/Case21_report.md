# Case21 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 51.47
- Initial validation errors: 61
- Final validation errors: 61

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 61
- Warnings: 1

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 1065
- completion_tokens: 829
- total_tokens: 1894

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 17: missing ';' at 'cooler_on'
2. /CaseProject/modified_model.aadl | line 30: Couldn't resolve reference to property definition 'AGREE::Initial_Value'.
3. /CaseProject/modified_model.aadl | line 31: Couldn't resolve reference to property definition 'AGREE::Next_Value'.
4. /CaseProject/modified_model.aadl | line 31: The required feature 'ownedValue' of 'org.osate.aadl2.impl.ModalPropertyValueImpl@7b8b755d{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.5/@ownedPropertyAssociation.1/@ownedValue.0}' must be set
5. /CaseProject/modified_model.aadl | line 32: Couldn't resolve reference to property definition 'if'. Property set name may be missing.
6. /CaseProject/modified_model.aadl | line 32: Couldn't resolve reference to property definition 'k'. Property set name may be missing.
7. /CaseProject/modified_model.aadl | line 32: Couldn't resolve reference to property definition 'prev'. Property set name may be missing.
8. /CaseProject/modified_model.aadl | line 32: Couldn't resolve reference to property definition 'then'. Property set name may be missing.
9. /CaseProject/modified_model.aadl | line 32: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@12f8682a{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.5/@ownedPropertyAssociation.5}' with 0 values must have at least 1 values
10. /CaseProject/modified_model.aadl | line 32: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@31b6b0c7{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.5/@ownedPropertyAssociation.3}' with 0 values must have at least 1 values
11. /CaseProject/modified_model.aadl | line 32: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@5d01b0d8{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.5/@ownedPropertyAssociation.2}' with 0 values must have at least 1 values
12. /CaseProject/modified_model.aadl | line 32: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@7d1cb59f{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.5/@ownedPropertyAssociation.4}' with 0 values must have at least 1 values
13. /CaseProject/modified_model.aadl | line 32: mismatched character ' ' expecting '>'
14. /CaseProject/modified_model.aadl | line 32: no viable alternative at character '>'
15. /CaseProject/modified_model.aadl | line 32: no viable alternative at input '('
16. /CaseProject/modified_model.aadl | line 32: no viable alternative at input ')'
17. /CaseProject/modified_model.aadl | line 33: Couldn't resolve reference to property definition 'k'. Property set name may be missing.
18. /CaseProject/modified_model.aadl | line 33: Couldn't resolve reference to property definition 'prev'. Property set name may be missing.
19. /CaseProject/modified_model.aadl | line 33: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@5613247e{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.5/@ownedPropertyAssociation.7}' with 0 values must have at least 1 values
20. /CaseProject/modified_model.aadl | line 33: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@7752c0e7{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.5/@ownedPropertyAssociation.6}' with 0 values must have at least 1 values
21. /CaseProject/modified_model.aadl | line 33: no viable alternative at input '('
22. /CaseProject/modified_model.aadl | line 33: no viable alternative at input ')'
23. /CaseProject/modified_model.aadl | line 33: no viable alternative at input 'prev'
24. /CaseProject/modified_model.aadl | line 34: Couldn't resolve reference to property definition 'else'. Property set name may be missing.
25. /CaseProject/modified_model.aadl | line 34: Couldn't resolve reference to property definition 'if'. Property set name may be missing.
26. /CaseProject/modified_model.aadl | line 34: Couldn't resolve reference to property definition 'k'. Property set name may be missing.
27. /CaseProject/modified_model.aadl | line 34: Couldn't resolve reference to property definition 'prev'. Property set name may be missing.
28. /CaseProject/modified_model.aadl | line 34: Couldn't resolve reference to property definition 'then'. Property set name may be missing.
29. /CaseProject/modified_model.aadl | line 34: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@1c171746{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.5/@ownedPropertyAssociation.9}' with 0 values must have at least 1 values
30. /CaseProject/modified_model.aadl | line 34: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@4e8d9bb6{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.5/@ownedPropertyAssociation.12}' with 0 values must have at least 1 values
31. /CaseProject/modified_model.aadl | line 34: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@586737ff{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.5/@ownedPropertyAssociation.10}' with 0 values must have at least 1 values
32. /CaseProject/modified_model.aadl | line 34: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@685e6a68{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.5/@ownedPropertyAssociation.11}' with 0 values must have at least 1 values
33. /CaseProject/modified_model.aadl | line 34: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@9e50283{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.5/@ownedPropertyAssociation.8}' with 0 values must have at least 1 values
34. /CaseProject/modified_model.aadl | line 34: mismatched character '=' expecting '-'
35. /CaseProject/modified_model.aadl | line 34: no viable alternative at input '('
36. /CaseProject/modified_model.aadl | line 34: no viable alternative at input ')'
37. /CaseProject/modified_model.aadl | line 34: no viable alternative at input 'if'
38. /CaseProject/modified_model.aadl | line 35: Couldn't resolve reference to property definition 'k'. Property set name may be missing.
39. /CaseProject/modified_model.aadl | line 35: Couldn't resolve reference to property definition 'prev'. Property set name may be missing.
40. /CaseProject/modified_model.aadl | line 35: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@2673487b{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.5/@ownedPropertyAssociation.13}' with 0 values must have at least 1 values
41. /CaseProject/modified_model.aadl | line 35: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@ff5d4f1{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.5/@ownedPropertyAssociation.14}' with 0 values must have at least 1 values
42. /CaseProject/modified_model.aadl | line 35: no viable alternative at input '('
43. /CaseProject/modified_model.aadl | line 35: no viable alternative at input ')'
44. /CaseProject/modified_model.aadl | line 35: no viable alternative at input 'prev'
45. /CaseProject/modified_model.aadl | line 36: Couldn't resolve reference to property definition 'else'. Property set name may be missing.
46. /CaseProject/modified_model.aadl | line 36: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@254e9709{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.5/@ownedPropertyAssociation.15}' with 0 values must have at least 1 values
47. /CaseProject/modified_model.aadl | line 37: Couldn't resolve reference to property definition 'k'. Property set name may be missing.
48. /CaseProject/modified_model.aadl | line 37: Couldn't resolve reference to property definition 'prev'. Property set name may be missing.
49. /CaseProject/modified_model.aadl | line 37: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@147c00aa{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.5/@ownedPropertyAssociation.16}' with 0 values must have at least 1 values
50. /CaseProject/modified_model.aadl | line 37: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@4db728df{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.5/@ownedPropertyAssociation.17}' with 0 values must have at least 1 values
51. /CaseProject/modified_model.aadl | line 37: no viable alternative at input '('
52. /CaseProject/modified_model.aadl | line 37: no viable alternative at input ')'
53. /CaseProject/modified_model.aadl | line 37: no viable alternative at input 'prev'
54. /CaseProject/modified_model.aadl | line 38: Couldn't resolve reference to property definition 'endif'. Property set name may be missing.
55. /CaseProject/modified_model.aadl | line 38: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@74bdfa0b{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.5/@ownedPropertyAssociation.18}' with 0 values must have at least 1 values
56. /CaseProject/modified_model.aadl | line 39: Couldn't resolve reference to property definition 'endif'. Property set name may be missing.
57. /CaseProject/modified_model.aadl | line 39: The feature 'ownedValue' of 'org.osate.aadl2.impl.PropertyAssociationImpl@1c2096c6{platform:/resource/CaseProject/modified_model.aadl#/0/@ownedPublicSection/@ownedClassifier.5/@ownedPropertyAssociation.19}' with 0 values must have at least 1 values
58. /CaseProject/modified_model.aadl | line 39: no viable alternative at input ';'
59. /CaseProject/modified_model.aadl | line 39: no viable alternative at input 'endif'
60. /CaseProject/modified_model.aadl | line 40: Couldn't resolve reference to Property Constant, Property Definition, Enumeration or Unit literal 'k'. For classifier references use classifier( <ref> ).
61. /CaseProject/modified_model.aadl | line 40: Couldn't resolve reference to property definition 'AGREE::Output_Value'.
