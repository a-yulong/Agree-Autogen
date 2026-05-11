# Knowledge Source Inventory

AGREE-AutoGen uses retrieval material to ground contract synthesis, fusion, and repair in domain-specific AGREE/AADL knowledge. The public artifact records the source categories and local organization used by the framework.

## 1. AGREE Syntax and User Documentation

Role: `Ksyn`

Purpose:

- AGREE annex structure and clause forms.
- `assume`, `guarantee`, `eq`, and `assign` placement guidance.
- Type consistency and temporal-expression patterns.
- Common well-formedness constraints used during generation and repair.

Expected local directory:

```text
knowledge_base/curated/ksyn/
```

Public release status: source inventory and format examples are included. Project users can place prepared AGREE syntax notes, user-guide excerpts they are allowed to use, and locally curated rule summaries in this directory.

## 2. AADL Architecture and Scope Information

Role: architecture-aware grounding

Purpose:

- Component hierarchy and implementation relationships.
- Port names, directions, and data types.
- Valid AGREE scopes for component types and implementations.
- Data-flow relations used by the Model Fusion Agent.

Primary source:

- The input AADL architecture provided for each run.
- The Model Analyst Agent's structured analysis of that architecture.

Expected local directory for static modeling notes:

```text
knowledge_base/curated/ksyn/
```

Static KB material may include AADL modeling notes, but case-specific identifiers should come from the analyzed AADL input rather than from retrieval snippets.

## 3. Verified AGREE Examples

Role: `Kexp`

Purpose:

- RequirementNL-LogicProp-CodeAGREE alignment examples.
- In-context patterns for threshold properties, output implications, temporal state, and component-level contracts.
- Examples that demonstrate valid scope and identifier use.

Expected local directory:

```text
knowledge_base/curated/kexp/
```

Recommended preparation:

- Keep examples small and traceable.
- Record the source, component scope, input/output identifiers, and validation status.
- Normalize examples into concise text chunks or structured triplets before indexing.

## 4. Defensive Heuristic Rules

Role: `Kdef`

Purpose:

- Prevent common generation and repair failures.
- Capture rules such as label quotation, identifier grounding, scope-aware placement, package imports, and type consistency.
- Provide compact reminders for the AGREE Generator Agent and Validation-and-Repair Agent.

Expected local directory:

```text
knowledge_base/curated/kdef/
```

These rules are project-curated and can be maintained directly in the repository when they are written as original summaries.

## 5. Paper Benchmark-Specific Materials

The paper experiments may use a larger local KB containing additional curated examples, diagnostic summaries, and source documents. The public repository records the expected inventory and loading procedure, while the full local KB can be reconstructed by preparing the source categories above and pointing `AGREE_DOCS_DIR` to the prepared directory.
