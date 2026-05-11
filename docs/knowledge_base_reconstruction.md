# Knowledge-Base Reconstruction

The public KB contains toy-level entries for review and testing. Larger KBs should be reconstructed locally from materials that the user is allowed to use.

## Ksyn

Add project-owned syntax, scope, type, and temporal-pattern rules. Do not paste full standards or official manuals unless redistribution is permitted.

Required fields:

- `id`
- `category`
- `description`
- `pattern`
- `notes`

## Kexp

Add validated RequirementNL-LogicProp-CodeAGREE triples. Keep examples small and traceable.

Required fields:

- `id`
- `category`
- `requirement_nl`
- `logic_prop`
- `code_agree`
- `notes`

## Kdef

Add defensive rules and observed error patterns, preferably derived from project-owned diagnostics.

Required fields:

- `id`
- `category`
- `description`
- `pattern` or `example`
- `notes`

## Non-Redistributable Sources

For private or license-unclear resources, keep files outside the repository. Record source names, versions, access instructions, and license notes in local metadata only.
