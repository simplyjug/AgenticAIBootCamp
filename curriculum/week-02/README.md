# Week 2: Module 1 — Data curation engineering

**Time:** ~10–14 hours · **Prerequisites:** Week 1 (documents as raw inputs)

## Outcomes

- Design **sourcing** pipelines (API, crawl, batch) with backoff and politeness.
- Apply **deduplication** (hash, SimHash/MinHash intuition, embedding clustering).
- Improve **label quality** via audits and weak supervision patterns.
- Draft **governance**: versioning, lineage, access boundaries.

## Self-service flow

1. **[docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-2)** — embeddings / dedup intuition.
2. Days **1–6** below; labs live under `labs/week2/`.
3. Run `python labs/week2/day01_data_sourcing.py` (inspect `--help` if added) and iterate.

## Day-by-day

| Day | Topic | Guide | Lab |
|-----|--------|--------|-----|
| 1 | Data sourcing | [day-01-data-sourcing.md](day-01-data-sourcing.md) | `labs/week2/day01_data_sourcing.py` |
| 2 | Dedup | [day-02-deduplication.md](day-02-deduplication.md) | `labs/week2/day02_deduplication.py` |
| 3 | Semantic dedup | [day-03-semantic-dedup.md](day-03-semantic-dedup.md) | `labs/week2/day03_semantic_dedup.py` |
| 4 | Metadata & taxonomy | [day-04-metadata-taxonomy.md](day-04-metadata-taxonomy.md) | Notebook or script in `labs/week2/` |
| 5 | Labeling & active learning | [day-05-labeling.md](day-05-labeling.md) | Design doc + small prototype |
| 6 | Governance | [day-06-governance.md](day-06-governance.md) | Policy checklist |

## Concepts (AI engineering)

- **Near-duplicate detection** at scale: hash bands vs embedding similarity vs hybrid.
- **Data lineage:** trace dataset version → model artifact → evaluation report.
- **Cost-aware curation:** human labels only where uncertainty is high.

## Done when

- [ ] Three duplicate-detection strategies compared (precision/recall tradeoff in words).
- [ ] One enrichment pipeline diagram (inputs → stores → consumers).
- [ ] Governance section lists owners, PII handling, and rollback for bad batches.
