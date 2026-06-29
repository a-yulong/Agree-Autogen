# AGREE-AutoGen Experiment Summary

| RQ | Model | Setting | Cases | Success | Fail | Success rate | First-pass | Stage errors |
|---|---|---|---|---|---|---|---|---|
| RQ1_full_e2_rag_models | codestral-2508 | e2-full-rag | 459 | 367 | 92 | 79.96% | 211 | 8 |
| RQ1_full_e2_rag_models | gemma-3-27b-it | e2-full-rag | 459 | 232 | 227 | 50.54% | 0 | 129 |
| RQ1_full_e2_rag_models | gpt-5.4 | e2-full-rag | 459 | 88 | 371 | 19.17% | 86 | 367 |
| RQ1_full_e2_rag_models | llama-3.1-70b-instruct | e2-full-rag | 459 | 306 | 153 | 66.67% | 277 | 95 |
| RQ1_full_e2_rag_models | qwen3-coder-30b-a3b-instruct | e2-full-rag | 459 | 391 | 68 | 85.19% | 323 | 0 |
| RQ2_rag_topk | qwen3-coder-30b-a3b-instruct | e2-digest-topk111 | 459 | 383 | 76 | 83.44% | 309 | 0 |
| RQ2_rag_topk | qwen3-coder-30b-a3b-instruct | e2-digest-topk333-baseline-from-rq1 | 459 | 391 | 68 | 85.19% | 323 | 0 |
| RQ2_rag_topk | qwen3-coder-30b-a3b-instruct | e2-digest-topk555 | 459 | 390 | 69 | 84.97% | 317 | 0 |
| RQ2_rag_topk | qwen3-coder-30b-a3b-instruct | e2-digest-topk777 | 459 | 384 | 75 | 83.66% | 309 | 1 |
| RQ3_agent | qwen3-coder-30b-a3b-instruct | e1-direct-one-shot | 459 | 177 | 282 | 38.56% | 177 | 2 |
| RQ3_agent | qwen3-coder-30b-a3b-instruct | e5-no-model-analyst | 459 | 385 | 74 | 83.88% | 284 | 0 |
| RQ3_agent | qwen3-coder-30b-a3b-instruct | e6-no-requirement-analyst | 459 | 394 | 65 | 85.84% | 307 | 1 |
| RQ3_agent | qwen3-coder-30b-a3b-instruct | e7-no-dual-analysts | 459 | 393 | 66 | 85.62% | 290 | 0 |
| RQ4_optimization | qwen3-coder-30b-a3b-instruct | e2-full-target-context | 459 | 388 | 71 | 84.53% | 268 | 2 |
| RQ4_optimization | qwen3-coder-30b-a3b-instruct | e2-no-agent-strategy-guidance | 459 | 374 | 85 | 81.48% | 321 | 1 |
| RQ4_optimization | qwen3-coder-30b-a3b-instruct | e2-raw-rag-no-digest | 459 | 389 | 70 | 84.75% | 316 | 1 |
