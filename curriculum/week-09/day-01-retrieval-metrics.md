# Day 1: Retrieval metrics (Recall@k, MRR, nDCG)

## Learning objectives

- Compute **Recall@k**, **MRR**, and **nDCG** on a labeled **query–relevance** table.
- Script metrics in `labs/week9/rag_evaluation.py` or a companion notebook.

## Hands-on

1. Build **20 labeled queries** with relevant chunk IDs (even synthetic).
2. Run retrieval; compute Recall@5 and MRR.
3. Compare **two** retrieval configs (e.g., top_k or embedding model) on the same labels.

## Concepts

- **Labels are precious** — stratify easy vs hard queries in reporting.

## Done when

- [ ] CSV or JSONL `golden_set.jsonl` committed under `datasets/eval/` (no secrets).
- [ ] Metrics table for two configs.

## Resources

- [docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-9)
