# Troubleshooting

## API key is missing

Set `AGREE_MODEL_API_KEY` or pass `--llm-api-key` to `run_case.py`.

## Validator path is wrong

Check:

- `AADL_INSPECTOR_PATH`
- `JAVA_HOME`
- `OSATE_HOME`
- `AGREE_VALIDATOR_ROOT`

Validator wrappers return `not_configured` when required paths are missing.

## RAG index is missing

If RAG is enabled, ensure `AGREE_DOCS_DIR` or the configured knowledge-base path exists and contains redistributable documents. For smoke tests, use `--no-rag`.

## AADL parsing failure

Check package names, `with` clauses, component declarations, feature declarations, connections, and `end` statements.

## LLM output is malformed

The pipeline rejects empty or incomplete outputs. Retry with a lower temperature or a stronger model, and inspect saved first-pass artifacts.

## Repair reaches maximum rounds

Inspect the initial diagnostics and final artifact. Common causes include missing dependencies, invalid scopes, unresolved identifiers, or type mismatches.

