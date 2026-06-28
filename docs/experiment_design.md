# Experiment Design

The experimental evaluation studies how model choice, retrieval support, agent decomposition, and optimization mechanisms affect AGREE contract generation. All experiments use the same reporting format so that per-case outcomes can be aggregated into success rates, first-pass success rates, repair behavior, validator failures, and stage-error counts.

## Dataset

Experiments are organized over case directories containing:

- an AADL architecture model;
- a natural-language requirement;
- case metadata;
- optional dependency files required by validation.

Each case produces a structured report. Aggregate metrics are computed from these reports rather than from completion markers alone.

## Common Outcome Categories

The evaluation distinguishes:

- **Success:** the generated and fused artifact passes the configured validation checks.
- **Validator failure:** the pipeline completed, but AADL/AGREE validation rejected the artifact.
- **Stage error:** the pipeline did not produce a complete report because an infrastructure or pipeline stage failed.
- **Missing report:** no valid per-case report exists for the expected case.

Validator failures are experimental outcomes. Missing reports and provider-related stage errors are execution issues and may be rerun according to the documented policy.

## RQ1: Model Comparison

RQ1 evaluates the effect of the base language model under a fixed AGREE-AutoGen workflow. The controlled variables include the benchmark cases, generation pipeline, validation policy, and metric computation.

Reported outputs should include:

- per-model case reports;
- aggregate success and failure counts;
- first-pass success counts;
- repair-round distributions;
- stage-error counts and rerun notes;
- final aggregate tables used by the paper.

This study supports claims about model capability under the same generation architecture.

## RQ2: Retrieval Configuration

RQ2 evaluates retrieval support for AGREE/AADL knowledge. It compares retrieval configurations while holding the model and pipeline fixed.

The comparison should report:

- number of completed reports per retrieval setting;
- success, validator failure, and stage-error counts;
- first-pass success rate;
- effect on repair usage;
- any missing or rerun cases.

Retrieval settings are part of the experimental configuration and should be reported with descriptive names in papers and documentation. Internal directory names may be kept in manifests for traceability.

## RQ3: Agent Ablation

RQ3 evaluates the contribution of agent decomposition. The ablation settings remove or simplify specific analysis stages while preserving the same benchmark and validation policy.

The study focuses on the following capabilities:

- direct generation without staged analysis;
- generation without architecture analysis;
- generation without requirement analysis;
- generation without both analysis stages.

Reported metrics should show how each capability affects grounding, first-pass success, repair usage, and final validation outcomes.

## RQ4: Optimization Ablation

RQ4 evaluates optimization mechanisms inside the full workflow. The study isolates how retrieval digestion, agent strategy guidance, and target-context expansion affect generation and validation.

The comparison should report:

- full workflow baseline;
- generation using raw retrieval context without digest compression;
- generation without higher-level agent strategy guidance;
- generation with expanded target context;
- aggregate and per-case metrics for each setting.

The goal is to measure which optimization mechanisms improve grounded and validator-acceptable AGREE generation.

## Metrics

The standard metrics are:

- total expected cases;
- completed reports;
- successful cases;
- validator failures;
- stage errors;
- missing reports;
- first-pass successes;
- successes after repair;
- repair-round distribution;
- selected error-type categories when available.

Metrics should be computed by scripts from per-case JSON reports. Manual counting from console logs should be avoided.

## Rerun Policy

Reruns are limited to cases affected by missing reports or infrastructure-stage failures such as provider errors, quota interruptions, timeouts, or empty responses. Ordinary validator failures remain part of the experimental result unless the experiment design explicitly calls for a separate recovery study.

All reruns should be documented with:

- affected case numbers;
- reason for rerun;
- original status;
- final status;
- script used to rerun.

## Reporting Requirements

Each experiment directory should contain or link to:

- per-case reports;
- aggregate summaries;
- configuration files;
- model and provider metadata;
- retrieval settings;
- rerun notes;
- checksums for released result archives.

This structure makes the reported tables traceable to the underlying case-level artifacts.
