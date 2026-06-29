# Data

This directory contains the benchmark inputs used by the released AGREE-AutoGen experiments.

```text
data/benchmark/
  cases/
    Case001/
      Case001_Base.aadl
      Case001_Base.txt
      Case001_Req.txt
      Case001_Req_Expected.json
    ...
    Case459/
  cases_manifest.csv
```

Each case contains an AADL model, the natural-language requirement, and the expected requirement-analysis reference used for inspection. Generated outputs are not mixed into this directory; experiment reports are written to a separate result root.

