# AADL Scope Notes

This Ksyn note summarizes AADL scope knowledge used by AGREE-AutoGen during architecture grounding and fusion. The AADL AS5506C standard is recorded as a local source through `raw/ksyn/AADL_AS5506C.local_source.md` and `local_sources.example.yaml`.

## Architecture Grounding

The authoritative source for component names, ports, directions, data types, subcomponents, and connections is the input AADL model. The Model Analyst Agent extracts this structure before AGREE generation and fusion.

## Component Type and Implementation Scope

AGREE assumptions and guarantees that refer to component ports should be placed in valid component type scopes. Implementation-level bindings should be placed in implementation scopes after relevant subcomponents and connections. Subcomponent ports should not be used in a component type contract unless represented through valid variables or outputs.

## Package and Feature References

AADL package references require matching `with` clauses. Generated AGREE code should not introduce package-qualified identifiers, data types, or property references that are absent from the analyzed model and its configured dependencies.
