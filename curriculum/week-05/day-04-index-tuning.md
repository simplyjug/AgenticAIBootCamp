# Day 4: Index tuning & rebuilding

## Learning objectives

- Define **SLO** for rebuild duration and acceptable **query degradation** during swap.
- Tune **HNSW efConstruction** vs build time; **IVF nlist** vs recall.

## Hands-on

1. Pick one engine you used this week; run **two** configs differing by ≥20% build time.
2. Record recall@k for both on the same query set.
3. Draft a **runbook**: daily incremental upserts vs weekly full rebuild.

## Concepts

- **Fragmentation:** deletes leaving holes — some stores require compaction jobs.
- **Back-pressure:** pause ingestion if queue depth exceeds threshold.

## Done when

- [ ] Runbook markdown with rollback step.
- [ ] Graph or table: build time vs recall.

## Resources

- Store-specific tuning guides (FAISS wiki / Milvus index params)
