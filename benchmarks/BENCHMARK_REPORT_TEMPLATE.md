# Benchmark Report Template

**Bootcamp: Advanced AI Engineering & RAG Systems**

---

## Benchmark Metadata

| Field | Value |
|-------|-------|
| **Run Date** | YYYY-MM-DD |
| **Environment** | local / staging / production |
| **Hardware** | CPU, RAM, GPU (if applicable) |
| **Dataset** | Name, size, characteristics |

---

## Ingestion Pipeline Benchmark

| Metric | Value |
|--------|-------|
| Documents processed | |
| Throughput (docs/sec) | |
| Avg latency per document (ms) | |
| P95 latency (ms) | |
| P99 latency (ms) | |
| Error rate (%) | |
| Memory peak (GB) | |

### By Document Type

| Type | Count | Avg Latency | Error Rate |
|------|-------|-------------|------------|
| PDF (text) | | | |
| PDF (scanned) | | | |
| HTML | | | |

---

## Embedding Benchmark

| Metric | Value |
|--------|-------|
| Embedding model | |
| Batch size | |
| Throughput (embeddings/sec) | |
| Latency P50 (ms) | |
| Latency P99 (ms) | |

---

## Retrieval Benchmark

| Metric | Index | Value |
|--------|-------|-------|
| Recall@1 | FAISS | |
| Recall@5 | FAISS | |
| Recall@10 | FAISS | |
| Latency P50 (ms) | | |
| Latency P99 (ms) | | |

---

## End-to-End RAG Benchmark

| Metric | Value |
|--------|-------|
| Total latency (query → response) P50 | |
| Total latency P99 | |
| Retrieval portion (%) | |
| Generation portion (%) | |

---

## Conclusions

- Key findings
- Bottlenecks identified
- Recommendations
