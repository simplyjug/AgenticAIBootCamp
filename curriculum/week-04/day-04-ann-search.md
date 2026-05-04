# Day 4: ANN search (HNSW, IVF)

## Learning objectives

- Configure **HNSW** (`M`, `efConstruction`, `efSearch`) vs **IVF** (`nlist`, `nprobe`).
- Plot **latency vs recall** for your hardware.

## Hands-on

1. Run `labs/week4/day04_faiss_index.py` (extend if minimal).
2. Sweep **efSearch** or `nprobe` and record QPS + recall@k vs brute force on a sample.
3. Capture **cold vs warm** timing (first query vs steady state).

## Concepts

- **efSearch** trades accuracy for latency on HNSW — tune per SLA tier.
- **Sharding:** partition vectors by tenant or topic to shrink graph size per query.

## Done when

- [ ] Graph or markdown table of latency vs recall.
- [ ] Written rule: when you’d pick IVF over HNSW (ingest rate, memory).

## Resources

- [docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-5) (vector DB concepts overlap)
