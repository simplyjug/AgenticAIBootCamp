"""
Week 2 - Day 2: Deduplication — MinHash, LSH, SimHash

Purpose:
- Remove exact and near-duplicate documents from datasets
- Use SimHash for fast near-duplicate detection (O(n) per doc)
- Use MinHash + LSH for scalable similarity search
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterator

import numpy as np


# =============================================================================
# SIMHASH - 64-bit fingerprint for near-duplicate detection
# Documents with Hamming distance < 3 are considered duplicates
# =============================================================================


def _tokenize(text: str, n: int = 3) -> list[str]:
    """
    Extract n-grams from text (shingles).
    n=3: "hello" -> ["hel", "ell", "llo"]
    Removes non-alphanumeric and lowercases.
    """
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text.lower())
    words = text.split()
    tokens = []
    for word in words:
        if len(word) >= n:
            for i in range(len(word) - n + 1):
                tokens.append(word[i : i + n])
        else:
            tokens.append(word)
    return tokens


def simhash(text: str, hash_bits: int = 64) -> int:
    """
    Compute SimHash fingerprint.
    Similar documents produce similar hashes (low Hamming distance).

    Algorithm:
    1. Tokenize text into n-grams
    2. Hash each token to hash_bits bits
    3. For each bit position: sum +1 if bit=1, -1 if bit=0 (weighted by token)
    4. Final fingerprint: bit i = 1 if sum > 0 else 0
    """
    tokens = _tokenize(text)
    if not tokens:
        return 0

    # Vector of size hash_bits; v[i] = sum of contributions to bit i
    v = np.zeros(hash_bits, dtype=np.int64)

    for token in tokens:
        # Hash token to integer, then to bit vector
        h = hash(token) & ((1 << hash_bits) - 1)
        for i in range(hash_bits):
            if (h >> i) & 1:
                v[i] += 1
            else:
                v[i] -= 1

    # Convert to fingerprint: 1 if v[i] > 0 else 0
    fingerprint = 0
    for i in range(hash_bits):
        if v[i] > 0:
            fingerprint |= 1 << i
    return fingerprint


def hamming_distance(a: int, b: int, bits: int = 64) -> int:
    """Count differing bits between two integers."""
    xor = a ^ b
    count = 0
    for _ in range(bits):
        count += xor & 1
        xor >>= 1
    return count


def is_near_duplicate(hash1: int, hash2: int, threshold: int = 3) -> bool:
    """True if Hamming distance <= threshold (default 3 for SimHash)."""
    return hamming_distance(hash1, hash2) <= threshold


# =============================================================================
# MINHASH - For Jaccard similarity estimation
# Jaccard(A, B) = |A ∩ B| / |A ∪ B|
# MinHash gives unbiased estimate with configurable error
# =============================================================================


def _minhash_signature(tokens: set[str], num_perm: int = 128, seed: int = 42) -> np.ndarray:
    """
    Compute MinHash signature of a set of tokens.
    Signature length num_perm; each value is min hash over permutations.
    """
    rng = np.random.default_rng(seed)
    # Permutations: (a, b) for hash = (a * x + b) % prime
    max_hash = 2**32 - 1
    a = rng.integers(1, max_hash, size=num_perm)
    b = rng.integers(0, max_hash, size=num_perm)

    sig = np.full(num_perm, max_hash, dtype=np.uint32)
    for t in tokens:
        x = hash(t) & max_hash
        for i in range(num_perm):
            h = (a[i] * x + b[i]) & max_hash
            if h < sig[i]:
                sig[i] = h
    return sig


def jaccard_from_minhash(sig1: np.ndarray, sig2: np.ndarray) -> float:
    """Estimate Jaccard similarity from MinHash signatures."""
    return np.mean(sig1 == sig2)


# =============================================================================
# LSH (Locality Sensitive Hashing) - For scalable near-duplicate search
# Bands and rows: tune for desired precision/recall
# =============================================================================


@dataclass
class LSHIndex:
    """
    LSH index for fast similarity search.
    Uses banding: split signature into bands; match if any band identical.
    """

    num_bands: int
    band_size: int
    # band -> hash -> list of doc_ids
    buckets: dict[tuple[int, int], list[str]]

    def __init__(self, num_bands: int = 20, band_size: int = 5):
        self.num_bands = num_bands
        self.band_size = band_size
        self.buckets = {}
        self._doc_signatures: dict[str, np.ndarray] = {}

    def _get_bands(self, sig: np.ndarray) -> list[tuple[int, int]]:
        """Get (band_id, band_hash) for each band."""
        bands = []
        for b in range(self.num_bands):
            start = b * self.band_size
            end = min(start + self.band_size, len(sig))
            band = tuple(sig[start:end].tolist())
            band_hash = hash(band)
            bands.append((b, band_hash))
        return bands

    def add(self, doc_id: str, sig: np.ndarray) -> None:
        """Add document signature to index."""
        self._doc_signatures[doc_id] = sig
        for band_id, band_hash in self._get_bands(sig):
            key = (band_id, band_hash)
            if key not in self.buckets:
                self.buckets[key] = []
            if doc_id not in self.buckets[key]:
                self.buckets[key].append(doc_id)

    def query(self, sig: np.ndarray, min_similarity: float = 0.5) -> list[str]:
        """Return candidate doc_ids that may be similar (LSH is approximate)."""
        candidates = set()
        for band_id, band_hash in self._get_bands(sig):
            key = (band_id, band_hash)
            candidates.update(self.buckets.get(key, []))

        # Optionally re-rank by exact MinHash similarity
        results = []
        for doc_id in candidates:
            sim = jaccard_from_minhash(sig, self._doc_signatures[doc_id])
            if sim >= min_similarity:
                results.append(doc_id)
        return results


# =============================================================================
# DEDUPLICATION PIPELINE
# =============================================================================


class DeduplicationPipeline:
    """
    End-to-end dedup pipeline.
    1. Exact dedup: content hash
    2. Near dedup: SimHash with threshold
    """

    def __init__(self, simhash_threshold: int = 3):
        self.simhash_threshold = simhash_threshold
        self.seen_hashes: set[int] = set()
        self.seen_content_hashes: set[str] = set()

    def _content_hash(self, text: str) -> str:
        """SHA256 of normalized text for exact dedup."""
        import hashlib
        normalized = " ".join(text.split()).lower()
        return hashlib.sha256(normalized.encode()).hexdigest()

    def is_duplicate(self, text: str) -> tuple[bool, str]:
        """
        Check if document is duplicate.
        Returns (is_dup, reason).
        """
        # Exact duplicate
        ch = self._content_hash(text)
        if ch in self.seen_content_hashes:
            return True, "exact"

        # Near duplicate (SimHash)
        sh = simhash(text)
        for seen in self.seen_hashes:
            if is_near_duplicate(sh, seen, self.simhash_threshold):
                return True, "near"

        return False, "unique"

    def add(self, text: str) -> bool:
        """Add document; return True if it was new (not duplicate)."""
        is_dup, _ = self.is_duplicate(text)
        if not is_dup:
            self.seen_content_hashes.add(self._content_hash(text))
            self.seen_hashes.add(simhash(text))
        return not is_dup


# =============================================================================
# EXAMPLE
# =============================================================================

if __name__ == "__main__":
    pipeline = DeduplicationPipeline(simhash_threshold=3)

    docs = [
        "The quick brown fox jumps over the lazy dog.",
        "The quick brown fox jumps over the lazy dog.",  # exact duplicate
        "The quick brown fox jumps over the lazy dog!",  # near duplicate
        "Machine learning is a subset of artificial intelligence.",  # unique
    ]

    for i, doc in enumerate(docs):
        is_new = pipeline.add(doc)
        print(f"Doc {i}: {'NEW' if is_new else 'DUPLICATE'}")
