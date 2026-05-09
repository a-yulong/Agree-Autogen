# Data Directory

This directory contains redistributable examples and benchmark metadata templates.

## Public examples

Small examples under `data/examples/` are intended for quick-start runs and documentation. They should be project-owned or explicitly redistributable.

## Benchmark data

Full benchmark inputs are not bundled by default. Place local benchmark sources under `data/Sources/` when running private experiments:

```text
data/Sources/Case01_A/Case01_Base.txt
data/Sources/Case01_A/Case01_Req.txt
data/Sources/Case01_A/Case01/*.aadl
```

Generated outputs are written to `results/` by default or to the path configured by `AGREE_RESULT_ROOT`.

## Third-party resources

Do not commit third-party standards, manuals, course materials, or repository snapshots unless redistribution is clearly allowed by their license. If a dataset cannot be redistributed, provide metadata and acquisition instructions instead.
