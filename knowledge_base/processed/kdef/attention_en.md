# AGREE Defensive Rule Notes

These notes provide defensive constraints for AGREE-AutoGen. They are used as Kdef knowledge and should be treated as hard constraints when generating or repairing AADL+AGREE artifacts.

## KDEF-1 Variable Declaration Rules

All internal variables used inside `annex agree {** ... **}` must be declared explicitly with `eq` and a type before use. Do not create isolated assignment-like statements that do not start with a legal AGREE construct such as `eq`, `const`, `assume`, `guarantee`, `assert`, or `assign`.

Do not redeclare AADL feature names with `eq`. Component ports are already visible to AGREE in the legal component scope. Re-declaring a port name creates a naming conflict.

If an auxiliary proposition is needed for a custom data type or domain concept, declare it explicitly in the appropriate annex before using it.

## KDEF-2 Type Alias and Package Reference Rules

Primitive aliases such as `int`, `real`, and `bool` must be declared at the AADL package level when the model uses them:

```aadl
data int extends Base_Types::Integer
end int;

data real extends Base_Types::Float
end real;

data bool extends Base_Types::Boolean
end bool;
```

Any use of a qualified name such as `Base_Types::Float` requires a matching `with Base_Types;` clause at the package level. AADL model references may use dot notation for subcomponent features, while package-qualified type or property references use `::`.

## KDEF-3 Annex Placement Rules

Declarative clauses such as `eq`, `const`, `assume`, and `guarantee` belong in the component type when they describe interface-level behavior. They should appear after features/properties and before `end <component>;`.

Implementation-oriented clauses such as `assign` belong in the matching component implementation, after subcomponents/connections and before `end <component.impl>;`.

Do not place `assume` clauses in component implementations unless the underlying AGREE syntax and scope explicitly allow it for the target context.

## KDEF-4 Assignment Rules

The left-hand side of an `assign` statement must already exist. It must be either an output feature or an auxiliary variable declared in the component type with `eq`. Do not use `assign` in an implementation to create a brand-new variable.

Do not define the same variable with both an initialized `eq` expression and an `assign` statement. If a value is defined in the type scope by `eq x : int = 5;`, do not assign `x` again in the implementation. If the implementation must assign it, use `eq x : int;` in the type scope and `assign x = 5;` in the implementation.

Use `=` for equality and assignment in AGREE expressions. Do not use `:=`.

## KDEF-5 Logical and Arithmetic Operators

Use AGREE logical operators: `and`, `or`, and `not (...)`. Do not use C/Java-style operators such as `&&`, `||`, or `!`.

Comparison operators such as `>`, `<`, `>=`, and `<=` return `bool`. Do not assign a boolean comparison result to a numeric variable unless the variable is typed as `bool`.

Both operands of arithmetic or comparison expressions should have compatible types.

Use `pre(x)` with parentheses. Do not write `pre x`.

## KDEF-6 Constants and State Recurrence

Fixed thresholds should be declared with `const`, for example:

```aadl
const low_altitude_threshold : real = 30.0;
const time_step : real = 0.001;
```

State recurrence based on `pre()` should be defined once with the `->` operator in a component type `eq` declaration, for example:

```aadl
eq t : real = 0.0 -> pre(t) + 1.0;
```

Do not put recurrence initialization in an `assume` clause or in an implementation-level `assign`.

## KDEF-7 Labels and Syntax Hygiene

Every `assume`, `guarantee`, `assert`, and `assign` label that requires a label must use a unique quoted string, for example:

```aadl
guarantee "safe after recovery": condition => response;
```

Do not introduce non-standard mathematical symbols or Unicode logic symbols. Use ASCII AGREE syntax.

AGREE does not support arbitrary built-in math-library functions such as `min`, `max`, `abs`, `sqrt`, or `sin` unless they are explicitly declared by a referenced node/library. Use explicit arithmetic or `if then else` logic when needed.

## KDEF-8 Requirement Logic Shape

Generated contracts should preserve a complete requirement chain: trigger condition, temporal or state constraint, and target behavior. Avoid overly abstract formulas that drop timing, state evolution, or the required response.

Use one-way implication `=>` in guarantees to express "if the condition holds, then the required result must hold". Do not use `<->` unless the requirement explicitly states a bidirectional equivalence.

AGREE does not support unsupported LTL liveness operators such as `eventually` in this validation setup. Prefer immediate safety-style properties over unsupported temporal constructs.

## KDEF-9 Structural Binding

Every AGREE variable must be grounded in the current AADL model, such as a feature, subcomponent output, declared auxiliary variable, or referenced package element. Do not introduce orphan variables or default values without a source.

Component-type annexes cannot directly reference implementation-only subcomponent paths unless those values are exposed through legal declarations and bindings. Bind subcomponent outputs through implementation-level assignments when needed.

Each `annex agree` block is scoped to the component declaration where it appears. An `eq` variable declared in a component type is not automatically visible from an unrelated implementation scope unless the language scope permits it.

When referencing a subcomponent port, the subcomponent implementation should contain at least an annex block if the validator requires AGREE context for that implementation.

## KDEF-10 Conditional Expressions

Branching logic must use nested `if ... then ... else` expressions. Do not use unsupported `elsif` syntax.

Example:

```aadl
assign selected = if cond1 then 1 else if cond2 then 2 else 3;
```
