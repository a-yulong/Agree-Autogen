# Known Limitations

AGREE-AutoGen is a research artifact for contract generation experiments. The repository is designed for inspection and reproducibility, but several boundaries should be considered when interpreting results or rerunning experiments.

## Model-Service Variability

Full generation depends on external model providers. Model revisions, routing policy, quota state, latency, and transient provider availability can affect outputs. Stored per-case reports and aggregate tables should be treated as the authoritative record for released results.

## Validation Environment

AADL and AGREE diagnostics can depend on OSATE, AGREE plugin, and JDK versions. The validator setup should record tool versions whenever results are released. Differences in diagnostic text do not necessarily imply a different semantic outcome, but they can affect repair prompts.

## Retrieval Assets

The knowledge base is curated for AGREE-AutoGen experiments. It is not a complete mirror of every AGREE or AADL reference document. Retrieval behavior depends on processed sources, chunking, embedding configuration, and digest prompts.

## Dataset Scope

Reported metrics apply to the released benchmark cases and configurations. They should not be interpreted as universal guarantees about all AADL models, all AGREE contracts, or all safety requirements.

## Validator Failures

A validator failure is an experimental outcome. It means the pipeline produced an artifact that did not pass configured validation. It should not be conflated with provider failure, missing output, or an incomplete run.

## Repair Scope

Validation-guided repair uses bounded edits from diagnostics. It is not a proof procedure and does not guarantee that every invalid artifact can be repaired within the configured repair budget.

## External Tool Distribution

OSATE and AGREE plugin installations are external dependencies. They are not bundled with the repository because of size and redistribution boundaries. The repository provides setup instructions and a standalone validator interface that connects to a local installation.
