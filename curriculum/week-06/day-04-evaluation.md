# Day 4: Chunk strategy evaluation (science, not taste)

> **Playbook:** [AI_ENGINEERING_PLAYBOOK.md](../../docs/AI_ENGINEERING_PLAYBOOK.md) §8 Evaluation  
> **Lab tie-in:** combine with `labs/week4` / `labs/week9` for metrics code

---

## 1. Scientific method for chunking

Hypothesis → experiment → metric → decision → **versioned** config.

**Bad:** “Overlap 20% felt better.”  
**Good:** “On golden-v0 (N=40 queries), recall@5 improved from 0.62 → 0.71 with +18% index rows; we ship with 15% overlap as Pareto knee.”

---

## 2. What you must freeze

When comparing chunk strategies, **freeze**:

1. Embedder model + pooling  
2. ANN index type and params  
3. Query set and relevance labels  
4. Any reranker (on or off — be consistent)

Only then is the chunk comparison **causal** in the engineering sense.

---

## 3. Metrics (minimum bar)

| Metric | What it tells you |
|--------|-------------------|
| **Recall@k** | Did the right chunk enter top‑k? |
| **MRR** | How high was the first relevant hit? |
| **nDCG** | Useful when relevance is graded (strong > weak) |
| **Answer faithfulness** | Downstream; only after retrieval is sane |

For chunk-only iteration, **retrieval metrics** are enough — do not confuse with end-task success yet.

---

## 4. Building a golden set (practical)

1. Sample **real user queries** or plausible synthetic paraphrases.  
2. For each query, label **one or more** `chunk_id` that contain the answer span.  
3. Store as `golden_set.jsonl` with schema:

```json
{"query_id": "q1", "query": "...", "relevant_chunk_ids": ["c_12", "c_13"], "difficulty": "hard"}
```

4. Version with git tag `eval/golden-v0`.

---

## 5. Slice analysis (senior signal)

Report metrics by:

- Document length bucket  
- Language  
- Domain (finance vs engineering docs)

**Interview:** “Aggregate recall hid a **40-point** gap on Japanese PDFs — we fixed OCR + tokenizer, not chunk overlap.”

---

## 6. Homework

1. Produce **one** markdown table comparing **two** chunk strategies on the same golden set.
2. Add a **pytest** that fails if recall@5 drops below a threshold on a **synthetic** toy index (fast CI guard).
3. Write `labs/week6/EVAL_PROTOCOL.md` documenting freezes and commands.

---

## 7. Done when

- [ ] Numbers, not adjectives, justify your chosen chunk config.
- [ ] Golden set exists (even tiny) with clear versioning story.
- [ ] You can defend **why** you did not chase higher recall if cost exploded.
