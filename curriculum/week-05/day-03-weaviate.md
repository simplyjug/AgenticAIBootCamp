# Day 3: Weaviate & hybrid search

## Learning objectives

- Define a **schema** with vectorizer modules vs bring-your-own vectors.
- Run **hybrid** queries combining BM25 + vector score — understand fusion (`alpha`).

## Hands-on

1. Start Weaviate (docker compose snippet from docs) or use Weaviate Cloud.
2. Create a class `Doc { title text body content vector }` matching tutorial patterns.
3. Issue **hybrid** query with `alpha=0.5` and compare results vs pure vector.

## Concepts

- **Hybrid fusion** reduces “semantic drift” when keywords are distinctive (SKUs, laws).
- **Schema migrations** in vector stores — forward-compatible field additions.

## Done when

- [ ] Example hybrid query JSON logged.
- [ ] When you’d disable BM25 (languages without good tokenizers, etc.).

## Resources

- [Weaviate hybrid search](https://weaviate.io/developers/weaviate/search/hybrid)
