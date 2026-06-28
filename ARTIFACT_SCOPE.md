# Artifact Scope

AGREE-AutoGen is released as a research artifact for studying automated AGREE contract generation from natural-language requirements and AADL architecture models. The repository is intended to make the method, prompts, validation interface, knowledge sources, experiment configuration, and reported results inspectable and reusable.

The artifact is organized around reproducibility and auditability rather than as a snapshot of a local working directory. Files included in the repository should support at least one of the following purposes:

- explaining the system architecture;
- running the generation pipeline;
- validating AADL/AGREE artifacts;
- rebuilding or inspecting retrieval resources;
- reproducing experiment settings and metrics;
- auditing reported case-level and aggregate results.

## Included Components

The repository should include:

- source code for the AGREE-AutoGen pipeline;
- model, retrieval, validator, and experiment configuration files;
- prompts used by each agent in the generation workflow;
- the standalone AGREE syntax and semantic validation tool;
- static AADL/AGREE libraries required by the validator;
- curated domain knowledge sources and processed retrieval assets;
- public examples and lightweight smoke-test inputs;
- scripts for single-case execution, batch execution, reruns, and aggregation;
- complete experimental results or a documented release artifact containing them;
- tests and smoke checks that can run without private credentials.

## External Dependencies

Some dependencies are intentionally not bundled:

- OSATE and AGREE plugin installations;
- model-provider API credentials;
- provider-specific service state, routing policy, or account settings;
- local operating-system caches and IDE-generated files.

The validator and experiment runners should document how to connect to these dependencies through environment variables or command-line parameters. A repository consumer should be able to identify which steps are fully offline and which steps require external tools or model services.

## Excluded Material

The repository must not contain:

- real API keys, bearer tokens, account identifiers, or `.env` files;
- private service logs or model-provider response logs containing credentials;
- local run caches such as `__pycache__`, `.pytest_cache`, `.aadlbin-gen`, or IDE metadata;
- crash dumps, temporary replay logs, and ad-hoc debugging outputs;
- operating-system-specific absolute paths as required defaults;
- full third-party binary tool distributions when their license or size makes redistribution unsuitable.

Large or license-sensitive materials should be referenced through installation instructions or release assets rather than committed directly.

## Result Artifacts

Experiment results should be organized so that each reported number can be traced to case-level records. A complete result release should include:

- per-case reports;
- aggregate CSV or JSON summaries;
- the scripts used to compute metrics;
- checksums for large files;
- a schema describing the meaning of each result field;
- notes on provider failures, validation failures, and rerun policy.

If the complete result set is too large for the Git repository, it should be published as a GitHub Release or archival dataset, with the repository retaining summaries, manifests, and checksums.

## Reproducibility Levels

The artifact supports three levels of reproduction:

- **Offline inspection:** read the code, prompts, configurations, knowledge sources, and reported outputs without external services.
- **Local smoke execution:** run tests, dry runs, and validator checks using bundled examples and locally installed OSATE/JDK.
- **Full experimental execution:** rerun selected or complete experiment suites with configured model-provider credentials.

This distinction is part of the artifact boundary. It makes clear which claims can be checked locally and which require model-service access.
