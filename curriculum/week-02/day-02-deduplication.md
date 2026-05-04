# Day 2: Deduplication — MinHash, LSH, SimHash

## Learning Objectives

1. **Implement** SimHash for fast near-duplicate detection
2. **Implement** MinHash for Jaccard similarity estimation
3. **Build** LSH index for scalable similarity search
4. **Design** embedding-based similarity clustering for semantic dedup

---

## 1. Theory

### SimHash
- 64-bit fingerprint; similar docs → low Hamming distance
- O(n) per document; threshold typically 3 bits

### MinHash + LSH
- MinHash: unbiased Jaccard estimator
- LSH: banding for sublinear search

---

## 2. Lab

See `labs/week2/day02_deduplication.py` — full pipeline with comments.
