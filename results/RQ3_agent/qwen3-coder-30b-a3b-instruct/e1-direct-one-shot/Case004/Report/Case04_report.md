# Case04 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 587.72
- Initial validation errors: 27
- Final validation errors: 27

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 27
- Warnings: 8

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 2521
- completion_tokens: 5712
- total_tokens: 8233

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 12: Couldn't resolve reference to DataSubcomponentType 'real'.
2. /CaseProject/modified_model.aadl | line 13: Couldn't resolve reference to DataSubcomponentType 'real'.
3. /CaseProject/modified_model.aadl | line 15: Couldn't resolve reference to DataSubcomponentType 'bool'.
4. /CaseProject/modified_model.aadl | line 16: Couldn't resolve reference to DataSubcomponentType 'bool'.
5. /CaseProject/modified_model.aadl | line 17: Couldn't resolve reference to DataSubcomponentType 'bool'.
6. /CaseProject/modified_model.aadl | line 22: Couldn't resolve reference to SystemSubcomponentType 'GCAS_singleton'.
7. /CaseProject/modified_model.aadl | line 23: Couldn't resolve reference to SystemSubcomponentType 'TCAS_singleton'.
8. /CaseProject/modified_model.aadl | line 26: Couldn't resolve reference to SystemSubcomponentType 'Supervisor'.
9. /CaseProject/modified_model.aadl | line 29: Couldn't resolve reference to ConnectionEnd 'gcas_timeToRecovery'.
10. /CaseProject/modified_model.aadl | line 29: Couldn't resolve reference to ConnectionEnd 'timeToRecovery'.
11. /CaseProject/modified_model.aadl | line 30: Couldn't resolve reference to ConnectionEnd 'tcas_timeToRecovery'.
12. /CaseProject/modified_model.aadl | line 30: Couldn't resolve reference to ConnectionEnd 'timeToRecovery'.
13. /CaseProject/modified_model.aadl | line 31: Couldn't resolve reference to ConnectionEnd 'geof_timeToRecovery'.
14. /CaseProject/modified_model.aadl | line 33: Couldn't resolve reference to ConnectionEnd 'gcas_timeToFailure'.
15. /CaseProject/modified_model.aadl | line 33: Couldn't resolve reference to ConnectionEnd 'timeToFailure'.
16. /CaseProject/modified_model.aadl | line 34: Couldn't resolve reference to ConnectionEnd 'tcas_timeToFailure'.
17. /CaseProject/modified_model.aadl | line 34: Couldn't resolve reference to ConnectionEnd 'timeToFailure'.
18. /CaseProject/modified_model.aadl | line 35: Couldn't resolve reference to ConnectionEnd 'geof_timeToFailure'.
19. /CaseProject/modified_model.aadl | line 37: Couldn't resolve reference to ConnectionEnd 'timeToFailure'.
20. /CaseProject/modified_model.aadl | line 38: Couldn't resolve reference to ConnectionEnd 'timeToRecovery'.
21. /CaseProject/modified_model.aadl | line 40: Couldn't resolve reference to ConnectionEnd 'p1'.
22. /CaseProject/modified_model.aadl | line 41: Couldn't resolve reference to ConnectionEnd 'p2'.
23. /CaseProject/modified_model.aadl | line 42: Couldn't resolve reference to ConnectionEnd 'p3'.
24. /CaseProject/modified_model.aadl | line 47: Couldn't resolve reference to DataSubcomponentType 'real'.
25. /CaseProject/modified_model.aadl | line 48: Couldn't resolve reference to DataSubcomponentType 'real'.
26. /CaseProject/modified_model.aadl | line 52: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@60dcf9ec{platform:/resource/CaseProject/modified_model.aadl#aviation.aviation_public.GeoFence_singleton.impl.agree}' must be set
27. /CaseProject/modified_model.aadl | line 52: mismatched character '<EOF>' expecting '*'
