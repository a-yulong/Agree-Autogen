# Artifact Evaluation Guide

This guide describes what the AGREE-AutoGen artifact supports and how reviewers or users can inspect it.

## Supported Claims

The artifact supports inspection of the following claims:

- the generation pipeline is decomposed into architecture analysis, requirement analysis, AGREE generation, model fusion, validation, and repair stages;
- prompts and configurations are available for inspection;
- retrieval knowledge sources and processed assets are available for audit;
- the standalone validator can be invoked outside the Python pipeline;
- per-case reports can be aggregated into experiment metrics;
- reported results can be traced to case-level artifacts when complete result archives are provided.

## Offline Checks

Users can inspect and run:

- Python unit and smoke tests;
- direct-file dry runs;
- retrieval index dry runs;
- prompt and configuration audits;
- result aggregation on released report files.

These checks do not require model-provider credentials.

## Validator Checks

With JDK and OSATE installed, users can invoke the standalone validator on bundled AADL examples or released generated artifacts. Validator reports are emitted as JSON and can be compared against case reports.

## Full Experiment Reruns

Full reruns require model-provider credentials and the same experiment configuration used for the released results. Exact byte-for-byte reproduction of LLM outputs is not guaranteed across provider revisions, but the scripts and stored reports support reproducible analysis of released artifacts.

## Expected Review Path

Recommended review order:

1. Read `README.md` and `ARTIFACT_SCOPE.md`.
2. Inspect `docs/architecture.md`.
3. Run offline tests from `docs/reproducibility.md`.
4. Run the dry-run example.
5. Configure JDK and OSATE, then run the validator check.
6. Inspect result schema and aggregate result files.
7. Recompute metrics from released per-case reports.

## Non-Goals

The artifact does not provide:

- API credentials;
- a bundled OSATE distribution;
- a guarantee that external model services will reproduce identical text;
- an automatic proof that generated contracts capture the full intent of every natural-language requirement;
- private run logs or local machine state.
