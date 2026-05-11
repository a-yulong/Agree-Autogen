# AGREE Syntax Notes

This Ksyn file summarizes syntax and semantic constraints used by AGREE-AutoGen during generation and repair. It is derived from project-curated rules and examples, not from a verbatim standards copy.

## Annex Structure

AGREE contracts are placed inside `annex agree {** ... **};` blocks. Component type annexes are used for assumptions, guarantees, constants, and equation declarations. Component implementation annexes are used for implementation-level assignments and assertions when supported by the target model.

## Clause Forms

- `assume "label": expression;`
- `guarantee "label": expression;`
- `eq name : type = expression;`
- `const name : type = value;`
- `assign output = expression;`

Labels should be explicit and quoted. Generated identifiers should be grounded in the analyzed AADL architecture.

## Logic and Temporal Patterns

Use AGREE logical operators such as `and`, `or`, `not(...)`, implication `=>`, nested `if ... then ... else`, and initialized temporal recurrence such as `0.0 -> pre(t) + step`. Avoid assuming helper functions unless they are defined by the model or imported package.

## Type Discipline

Comparisons return Boolean values. Numeric variables should be assigned numeric expressions, and Boolean variables should be assigned Boolean expressions. Binary operators should combine compatible operand types.
