# Experiments

`settings.yaml` defines the E1-E7 experiment matrix. The public runner currently executes E2 and E3 through the case-layout batch runner.

```powershell
python experiments/run_experiment.py --setting E2 --benchmark data/Sources --output-dir outputs/e2 --start 1 --end 10 --letters A
python experiments/run_experiment.py --setting E3 --benchmark data/Sources --output-dir outputs/e3 --start 1 --end 10 --letters A
python experiments/compute_metrics.py --results-dir outputs/e2 --output outputs/e2/metrics.csv
```

Unsupported settings return `unsupported_in_public_runner` with the missing runtime switch rather than generating placeholder results.
