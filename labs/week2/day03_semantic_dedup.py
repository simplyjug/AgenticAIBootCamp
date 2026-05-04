"""
Week 2 - Day 3: Semantic Deduplication & Noise Reduction

Uses embedding similarity to cluster semantically duplicate documents.
Documents in same cluster with similarity > threshold are considered duplicates.
"""
from __future__ import annotations

from typing import List

# Optional: use sentence-transformers for embeddings
try:
    from sentence_transformers import SentenceTransformer
    HAS_ST = True
except ImportError:
    HAS_ST = False


def embed_texts(texts: List[str], model_name: str = "all-MiniLM-L6-v2") -> List[List[float]]:
    """
    Embed texts using SentenceTransformers.
    Returns list of 384-dim vectors (for all-MiniLM-L6-v2).
    """
    if not HAS_ST:
        raise ImportError("pip install sentence-transformers")
    model = SentenceTransformer(model_name)
    return model.encode(texts, convert_to_numpy=True).tolist()


def cosine_similarity(a: List[float], b: List[float]) -> float:
    """Compute cosine similarity between two vectors."""
    import math
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    return dot / (na * nb) if na and nb else 0.0


def cluster_by_similarity(
    texts: List[str],
    threshold: float = 0.92,
) -> List[List[int]]:
    """
    Cluster indices of texts that are semantically similar.
    Uses greedy clustering: first doc forms cluster; others join if sim > threshold.
    """
    if not texts:
        return []
    if not HAS_ST:
        # Fallback: no clustering
        return [[i] for i in range(len(texts))]

    embeddings = embed_texts(texts)
    n = len(texts)
    assigned = [-1] * n  # cluster id per doc
    clusters = []
    next_cluster = 0

    for i in range(n):
        if assigned[i] >= 0:
            continue
        assigned[i] = next_cluster
        cluster = [i]
        for j in range(i + 1, n):
            if assigned[j] >= 0:
                continue
            sim = cosine_similarity(embeddings[i], embeddings[j])
            if sim >= threshold:
                assigned[j] = next_cluster
                cluster.append(j)
        clusters.append(cluster)
        next_cluster += 1

    return clusters
