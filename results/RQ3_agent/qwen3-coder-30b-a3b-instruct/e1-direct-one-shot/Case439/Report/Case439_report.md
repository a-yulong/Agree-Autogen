# Case439 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 61.69
- Initial validation errors: 6
- Final validation errors: 6

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 2
- AGREE errors: 4
- Warnings: 16

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 14128
- completion_tokens: 873
- total_tokens: 15001

## Final Diagnostics

1. autopilot_hard (identifier) is not a package or a property set visible or existing
2. Cannot analyze AADL specifications
3. /CaseProject/modified_model.aadl | line 35: Duplicate Element 'Tension' in PublicPackageSection 'autopilot_hard_public'
4. /CaseProject/modified_model.aadl | line 105: Duplicate Element 'Tension' in PublicPackageSection 'autopilot_hard_public'
5. /CaseProject/modified_model.aadl | line 112: The required feature 'sourceText' of 'org.osate.aadl2.impl.DefaultAnnexSubclauseImpl@2a04ab05{platform:/resource/CaseProject/modified_model.aadl#autopilot_hard.autopilot_hard_public.Tension.Impl.agree}' must be set
6. /CaseProject/modified_model.aadl | line 112: mismatched input '{' expecting RULE_ANNEXTEXT
