# Pipeline

AGREE-AutoGen is organized as a validation-centered multi-agent workflow.

## Model Analyst Agent

Input:

- AADL architecture model.
- Optional related AADL packages.

Output:

- Component hierarchy.
- Interfaces, port names, directions, and data types.
- Data-flow relations.
- Valid AGREE scopes.

## Requirement Analyst Agent

Input:

- Natural-language requirement.
- Architecture representation.

Output:

- Atomic functional units.
- Candidate assumptions and guarantees.
- Grounded AADL identifiers.
- Unresolved terms.

## AGREE Generator Agent

Input:

- Atomic requirements.
- Architecture representation.
- Retrieved knowledge snippets when RAG is enabled.

Output:

- AGREE clauses grounded in the AADL architecture.

## Model Fusion Agent

Input:

- Original AADL model.
- Generated AGREE clauses.
- Target component and valid scopes.

Output:

- Complete fused AADL+AGREE artifact.

## Validation-and-Repair Agent

Input:

- Fused artifact.
- AADL Inspector diagnostics.
- Standalone AGREE validator diagnostics.
- Previous repair history.

Output:

- Complete repaired AADL+AGREE artifact.

The repair loop runs until zero validation errors or the configured maximum number of repair rounds is reached.

## RAG knowledge injection

When enabled, retrieval augments generation and repair prompts with project-owned or redistributable knowledge from:

- `Ksyn`: syntax and semantic rules.
- `Kexp`: verified examples.
- `Kdef`: defensive heuristics.

