# Day 1: Embedding math & similarity

## Learning objectives

- Use **cosine similarity** and **dot product** correctly with **L2-normalized** vectors.
- Relate **distance metrics** to retrieval APIs (inner product index vs cosine).
- Implement a toy similarity matrix in **NumPy** mirroring `labs/week4/day01_embedding_similarity.py`.

## Concepts

- Normalization: \(\hat{v} = v / \|v\|\); cosine similarity of normalized vectors equals dot product.
- **Angular distance** vs Euclidean distance in high dimensions — intuition for “nearest neighbor feels weird.”

## Hands-on

1. Run and extend `labs/week4/day01_embedding_similarity.py`.
2. Verify numerically: \(\cos(u,v)\) vs \(\hat{u} \cdot \hat{v}\).
3. Plot a heatmap for **10×10** similarities on a small sentence list.

## Done when

- [ ] Short derivation or comment block in code tying cosine ↔ dot for normalized vectors.
- [ ] One paragraph on **why** APIs expose “cosine” vs “dot” configuration flags.

## Resources

- [docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-4)
