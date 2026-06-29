# Case367 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 51.95
- Initial validation errors: 6
- Final validation errors: 6

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 6
- Warnings: 3

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 4555
- completion_tokens: 2878
- total_tokens: 7433

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 98: Duplicate Element 'Interruption_Envoi_Servo.Elevator' in PublicPackageSection 'flyByWire_soft_public'
2. /CaseProject/modified_model.aadl | line 108: Duplicate Element 'Interruption_Envoi_Servo.Elevator' in PublicPackageSection 'flyByWire_soft_public'
3. /CaseProject/modified_model.aadl | line 108: mismatched input '.' expecting 'end'
4. /CaseProject/modified_model.aadl | line 110: Couldn't resolve reference to property definition 'AGREE::assumptions'.
5. /CaseProject/modified_model.aadl | line 113: Couldn't resolve reference to property definition 'AGREE::guarantees'.
6. /CaseProject/modified_model.aadl | line 116: mismatched input '.' expecting ';'
