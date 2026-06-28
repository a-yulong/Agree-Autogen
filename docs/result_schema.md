# Result Schema

AGREE-AutoGen reports are designed to make each case outcome auditable. A complete result artifact should include per-case JSON reports and aggregate CSV or JSON summaries computed from those reports.

Field names may vary slightly across experiment generations. This document defines the canonical interpretation used for analysis and publication.

## Case Identity

| Field | Meaning |
|---|---|
| `case_num` | Numeric case identifier. |
| `case_id` | String identifier if present. |
| `case_letter` | Case variant letter when the dataset contains multiple variants. |
| `setting` | Experiment setting or ablation label. |
| `model` | Model name used for generation. |
| `result_root` | Output directory for the suite or setting. |

## Outcome Fields

| Field | Meaning |
|---|---|
| `success` | `true` when the final artifact passes the configured validation checks. |
| `stage_error` | `true` when the pipeline did not complete because a stage failed. |
| `validation_status` | Final validator outcome when validation was reached. |
| `error_type` | Normalized failure category when available. |
| `stage` | Pipeline stage associated with a stage error or failure. |
| `message` | Human-readable diagnostic or status summary. |

Outcome interpretation:

- `success=true` is counted as a successful case.
- `success=false` with a completed validation report is counted as a validator failure.
- `stage_error=true` is counted separately from validator failure.
- missing report files are counted separately from completed reports.

## Repair Fields

| Field | Meaning |
|---|---|
| `first_pass_success` | The artifact passed validation before repair. |
| `repair_rounds` | Number of repair iterations attempted. |
| `repair_success` | The artifact failed initially and passed after repair. |
| `repair_actions` | Structured or textual repair actions when recorded. |
| `remaining_errors` | Diagnostics that remained after the repair budget was exhausted. |

Derived interpretation:

- first-pass success rate measures cases solved without iterative repair;
- repair success measures cases recovered by validation-guided repair;
- repair-round distribution measures how much validator feedback was required.

## Trace Fields

| Field | Meaning |
|---|---|
| `retrieved_context` | Raw or summarized retrieval material used by generation. |
| `rag_digest` | Compact retrieval digest passed to downstream agents. |
| `architecture_facts` | Model-analysis output such as visible symbols and target owner. |
| `requirement_items` | Requirement-analysis output such as semantic items and intent labels. |
| `generated_agree` | Candidate AGREE content before fusion. |
| `fusion_plan` | Target owner, content kind, and insertion operation. |
| `validation_report` | Structured validator diagnostics. |
| `final_artifact` | Final fused AADL/AGREE output path or content summary. |

Trace fields are used for qualitative inspection and ablation analysis. They should not be required for simple success-rate computation, but they should be retained when releasing complete experiment artifacts.

## Aggregate Metrics

Aggregate scripts should compute:

| Metric | Definition |
|---|---|
| `expected_cases` | Number of cases expected in the suite. |
| `completed_reports` | Number of parseable case reports containing a case identifier and outcome fields. |
| `success_count` | Number of completed reports with `success=true`. |
| `success_rate` | `success_count / expected_cases` or `success_count / completed_reports`, with denominator stated. |
| `first_pass_success_count` | Number of cases that passed before repair. |
| `first_pass_success_rate` | `first_pass_success_count / expected_cases` or documented denominator. |
| `validator_failure_count` | Completed reports that reached validation and failed. |
| `stage_error_count` | Reports marked as stage errors. |
| `missing_count` | Expected cases without a parseable report. |
| `repair_success_count` | Cases that passed after one or more repair rounds. |

Every published table should state its denominator. For full benchmark results, the preferred denominator is the expected number of cases. For partial progress reports, the denominator may be completed reports, but it must be labeled.

## Stage Errors and Reruns

Stage errors represent pipeline or infrastructure interruptions. Examples include:

- provider API errors;
- quota exhaustion;
- request timeouts;
- malformed or empty model responses;
- filesystem interruption;
- validator process launch failure.

Stage errors may be rerun when the experiment policy allows it. Validator failures should not be silently rerun as infrastructure failures.

## Recommended Release Files

A complete result release should contain:

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

Large releases may store per-case reports in a GitHub Release or archival dataset while keeping aggregate tables and manifests in the repository.
