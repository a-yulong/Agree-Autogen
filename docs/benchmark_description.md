# Benchmark Description

Benchmark metadata should be recorded in CSV form. See `data/benchmark/metadata.example.csv`.

Recommended fields:

- `case_id`: unique case identifier.
- `case_type`: `reconstruction` or `generation`.
- `requirement_path`: path to the natural-language requirement.
- `aadl_path`: path to the base AADL model.
- `target_component`: target component or implementation.
- `data_source`: project-owned, public dataset, local dataset, or third-party source.
- `access_status`: included, local preparation, or external acquisition.
- `notes`: additional details.

## Case types

`reconstruction` cases have a known target logic or expected contract pattern.

`generation` cases are evaluated by validation results, manual review, or downstream formal-analysis criteria.

## Source tracking

For each case, record where the requirement and AADL model came from, how the target component was selected, and whether the files are included in the public artifact or prepared locally for a reproduction run.

