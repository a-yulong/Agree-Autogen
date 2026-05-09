# Troubleshooting

| Symptom | Likely cause | Action |
| --- | --- | --- |
| API key error | `AGREE_MODEL_API_KEY` is unset | Set model environment variables or run `scripts/run_files.py --dry-run`. |
| Validator reports `not_configured` | AADL Inspector, Java, OSATE, or validator root is missing | Set `AADL_INSPECTOR_PATH`, `JAVA_HOME`, `OSATE_HOME`, and `AGREE_VALIDATOR_ROOT`. |
| RAG index error | Knowledge-base path is absent or empty | Use `--disable-rag` for smoke runs or configure `AGREE_DOCS_DIR`. |
| AADL parsing failure | Invalid package, `with` clause, component, feature, connection, or `end` statement | Inspect the generated artifact and validator diagnostics. |
| LLM output malformed | Empty, partial, JSON-like, or non-AADL output | Inspect first-pass artifacts and retry with stricter prompts or a different model. |
| Repair limit reached | Missing dependencies, invalid scope, unresolved identifiers, or type mismatch | Review initial diagnostics and final artifact. |
| Direct-file dry run fails | Missing input or config path | Check `--requirement`, `--aadl`, `--config`, and output directory permissions. |

