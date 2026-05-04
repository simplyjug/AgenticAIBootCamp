# Day 5: Custom Embeddings & SentenceTransformers

## Learning Objectives

1. **Fine-tune** embeddings with contrastive learning
2. **Understand** training objectives like triplet loss
3. **Evaluate** custom embeddings
4. **Decide** when fine-tuning is worthwhile

---

## 1. Theory

### Why Custom Embeddings?

Pre-trained embeddings (like BERT) are general. Fine-tune for your domain.

**For beginners:** Like teaching a model your company's jargon.

### 1.1 Contrastive Learning

Train by pulling similar pairs close, pushing dissimilar apart.

**Triplet:** Anchor, positive, negative.

**Multiple negatives:** One positive, many negatives.

### 1.2 Training Objectives

- **Triplet loss:** Minimize distance to positive, maximize to negative
- **MNRL:** InfoNCE loss for multiple negatives

**Hard negatives:** Challenging examples that are close but wrong.

### 1.3 When to Fine-Tune

- **Pros:** Better performance on domain
- **Cons:** Needs data, can overfit

**Rule:** At least 100-1000 examples.

### 1.4 Evaluation

- **MRR:** Mean reciprocal rank
- **Recall@K:** % relevant in top K

**Leakage:** Ensure eval data not in training.

---

## 2. Practical: Fine-Tuning Embeddings

### Setup
Install sentence-transformers: `pip install sentence-transformers`

### Hands-on Exercises
1. Prepare triplets.
2. Fine-tune model.
3. Evaluate improvement.

## Code Examples

### Load Model
```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
print("Model loaded")
```

### Prepare Data
```python
from sentence_transformers import InputExample

# Synthetic triplets
train_examples = [
    InputExample(texts=['What is AI?', 'Artificial Intelligence is...', 'Cats are pets']),
    InputExample(texts=['How to code?', 'Programming involves...', 'Cooking recipes']),
    # Add more...
]

print(f"Training examples: {len(train_examples)}")
```

### Fine-Tune
```python
from sentence_transformers import losses
from torch.utils.data import DataLoader

# DataLoader
train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=8)

# Loss
train_loss = losses.MultipleNegativesRankingLoss(model)

# Train
model.fit(train_objectives=[(train_dataloader, train_loss)], epochs=1, warmup_steps=10)
print("Fine-tuned")
```

### Evaluate
```python
# Corpus and queries
corpus = [
    "AI is artificial intelligence",
    "Programming is writing code",
    "Cats are animals"
]

queries = [
    "What is AI?",
    "How to program?"
]

# Encode
corpus_emb = model.encode(corpus)
query_emb = model.encode(queries)

# Search (simple)
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

similarities = cosine_similarity(query_emb, corpus_emb)
ranks = np.argsort(-similarities, axis=1)

# MRR
def mrr(ranks, relevant_indices):
    mrr_sum = 0
    for i, rank in enumerate(ranks):
        rel_idx = relevant_indices[i]
        if rel_idx in rank:
            pos = np.where(rank == rel_idx)[0][0] + 1
            mrr_sum += 1 / pos
    return mrr_sum / len(ranks)

relevant = [0, 1]  # Indices of relevant docs
mrr_score = mrr(ranks, relevant)
print(f"MRR: {mrr_score:.3f}")
```

### Before/After Comparison
```python
# Before fine-tune
model_orig = SentenceTransformer('all-MiniLM-L6-v2')
corpus_emb_orig = model_orig.encode(corpus)
query_emb_orig = model_orig.encode(queries)
sim_orig = cosine_similarity(query_emb_orig, corpus_emb_orig)
ranks_orig = np.argsort(-sim_orig, axis=1)
mrr_orig = mrr(ranks_orig, relevant)

print(f"Original MRR: {mrr_orig:.3f}")
print(f"Fine-tuned MRR: {mrr_score:.3f}")
```

### Hard Negatives
```python
# Add hard negatives (close but wrong)
hard_examples = [
    InputExample(texts=['AI definition', 'AI stands for...', 'Machine learning is AI subset']),  # Hard negative
]

train_examples.extend(hard_examples)
```

---

## 3. Homework

Fine-tune on domain data and measure improvement.

---

## 4. Interview Questions

- When to fine-tune embeddings?
- Difference between triplet and contrastive loss?

## Resources
- [SentenceTransformers Training](https://www.sbert.net/docs/training/overview.html)
- [Contrastive Learning](https://arxiv.org/abs/2002.05709)

## Done When
- [ ] Before/after MRR table.
- [ ] Minimum pairs criteria.
