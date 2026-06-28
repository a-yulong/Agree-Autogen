# Prompts

This directory contains the prompts used by AGREE-AutoGen agents. The prompts are part of the method: they define the responsibilities, boundaries, and output schemas of each stage in the pipeline.

## Prompt Roles

| Prompt | Role |
|---|---|
| `bare_direct.txt` | Direct generation baseline prompt. |
| `rag_digest.txt` | Converts retrieved knowledge into compact rules. |
| `model_analyst.txt` | Extracts architecture scope and target interface information. |
| `requirement_analyst.txt` | Converts natural-language requirements into semantic items. |
| `agree_generator.txt` | Generates candidate AGREE content from grounded inputs. |
| `model_fusion_target.txt` | Identifies the target owner for fusion. |
| `model_fusion_plan.txt` | Builds an insertion or replacement plan. |
| `model_fusion.txt` | Produces the fused AADL artifact. |
| `validation_repair_plan.txt` | Plans bounded repair from diagnostics. |
| `validation_repair_execute.txt` | Applies focused repair actions. |
| `validation_repair.txt` | General repair prompt for runner paths that use a single repair step. |

## Stage Boundaries

The prompts are designed to keep responsibilities separate:

- Model analysis extracts AADL facts and visible names; it does not interpret requirement intent.
- Requirement analysis produces semantic items; it does not generate AGREE syntax.
- Generation emits candidate AGREE clauses; it does not insert them into the AADL file.
- Fusion inserts generated content into the selected owner; it does not derive new requirement semantics.
- Repair acts on validator diagnostics; it does not restart unconstrained generation.

These boundaries are important for experiment interpretation because each ablation removes or modifies a defined capability rather than a hidden implementation detail.

## Output Discipline

Prompts should prefer structured outputs when downstream code parses them. They should also make the following constraints explicit:

- use only grounded AADL identifiers;
- avoid undeclared predicates and filler variables;
- preserve explicit numeric bounds and operators;
- keep assumptions and guarantees labeled;
- distinguish type-level contracts from implementation-level bindings;
- report blocked or partially grounded content rather than inventing missing model elements.

## Updating Prompts

Prompt changes can affect experiment results. Any release that modifies prompts should record:

- the changed prompt files;
- the experiment settings affected by the change;
- the date or version of the result set generated with those prompts;
- whether previously released metrics were recomputed.
