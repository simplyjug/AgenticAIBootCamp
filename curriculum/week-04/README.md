# Week 4: Module 3 — Embeddings deep dive

**Time:** ~10–14 hours · **Prerequisites:** Linear algebra intuition, Week 3 metrics

## Outcomes

- Explain **why cosine vs dot product** matters when vectors are normalized or not.
- Detect **embedding drift** and compress / quantize indices responsibly.
- Build **ANN** indexes with FAISS and interpret latency vs recall curves.

## Self-service flow

1. **[docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-4)**.
2. Labs: `labs/week4/day01_embedding_similarity.py`, `labs/week4/day04_faiss_index.py`.

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
