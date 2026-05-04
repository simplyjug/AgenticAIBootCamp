"""
Week 4 - Day 4: FAISS Index Build — Flat, IVF, HNSW

Compares:
- IndexFlatIP: Exact search, O(n), no compression
- IndexIVFFlat: Approximate, cluster-based, faster for large n
- IndexHNSWFlat: Graph-based ANN, high recall, low latency
"""
from __future__ import annotations

import time
from typing import List, Tuple

import numpy as np

try:
    import faiss
    HAS_FAISS = True
except ImportError:
    HAS_FAISS = False


def build_flat_index(vectors: np.ndarray) -> "faiss.Index":
    """
    Build exact search index (IndexFlatIP).
    Uses inner product; vectors should be L2-normalized for cosine.
    """
    if not HAS_FAISS:
        raise ImportError("pip install faiss-cpu")
    d = vectors.shape[1]
    index = faiss.IndexFlatIP(d)
    faiss.normalize_L2(vectors)
    index.add(vectors)
    return index


def build_ivf_index(
    vectors: np.ndarray,
    nlist: int = 100,
    nprobe: int = 10,
) -> "faiss.Index":
    """
    Build IVF (Inverted File) index.
    nlist: number of clusters
    nprobe: number of clusters to search at query time (higher = more accurate, slower)
    """
    if not HAS_FAISS:
        raise ImportError("pip install faiss-cpu")
    d = vectors.shape[1]
    faiss.normalize_L2(vectors)
    quantizer = faiss.IndexFlatIP(d)
    index = faiss.IndexIVFFlat(quantizer, d, nlist, faiss.METRIC_INNER_PRODUCT)
    index.train(vectors)
    index.add(vectors)
    index.nprobe = nprobe
    return index


def build_hnsw_index(
    vectors: np.ndarray,
    M: int = 32,
    efConstruction: int = 200,
    efSearch: int = 128,
) -> "faiss.Index":
    """
    Build HNSW (Hierarchical Navigable Small World) index.
    M: number of connections per node
    efConstruction: size of dynamic candidate list during build
    efSearch: size of dynamic candidate list during search
    """
    if not HAS_FAISS:
        raise ImportError("pip install faiss-cpu")
    d = vectors.shape[1]
    faiss.normalize_L2(vectors)
    index = faiss.IndexHNSWFlat(d, M, faiss.METRIC_INNER_PRODUCT)
    index.hnsw.efConstruction = efConstruction
    index.hnsw.efSearch = efSearch
    index.add(vectors)
    return index


def benchmark_index(
    index,
    query_vectors: np.ndarray,
    k: int = 10,
    num_runs: int = 10,
) -> Tuple[List[float], np.ndarray]:
    """
    Measure search latency and return results.
    Returns (latencies_ms, distances).
    """
    faiss.normalize_L2(query_vectors)
    latencies = []
    for _ in range(num_runs):
        start = time.perf_counter()
        distances, indices = index.search(query_vectors, k)
        latencies.append((time.perf_counter() - start) * 1000)
    return latencies, distances


if __name__ == "__main__" and HAS_FAISS:
    np.random.seed(42)
    n, d = 10000, 384
    vectors = np.random.randn(n, d).astype(np.float32)
    faiss.normalize_L2(vectors)
    queries = np.random.randn(100, d).astype(np.float32)

    for name, idx in [
        ("Flat", build_flat_index(vectors)),
        ("IVF", build_ivf_index(vectors)),
        ("HNSW", build_hnsw_index(vectors)),
    ]:
        latencies, _ = benchmark_index(idx, queries)
        print(f"{name}: P50={np.median(latencies):.2f}ms")
