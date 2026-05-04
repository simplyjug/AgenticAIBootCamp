# Interview companion — oral exam prep for AI / LLM / RAG roles

Use with [AI_ENGINEERING_PLAYBOOK.md](AI_ENGINEERING_PLAYBOOK.md), [AGENTIC_AI_ENGINEERING.md](AGENTIC_AI_ENGINEERING.md), and [CAREER_PORTFOLIO.md](CAREER_PORTFOLIO.md). **Practice out loud**; reading silently is not enough.

---

## Part A — How you open an answer (30 seconds)

Structure every design answer:

1. **Clarify** — users, scale, latency SLO, privacy, offline vs online updates.
2. **Baseline** — simplest architecture that could work.
3. **Iterate** — add hybrid retrieval, reranker, cache, eval, agents only with **reason**.
4. **Tradeoffs** — cost, complexity, failure modes, team skill.
5. **Rollout** — shadow → canary → full; rollback triggers.

---

## Part B — System design prompts (with skeleton answers)

### B1. “Build ChatGPT over our Google Drive”

**Skeleton:** OAuth + incremental sync → object store raw files → parser pipeline → chunk/embed → per-user ACL vector index (or shared index + strict filter on `acl_user_ids`) → RAG API with citation → audit log → eval golden set from real support tickets → rate limits + abuse detection.

**Push:** “I’d **never** send all Drive to one flat index without ACL in the retrieval path — that’s a data exfiltration incident.”

### B2. “Latency p95 must be under 2 seconds”

**Skeleton:** parallel embed query + ANN; cap `top_k`; rerank only top 32; stream first token; cache frequent queries; warm pools; avoid giant PDFs in one chunk pass — precompute.

### B3. “We have 50 languages”

**Skeleton:** language detect on query; route to language-specific embedder or multilingual model; separate indexes vs shared + filter; measure **per-language** recall slice.

### B4. “How do you update the index hourly?”

**Skeleton:** CDC or event stream of doc changes → incremental delete/update vectors; background workers; **dual-buffer** index swap; monitor lag; SLA on “staleness.”

### B5. “Model says wrong medical facts”

**Skeleton:** high-risk domain → stricter abstain; human-in-the-loop; **secondary** verification chain; no single-model path; regulatory logging; possibly smaller model with higher precision on policy excerpts only.

---

## Part C — Deep technical rapid-fire (answer format: definition + why + pitfall)

**Q: What is MRR?**  
Mean reciprocal rank of first relevant hit. Sensitive to first position — good when one gold doc exists.

**Q: Why cosine similarity?**  
Scale-invariant direction similarity when vectors normalized; dot product equivalent then.

**Q: IVF vs HNSW?**  
IVF: partition cells, probe nprobe cells — good large-scale; HNSW: graph navigates — often better recall/latency balance but heavier memory.

**Q: What is RRF?**  
Reciprocal Rank Fusion merges ranked lists without score calibration — useful hybrid fusion.

**Q: Temperature vs top-p?**  
Both shape randomness; for factual RAG often **low** temperature + structured output.

**Q: KV cache?**  
Reuse prefix activations across tokens — critical for long conversations; affects batching and memory planning for self-hosted inference.

**Q: LoRA vs full fine-tune?**  
LoRA adapts small adapters — cheaper; full FT when data large and distribution shift huge.

**Q: When does RAG lose to fine-tune?**  
Style/format inside narrow domain with abundant supervised pairs; still often **combine** (FT embedder + RAG).

---

## Part D — Behavioral (STAR) templates

Situation → Task → Action → Result (with **numbers**).

Fill five stories from this repo:

1. **Debugging** — empty retrieval; what you measured; fix.
2. **Performance** — p95 regression; profiling; fix.
3. **Conflict** — PM wanted feature that hurt safety; how you negotiated.
4. **Mistake** — wrong metric optimized; how you corrected.
5. **Leadership** — mentored someone on eval discipline.

---

## Part E — Agentic & safety (favorite at frontier labs)

Be ready to whiteboard:

- Tool schema + validation + idempotency for writes.
- Max steps + cost cap + duplicate tool call detection.
- Injection via retrieved document — mitigations (instruction/data isolation, cite-only, allowlisted tools).
- **Human-in-the-loop** placement in graph (before send-email, not after).

---

## Part F — “Do you have questions for us?”

Good questions reveal seniority:

- How do you **version** prompts vs model weights in prod?
- What is the **top incident class** for the LLM stack last quarter?
- How is **ground truth** for eval created and maintained?
- What is the **approval process** for new tools or new data sources?

---

## Part G — 60-second “why you” closing

“I ship **measured** LLM systems: golden sets, hybrid retrieval, strict tool boundaries, and dashboards for latency and empty retrieval. I want to work where that bar is the default — I’m excited about **your** [product] because [specific].”

---

## Part H — Checklist the night before

- [ ] Sleep > cramming last 30 pages.
- [ ] Repo runs: `pytest`, one `uvicorn` demo path.
- [ ] Three diagrams drawn from memory.
- [ ] Five numbers memorized (even approximate) from your own runs.

Good luck. You are building a **craft**, not collecting certificates.
