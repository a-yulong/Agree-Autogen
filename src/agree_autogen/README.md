# Runtime Package

The package contains the implementation used by the released pipeline.

```text
agree_autogen/
  case_runner.py              Benchmark case loading and AADL dependency collection
  refactor/
    agents.py                 Model analyst, requirement analyst, generator, fusion, and repair agents
    orchestrator.py           Stage orchestration and report generation
    rag_bundle.py             Three-source retrieval and post-retrieval digest support
    validation.py             AADL Inspector and standalone AGREE validator integration
  metrics/                    Aggregate metrics and error taxonomy helpers
  validators/                 Thin wrappers around validation tools
```

The default benchmark root is `data/benchmark/cases`. Runtime paths can be overridden with environment variables such as `AGREE_SOURCE_ROOT`, `AGREE_RESULT_ROOT`, `AGREE_DOCS_DIR`, `AGREE_MODEL_BASE_URL`, `AGREE_MODEL_API_KEY`, and `AGREE_MODEL_NAME`.
