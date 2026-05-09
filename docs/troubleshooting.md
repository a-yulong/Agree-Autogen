# Troubleshooting

## API key is missing

Set `AGREE_MODEL_API_KEY` or pass `--llm-api-key` to `run_case.py`.

For `scripts/run_files.py`, a missing key produces `report.json` with a configuration error. Use `--dry-run` to check inputs without a key.

## Validator path is wrong

Check:

- `AADL_INSPECTOR_PATH`
- `JAVA_HOME`
- `OSATE_HOME`
- `AGREE_VALIDATOR_ROOT`

Validator wrappers return `not_configured` when required paths are missing.

## RAG index is missing

If RAG is enabled, ensure `AGREE_DOCS_DIR` or the configured knowledge-base path exists and contains redistributable documents. For smoke tests, use `--no-rag`.

For direct-file runs, use `--disable-rag` to run without a knowledge-base index.

## AADL parsing failure

Check package names, `with` clauses, component declarations, feature declarations, connections, and `end` statements.

## LLM output is malformed

The pipeline rejects empty or incomplete outputs. Retry with a lower temperature or a stronger model, and inspect saved first-pass artifacts.

## Repair reaches maximum rounds

Inspect the initial diagnostics and final artifact. Common causes include missing dependencies, invalid scopes, unresolved identifiers, or type mismatches.

## Direct-file dry run fails

Check that `--requirement`, `--aadl`, and `--config` point to existing files. The dry-run report is written to `OUTPUT_DIR/dry_run_report.json` when the output directory can be created.
