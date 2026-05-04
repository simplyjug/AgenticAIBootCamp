"""
Week 4 - Day 1: Embedding Math & Similarity

Demonstrates:
- Cosine similarity (normalized dot product)
- Dot product vs Euclidean distance
- L2 normalization for FAISS compatibility
"""
from __future__ import annotations

import math
from typing import List

import numpy as np

# Optional: SentenceTransformers for real embeddings
try:
    from sentence_transformers import SentenceTransformer
    HAS_ST = True
except ImportError:
    HAS_ST = False


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """
    Cosine similarity = (a · b) / (||a|| * ||b||)
    Range: [-1, 1]. 1 = identical direction.
    """
    dot = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return float(dot / (norm_a * norm_b))


def dot_product_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """
    Raw dot product. For normalized vectors, equals cosine similarity.
    FAISS IndexFlatIP uses dot product on L2-normalized vectors.
    """
    return float(np.dot(a, b))


def euclidean_distance(a: np.ndarray, b: np.ndarray) -> float:
    """
    L2 distance = ||a - b||
    For unit vectors: 2 - 2*cos(a,b), so smaller = more similar.
    """
    return float(np.linalg.norm(a - b))


def l2_normalize(v: np.ndarray) -> np.ndarray:
    """
    Normalize vector to unit length.
    Required for FAISS IndexFlatIP (inner product = cosine for unit vectors).
    """
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm


def embed_texts(texts: List[str], model_name: str = "all-MiniLM-L6-v2") -> np.ndarray:
    """
    Embed texts using SentenceTransformers.
    Returns numpy array of shape (n, dim) with L2-normalized vectors.
    """
    if not HAS_ST:
        # Random vectors for testing without sentence-transformers
        return np.random.randn(len(texts), 384).astype(np.float32)
    model = SentenceTransformer(model_name)
    embs = model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)
    return embs.astype(np.float32)


if __name__ == "__main__":
    texts = ["Machine learning", "Deep learning", "Weather forecast"]
    embs = embed_texts(texts)
    print("Cosine sim (0,1):", cosine_similarity(embs[0], embs[1]))
    print("Cosine sim (0,2):", cosine_similarity(embs[0], embs[2]))
