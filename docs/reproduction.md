# Reproduction

## Experiment Settings

| ID | Setting | Public script status |
| --- | --- | --- |
| E1 | Bare Model | Template |
| E2 | Full Framework | Connected to case-layout runner |
| E3 | NoRAG | Connected to case-layout runner |
| E4 | NoRepair | Template |
| E5 | No Model Analyst | Template |
| E6 | No Requirement Analyst | Template |
| E7 | No Dual Analysts | Template |

## Commands

```powershell
python experiments/run_e2_full_framework.py --start 1 --end 10 --letters A --result-root ./results
python experiments/run_ablation.py --setting E3 --start 1 --end 10 --letters A --result-root ./results
python experiments/compute_metrics.py --results-dir ./results --output ./results/metrics/metrics.csv
```

## Metrics

| Metric | Meaning |
| --- | --- |
| FVSR | Final Validation Success Rate |
| ZRR | Zero-Repair Rate |
| IEC | Initial Error Count |
| ARR | Average Repair Rounds |
| RRR | Rescue Rate |
| MFR | Multi-Round Failure Ratio |
| ART | Average Runtime |
| ATC | Average Token Consumption |

Full benchmark data is not bundled. Use `data/benchmark/metadata.example.csv` for metadata structure.

