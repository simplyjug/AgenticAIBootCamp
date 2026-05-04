"""
Run all benchmarks for the bootcamp.
Usage: python benchmarks/run_all.py
"""
from __future__ import annotations

import json
import time
from pathlib import Path


def run_ingestion_benchmark():
    """Placeholder for ingestion benchmark."""
    print("Ingestion benchmark: (implement in benchmarks/ingestion_benchmark.py)")
    return {"status": "placeholder", "docs_per_sec": 0}


def main():
    results = {}
    print("Running benchmarks...")
    results["ingestion"] = run_ingestion_benchmark()
    out_path = Path(__file__).parent / "results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Results saved to {out_path}")


if __name__ == "__main__":
    main()
