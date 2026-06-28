# Results

This directory is reserved for released experiment results. Results should be organized so that aggregate metrics can be traced back to per-case reports.

## Recommended Layout

```text
results/
  aggregates/
    rq1_summary.csv
    rq2_summary.csv
    rq3_summary.csv
    rq4_summary.csv
  rq1/
    <setting>/
      Case001_report.json
      ...
  rq2/
  rq3/
  rq4/
  MANIFEST.csv
  SHA256SUMS.txt
```

Large result archives may be published as GitHub Release assets. In that case, this directory should still contain:

- aggregate tables;
- a manifest of released files;
- checksums;
- links to the release assets;
- notes describing how metrics were computed.

## Required Metadata

Each result suite should document:

- model name and provider interface;
- experiment setting;
- retrieval configuration;
- case range;
- expected case count;
- completed report count;
- rerun policy;
- aggregation script and command;
- generation or release date.

## Per-Case Reports

Per-case reports should be valid JSON files containing:

- case identifier;
- success or failure status;
- validation outcome;
- stage-error status when applicable;
- repair-round information when applicable;
- trace artifacts when available.

See `docs/result_schema.md` for field definitions and metric interpretation.

## Release Discipline

Results should not include:

- API keys or provider credentials;
- private service logs;
- console-only progress logs;
- process crash dumps;
- temporary rerun folders;
- generated caches.

Provider or quota interruptions should be summarized in release notes or rerun logs, not mixed into result tables as validation failures.
