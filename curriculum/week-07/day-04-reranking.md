# Day 4: Query rewriting & reranking

## Learning objectives

- Add a **cross-encoder** or API reranker on **top-k** FAISS hits to fix embedding mistakes.
- Try **query expansion** (synonyms, HyDE-style synthetic doc) at the cost of extra LLM calls.

## Concepts

- **Two-stage retrieval:** cheap recall (100) → expensive precision (10).
- **Latency budget:** reranker batch size vs user-facing p95.

## Hands-on

1. Take `top_k=20` from `SimpleRetriever`; rerank to top 5 using:
   - a small cross-encoder from `sentence_transformers`, OR
   - a manual scoring function as placeholder with documented swap-in.
2. Measure **MRR** change on 5 hand-built queries if you have labels; else qualitative ranking notes.

## Done when

- [ ] Before/after anecdote or metric for at least 3 queries.
- [ ] Rule for when reranking is **skipped** (low traffic tier).

## Resources

- [sentence-transformers cross-encoder](https://www.sbert.net/examples/applications/cross-encoder/README.html)
