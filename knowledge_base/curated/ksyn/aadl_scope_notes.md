# AADL Scope Notes

This Ksyn file records scope and placement guidance used by AGREE-AutoGen. Case-specific component names, ports, directions, and data types are extracted by the Model Analyst Agent from the input AADL model.

## Component Type Scope

Component type declarations expose features such as input and output ports. AGREE assumptions and guarantees that refer to component ports should be inserted into a valid component type scope.

## Component Implementation Scope

Component implementations contain subcomponents and connections. Implementation-level AGREE content should be used for bindings that are valid in that implementation context. Subcomponent ports should not be referenced from a component type guarantee unless they are first represented through valid variables or outputs.

## Package and Type References

AADL package references require matching `with` clauses. AGREE code should not introduce package-qualified identifiers that are absent from the AADL model or dependency set. Data types such as Boolean, Integer, and Float should match the available base types or project-defined aliases.

## Architecture Grounding

The static RAG corpus provides syntax and modeling guidance. The authoritative source for available identifiers is the current AADL input and the architecture representation produced during the run.
