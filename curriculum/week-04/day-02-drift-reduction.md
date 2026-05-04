# Day 2: Dimensionality Reduction & Drift Signals

## Learning Objectives

1. **Apply** PCA/UMAP for embedding visualization
2. **Detect** embedding drift over time
3. **Define** mitigation strategies
4. **Understand** covariate shift in retrieval

---

## 1. Theory

### Dimensionality Reduction

Embeddings are high-dimensional (e.g., 768D). Reduce to 2D/3D for plotting.

**For beginners:** Like shrinking a photo to fit on screen – lose some detail but see the big picture.

### 1.1 PCA (Principal Component Analysis)

Finds directions of maximum variance. Linear method.

**Pros:** Fast, interpretable
**Cons:** Linear only

### 1.2 UMAP (Uniform Manifold Approximation)

Non-linear reduction. Preserves local structure better.

**Pros:** Better clusters
**Cons:** Slower, less interpretable

### 1.3 Embedding Drift

Embeddings change over time due to:
- Model updates
- Data changes
- Concept drift (meanings evolve)

**Detection:** Compare centroids, neighbor overlaps.

### 1.4 Covariate Shift

Query distribution changes, but documents stay same.

**Example:** New topics become popular.

**Impact:** Retrieval gets worse.

---

## 2. Practical: Reducing Dimensions & Detecting Drift

### Setup
Install sklearn, umap: `pip install scikit-learn umap-learn matplotlib`

### Hands-on Exercises
1. Reduce dimensions.
2. Visualize clusters.
3. Simulate drift.

## Code Examples

### PCA Reduction
```python
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

# Sample embeddings (100 samples, 768 dim)
embeddings = np.random.randn(100, 768)

# PCA to 2D
pca = PCA(n_components=2)
reduced = pca.fit_transform(embeddings)

plt.scatter(reduced[:, 0], reduced[:, 1])
plt.title('PCA Reduced Embeddings')
plt.show()
```

### UMAP Reduction
```python
import umap

# UMAP to 2D
reducer = umap.UMAP(n_neighbors=15, min_dist=0.1)
reduced_umap = reducer.fit_transform(embeddings)

plt.scatter(reduced_umap[:, 0], reduced_umap[:, 1])
plt.title('UMAP Reduced Embeddings')
plt.show()
```

### Clustering Check
```python
from sklearn.cluster import KMeans

# Cluster in reduced space
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(reduced)

plt.scatter(reduced[:, 0], reduced[:, 1], c=clusters, cmap='viridis')
plt.title('Clusters in PCA Space')
plt.show()
```

### Drift Detection
```python
# Simulate old vs new embeddings
old_embeddings = np.random.randn(50, 768)
new_embeddings = old_embeddings + np.random.randn(50, 768) * 0.1  # Small drift

# Centroid movement
old_centroid = np.mean(old_embeddings, axis=0)
new_centroid = np.mean(new_embeddings, axis=0)
drift_distance = np.linalg.norm(old_centroid - new_centroid)
print(f"Centroid drift: {drift_distance:.3f}")

# Nearest neighbor overlap (simplified)
from sklearn.neighbors import NearestNeighbors

nn = NearestNeighbors(n_neighbors=5)
nn.fit(old_embeddings)
distances, indices = nn.kneighbors(new_embeddings)
overlap = np.mean(distances < 0.5)  # Threshold
print(f"NN overlap: {overlap:.3f}")
```

### Drift Checklist
- Compare centroids: Cosine similarity
- Check norm distributions: KL divergence
- Neighbor overlap: % same neighbors
- Threshold: Retrain if drift > 0.2

---

## 3. Homework

Apply to real embeddings and detect drift.

---

## 4. Interview Questions

- How to detect embedding drift?
- When to retrain vs re-index?

## Resources
- [PCA Explained](https://www.youtube.com/watch?v=FgakZw6y1OU)
- [UMAP Paper](https://arxiv.org/abs/1802.03426)

## Done When
- [ ] Visualization of time slices.
- [ ] Cheap vs expensive mitigations.
