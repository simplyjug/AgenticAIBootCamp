# Day 3: Semantic Deduplication & Noise Reduction

## Learning Objectives

1. **Cluster** near-duplicates using embedding similarity
2. **Measure** noise like OCR errors or boilerplate text
3. **Implement** filters before deduplication
4. **Handle** transitive duplicates carefully

---

## 1. Theory

### What is Semantic Deduplication?

Regular deduplication finds exact copies. Semantic deduplication finds documents that mean the same thing, even if worded differently.

**For beginners:** It's like recognizing that "The feline rested on the rug" and "A cat sat on the mat" are about the same event.

### 1.1 Embedding Similarity

Embeddings turn text into numbers (vectors). Similar meanings have similar vectors.

**Cosine similarity:** Measures angle between vectors. 1.0 = identical, 0.0 = unrelated.

**Threshold:** Decide what's "similar enough" – e.g., 0.9 for very close, 0.7 for related.

### 1.2 Noise Reduction

Noise is unwanted text that confuses the model.

**Types:**
- **OCR junk:** Scanned text errors like "Th3 cat s4t"
- **Boilerplate:** Headers, footers, ads
- **Short fragments:** Incomplete sentences

**How to detect:** Use rules like "too many numbers" or "repetitive phrases".

### 1.3 Transitive Duplicates

A is similar to B, B to C, but A and C are different.

**Problem:** If you delete based on chains, you might lose unique info.

**Solution:** Use careful clustering, not just pairwise checks.

---

## 2. Practical: Semantic Deduplication

### Setup
Install sentence-transformers: `pip install sentence-transformers scikit-learn`

### Hands-on Exercises
1. Compute embeddings for texts.
2. Cluster with DBSCAN.
3. Filter noise.

## Code Examples

### Embedding Similarity
```python
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

texts = [
    "The cat sat on the mat",
    "A feline was on the rug",
    "Dogs are pets too"
]

embeddings = model.encode(texts)

# Cosine similarity
def cosine_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

sim = cosine_sim(embeddings[0], embeddings[1])
print(f"Similarity: {sim:.2f}")  # High for similar
```

### Clustering
```python
from sklearn.cluster import DBSCAN

# Cluster embeddings
db = DBSCAN(eps=0.5, min_samples=1, metric='cosine').fit(embeddings)
labels = db.labels_

for i, label in enumerate(labels):
    print(f"Text {i}: Cluster {label}")
```

### Noise Filter
```python
def is_noise(text):
    # Simple rules
    if len(text.split()) < 5:  # Too short
        return True
    if text.count('?') > 5:  # Too many questions (maybe OCR)
        return True
    return False

clean_texts = [t for t in texts if not is_noise(t)]
print(f"Kept {len(clean_texts)} clean texts")
```

---

## 3. Homework

Implement transitive closure check and compare clustering methods.

---

## 4. Interview Questions

- How to balance deduplication accuracy vs data loss?
- Design noise filter for multilingual documents.

## Resources
- [Sentence Transformers](https://www.sbert.net/)
- [DBSCAN Clustering](https://scikit-learn.org/stable/modules/clustering.html#dbscan)

## Done When
- [ ] You can explain semantic vs exact deduplication.
- [ ] You've clustered sample texts with embeddings.
