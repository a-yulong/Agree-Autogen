# Architecture

AGREE-AutoGen generates AGREE contracts by decomposing the task into constrained intermediate decisions. The pipeline does not rely on a single prompt to translate a requirement directly into an AADL annex. Instead, it preserves separate artifacts for retrieved rules, architecture scope, requirement intent, candidate clauses, fusion plans, validation diagnostics, and repair actions.

## Pipeline Overview

```text
Natural-language requirement
        +
AADL architecture
        |
        v
Retrieval-augmented knowledge support
        |
        v
Model Analyst  ---- architecture scope and target interface
        |
        v
Requirement Analyst ---- semantic requirement items
        |
        v
AGREE Generator ---- candidate AGREE clauses or annex
        |
        v
Model Fusion ---- owner-aware insertion plan
        |
        v
Validation Repair ---- bounded edits from validator diagnostics
        |
        v
Fused AADL+AGREE artifact and report
```

Each stage narrows the space of valid outputs. The architecture stage prevents references to invisible AADL names. The requirement stage avoids premature formalization. The generation stage restricts clauses to grounded operands and AGREE syntax. The fusion stage limits model changes to the intended owner. The repair stage acts on validator feedback rather than restarting unconstrained generation.

## Retrieval-Augmented Knowledge Support

The retrieval component supplies compact AGREE/AADL guidance to downstream agents. It uses three kinds of knowledge:

- syntax and scope rules for AGREE and AADL;
- verified example patterns;
- defensive rules that prevent common invalid outputs.

Retrieved material is converted into short digest rules before it is passed to agents. The digest form reduces example copying and keeps the generation prompt focused on constraints such as visible identifiers, labeled assumptions and guarantees, valid owner placement, and unsupported constructs.

## Model Analyst

The Model Analyst extracts architecture facts from the target AADL model. Its output describes what is visible in the target component context and how model elements are owned.

The stage distinguishes:

- component types and implementations;
- features, subcomponents, connections, and properties;
- candidate AGREE operands and non-expression structural facts;
- target interface profiles used by later generation and fusion stages.

This stage does not interpret requirement intent and does not generate AGREE clauses. Its role is to make model scope explicit before formalization begins.

## Requirement Analyst

The Requirement Analyst converts natural-language requirements into semantic items. It identifies behavioral obligations, input-side conditions, structural descriptions, property statements, and statements that require grounding against the architecture.

The output is not an AGREE formula. It is a set of formalization candidates with intent labels such as assumption, guarantee, or description. This separation helps the generator avoid inventing predicates when a requirement mentions a concept that is not visible in the target interface.

## AGREE Generator

The AGREE Generator is the first stage that emits AGREE syntax. It receives:

- semantic items from the Requirement Analyst;
- the target interface and visible identifiers from the Model Analyst;
- digest rules from retrieval;
- the original requirement and focused model context.

The generator must use visible operands, labeled assumptions or guarantees, and valid AGREE syntax. When a requirement is only partially grounded, the generator may emit a legal partial contract or block a clause instead of inventing missing identifiers.

## Model Fusion

The Model Fusion stage inserts generated AGREE content into the AADL model. It determines the target owner and operation, such as inserting or replacing an annex under a component type.

Fusion is owner-aware and local. It preserves unrelated model content and does not reinterpret the requirement. Its output records the selected owner, generated content kind, operation, and preserved artifacts.

## Validation Repair

The Validation Repair stage closes the loop with external diagnostics. It runs AADL/AGREE validation, reads focused errors, prepares a bounded repair plan, applies a minimal edit, and validates again.

Repair is not a second free-form generation pass. It is constrained by:

- validator diagnostics;
- the failed artifact;
- the target owner;
- the generated annex or fused model;
- a fixed repair budget.

The report records diagnostics, repair actions, validation status, and remaining failures.

## Artifact Traceability

Each case report is intended to support inspection after the run. A complete report may contain:

- original inputs;
- retrieved knowledge and digest rules;
- architecture facts;
- requirement semantic items;
- generated AGREE content;
- fusion decisions;
- validation diagnostics;
- repair plans and actions;
- final success or failure status.

This traceability is necessary for experiment analysis. It allows a reported success, validator failure, or stage error to be traced back to the artifacts that produced it.
