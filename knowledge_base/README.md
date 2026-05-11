# Knowledge Base

This directory contains the public sample RAG knowledge base for AGREE-AutoGen.

The sample KB is intentionally small and project-owned. It is meant to make the artifact inspectable and runnable without redistributing standards text, official manuals, private notes, or license-unclear third-party content.

## Structure

- `manifest.yaml`: index of public KB files.
- `ksyn/`: toy AADL/AGREE syntax, scope, and temporal-pattern rules.
- `kexp/`: toy RequirementNL-LogicProp-CodeAGREE triples.
- `kdef/`: defensive heuristics and common error patterns.
- `sources/`: reconstruction notes for larger local KBs.

## Public Sample KB vs. Full Paper KB

The public sample KB documents the expected schema and contains redistributable seed entries. A full paper KB may contain additional project notes, validated examples, diagnostics, and locally available references. Materials that cannot be redistributed should remain outside this repository and be documented through metadata or reconstruction instructions.

## Entry Schema

Each rule or pattern should include:

- `id`
- `category`
- `description`
- `pattern` or `example`
- `notes`

Each exemplar triplet should include:

- `id`
- `category`
- `requirement_nl`
- `logic_prop`
- `code_agree`
- `notes`
