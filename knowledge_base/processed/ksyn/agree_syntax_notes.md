# AGREE Syntax Notes

This Ksyn note summarizes AGREE syntax and semantic knowledge used by AGREE-AutoGen. It is aligned with `raw/ksyn/AGREE_knowledge_dataset_en.pdf`, `raw/ksyn/AGREE_Users_Guide.pdf`, the Kdef rules, and the code examples in Kexp.

## Annex and Clause Structure

AGREE contracts are written inside `annex agree {** ... **};` blocks. Component type annexes are the normal location for assumptions, guarantees, constants, and equation declarations. Component implementation annexes are used for implementation-level bindings such as assignments when they are valid in that scope.

Common clause forms include:

- `assume "label": expression;`
- `guarantee "label": expression;`
- `eq name : type = expression;`
- `const name : type = value;`
- `assign output = expression;`

## Temporal and Expression Patterns

Stateful equations should use initialized temporal recurrence, for example `0.0 -> pre(t) + step`. Branching logic should use nested `if ... then ... else`. Generated contracts should use AGREE logical operators such as `and`, `or`, `not(...)`, and implication `=>`.

## Type and Reference Constraints

Generated expressions should preserve type consistency. Numeric variables should receive numeric expressions, Boolean variables should receive Boolean expressions, and package-qualified references should match imports and available model units. Helper functions should only be used when defined by the model or imported package.
