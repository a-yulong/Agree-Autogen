# Case250 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 154.24
- Initial validation errors: 19
- Final validation errors: 19

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 19
- Warnings: 1

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 3692
- completion_tokens: 3517
- total_tokens: 7209

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 197: Couldn't resolve reference to ThreadSubcomponentType 'doors_int.imp'.
2. /CaseProject/modified_model.aadl | line 233: Couldn't resolve reference to ConnectionEnd 'cll'.
3. /CaseProject/modified_model.aadl | line 236: Couldn't resolve reference to ConnectionEnd 'door2'.
4. /CaseProject/modified_model.aadl | line 237: Couldn't resolve reference to ConnectionEnd 'door1'.
5. /CaseProject/modified_model.aadl | line 284: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@5002fde9{platform:/resource/CaseProject/modified_model.aadl#DMS.DMS_public.door_handler.imp.agree}' must be set
6. /CaseProject/modified_model.aadl | line 284: mismatched input '{' expecting RULE_ANNEXTEXT
7. /CaseProject/modified_model.aadl | line 286: mismatched character ' ' expecting '>'
8. /CaseProject/modified_model.aadl | line 287: mismatched character ' ' expecting '>'
9. /CaseProject/modified_model.aadl | line 288: mismatched character ' ' expecting '>'
10. /CaseProject/modified_model.aadl | line 289: mismatched character ' ' expecting '>'
11. /CaseProject/modified_model.aadl | line 292: mismatched character ' ' expecting '>'
12. /CaseProject/modified_model.aadl | line 292: mismatched character '=' expecting '-'
13. /CaseProject/modified_model.aadl | line 292: no viable alternative at character '>'
14. /CaseProject/modified_model.aadl | line 295: mismatched character ' ' expecting '>'
15. /CaseProject/modified_model.aadl | line 295: mismatched character '=' expecting '-'
16. /CaseProject/modified_model.aadl | line 295: no viable alternative at character '>'
17. /CaseProject/modified_model.aadl | line 296: mismatched input 'package' expecting RULE_ID
18. /CaseProject/modified_model.aadl | line 297: extraneous input '}' expecting 'end'
19. /CaseProject/modified_model.aadl | line 298: mismatched input '.' expecting ';'
