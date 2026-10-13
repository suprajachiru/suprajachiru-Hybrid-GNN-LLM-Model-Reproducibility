#!/usr/bin/env python3
"""Regenerate charts from repository CSVs; this does not train models."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = RESULTS / "figures"
FIGURES.mkdir(parents=True, exist_ok=True)

metrics = pd.read_csv(RESULTS / "manuscript_reported_metrics.csv")
datasets = metrics[metrics["dataset"] != "Average"].copy()
metric_cols = [
    ("accuracy_percent_reported", "Accuracy (%)"),
    ("precision_percent_reported", "Precision (%)"),
    ("recall_percent_reported", "Recall (%)"),
    ("f1_percent_reported", "F1-score (%)"),
]
fig, ax = plt.subplots(figsize=(10, 5.5))
x = range(len(datasets))
width = 0.19
for i, (col, label) in enumerate(metric_cols):
    ax.bar([v + (i - 1.5) * width for v in x], datasets[col], width, label=label)
ax.set_xticks(list(x), datasets["dataset"], rotation=10, ha="right")
ax.set_ylabel("Reported score (%)")
ax.set_ylim(0, 100)
ax.set_title("Manuscript-reported performance by dataset")
ax.legend(ncol=2)
ax.grid(axis="y", alpha=.25)
fig.tight_layout()
fig.savefig(FIGURES / "manuscript_performance_metrics.png", dpi=180)
plt.close(fig)

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(datasets["dataset"], datasets["auc_reported"])
ax.set_ylabel("Reported AUC")
ax.set_ylim(0, 1.05)
ax.set_title("Manuscript-reported AUC by dataset")
ax.tick_params(axis="x", rotation=10)
ax.grid(axis="y", alpha=.25)
fig.tight_layout()
fig.savefig(FIGURES / "manuscript_auc.png", dpi=180)
plt.close(fig)

ab = pd.read_csv(RESULTS / "manuscript_ablation_results.csv")
fig, ax = plt.subplots(figsize=(10, 5.5))
x = range(len(ab))
w = .36
ax.bar([i-w/2 for i in x], ab["accuracy_percent_reported"], w, label="Accuracy")
ax.bar([i+w/2 for i in x], ab["f1_percent_reported"], w, label="F1-score")
ax.set_xticks(list(x), ab["model_variant"], rotation=15, ha="right")
ax.set_ylabel("Reported score (%)")
ax.set_ylim(0, 100)
ax.set_title("Manuscript-reported ablation results")
ax.legend()
ax.grid(axis="y", alpha=.25)
fig.tight_layout()
fig.savefig(FIGURES / "manuscript_ablation_accuracy_f1.png", dpi=180)
plt.close(fig)

baseline_path = RESULTS / "manuscript_baseline_comparison.csv"
if baseline_path.exists():
    baseline = pd.read_csv(baseline_path)
    fig, ax = plt.subplots(figsize=(10, 5.5))
    x = list(range(len(baseline)))
    width = .25
    for i, (col, label) in enumerate([
        ("accuracy_percent_reported", "Accuracy"),
        ("f1_percent_reported", "F1-score"),
    ]):
        bars = ax.bar([v + (i - .5) * width for v in x], baseline[col], width, label=label)
        ax.bar_label(bars, fmt="%.1f", padding=2, fontsize=8)
    ax.set_xticks(x, baseline["method"], rotation=18, ha="right")
    ax.set_ylabel("Reported score (%)")
    ax.set_ylim(0, 100)
    ax.set_title("Manuscript-reported baseline comparison (Table 7)")
    ax.legend()
    ax.grid(axis="y", alpha=.25)
    fig.tight_layout()
    fig.savefig(FIGURES / "manuscript_baseline_comparison.png", dpi=180)
    plt.close(fig)

runtime_csv = RESULTS / "runtime_measurements.csv"
runtime_png = FIGURES / "runtime_measurements.png"
if runtime_csv.exists():
    runtime = pd.read_csv(runtime_csv)
    if not runtime.empty and "elapsed_seconds" in runtime.columns:
        fig, ax = plt.subplots(figsize=(9, 5))
        ax.bar(runtime["label"], runtime["elapsed_seconds"])
        ax.set_ylabel("Measured wall-clock time (seconds)")
        ax.set_title("Measured command execution time (actual logged runs)")
        ax.tick_params(axis="x", rotation=15)
        ax.grid(axis="y", alpha=.25)
        fig.tight_layout()
        fig.savefig(runtime_png, dpi=180)
        plt.close(fig)
print(f"Charts saved to {FIGURES}")
if not runtime_csv.exists():
    print("No runtime graph created: run scripts/time_command.py on a real workload first.")
