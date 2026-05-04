# Day 2: Milvus & Pinecone (managed vs self-hosted)

## Learning objectives

- Map **collection / index / partition** concepts to Milvus; **index + namespace** to Pinecone.
- Run a **hello query** against one cloud or local instance (free tier or docker).
- Compare **ops burden:** who patches OS, who handles replication.

## Hands-on

1. Follow official quickstart for **one** of: Milvus standalone (docker), Pinecone free index, or Zilliz Cloud trial.
2. Upsert **100** 384-dim vectors with metadata `{source, ts}`.
3. Query with metadata filter `source == "wiki"` and report latency.

## Concepts

- **Eventual consistency** in managed ANN — know refresh intervals.
- **Cost model:** read units, write units, storage — back-of-napkin for 1M vectors.

## Done when

- [ ] Screenshot or log of successful filter query.
- [ ] 5 bullets: Milvus vs Pinecone for *your* constraints.

## Resources

- [Milvus quickstart](https://milvus.io/docs/install_standalone-docker.md) · [Pinecone quickstart](https://docs.pinecone.io/docs/quickstart)
