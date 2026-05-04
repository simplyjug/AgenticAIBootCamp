# Day 3: Quantization & Compression

## Learning Objectives

1. **Compare** float32 vs quantized formats
2. **Implement** product quantization (PQ)
3. **Measure** memory and latency tradeoffs
4. **Understand** when compression is risky

---

## 1. Theory

### Why Quantization?

Embeddings take lots of memory. Quantization reduces size by using fewer bits.

**For beginners:** Like compressing photos – smaller file, but some quality loss.

### 1.1 Float32 vs Int8

- **Float32:** 4 bytes per number, full precision
- **Int8:** 1 byte, approximate (quantized)

**Tradeoff:** 4x smaller, but less accurate.

### 1.2 Product Quantization (PQ)

Splits vector into sub-vectors, quantizes each separately.

**How:** Cluster sub-vectors, use cluster IDs as codes.

**Benefit:** Compress large datasets.

### 1.3 ANN vs Exact Search

- **ANN:** Approximate nearest neighbor (fast, approximate)
- **Exact:** Brute force (slow, perfect)

**Re-ranking:** ANN for candidates, exact for top-K.

### 1.4 Risks

In high-stakes areas (medical, legal), small errors matter.

**Mitigation:** Use higher precision or re-ranking.

---

## 2. Practical: Quantizing Embeddings

### Setup
Install faiss: `pip install faiss-cpu numpy`

### Hands-on Exercises
1. Build baseline index.
2. Add PQ index.
3. Compare performance.

## Code Examples

### Baseline Flat Index
```python
import faiss
import numpy as np

# Sample data (1000 vectors, 128 dim)
d = 128
nb = 1000
nq = 10  # Queries
np.random.seed(42)
xb = np.random.random((nb, d)).astype('float32')
xq = np.random.random((nq, d)).astype('float32')

# Flat index (exact search)
index_flat = faiss.IndexFlatL2(d)
index_flat.add(xb)

# Search
k = 10
D_flat, I_flat = index_flat.search(xq, k)
print(f"Flat index memory: {index_flat.ntotal * d * 4 / 1024:.1f} KB")
```

### PQ Index
```python
# PQ index
m = 8  # Sub-vectors
nbits = 8  # Bits per sub-vector
index_pq = faiss.IndexPQ(d, m, nbits)
index_pq.train(xb)
index_pq.add(xb)

# Search
D_pq, I_pq = index_pq.search(xq, k)
print(f"PQ index memory: {index_pq.pq.ksub * 2**nbits * m / 1024:.1f} KB")  # Rough
```

### Compare Recall
```python
def recall_at_k(true_indices, pred_indices, k):
    recalls = []
    for t, p in zip(true_indices, pred_indices):
        intersection = set(t[:k]) & set(p[:k])
        recalls.append(len(intersection) / k)
    return np.mean(recalls)

recall_flat = recall_at_k(I_flat, I_flat, k)  # Perfect
recall_pq = recall_at_k(I_flat, I_pq, k)
print(f"Recall@{k}: Flat={recall_flat:.3f}, PQ={recall_pq:.3f}")
```

### IVF + PQ (Better)
```python
nlist = 10  # Clusters
index_ivfpq = faiss.IndexIVFPQ(faiss.IndexFlatL2(d), d, nlist, m, nbits)
index_ivfpq.train(xb)
index_ivfpq.add(xb)

D_ivf, I_ivf = index_ivfpq.search(xq, k)
recall_ivf = recall_at_k(I_flat, I_ivf, k)
print(f"IVF+PQ recall@{k}: {recall_ivf:.3f}")
```

### Memory Table
```python
import pandas as pd

data = {
    'Index': ['Flat', 'PQ', 'IVF+PQ'],
    'Memory (KB)': [index_flat.ntotal * d * 4 / 1024, 
                    index_pq.pq.ksub * 2**nbits * m / 1024,
                    index_ivfpq.ntotal * (m * nbits / 8) / 1024],  # Rough
    'Recall@10': [recall_flat, recall_pq, recall_ivf],
    'Build Time': ['Fast', 'Medium', 'Slow']
}

df = pd.DataFrame(data)
print(df)
```

---

## 3. Homework

Experiment with different PQ parameters.

---

## 4. Interview Questions

- When to use quantization?
- Tradeoffs of PQ vs exact search?

## Resources
- [FAISS IVF and PQ](https://github.com/facebookresearch/faiss/wiki/Faiss-indexes)
- [Quantization Overview](https://arxiv.org/abs/1609.07061)

## Done When
- [ ] Performance table created.
- [ ] Risk statement for regulated domains.
