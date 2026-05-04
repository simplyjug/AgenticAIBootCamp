# AI engineering playbook — from data to deployed agents

**Audience:** Engineers targeting **applied AI**, **LLM platform**, **RAG**, and **agentic systems** roles (OpenAI, Anthropic, NVIDIA, Meta, startups).  
**How to use:** Read linearly once, then use **§ numbers** as spaced-repetition before interviews. Pair with `labs/` and `curriculum/`.

---

## §0. Role definition — what “AI engineer” means now

You are expected to blend:

- **Software engineering** — APIs, typing, tests, observability, security.
- **ML systems** — data quality, evaluation, drift, cost/latency tradeoffs.
- **LLM-specific craft** — prompting, context construction, tool design, agent control flow.

**Interview framing:** “I own the **vertical slice** from ingestion quality to user-visible answer quality, including evals and rollback — not only the Jupyter notebook.”

---

## §1. Mental model — the modern LLM stack

```
Sources → Ingest/Clean → Chunk → Embed → Index (ANN) → Retrieve (± rerank)
    → Assemble context → Generate → Guardrails → Log/Eval → Ship/Iterate
```

**Non-goals:** Training frontier LLMs from scratch (different job). **Your job:** compose, evaluate, operate.

---

## §2. Data & curation (everything rests on this)

### 2.1 Quality dimensions

- **Coverage** — Do we have the right documents?
- **Freshness** — Stale docs worse than missing docs for some domains.
- **Deduplication** — Near-dupes waste index budget and confuse retrieval.
- **PII / secrets** — Quarantine before embed; scan at ingest.

### 2.2 Lineage

Store: `doc_id`, `source_url`, `ingest_version`, `hash`, `acl`, `language`.  
**Interview:** “We can replay ingest and know which model saw which snapshot.”

### 2.3 Leakage (silent killer)

Train/test contamination, future dates in text, filenames that reveal labels — **audit** before trusting metrics.

---

## §3. Classification (still everywhere)

Even “just RAG” uses classifiers: intent routing, safety classifiers, language ID, document type.

**Calibration:** threshold on probabilities must be **tuned on validation**, not default 0.5.  
**Slices:** report metrics per language/region/product line — aggregates lie.

**Interview:** “I’d ship a **shadow** intent classifier before switching router traffic.”

---

## §4. Embeddings — geometry, similarity, drift

### 4.1 Cosine vs dot product

For **L2-normalized** vectors, cosine similarity equals dot product. If not normalized, dot product favors long vectors — know when your stack normalizes.

### 4.2 ANN vs exact

ANN (HNSW, IVF-PQ) trades recall for speed. **Always** measure **recall@k** vs brute force on a sample before trusting index params.

### 4.3 Drift

Embedding drift = query distribution or document mix shifted. Signals: centroid movement, neighbor overlap drop, NDCG collapse on golden set.

**Mitigation:** periodic re-embed hot docs; versioned embedding namespace; canary new embedder.

---

## §5. Chunking — a retrieval policy, not preprocessing trivia

Chunk size/shape dominates **precision** of first-stage retrieval.

- Too large → noise in context; too small → fragmented concepts.
- **Overlap** reduces boundary misses; increases storage.
- **Parent–child** — retrieve child, expand parent for reader context.

**Interview:** “I’d run a **chunk sweep** with frozen embedder and measure recall@k before touching the LLM prompt.”

---

## §6. RAG architecture (interview bread and butter)

### 6.1 Naive RAG

Retrieve top-k → concatenate → generate. **Baseline** everyone should implement once.

### 6.2 Hybrid retrieval

Dense (embedding) + sparse (BM25). Fusion: RRF or weighted sum. **When BM25 wins:** SKUs, legal citations, rare tokens.

### 6.3 Query transformation

Multi-query, HyDE, step-back prompts — **cost latency**; only adopt with eval proof.

### 6.4 Reranking

Two-stage: ANN recall **wide** (100–200), cross-encoder or mono-t5 style reranker to **narrow** (5–10). Watch **p95** budget.

### 6.5 Agentic RAG

Retriever becomes a **tool** inside a loop. See [AGENTIC_AI_ENGINEERING.md](AGENTIC_AI_ENGINEERING.md).

### 6.6 Citations & grounding

Every claim should map to `chunk_id`. UI shows sources. **Failure:** “model sounds confident with empty retrieval” — detect `no_docs` path.

---

## §7. Context construction & prompts

- **Order effects** (lost-in-the-middle) — put critical evidence at **edges** when using long context.
- **Structured wrappers** — XML-ish tags or JSON blocks for chunks reduce conflation.
- **System vs developer vs user** boundaries — know your API’s message hierarchy.

**Version prompts** like code (`prompts/rag/v1.3.txt` + changelog).

---

## §8. Evaluation — how you earn trust

### 8.1 Retrieval metrics

- **Recall@k**, **MRR**, **nDCG** — need labeled pairs `(query, relevant_ids)`.
- Build a **golden set** early; freeze it; version it.

### 8.2 Generation metrics

- **Faithfulness** — supported by cited context (LLM judge + human spot checks).
- **Usefulness** — task completion (harder; often human rubric 1–5).

### 8.3 LLM-as-judge pitfalls

Position bias, verbosity bias, **judge model mismatch** with production model — mitigate with **pairwise** comparisons and periodic human calibration.

### 8.4 Online vs offline

Offline catches regressions; online (A/B) catches real user intent shift. Define **guardrail metrics** (toxicity rate, abstain rate) before shipping A/B.

---

## §9. Metadata & hybrid filters

Filters reduce candidate space — **pre-filter vs post-filter** latency story matters.

Design **schema** with explicit `filterable` fields vs display-only. Plan **schema migrations** without breaking clients.

---

## §10. Production engineering

### 10.1 Observability

Log: `trace_id`, `latency_ms` per stage, `retrieval_scores`, `model_name`, `token_in/out`, `error_code`.  
Metrics: RPS, p95/p99 latency, error rate, **empty retrieval rate**, cost per query.

### 10.2 Reliability

Timeouts per dependency, retries only where **idempotent**, circuit breakers, graceful degradation (keyword fallback).

### 10.3 Deployment

Blue/green or canary for **prompt** and **index** changes separately when possible.

### 10.4 Cost

Cache **embeddings** for repeated queries; be cautious caching **answers** if facts change. Track **$/1k queries** and **$/1M tokens**.

### 10.5 Multi-tenant

Isolation at **API key**, **index namespace**, and **network** layers. Test cross-tenant queries in CI.

---

## §11. Safety, abuse, compliance

- **Prompt injection** via user text **and** retrieved docs — defense in depth: isolate instructions, strip unknown HTML, tool egress allowlists.
- **Output policies** — refusal templates, PII blockers, secret scanners on model output.
- **Red teaming** — structured suites + periodic external review for high-risk domains.

---

## §12. System design templates (whiteboard)

### 12.1 “Design Slack’s internal Q&A bot”

Clarify: data residency, ACL per channel, freshness, human feedback loop, eval metrics, incident response.

Sketch: connectors → queue → chunk/embed → vector index per workspace → router → RAG → audit log.

### 12.2 “100M PDFs, 10k QPS read”

Partition by tenant/shard; offline GPU embedding fleet; online CPU ANN; **regional** indexes; CDN for nothing sensitive; strict ACL on retrieval path.

### 12.3 “Model update without downtime”

Dual-write new embeddings to shadow index; compare recall on golden set; hot-swap alias; rollback pointer.

---

## §13. Quick question bank (answer in 60–90 seconds each)

Practice aloud:

1. When would you **not** use RAG?
2. How do you detect **embedding drift** in production?
3. Why **hybrid** search?
4. How do you stop an **agent loop**?
5. What’s in your **on-call runbook** for empty retrieval spikes?
6. How do you **version** prompts and indexes together?
7. How do you evaluate **faithfulness** cheaply?
8. What breaks when context window hits **2M tokens**?
9. How do you **test** tool-using agents?
10. What is your **rollback** for a bad deploy?

(Add 20 more from your own failure stories.)

---

## §14. Map to this repo

| Topic | Where |
|-------|--------|
| Ingestion | `curriculum/week-01`, `labs/week1`, `src/ingestion` |
| Data / dedup | `curriculum/week-02`, `labs/week2` |
| Classification | `week-03`, `labs/week3` |
| Embeddings / FAISS | `week-04`, `labs/week4` |
| Vector DBs | `week-05`, `labs/week5` |
| Chunking | `week-06`, `labs/week6` |
| RAG / chat | `week-07`, `week-08`, `labs/week7`, `labs/week8` |
| Eval | `week-09`, `labs/week9` |
| Metadata | `week-10`, `labs/week10` |
| Prod | `week-11` |
| Agentic | `week-12`, [AGENTIC_AI_ENGINEERING.md](AGENTIC_AI_ENGINEERING.md) |
| Multi-agent | `week-13`, `labs/week13` |
| Capstone | `week-14` |

---

## §15. Closing — what “very good” looks like

You can **draw** the system, **name** three failure modes with mitigations, **cite** metrics you’d watch, and **show** code or a PR that proves you shipped the hard parts. This playbook is the **spine**; your fork is the **proof**.

Continue: [INTERVIEW_COMPANION.md](INTERVIEW_COMPANION.md) · [CAREER_PORTFOLIO.md](CAREER_PORTFOLIO.md) · [VIDEO_RESOURCES.md](VIDEO_RESOURCES.md).

---

## §16. RAG failure taxonomy (memorize)

| Symptom | Likely cause | First checks |
|---------|----------------|--------------|
| Correct answer but no citations | Prompt allows unstated inference | tighten “answer only from context”; add `no_answer` path |
| Citations irrelevant | Bad retrieval / wrong embedder | hybrid search; reranker; query rewrite |
| Contradictions in answer | Chunks disagree | dedupe corpus; add “conflict” detection; ask clarifying |
| Empty retrieval | over-filter; wrong language; index stale | relax filters; language detect; index health |
| Slow p95 | huge chunks; no cache; serial tool calls | shrink chunks; cache embeds; parallelize |
| Cost spike | huge context every turn | summarize history; compress retrieved text |

---

## §17. Cost model (back-of-envelope template)

Per **1,000** user queries, estimate:

- **Embedding tokens** (query side) + **cached?**
- **Retrieved tokens** sent to LLM (dominant variable)
- **Output tokens**
- **Reranker** calls (CPU/GPU or API)
- **Vector DB** read units

**Interview:** “I’d put **budget caps** per user tier and degrade gracefully (shorter context, cheaper model) rather than surprise bills.”

---

## §18. Consistency & determinism (when it matters)

LLMs are stochastic. For **regulated** flows:

- Lower temperature for extraction; **structured outputs** (JSON schema) with validation/repair loop.
- Separate **creative** vs **factual** tasks — different models/settings.
- Log **full** prompt + tool I/O for replay where policy allows (redact PII).

---

## §19. GPU vs CPU (NVIDIA-style talking points)

- **Offline index build** — GPU batch embedding can amortize cost over huge corpora.
- **Online path** — often CPU ANN + small reranker; GPU when single-node LLM self-hosted.
- **Batching** — dynamic batching improves throughput at cost of tail latency — expose **SLO** tension.

---

## §20. Open research you can cite humbly

- **Lost in the middle** — motivates reranking and chunk ordering.
- **RAG vs long context** — context helps but does not replace **fresh** and **permissioned** retrieval.
- **Tool use reliability** — still active area; your edge is **engineering discipline** (tests, budgets, audits).

---

## §21. One-week “interview sprint” schedule

| Day | Morning | Afternoon |
|-----|---------|-------------|
| 1 | Read this playbook + draw architecture | Implement recall@k on toy set |
| 2 | Hybrid retrieval reading + notes | Extend `rag_service` with logging |
| 3 | Agentic patterns doc + trace design | Add max-steps + tool audit stub |
| 4 | Interview companion + mock aloud | Write 5 STAR stories tied to this repo |
| 5 | System design whiteboard x2 | Load test script skeleton + results template |

---

## §22. Integrity (again)

Interviewers probe **depth on one axis**. Pick **two** strengths (e.g., eval + prod) and **one** honest gap you are closing. Never bluff frontier research — **ship discipline** wins more offers than buzzwords.
