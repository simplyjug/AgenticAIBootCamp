# Day 4: Production enrichment pipeline (async, idempotent, observable)

> **Playbook:** [AI_ENGINEERING_PLAYBOOK.md](../../docs/AI_ENGINEERING_PLAYBOOK.md) §10  
> **Prior day:** [day-03-schema-design.md](day-03-schema-design.md)

---

## 1. Problem

NER, keywords, topics, and embeddings **must not** block the synchronous ingest API. Users expect upload ACK fast; enrichment can lag **seconds to minutes** with clear status.

---

## 2. Pipeline shape

```
ingest_complete(doc_id) -> enqueue EnrichJob
worker: load doc -> run NER -> run keywords -> merge -> validate against schema -> upsert index row -> mark status=READY
```

**States:** `RECEIVED`, `ENRICHING`, `READY`, `FAILED` (+ `reason_code`).

---

## 3. Idempotency

Jobs keyed by `(doc_id, enrichment_version)`. Re-running after crash should **overwrite** the same logical artifact, not duplicate rows.

Use **outbox pattern** if you need exactly-once to external systems.

---

## 4. Retries & poison messages

- Transient errors (rate limit) → exponential backoff with jitter.
- Permanent errors (schema violation) → DLQ + alert; do not infinite spin.

---

## 5. Observability

Per stage timings as histograms: `enrich_ner_ms`, `enrich_keywords_ms`, `embed_ms`, `index_ms`.

Logs must include `doc_id`, `tenant_id`, `job_id` — **never** raw PII in log message text; use hashed IDs where required.

---

## 6. Hands-on

1. Write `labs/week10/enrichment_stub.py` with a queue interface (`enqueue`, `worker_loop` fake sleep).
2. Add **retry** decorator with max 3 attempts.
3. Document states in `labs/week10/ENRICHMENT_STATES.md`.

---

## 7. Done when

- [ ] State machine diagram (ASCII or image) in repo.
- [ ] Clear **SLA** statement: e.g., “p95 READY < 5 min for docs < 2MB.”
- [ ] You can explain **outbox** vs “fire-and-forget HTTP” in an interview.
