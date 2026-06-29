# Case33 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 77.39
- Initial validation errors: 17
- Final validation errors: 17

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 17
- Warnings: 3

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 1806
- completion_tokens: 1759
- total_tokens: 3565

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 34: Couldn't resolve reference to SystemSubcomponentType 'ThreatDetection.impl'.
2. /CaseProject/modified_model.aadl | line 35: Couldn't resolve reference to SystemSubcomponentType 'ManeuverTemplates.impl'.
3. /CaseProject/modified_model.aadl | line 36: Couldn't resolve reference to SystemSubcomponentType 'ResponseSelection.impl'.
4. /CaseProject/modified_model.aadl | line 49: Couldn't resolve reference to ConnectionEnd 'altitude'.
5. /CaseProject/modified_model.aadl | line 50: Couldn't resolve reference to ConnectionEnd 'heading'.
6. /CaseProject/modified_model.aadl | line 51: Couldn't resolve reference to ConnectionEnd 'verticalVelocity'.
7. /CaseProject/modified_model.aadl | line 52: Couldn't resolve reference to ConnectionEnd 'nearestIntruderAltitude'.
8. /CaseProject/modified_model.aadl | line 53: Couldn't resolve reference to ConnectionEnd 'nearestIntruderGroundDistance'.
9. /CaseProject/modified_model.aadl | line 55: Couldn't resolve reference to ConnectionEnd 'threatDetected'.
10. /CaseProject/modified_model.aadl | line 57: Couldn't resolve reference to ConnectionEnd 'ownAltitude'.
11. /CaseProject/modified_model.aadl | line 58: Couldn't resolve reference to ConnectionEnd 'threatAltitude'.
12. /CaseProject/modified_model.aadl | line 60: Couldn't resolve reference to ConnectionEnd 'ownLongitude'.
13. /CaseProject/modified_model.aadl | line 61: Couldn't resolve reference to ConnectionEnd 'threatLongitude'.
14. /CaseProject/modified_model.aadl | line 63: Couldn't resolve reference to ConnectionEnd 'requiredVerticalVelocity'.
15. /CaseProject/modified_model.aadl | line 112: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@4c24f3a2{platform:/resource/CaseProject/modified_model.aadl#tcas.tcas_public.TrajectoryExtrapolation.impl.agree}' must be set
16. /CaseProject/modified_model.aadl | line 112: mismatched input '{' expecting RULE_ANNEXTEXT
17. /CaseProject/modified_model.aadl | line 146: mismatched character '<EOF>' expecting '''
