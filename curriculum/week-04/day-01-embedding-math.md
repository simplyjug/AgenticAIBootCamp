# Day 1: Embedding Math & Similarity

## Learning Objectives

1. **Compute** cosine similarity and dot products
2. **Understand** distance metrics for retrieval
3. **Implement** similarity matrices in NumPy
4. **Relate** math to vector search APIs

---

## 1. Theory

### What are Embeddings?

Embeddings turn words/text into numbers (vectors) that capture meaning.

**For beginners:** Like coordinates on a map – similar things are close together.

### 1.1 Cosine Similarity

Measures angle between vectors. 1 = identical direction, 0 = perpendicular, -1 = opposite.

**Formula:** \(\cos(\theta) = \frac{u \cdot v}{\|u\| \|v\|}\)

**Why useful:** Ignores length, focuses on direction (meaning).

### 1.2 Dot Product

Sum of element-wise products: \(u \cdot v = \sum u_i v_i\)

**For normalized vectors:** Dot product = cosine similarity.

**Normalization:** \(\hat{v} = \frac{v}{\|v\|}\) (unit vector)

### 1.3 Distance Metrics

- **Euclidean:** Straight-line distance (Pythagoras)
- **Cosine:** Angular distance
- **Manhattan:** Sum of absolute differences

**In high dimensions:** Cosine often better for text.

### 1.4 Retrieval APIs

Vector databases use these for search.

- **Inner product:** Dot product (favors longer vectors)
- **Cosine:** Normalized dot product

**Choose based on data:** Cosine for text embeddings.

---

## 2. Practical: Computing Similarities

### Setup
Install numpy, matplotlib: `pip install numpy matplotlib`

### Hands-on Exercises
1. Compute similarities.
2. Verify math.
3. Plot heatmap.

## Code Examples

### Cosine Similarity
```python
import numpy as np

def cosine_similarity(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

# Example vectors
u = np.array([1, 2, 3])
v = np.array([1, 2, 4])

sim = cosine_similarity(u, v)
print(f"Cosine similarity: {sim:.3f}")
```

### Normalization
```python
def normalize(v):
    return v / np.linalg.norm(v)

u_norm = normalize(u)
v_norm = normalize(v)

# Dot product of normalized = cosine
dot_norm = np.dot(u_norm, v_norm)
print(f"Dot of normalized: {dot_norm:.3f}")  # Same as cosine
```

### Similarity Matrix
```python
# Multiple vectors
vectors = np.array([
    [1, 0, 0],  # Red
    [0, 1, 0],  # Green
    [0, 0, 1],  # Blue
    [1, 1, 0]   # Yellow
])

# Normalize
norm_vectors = np.array([normalize(v) for v in vectors])

# Similarity matrix
sim_matrix = np.dot(norm_vectors, norm_vectors.T)
print("Similarity matrix:")
print(sim_matrix)
```

### Heatmap
```python
import matplotlib.pyplot as plt

plt.imshow(sim_matrix, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Similarity Heatmap')
plt.xticks(range(len(vectors)), ['Red', 'Green', 'Blue', 'Yellow'])
plt.yticks(range(len(vectors)), ['Red', 'Green', 'Blue', 'Yellow'])
plt.show()
```

### Sentence Embeddings
```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
sentences = ["I love cats", "Cats are great", "I hate dogs", "Feline pets"]

embeddings = model.encode(sentences)
sim_matrix = np.dot(embeddings, embeddings.T)  # Assuming normalized

plt.imshow(sim_matrix, cmap='viridis')
plt.colorbar()
plt.title('Sentence Similarity')
plt.xticks(range(len(sentences)), sentences, rotation=45)
plt.yticks(range(len(sentences)), sentences)
plt.show()
```

---

## 3. Homework

Compute similarities for 20 sentences and analyze clusters.

---

## 4. Interview Questions

- Difference between cosine and dot product?
- When to use Euclidean vs cosine distance?

## Resources
- [Cosine Similarity Explained](https://en.wikipedia.org/wiki/Cosine_similarity)
- [Vector Databases](https://milvus.io/docs/overview.md)

## Done When
- [ ] Code shows cosine = dot for normalized vectors.
- [ ] Explanation of API choices.
