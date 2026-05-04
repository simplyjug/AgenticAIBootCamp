# Week 5: Module 4 — Vector databases deep dive

**Time:** ~12–16 hours (with Docker) · **Prerequisites:** Week 4 (FAISS, embeddings)

## Outcomes

- Operate **FAISS** in a service-shaped mental model (build, persist, query).
- Contrast **Milvus, Pinecone, Weaviate** for metadata filters and ops.
- Design **multi-tenant** isolation and **index rebuild** playbooks.

## Self-service flow

1. **[docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-5)**.
2. Start local vector DBs via [SETUP.md](../../SETUP.md) / `docker-compose` if available.
3. Use `labs/week5/` exercises (stubs you can extend) and day guides.

## Reading-only path

This week explains vector databases and production index design. Reading-only learners should understand the characteristics of each store and how metadata interacts with search.

- Learn the difference between FAISS, Milvus, Pinecone, and Weaviate.
- Understand filterable retrieval, schema modeling, and index rebuild patterns.
- Think through multi-tenant isolation, API keys, and RBAC boundaries.
- Note how operational burdens change with cloud vs self-hosted DBs.

Summarize one vector store decision, one filter design, and one rebuild/playbook strategy.

## Day-by-day

| Day | Topic | Guide | Notes |
|-----|--------|--------|--------|
| 1 | FAISS production | [day-01-faiss.md](day-01-faiss.md) | Benchmark script |
| 2 | Milvus & Pinecone | [day-02-milvus-pinecone.md](day-02-milvus-pinecone.md) | Cloud + local |
| 3 | Weaviate & filters | [day-03-weaviate.md](day-03-weaviate.md) | Schema + hybrid |
| 4 | Index tuning | [day-04-index-tuning.md](day-04-index-tuning.md) | Rebuild SLO |
| 5 | Multi-tenant | [day-05-multitenant.md](day-05-multitenant.md) | Namespaces, RBAC |

## Concepts

- **Filterable ANN:** pre-filter vs post-filter, and why latency spikes.
- **Capacity planning:** QPS, dimension, HNSW `efSearch`, memory headroom.

## Done when

- [ ] Diagram of your **target** production store (one page).
- [ ] One load test or scripted batch insert with metrics captured.
- [ ] Tenancy model written down (org → index/collection → API key).

## Portfolio path

This week’s portfolio artifact should be a production design note:

- One **vector store architecture diagram** with store choice rationale.
- One **load test or insertion plan** with observed metrics.
- One **interview story** about choosing a vector database and handling tenant isolation.

If you are reading only, write a note that contrasts the vector stores and explains the index/tenant model.
