# Day 2: Topic modeling & taxonomy design

> **Playbook:** [AI_ENGINEERING_PLAYBOOK.md](../../docs/AI_ENGINEERING_PLAYBOOK.md) §9  
> **Career:** [CAREER_PORTFOLIO.md](../../docs/CAREER_PORTFOLIO.md) §4 (what to add in your fork)

---

## 1. Why taxonomies still matter

Embeddings capture **similarity**, not **obligation**. Enterprise search often needs **hard** boundaries: “only HR policy,” “only customer X data,” “only post-2024 compliance.” Taxonomy + ACL metadata implements those boundaries **before** vector magic runs.

---

## 2. LDA vs modern alternatives

- **LDA / NMF** — fast, interpretable baselines; weak on short texts.
- **BERTopic** — clusters embeddings + c-TF-IDF; good exploration.
- **LLM assignment** — flexible labels; expensive; needs **rubric** and validation.

**Interview:** “I’d use BERTopic to **suggest** clusters, but humans **approve** leaf nodes before wiring to production filters.”

---

## 3. Designing stable IDs

Bad: free-text topic = `"Returns"` vs `"returns "` vs `"RETURNS"`.  
Good: canonical `topic_id = hr.policy.leave.v2` with display name mapped in UI.

**Migration:** never rename IDs in place — deprecate `...v1` with mapping table.

---

## 4. Hands-on

1. Author `labs/week10/taxonomy.json` with ≥15 **leaf** nodes across 3 branches.
2. Label 20 documents → leaf IDs; compute **confusion pairs** (where you hesitated).
3. Optional: run BERTopic on a CSV of abstracts; compare its clusters to your manual tree — write 10 bullets of insights.

---

## 5. Downstream retrieval

Taxonomy becomes:

- **Pre-filter** in Milvus/Weaviate/ES hybrid queries.
- **Boost** signal (multiply score) rather than hard filter when recall is fragile.

Document **relaxation policy** when filters return <3 results (Playbook §9).

---

## 6. Done when

- [ ] `taxonomy.json` committed with stable IDs.
- [ ] Written governance: who can add a leaf node?
- [ ] One paragraph linking taxonomy to **security** (wrong bucket = wrong ACL).
