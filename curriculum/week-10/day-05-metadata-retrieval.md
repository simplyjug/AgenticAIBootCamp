# Day 5: Metadata-first retrieval UX & relaxation policies

> **Playbook:** [AI_ENGINEERING_PLAYBOOK.md](../../docs/AI_ENGINEERING_PLAYBOOK.md) §9 · §16  
> **Agentic:** filters injected server-side — see [AGENTIC_AI_ENGINEERING.md](../../docs/AGENTIC_AI_ENGINEERING.md) §2.1

---

## 1. User-visible retrieval

Power users want **facets** (topic, date, author). Casual users want **answers**. Your API must support **progressive disclosure**: start strict, relax when empty.

---

## 2. Relaxation algorithm (example)

1. Run query with all active user filters.  
2. If `hits < k_min`, drop **lowest priority** filter (e.g., `department` before `tenant`).  
3. Never drop `tenant_id` or `acl` — non-negotiable.  
4. Return metadata to UI: `relaxed_filters: ["department"]` for transparency.

**Trust:** users forgive fewer results more than wrong-tenant results.

---

## 3. Hybrid scoring with metadata boosts

Instead of binary filter, try **boost**:

\[
\text{score} = w_{\text{vec}} s_{\text{vec}} + w_{\text{bm25}} s_{\text{bm25}} + w_{\text{meta}} \mathbb{1}[\text{topic matches}]
\]

Tune \(w_{\text{meta}}\) offline — too high collapses recall on rare topics.

---

## 4. Evaluation

Measure:

- **Zero-hit rate** before/after relaxation policy change.  
- **CTR** on relaxed searches (if product telemetry exists).  
- **Precision@k** on golden queries with filters ON.

---

## 5. Hands-on

1. Implement `relax_filters(query, filters, min_hits=5)` pseudo-code in `labs/week10/relaxation.md`.
2. List **priority order** for your domain’s filters with rationale.
3. Optional: simulate in a notebook with fake hit counts.

---

## 6. Done when

- [ ] Written policy for **which filters never relax**.
- [ ] UX copy examples: honest messages when widening search.
- [ ] Linked this behavior to **safety** (ACL) in 3 sentences.
