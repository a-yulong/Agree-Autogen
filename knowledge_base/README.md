# Knowledge base

| Module | Content | Runtime cards |
| --- | --- | ---: |
| Ksyn | AGREE syntax, types, declarations, and AADL scope | 21 |
| Kexp | Contract examples and formalization patterns | 18 |
| Kdef | Generation and repair rules | 38 |

`raw/` contains the input documents. `processed/` contains the text and JSONL inputs read by the pipeline. `runtime_cards.jsonl` contains the cards loaded by `RagBundleBuilder`; `card_counts.json` contains their counts. Kexp contains 12 package examples, split into 18 runtime cards. Kdef contains 34 JSONL rules and four rules defined in `rag_bundle.py`.

The loader and retrieval code are in `src/agree_autogen/refactor/rag_bundle.py`. Recorded Case003 queries, candidates, selected cards, and digest are in `examples/recorded_case003/`.

Build the document corpus:

```powershell
python scripts/build_rag_index.py --knowledge-base knowledge_base --output knowledge_base/index
```
