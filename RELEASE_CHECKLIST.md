# Release Checklist

- [ ] `python -m compileall src experiments scripts tests` passes.
- [ ] `python -m pytest -q` passes.
- [ ] No `.env`, API keys, tokens, passwords, or local credentials are committed.
- [ ] Only selected research result records and numerical summaries are released. Private logs, vector stores, local caches, and compiled tool artifacts are excluded.
- [ ] README and docs match the current CLI behavior.
- [ ] `CITATION.cff` is current.
- [ ] License and third-party redistribution status are checked.
- [ ] Validator setup notes are accurate.
- [ ] Benchmark and knowledge-base redistribution status is documented.

