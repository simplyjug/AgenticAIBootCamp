# Day 3: Parent–child & hierarchical chunking

> **Playbook:** [AI_ENGINEERING_PLAYBOOK.md](../../docs/AI_ENGINEERING_PLAYBOOK.md) §5  
> **Also read:** [AGENTIC_AI_ENGINEERING.md](../../docs/AGENTIC_AI_ENGINEERING.md) §3.3 (router pattern — analogy: parent scope)

---

## 1. Core idea

**Child chunks** (small) are indexed for **high precision** retrieval.  
**Parent spans** (large — section, article, parent paragraph) provide **context** for the generator after a child hits.

Why it works: small chunks place the needle in embedding space; large parents restore **surrounding clauses** the model needs for faithful generation (policies, contracts, runbooks).

---

## 2. Data model (what you store)

Minimum viable schema (conceptual):

| Field | Purpose |
|-------|---------|
| `child_id` | Stable ID for vector row |
| `child_text` | Embedded text |
| `parent_id` | Foreign key to parent record |
| `parent_text` or `parent_uri` | Text blob or blob-store pointer |
| `offsets` | Optional traceability to source PDF/HTML |

At query time:

1. ANN search returns top‑k **children**.
2. Map to **unique parent_ids** (dedupe).
3. Concatenate parent texts with **budget** (max tokens) — may need summarization if many children hit different parents.

---

## 3. Tradeoffs (memorize)

| Pro | Con |
|-----|-----|
| Better precision than giant chunks alone | Parent blow-up: many children → huge context |
| Explainable “why this paragraph” | More complex ingest; two-level consistency |
| Works well for structured docs | Poor for unstructured chat logs without hierarchy |

**Interview question:** “What if 10 retrieved children map to **10 different parents**?”  
Answer: cap parents, **score** parents by aggregate child scores, or **summarize** each parent first — this is a product decision with cost implications.

---

## 4. Implementation sketch (hands-on)

Without a full DB, simulate in Python:

```python
children = [{"id": "c1", "text": "...", "parent_id": "p1"}, ...]
parents = {"p1": "FULL SECTION TEXT ...", ...}

def expand(children_hits, max_parents=3, max_chars=8000):
    seen = []
    for c in children_hits:
        if c["parent_id"] not in seen:
            seen.append(c["parent_id"])
        if len(seen) >= max_parents:
            break
    blob = "\n\n".join(parents[pid] for pid in seen)
    return blob[:max_chars]
```

Add **ordering**: parents sorted by **best child rank**.

---

## 5. Evaluation

Compare **parent–child** vs **flat large chunks** vs **flat small** on the same golden queries:

- **Recall@k** on child index (does the right child surface?)
- **Faithfulness** on final answers (does parent context reduce hallucination?)

Document **confounders**: if embedder or reranker changes, invalidate comparison.

---

## 6. Failure modes

- **Stale parent** updated but children not re-embedded — version parent and bump `child_version` on change.
- **Wrong parent link** from buggy parser — catastrophic wrong answers; add **checksum** sampling in QA.

---

## 7. Done when

- [ ] Working simulation OR schema diagram checked into `labs/week6/`.
- [ ] Written rule for **max parents** and **overflow** handling.
- [ ] You can whiteboard the data flow in **90 seconds**.
