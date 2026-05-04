# Week 10: Module 8 — Metadata enrichment

**Time:** ~10–12 hours · **Prerequisites:** Weeks 2–4 (structured thinking + NLP)

## Outcomes

- Extract **entities & keywords**; improve **topic / taxonomy** assignment.
- Design **schemas** that play well with hybrid retrieval.
- Run an **incremental enrichment** pipeline and connect metadata to **filters**.

## Self-service flow

1. **[docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-10)**.
2. Implement small scripts under `labs/week10/` (create if missing — see day guides).

## Reading-only path

This week is about metadata enrichment and schema-driven retrieval. Reading-only learners should focus on the data model and how metadata supports filters and ranking.

- Learn how NER and keywords improve document understanding.
- Understand how taxonomy and topic assignment enable better search UX.
- Review schema design for downstream filter and retrieval compatibility.
- Think through enrichment pipelines, idempotency, and metadata freshness.

Write down one schema design, one enrichment pipeline flow, and one filtered retrieval example.

## Day-by-day

| Day | Topic | Guide |
|-----|--------|--------|
| 1 | NER & keywords | [day-01-ner-keywords.md](day-01-ner-keywords.md) |
| 2 | Topic & taxonomy | [day-02-topic-taxonomy.md](day-02-topic-taxonomy.md) |
| 3 | Schema design | [day-03-schema-design.md](day-03-schema-design.md) |
| 4 | Enrichment pipeline | [day-04-enrichment-pipeline.md](day-04-enrichment-pipeline.md) |
| 5 | Metadata for retrieval | [day-05-metadata-retrieval.md](day-05-metadata-retrieval.md) |

## Concepts

- **Enrichment lag:** async jobs vs blocking ingest path.
- **Schema drift:** evolving fields without breaking consumers.

## Done when

- [ ] Schema diagram (Pydantic / JSON Schema acceptable).
- [ ] One enrichment job idempotent by document ID.
- [ ] Example query using **metadata filter** + vector search together.

## Portfolio path

This week’s portfolio artifact should show how metadata enriches search:

- One **metadata schema diagram** with field purpose.
- One **enrichment pipeline note** including idempotency.
- One **interview story** about using metadata filters with vector search.

If you are reading only, write a summary of how metadata improves retrieval and supports filters.
