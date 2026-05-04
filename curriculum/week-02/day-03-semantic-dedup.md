# Day 3: Semantic dedup & noise reduction

## Learning objectives

- Cluster near-duplicates using **embedding similarity** (threshold + transitive closure caution).
- Measure **noise**: OCR junk lines, boilerplate — filters before dedup.

## Hands-on

1. Run `labs/week2/day03_semantic_dedup.py`; extend with a configurable **cosine threshold**.
2. For one cluster with >3 items, manually inspect — are they true dupes?
3. Add **representative selection**: keep shortest clean doc or highest OCR confidence.

## Concepts

- **Transitive duplicates:** A≈B and B≈C but A≉C — consider hierarchical clustering or union-find with care.
- **Semantic dedup risks:** paraphrases wrongly merged — require **high** thresholds for deletion.

## Done when

- [ ] Histogram or stats table of intra-cluster similarity.
- [ ] Written rule for **hard delete** vs **soft link** duplicate records.

## Resources

- [docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-2)
