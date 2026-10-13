# Results and provenance

The top-level result tables and figures in this folder reflect the uploaded manuscript only. Values are transcribed from Tables 4, 6, 7, and 9 and are labelled manuscript-reported; they have not been independently retrained or verified by this repository.

- `manuscript_reported_metrics.csv`: Table 6 metrics plus Table 4 dataset counts and split counts.
- `manuscript_ablation_results.csv`: Table 9 ablation metrics.
- `manuscript_baseline_comparison.csv`: Table 7 baseline comparison (accuracy, F1, AUC).
- `figures/`: regenerated charts from manuscript-reported tables only.
- `prototype_runs/`: separate, lower-accuracy development experiments and user-reported 10K run. These are not the paper's reported results and are deliberately separated to prevent confusion.
- `runtime_measurements.csv` and `figures/runtime_measurements.png` are created only after the timing wrapper records actual runs. No synthetic runtime values are included.

Do not label manuscript-reported values as independently reproduced. For a new run, record dataset version, sample count, model/configuration, split, environment, timestamp, and logs.
