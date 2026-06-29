# Case157 Refactored Experiment Report

## Summary

- Setting: E1 (Bare Model)
- Final status: Fail
- Repair rounds: 0
- Runtime seconds: 52.34
- Initial validation errors: 2
- Final validation errors: 2

## Validation

- AADL Inspector executed: True
- AGREE validator executed: True
- AADL errors: 0
- AGREE errors: 2
- Warnings: 2

## Modules

- rag: False
- repair: False
- requirement_analyst: False
- model_analyst: False
- agree_generator: direct
- model_fusion: False

## Token Usage

- prompt_tokens: 1776
- completion_tokens: 1632
- total_tokens: 3408

## Final Diagnostics

1. /CaseProject/modified_model.aadl | line 119: Couldn't resolve reference to property definition 'AGREE::assumptions'.
2. /CaseProject/modified_model.aadl | line 122: Couldn't resolve reference to property definition 'AGREE::guarantees'.
