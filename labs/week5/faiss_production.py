"""
Week 5 — FAISS production mini-lab: build, persist, benchmark.

Run:
  python -m labs.week5.faiss_production

Requires: numpy, faiss-cpu (see requirements.txt)
"""
from __future__ import annotations

import json
import os
import tempfile
import time
from pathlib import Path

import numpy as np

try:
    import faiss
except ImportError as e:
    raise SystemExit("Install faiss-cpu: pip install faiss-cpu") from e


def make_random_vectors(n: int, dim: int, seed: int = 42) -> np.ndarray:
    rng = np.random.default_rng(seed)
    x = rng.standard_normal((n, dim)).astype("float32")
    faiss.normalize_L2(x)
    return x


def build_flat_ip_index(vectors: np.ndarray) -> faiss.Index:
    dim = vectors.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(vectors)
    return index


def benchmark_queries(index: faiss.Index, queries: np.ndarray, k: int = 10, rounds: int = 3) -> dict:
    latencies_ms: list[float] = []
    for _ in range(rounds):
        t0 = time.perf_counter()
        _ = index.search(queries, k)
        latencies_ms.append((time.perf_counter() - t0) * 1000)
    arr = np.array(latencies_ms)
    return {"p50_ms": float(np.percentile(arr, 50)), "p95_ms": float(np.percentile(arr, 95))}


def main() -> None:
    n_vec, dim, n_q = 10_000, 128, 256
    vectors = make_random_vectors(n_vec, dim)
    queries = make_random_vectors(n_q, dim)

    index = build_flat_ip_index(vectors)

    stats = benchmark_queries(index, queries)
    out_dir = Path(tempfile.mkdtemp(prefix="faiss_lab_"))
    index_path = out_dir / "index.faiss"
    faiss.write_index(index, str(index_path))

    meta = {
        "n_vectors": n_vec,
        "dim": dim,
        "index_path": str(index_path),
        "benchmark": stats,
        "note": "Swap IndexFlatIP with IndexHNSWFlat for larger corpora (tune M, efConstruction).",
    }
    print(json.dumps(meta, indent=2))
    print(f"Index bytes on disk: {index_path.stat().st_size}")


if __name__ == "__main__":
    main()
