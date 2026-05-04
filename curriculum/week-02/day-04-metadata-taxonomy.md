# Day 4: Metadata enrichment & taxonomy

## Learning objectives

- Build a **controlled vocabulary** for tags (no free-text chaos until necessary).
- Connect taxonomy nodes to **downstream filters** in retrieval (Week 10 preview).

## Hands-on

1. Draft `taxonomy.yaml` with domains relevant to your corpus (≥15 leaf tags).
2. Label **50** docs with ≥1 tag each (spreadsheet export CSV acceptable).
3. Compute tag **frequency** — merge ultra-rare tags into “other” bucket policy.

## Concepts

- **Stable IDs:** never rename leaf IDs in place — deprecate + map instead.

## Done when

- [ ] Taxonomy file + README on governance (who approves new tags).
- [ ] Example query using tags + future vector retrieval narrative.

## Resources

- [SKOS primer](https://www.w3.org/TR/skos-primer/) — skim for enterprise taxonomy mindset
