# Day 2: Deduplication — MinHash, LSH, SimHash

## Learning Objectives

1. **Implement** SimHash for fast near-duplicate detection
2. **Implement** MinHash for Jaccard similarity estimation
3. **Build** LSH index for scalable similarity search
4. **Design** embedding-based similarity clustering for semantic dedup

---

## 1. Theory

### Why Deduplication Matters

Imagine you have a library with 1 million books, but half are copies of the same book. Your AI model would waste time learning the same thing twice. Deduplication removes duplicates to make your data cleaner and your models faster.

For new graduates: It's like organizing your notes – you don't want to study the same topic twice.

### 1.1 SimHash: Fast Fingerprinting

SimHash creates a "fingerprint" for each document. Similar documents have similar fingerprints.

**How it works (simple version):**
1. Break text into words.
2. For each word, create a hash (like a number ID).
3. Count how many times words appear.
4. Combine into a 64-bit number.

**Example:** Two articles about "cats" will have similar SimHash if they use similar words.

**Pros:** Very fast, works on any text.
**Cons:** Only finds exact or very similar duplicates.

### 1.2 MinHash: Estimating Similarity

MinHash helps find documents that are similar but not identical. It uses "Jaccard similarity" – how much overlap two sets have.

**Simple analogy:** If two playlists share 50% songs, Jaccard is 0.5.

**How it works:**
1. Shingle the text (break into small pieces).
2. Hash each shingle.
3. Pick the smallest hash for each "bucket".

**Why useful:** Can estimate similarity without comparing everything.

### 1.3 LSH: Scalable Search

Locality Sensitive Hashing groups similar items together. Instead of checking every pair, it only checks likely similar ones.

**Think of it as:** Sorting books by color – red books are near other red books.

**For deduplication:** Put similar documents in the same "bucket" to check for duplicates.

### 1.4 Embedding-Based Clustering

Use AI embeddings (like from BERT) to find semantic duplicates. Even if words differ, meaning is similar.

**Example:** "Feline pets" and "Cats as companions" are similar semantically.

---

## 2. Practical: Implementing Deduplication

### Setup
Install datasketch: `pip install datasketch`

### Hands-on Exercises
1. Compute SimHash for texts.
2. Find duplicates with LSH.
3. Cluster with embeddings.

## Code Examples

### SimHash Example
```python
from simhash import Simhash

# Simple texts
text1 = "The cat sat on the mat"
text2 = "A cat was sitting on a mat"

hash1 = Simhash(text1)
hash2 = Simhash(text2)

distance = hash1.distance(hash2)  # Hamming distance
print(f"Distance: {distance}")  # Low if similar
```

### MinHash + LSH
```python
from datasketch import MinHash, MinHashLSH

# Create MinHash for texts
def get_minhash(text):
    m = MinHash(num_perm=128)
    for word in text.split():
        m.update(word.encode('utf8'))
    return m

m1 = get_minhash(text1)
m2 = get_minhash(text2)

# LSH index
lsh = MinHashLSH(threshold=0.5, num_perm=128)
lsh.insert("doc1", m1)
lsh.insert("doc2", m2)

# Query similar
result = lsh.query(m1)
print(result)  # Should include doc2 if similar
```

### Embedding Clustering
```python
from sentence_transformers import SentenceTransformer
from sklearn.cluster import DBSCAN

model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode([text1, text2])

# Cluster
db = DBSCAN(eps=0.5, min_samples=1).fit(embeddings)
labels = db.labels_
print(labels)  # Same label if similar
```

---

## 3. Homework

Compare deduplication methods on a dataset of 1000 news articles.

---

## 4. Interview Questions

- When would you use SimHash vs embeddings for deduplication?
- How to handle deduplication at scale (1B documents)?

## Resources
- [SimHash Paper](https://www.cs.princeton.edu/courses/archive/spring04/cos598B/bib/CharikarEstim.pdf)
- [MinHash Tutorial](https://ekzhu.com/datasketch/lsh.html)

## Done When
- [ ] You can explain why deduplication matters.
- [ ] You've implemented SimHash on sample texts.
