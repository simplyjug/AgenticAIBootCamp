# Day 3: Quantization & compression

## Learning objectives

- Compare **float32** vs **int8** / **PQ** for index size and recall@k.
- Explain **product quantization (PQ)** as subspace clustering at a high level.
- Record **memory/latency** tradeoffs in a one-page table.

## Concepts

- **ADC (asymmetric distance computation):** query float, database PQ — common FAISS pattern.
- **Re-ranking:** cheap ANN top-200 + cross-encoder on top-20 for quality.

## Hands-on

1. Build a small FAISS `IndexFlatL2` baseline; measure memory.
2. Add `IndexIVFPQ` or equivalent tutorial index with same vectors; compare recall@10 vs baseline brute force on a held-out query set (even random queries okay for pedagogy).
3. Summarize when PQ is unacceptable (legal/medical high-precision regimes).

## Done when

- [ ] Table: index type | memory | recall@k | build time.
- [ ] Risk statement for **lossy** compression in regulated domains.

## Resources

- FAISS [wiki — IVF and PQ](https://github.com/facebookresearch/faiss/wiki/Faiss-indexes)
