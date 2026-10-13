#!/usr/bin/env python3
"""Time a real command and append measured runtime to results/runtime_measurements.csv."""
from pathlib import Path
import argparse, csv, subprocess, time, datetime, sys

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = RESULTS / "figures"
CSV_PATH = RESULTS / "runtime_measurements.csv"

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--label", required=True, help="Short label for the workload, e.g. yelpchi_baseline")
    parser.add_argument("command", nargs=argparse.REMAINDER, help="Command to run after --")
    args = parser.parse_args()
    command = args.command
    if command and command[0] == "--":
        command = command[1:]
    if not command:
        parser.error("Supply a real command after --, for example -- python train.py")
    start_wall = datetime.datetime.now(datetime.timezone.utc).isoformat()
    start = time.perf_counter()
    result = subprocess.run(command, cwd=ROOT)
    elapsed = time.perf_counter() - start
    RESULTS.mkdir(parents=True, exist_ok=True)
    new_file = not CSV_PATH.exists()
    with CSV_PATH.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp_utc", "label", "elapsed_seconds", "exit_code", "command"])
        if new_file:
            writer.writeheader()
        writer.writerow({
            "timestamp_utc": start_wall,
            "label": args.label,
            "elapsed_seconds": round(elapsed, 4),
            "exit_code": result.returncode,
            "command": " ".join(command),
        })
    print(f"Measured elapsed time: {elapsed:.2f} seconds; exit code: {result.returncode}")
    # Regenerate charts, including the measured runtime plot.
    subprocess.run([sys.executable, str(ROOT / "scripts" / "plot_results.py")], cwd=ROOT, check=False)
    raise SystemExit(result.returncode)

if __name__ == "__main__":
    main()
