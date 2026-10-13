# Hybrid GNN–LLM Model for Fake Review and Misinformation Detection

**Repository:** https://github.com/suprajachiru/Hybrid-GNN-LLM-Reproducibility

This repository accompanies the manuscript **“Hybrid GNN–LLM Model for Fake Review and Misinformation Detection.”** It contains the available Python/Colab prototype, dataset acquisition guidance, result tables, metric visualizations, and utilities for recording real execution time.

> **Important result distinction:** The top-level `results/` tables and figures now show the manuscript-reported metrics only: YelpCHI 94.8%, FakeNewsNet 93.4%, Amazon Reviews’23 (All Beauty) 95.1%, and 94.4% average accuracy as reported in Table 6. The lower-accuracy development experiments (including the user-reported 76.66% on 10,000 examples and a separate 76.80% YelpZip/MiniLM prototype result) are moved to `results/prototype_runs/` and are not the manuscript results. Paper metrics are transcribed from the manuscript and are **not independently reproduced** by this repository.

## Repository contents

- `notebooks/Full_Colab_Code_Fake_Review_Detection.ipynb` — dataset audit, preprocessing, baselines, GNN prototypes, and text/hybrid development steps.
- `src/full_colab_code_fake_review_detection.py` — Python implementation/scaffold.
- `requirements.txt` — required Python packages.
- `data/README.md` — dataset sources and labeling/access cautions.
- `results/manuscript_reported_metrics.csv` — manuscript Table 6 values and Table 4 dataset counts.
- `results/manuscript_ablation_results.csv` — manuscript Table 9 values.
- `results/manuscript_baseline_comparison.csv` — manuscript Table 7 baseline comparison.
- `results/prototype_runs/` — separate preliminary/prototype measurements, kept apart from manuscript-reported results.
- `results/figures/` — charts generated from reported/recorded metric tables.
- `scripts/plot_results.py` — regenerate metric charts from CSVs.
- `scripts/time_command.py` — measure an actual command's wall-clock time and plot logged execution durations.

## 1. Mandatory installation

### Google Colab

1. Open `notebooks/Full_Colab_Code_Fake_Review_Detection.ipynb` in Colab.
2. Upload or clone the repository. If cloned to `/content/Hybrid-GNN-LLM-Reproducibility`, run:

```python
%pip install -r /content/Hybrid-GNN-LLM-Reproducibility/requirements.txt
```

If the repository is stored elsewhere, change the path to the actual `requirements.txt` location. You can also upload `requirements.txt` to Colab and run `%pip install -r requirements.txt`.

3. Run notebook cells in order. Several cells use `/content/hybrid_gnn_llm` as their working directory; keep this path consistent or update all corresponding paths. Dataset acquisition and larger model steps may take substantial time and RAM.

### Local Python

Python 3.10 or 3.11 is recommended.

```bash
git clone https://github.com/suprajachiru/Hybrid-GNN-LLM-Reproducibility.git
cd Hybrid-GNN-LLM-Reproducibility
python -m venv .venv
```

Activate the environment:
- Windows PowerShell: `.venv\\Scripts\\Activate.ps1`
- macOS/Linux: `source .venv/bin/activate`

Then install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

For GPU use, install a PyTorch build compatible with your OS/CUDA version using the official PyTorch selector. Existing CSV plots can be regenerated without downloading datasets or training a model.

## 2. Dataset sizes reported in the manuscript

Manuscript Table 4 reports the following counts and a stratified 70:15:15 train/validation/test split:

| Dataset | Total | Train | Validation | Test |
|---|---:|---:|---:|---:|
| YelpCHI | 67,395 | 47,177 | 10,109 | 10,109 |
| FakeNewsNet | 23,196 | 16,237 | 3,480 | 3,479 |
| Amazon Reviews’23 (All Beauty) | 701,528 | 491,070 | 105,229 | 105,229 |

These are manuscript-reported counts, not independently verified by this package. See `data/README.md` for source links and restrictions. Do not redistribute raw datasets unless their terms permit it.

**Label caution:** Amazon Reviews’23 raw records do not inherently provide verified fake/genuine labels for every review. Do not invent binary labels from ratings or other fields.

## 3. Manuscript-reported accuracy and related metrics

Paper Table 6 reports:

| Dataset | Accuracy | Precision | Recall | F1-score | AUC |
|---|---:|---:|---:|---:|---:|
| YelpCHI | 94.8% | 93.6% | 92.9% | 93.2% | 0.972 |
| FakeNewsNet | 93.4% | 92.1% | 91.8% | 91.9% | 0.964 |
| Amazon Reviews’23 (All Beauty) | 95.1% | 94.2% | 93.7% | 93.9% | 0.978 |
| **Average (as reported)** | **94.4%** | **93.3%** | **92.8%** | **93.0%** | **0.971** |

Paper Table 9 reports these ablation results:

| Model variant | Accuracy | F1-score |
|---|---:|---:|
| Full model | 94.4% | 93.0% |
| Without GNN | 89.1% | 87.4% |
| Without LLM | 90.3% | 88.9% |
| Without structural features | 87.8% | 86.2% |
| Without semantic features | 88.6% | 87.0% |

These tables and associated charts are **transcribed/visualized from the manuscript**, not fresh training results. The average row is copied from the paper, not recalculated here.

### 10,000-example prototype

The user-reported 76.66% result and the separately recorded YelpZip/MiniLM prototype metrics are retained under `results/prototype_runs/` for traceability. They are different experiments, not the manuscript-reported three-dataset results, and must not be mixed into the main paper-result charts.

### Regenerate metric charts

```bash
python scripts/plot_results.py
```

This script regenerates charts from the CSVs. It does not train the model.

## 4. Real execution-time graphs

No verified per-epoch training timings or complete runtime trace from the paper experiments are included. **Runtime plots are generated only from measurements of commands you actually execute**—no synthetic times are bundled.

Example:

```bash
python scripts/time_command.py --label "yelpchi_baseline" -- python src/full_colab_code_fake_review_detection.py
```

The wrapper records timestamp, label, measured wall-clock seconds, and exit status in `results/runtime_measurements.csv`, then writes `results/figures/runtime_measurements.png`. Repeat with a different label for each actual run. Use a command that truly performs the workload you want to time; simply timing a script that exits without training does not measure training runtime.

For a notebook training cell, use:

```python
import time
start = time.perf_counter()
# Run the actual training/evaluation call here.
elapsed_seconds = time.perf_counter() - start
print(f"Measured execution time: {elapsed_seconds:.2f} seconds")
```

The runtime chart is absent until real measurements are recorded.

## 5. Reproducibility notes and limitations

- This repository provides the available notebook/prototype and supporting artifacts; it has **not been independently verified as an exact, end-to-end reproduction** of the complete three-dataset hybrid pipeline.
- The recorded 10K text experiment uses MiniLM, while the manuscript describes Llama 3.1 8B Instruct.
- The 10K YelpZip run, YelpCHI baseline experiments, and manuscript-reported results are separate experiments.
- Raw datasets, full model checkpoints, all embeddings, and complete run logs are not bundled.
- Do not claim the 94.4% average accuracy was reproduced unless a clean run regenerates it and configuration, data provenance, environment, and logs are retained.
- Results may vary with dataset version, label mapping, preprocessing, split seed, hardware, package versions, and model configuration.

## 6. Repository layout

```text
.
├── README.md
├── requirements.txt
├── .gitignore
├── data/README.md
├── notebooks/Full_Colab_Code_Fake_Review_Detection.ipynb
├── src/full_colab_code_fake_review_detection.py
├── scripts/
│   ├── plot_results.py
│   └── time_command.py
└── results/
    ├── README.md
    ├── manuscript_reported_metrics.csv
    ├── manuscript_ablation_results.csv
    ├── recorded_evaluation_metrics.csv
    ├── user_reported_10k_run.csv
    └── figures/
```

## 7. Reporting result provenance

Clearly label results as **manuscript-reported**, **recorded prototype**, or **newly measured/reproduced**. Do not describe manuscript-reported values as reproduced unless the experiments have actually been run and verified.
