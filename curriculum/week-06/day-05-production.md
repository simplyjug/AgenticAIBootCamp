# Day 5: Production chunking pipeline

> **Playbook:** [AI_ENGINEERING_PLAYBOOK.md](../../docs/AI_ENGINEERING_PLAYBOOK.md) §10 Production · §17 Cost  
> **Forward link:** `curriculum/week-11` (observability)

---

## 1. From notebook to service

Production chunking is a **stage** in a DAG with:

- **Inputs:** normalized document record (`doc_id`, `mime`, `text` or `blob_uri`, `acl`, `version`).
- **Outputs:** `ChunkRecord[]` each with stable `chunk_id`, `text`, `offsets`, `parent_id?`, `tokenizer_version`, `embed_status`.

Stages must be **idempotent** and **replayable** after failures.

---

## 2. Idempotency & versioning

Define:

```
chunk_id = hash(doc_id + content_hash + chunker_version + tokenizer_version + slice_index)
```

When **chunker_version** bumps, you must **re-chunk** or run a migration job; embeddings tied to old `chunk_id` must be invalidated or remapped.

**Interview:** “We blue/green the **index alias** after backfill completes — not in-place mutation during traffic.”

---

## 3. Async & backpressure

Large PDFs and web crawls must not block API threads.

- Queue (**Celery / RQ / cloud tasks**) with concurrency limits per tenant.
- **DLQ** for poison documents (infinite OCR, corrupt files).
- **Rate limits** on external fetchers.

---

## 4. Monitoring (what to chart)

| Metric | Alert idea |
|--------|------------|
| Chunk count per doc (p95) | Spike → parser bug or wrong MIME |
| Empty chunk rate | Regression in cleaning |
| Tokenizer failures | tiktoken / model mismatch |
| Stage lag seconds | Queue backlog |
| Embed backlog depth | Downstream indexer cannot keep up |

---

## 5. Security & ACL

Chunk text inherits **document ACL**. The indexer must attach `tenant_id` / `allowed_roles[]` to each vector row so retrieval never crosses tenants.

**Interview:** “Chunking is not ‘text only’ — it’s a **security boundary** if you forget metadata.”

---

## 6. Configuration management

Commit a **`chunking.yaml`** (example):

```yaml
version: 2
strategy: recursive
separators: ["\n\n", "\n", " "]
max_tokens: 256
overlap_tokens: 32
parent: section
```

Load in code; reject unknown fields in strict mode to avoid silent typos.

---

## 7. Rollout playbook

1. Shadow mode: new chunker writes to **side index**; compare metrics.  
2. Canary: 5% traffic reads new index.  
3. Full cut + keep old index read-only **48h** for rollback.

---

## 8. Homework (portfolio)

1. Add `chunking.yaml` + loader in `labs/week6/` (small PR-sized change).
2. Write `labs/week6/ROLLOUT.md` with rollback triggers.
3. Optional: Dockerize a worker that pulls from a queue and writes chunk rows to SQLite.

---

## 9. Done when

- [ ] You can narrate **idempotency**, **versioning**, and **rollback** in under 2 minutes.
- [ ] At least **three** metrics identified for dashboards.
- [ ] Read Playbook **§10** once more and highlight one sentence you disagree with (and why) — critical thinking impresses panels.
