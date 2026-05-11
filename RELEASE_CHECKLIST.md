# Release Checklist

- [ ] `python -m compileall src experiments scripts tests` passes.
- [ ] `python -m pytest -q` passes.
- [ ] No `.env`, API keys, tokens, passwords, or local credentials are committed.
- [ ] No generated outputs, logs, vector stores, caches, or compiled artifacts are committed.
- [ ] README and docs match the current CLI behavior.
- [ ] `CITATION.cff` is current.
- [ ] License and third-party redistribution status are checked.
- [ ] Validator setup notes are accurate.
- [ ] Benchmark and knowledge-base redistribution status is documented.

