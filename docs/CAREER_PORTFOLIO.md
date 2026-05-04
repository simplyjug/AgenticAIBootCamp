# Career & portfolio — using this repo for top AI engineering roles

This repository is structured so you can **study like a product** and **talk like a staff engineer** in interviews at **OpenAI**, **Anthropic**, **NVIDIA**, and similar labs. Depth lives in the playbooks; the `curriculum/` tree is your **execution spine**.

---

## 1. How hiring managers read a GitHub portfolio

They scan for **five signals** (in roughly this order):

1. **README clarity** — Can I understand scope, quality bar, and how to run it in 60 seconds?
2. **System judgment** — Tradeoffs, failure modes, cost, safety — not only “it works on my laptop.”
3. **Evaluation discipline** — Metrics, golden sets, A/B thinking — not vibes.
4. **Production instinct** — Observability, versioning, rollbacks, multi-tenant boundaries.
5. **Agentic maturity** — Tools are APIs; loops have budgets; humans have escalation paths.

Your job is to **annotate your fork** with what *you* built (see §4). The upstream curriculum gives you vocabulary and patterns; your commits prove execution.

---

## 2. Suggested study order for interview cram (not calendar weeks)

| Phase | Focus | Primary docs |
|-------|--------|----------------|
| **A** | RAG end-to-end + failure modes | [AI_ENGINEERING_PLAYBOOK.md](AI_ENGINEERING_PLAYBOOK.md) §RAG, `labs/week7`, `labs/week8` |
| **B** | Embeddings, ANN, chunking | Playbook §Embeddings, §Vectors, §Chunking; `labs/week4`, `labs/week6` |
| **C** | Evaluation & groundedness | Playbook §Evaluation; `labs/week9` |
| **D** | Agentic & multi-agent | [AGENTIC_AI_ENGINEERING.md](AGENTIC_AI_ENGINEERING.md); `labs/week12`, `labs/week13` |
| **E** | Production & cost | Playbook §Production; `curriculum/week-11` |
| **F** | System design whiteboard | [INTERVIEW_COMPANION.md](INTERVIEW_COMPANION.md) |

---

## 3. One-page “repo walk” script (10 minutes)

Use this when a recruiter or engineer says “walk me through your strongest project.”

1. **Problem** — “Enterprise / research assistants need grounded answers over private corpora with measurable quality.”
2. **Architecture** — Ingest → chunk → embed → index → retrieve → (optional rerank) → generate → cite. Draw five boxes.
3. **Differentiation** — “I implemented hybrid retrieval + eval harness + agentic tool loop with caps and audit logs.”
4. **Metrics** — “Recall@k / MRR on a golden set; faithfulness rubric; p95 latency and cost per query.”
5. **Failure** — “Empty retrieval, injection via docs, tool exfiltration — here’s how I’d detect and mitigate.”
6. **What’s next** — “Load tests, multi-tenant isolation, stronger judge calibration.”

---

## 4. What to add in *your* fork (stars + credibility)

Fork this repo, then:

- [ ] **Pin** 1–3 commits that show *your* extensions (eval set, Dockerfile, load test, agent guardrails).
- [ ] Add **`portfolio/NOTES.md`** — 10 bullets: what you changed, metrics before/after, time spent.
- [ ] Optional: **short Loom** or GIF of `uvicorn` + one great query with citations.
- [ ] **Open issues** on your fork labeled `good-first-issue` if you want community (helps stars over time).

---

## 5. Role-specific emphasis

| Company archetype | Lean into |
|-------------------|-----------|
| **API / model labs** | Eval harnesses, safety, tool schemas, latency SLOs, token economics |
| **Applied research** | Novel retrieval + ablations, embedding analysis, error taxonomy |
| **GPU / infra (e.g. NVIDIA)** | Batch vs online inference, GPU memory for embedders, throughput, Triton-style serving concepts |
| **Enterprise AI** | RBAC, tenancy, audit logs, data residency, human-in-the-loop |

---

## 6. Integrity

Do not claim you built what you only read. **Point to sections you implemented** and be ready to live-code small pieces (metrics, FastAPI route, FAISS index build). That is how senior loops work.

Return to [README.md](../README.md) or open the [AI engineering playbook](AI_ENGINEERING_PLAYBOOK.md).
