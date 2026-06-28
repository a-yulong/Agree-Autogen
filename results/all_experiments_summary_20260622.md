# AGREE-AutoGen Experiment Summary

Generated: 2026-06-22

All formal settings use 459 cases. `First pass` means successful with zero repair rounds. GPT-5.4 uses the Yunwu stable full rerun; the earlier provider-unstable run is excluded.

| RQ | Setting | Success / 459 | Success % | First pass / 459 | First pass % | Repair success | Stage error | Avg runtime s | Avg tokens |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| RQ1 | Qwen3-Coder-30B | 391 | 85.19 | 323 | 70.37 | 68 | 0 | 198.2 | 18,959 |
| RQ1 | Codestral-2508 | 367 | 79.96 | 211 | 45.97 | 156 | 0 | 181.3 | 23,076 |
| RQ1 | Llama-3.1-70B | 306 | 66.67 | 277 | 60.35 | 29 | 0 | 202.4 | 15,031 |
| RQ1 | Gemma-3-27B | 232 | 50.54 | 0 | 0.00 | 232 | 0 | 248.6 | 23,881 |
| RQ1 | GPT-5.4-high Yunwu stable | 406 | 88.45 | 372 | 81.05 | 34 | 0 | 240.5 | 45,561 |
| RQ2 | topk111 | 383 | 83.44 | 309 | 67.32 | 74 | 0 | 185.3 | 18,400 |
| RQ2 | topk333 baseline | 391 | 85.19 | 323 | 70.37 | 68 | 0 | 198.2 | 18,959 |
| RQ2 | topk555 | 390 | 84.97 | 317 | 69.06 | 73 | 0 | 185.2 | 20,472 |
| RQ2 | topk777 | 384 | 83.66 | 309 | 67.32 | 75 | 0 | 189.0 | 22,387 |
| RQ3 | direct-one-shot | 177 | 38.56 | 177 | 38.56 | 0 | 0 | 77.4 | 6,561 |
| RQ3 | no-model-analyst | 385 | 83.88 | 284 | 61.87 | 101 | 0 | 156.4 | 18,069 |
| RQ3 | no-requirement-analyst | 394 | 85.84 | 307 | 66.88 | 87 | 0 | 172.0 | 17,578 |
| RQ3 | no-dual-analysts | 393 | 85.62 | 290 | 63.18 | 103 | 0 | 152.8 | 16,284 |
| RQ4 | raw-rag-no-digest | 389 | 84.75 | 316 | 68.85 | 73 | 0 | 149.0 | 15,356 |
| RQ4 | no-agent-strategy-guidance | 374 | 81.48 | 321 | 69.93 | 53 | 0 | 153.9 | 13,729 |
| RQ4 | full-target-context | 388 | 84.53 | 268 | 58.39 | 120 | 0 | 235.0 | 31,796 |

## Main Findings

- RQ1: the stable GPT-5.4-high rerun ranks first in final success (406, 88.45%) and first-pass success (372, 81.05%). Qwen follows at 391 (85.19%).
- RQ2: balanced 3-3-3 retrieval is the best overall setting. Topk555 is nearly tied in final success but costs more tokens; topk777 adds cost without improving accuracy.
- RQ3: one-shot generation collapses to 177 successes. Removing the model analyst reduces final and first-pass performance. Removing requirement analysis or both analysts preserves final success through substantially more repair, while reducing first-pass success.
- RQ4: removing agent strategy guidance causes the largest final-success loss (374 vs. baseline 391). Raw RAG without digest is close to baseline. Full target context sharply lowers first-pass success and raises cost, with repair recovering much of the final accuracy.
