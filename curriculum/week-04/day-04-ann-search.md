# Day 4: ANN Search (HNSW, IVF)

## Learning Objectives

1. **Configure** HNSW and IVF indexes
2. **Tune** parameters for latency vs recall
3. **Measure** performance tradeoffs
4. **Choose** index type by use case

---

## 1. Theory

### Approximate Nearest Neighbor (ANN)

Exact search is slow for millions of vectors. ANN approximates for speed.

**For beginners:** Like finding nearest store – exact GPS vs "near downtown".

### 1.1 HNSW (Hierarchical Navigable Small World)

Graph-based. Layers for fast search.

**Parameters:**
- **M:** Max connections per node (higher = better recall, more memory)
- **efConstruction:** Build quality (higher = better, slower build)
- **efSearch:** Search quality (higher = better recall, slower query)

### 1.2 IVF (Inverted File)

Clusters vectors, searches nearby clusters.

**Parameters:**
- **nlist:** Number of clusters (more = better, more memory)
- **nprobe:** Clusters to search (higher = better recall, slower)

### 1.3 Tradeoffs

- **HNSW:** Good for static data, high recall
- **IVF:** Good for dynamic data, fast updates

**Sharding:** Split by topic for smaller indexes.

---

## 2. Practical: Building ANN Indexes

### Setup
Install faiss: `pip install faiss-cpu`

### Hands-on Exercises
1. Build HNSW index.
2. Tune parameters.
3. Compare latency/recall.

## Code Examples

### HNSW Index
```python
import faiss
import numpy as np
import time

# Data
d = 128
nb = 10000
nq = 100
np.random.seed(42)
xb = np.random.random((nb, d)).astype('float32')
xq = np.random.random((nq, d)).astype('float32')

# HNSW
M = 32
efConstruction = 200
index_hnsw = faiss.IndexHNSWFlat(d, M)
index_hnsw.hnsw.efConstruction = efConstruction
index_hnsw.add(xb)

# Search with efSearch
efSearch = 64
index_hnsw.hnsw.efSearch = efSearch
start = time.time()
D_hnsw, I_hnsw = index_hnsw.search(xq, 10)
hnsw_time = time.time() - start
print(f"HNSW time: {hnsw_time:.3f}s")
```

### IVF Index
```python
# IVF
nlist = 100
quantizer = faiss.IndexFlatL2(d)
index_ivf = faiss.IndexIVFFlat(quantizer, d, nlist)
index_ivf.train(xb)
index_ivf.add(xb)

# Search with nprobe
nprobe = 10
index_ivf.nprobe = nprobe
start = time.time()
D_ivf, I_ivf = index_ivf.search(xq, 10)
ivf_time = time.time() - start
print(f"IVF time: {ivf_time:.3f}s")
```

### Compare to Brute Force
```python
index_flat = faiss.IndexFlatL2(d)
index_flat.add(xb)
start = time.time()
D_flat, I_flat = index_flat.search(xq, 10)
flat_time = time.time() - start
print(f"Flat time: {flat_time:.3f}s")
```

### Recall Calculation
```python
def recall_at_k(true_I, pred_I, k):
    recalls = []
    for t, p in zip(true_I, pred_I):
        intersection = set(t[:k]) & set(p[:k])
        recalls.append(len(intersection) / k)
    return np.mean(recalls)

recall_hnsw = recall_at_k(I_flat, I_hnsw, 10)
recall_ivf = recall_at_k(I_flat, I_ivf, 10)
print(f"HNSW recall@10: {recall_hnsw:.3f}")
print(f"IVF recall@10: {recall_ivf:.3f}")
```

### Parameter Sweep
```python
ef_values = [16, 32, 64, 128]
times = []
recalls = []

for ef in ef_values:
    index_hnsw.hnsw.efSearch = ef
    start = time.time()
    D, I = index_hnsw.search(xq, 10)
    t = time.time() - start
    r = recall_at_k(I_flat, I, 10)
    times.append(t)
    recalls.append(r)

# Plot
import matplotlib.pyplot as plt
plt.plot(recalls, times, 'o-')
plt.xlabel('Recall@10')
plt.ylabel('Time (s)')
plt.title('HNSW: Latency vs Recall')
plt.show()
```

### Cold vs Warm
```python
# Cold start
index_hnsw.hnsw.efSearch = 64
start = time.time()
D, I = index_hnsw.search(xq[:1], 10)  # First query
cold_time = time.time() - start

# Warm
start = time.time()
D, I = index_hnsw.search(xq[:1], 10)  # Same query
warm_time = time.time() - start

print(f"Cold: {cold_time:.4f}s, Warm: {warm_time:.4f}s")
```

---

## 3. Homework

Sweep parameters and plot curves.

---

## 4. Interview Questions

- HNSW vs IVF: When to use each?
- How to tune ANN for low latency?

## Resources
- [HNSW Paper](https://arxiv.org/abs/1603.09320)
- [FAISS Docs](https://github.com/facebookresearch/faiss)

## Done When
- [ ] Latency vs recall graph.
- [ ] Rule for choosing IVF over HNSW.
