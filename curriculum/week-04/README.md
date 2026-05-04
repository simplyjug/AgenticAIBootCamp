# Week 4: Module 3 — Embeddings deep dive

**Time:** ~10–14 hours · **Prerequisites:** Linear algebra intuition, Week 3 metrics

## Outcomes

- Explain **why cosine vs dot product** matters when vectors are normalized or not.
- Detect **embedding drift** and compress / quantize indices responsibly.
- Build **ANN** indexes with FAISS and interpret latency vs recall curves.

## Self-service flow

1. **[docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-4)**.
2. Labs: `labs/week4/day01_embedding_similarity.py`, `labs/week4/day04_faiss_index.py`.

## Reading-only path

This week is about embeddings and nearest-neighbor search. Reading-only learners should focus on the math and engineering tradeoffs.

- Learn when cosine similarity or dot product is appropriate.
- Understand drift, quantization, and index compression impacts on recall.
- Compare ANN algorithms and the cost of each design choice.
- Note how custom embeddings are built and when they are worth the effort.

Take notes on one example search pipeline, one drift detection approach, and one index tradeoff.

## Day-by-day

| Day | Topic | Guide | Lab |
|-----|--------|--------|-----|
| 1 | Embedding math | [day-01-embedding-math.md](day-01-embedding-math.md) | `day01_embedding_similarity.py` |
| 2 | Drift / PCA | [day-02-drift-reduction.md](day-02-drift-reduction.md) | Notebook |
| 3 | Quantization | [day-03-quantization.md](day-03-quantization.md) | Compare sizes |
| 4 | ANN / FAISS | [day-04-ann-search.md](day-04-ann-search.md) | `day04_faiss_index.py` |
| 5 | Custom embeddings | [day-05-custom-embeddings.md](day-05-custom-embeddings.md) | SentenceTransformers fine-tune sketch |

## Concepts

- **ANN tradeoffs:** HNSW, IVF, PQ — memory, build time, recall@k.
- **Monitoring embeddings:** centroid drift, neighbor overlap audits.

## Done when

- [ ] Similarity exercise documented with formulas + numpy code path.
- [ ] One FAISS benchmark table (k, recall@k, QPS).
- [ ] Short paragraph on when **fine-tuning embeddings** is worth the complexity.

## Portfolio path

This week’s portfolio artifact should show your ability to reason about vectors and search performance:

- One **embedding similarity note** with the chosen similarity function and why.
- One **benchmark table** comparing index settings or compression methods.
- One **interview story** on the tradeoff between recall and latency.

If you are reading only, write a summary of the embedding strategy, drift controls, and indexing tradeoffs.
