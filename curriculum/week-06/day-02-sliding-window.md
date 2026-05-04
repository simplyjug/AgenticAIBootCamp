# Day 2: Sliding window & overlap tuning

> **Playbook:** [AI_ENGINEERING_PLAYBOOK.md](../../docs/AI_ENGINEERING_PLAYBOOK.md) §5 · §16 (failure taxonomy)  
> **Lab:** `labs/week6/chunk_strategies.py` (`chunk_fixed_size`)

---

## 1. Problem statement

Facts often sit **on the boundary** between two fixed windows. Without overlap, a query that should match “the sentence pair” might retrieve **neither** window with strong score — a classic **recall** loss that no reranker can fix if the right text never entered the candidate set.

**Overlap** duplicates text across consecutive windows so at least one window contains a complete local context.

---

## 2. What you are sweeping

Parameters:

- **Window size** \(W\) (in words, chars, or tokens — be explicit in reports).
- **Stride** \(S = W - O\) where \(O\) is overlap in the same units.

Constraints:

- \(0 \leq O < W\) (overlap equals window is useless duplication of entire doc in many windows).
- Larger \(O\) → more chunks → **higher** ingest cost and ANN memory.

---

## 3. Experiment design (do this, not vibes)

1. **Freeze** embedder and index params.
2. Pick **15–50** queries with labeled **gold chunk IDs** (even hand-labeled on a small corpus).
3. Sweep \(O \in \{0, 10\%, 20\%, 30\%\}\) of \(W\) (or fixed token overlaps if using tiktoken).
4. Report **recall@5**, **mean chunks per doc**, and **duplicate n-gram rate** (proxy for wasted context at generation time).

**Interview line:** “I report **Pareto** curves, not a single magic overlap — the knee depends on corpus layout.”

---

## 4. Interaction with downstream generation

At **generation** time, overlapping chunks can produce **redundant** evidence in the prompt — the model may repeat itself or attend to duplicates (“lost in the middle” gets worse if you stuff redundant paragraphs).

Mitigations:

- **Dedupe at prompt assembly** — union chunks by `chunk_id`, or MMR-style diversity pruning.
- **Rerank** after retrieval to drop near-duplicate chunks (cross-encoder sees paraphrase overlap).

---

## 5. Code tasks

1. Extend `chunk_fixed_size` logging to print **chunk count** and **overlap fraction** per document.
2. Add a function `duplicate_rate(chunks, n=5)` using hashed character n-grams — rough redundancy metric.
3. Plot (matplotlib or CSV + Excel) **recall@5 vs chunk count** across overlap settings.

---

## 6. Failure modes

| Symptom | Cause | Mitigation |
|---------|-------|------------|
| Recall improves but latency spikes | Too many chunks per query path | cap max chunks in prompt; pre-merge |
| Same wrong answer | Redundant misleading chunks | dedupe; diversify retrieval |
| Index huge | overlap too high | reduce O; hierarchical chunking instead |

---

## 7. Interview prompts

- **How do you pick overlap without labels?**  
  Start with 10–20% of window on prose; lower on highly structured logs; always validate with **human** spot checks before expensive golden set work.

- **Does sliding window replace sentence chunking?**  
  Often you **compose**: sentence chunk first, then pack sentences into max-token windows with controlled overlap.

---

## 8. Done when

- [ ] Table of ≥3 overlap settings with recall@k **and** chunk count.
- [ ] One paragraph on **dedupe** before LLM prompt assembly.
- [ ] Linked this experiment to a **versioned** config file committed in git.
