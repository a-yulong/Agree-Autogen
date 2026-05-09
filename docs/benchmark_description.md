# Benchmark Description

Benchmark metadata should be recorded in CSV form. See `data/benchmark/metadata.example.csv`.

Recommended fields:

- `case_id`: unique case identifier.
- `case_type`: `reconstruction` or `generation`.
- `requirement_path`: path to the natural-language requirement.
- `aadl_path`: path to the base AADL model.
- `target_component`: target component or implementation.
- `data_source`: project-owned, public dataset, private dataset, or third-party source.
- `license_status`: redistributable, private, unknown, or not redistributed.
- `notes`: additional details.

## Case types

`reconstruction` cases have a known target logic or expected contract pattern.

`generation` cases are evaluated by validation results, manual review, or downstream formal-analysis criteria.

## Third-party data

Do not redistribute license-unclear standards, manuals, benchmark files, or repository snapshots. If a case depends on such material, publish metadata and acquisition instructions instead.

