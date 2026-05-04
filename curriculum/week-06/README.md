# Week 6: Module 5 — Chunking science

**Time:** ~8–12 hours · **Prerequisites:** Weeks 1, 4 (text + tokens)

> **Note:** In [CURRICULUM.md](../../CURRICULUM.md) this module is listed as “Module 5 — Chunking science” (calendar **week 6**).

## Outcomes

- Connect **tokenization** choices to chunk boundaries and model context.
- Compare **sliding window**, **parent–child**, and **adaptive** strategies.
- Measure chunking with **retrieval** experiments (not just heuristics).

## Self-service flow

1. Read **[docs/AI_ENGINEERING_PLAYBOOK.md](../../docs/AI_ENGINEERING_PLAYBOOK.md) §5** — chunking is framed the way senior interviewers expect.
2. **[docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-6)** (RAG playlist chunking episodes).
3. Lab: `labs/week6/chunk_strategies.py` — run, modify, and attach numbers to your fork’s `portfolio/` notes.

## Reading-only path

This week is about chunking strategy and retrieval quality. If you are reading only:

- Learn how tokenization influences chunk boundaries and context windows.
- Compare sliding window, parent-child, and adaptive chunking.
- Understand why chunking is part of retrieval policy, not just preprocessing.
- Review how to measure chunk quality with retrieval experiments.

Write down one chunking strategy, one evaluation metric, and one monitoring signal.

## Day-by-day

| Day | Topic | Guide | Lab / artifact |
|-----|--------|--------|----------------|
| 1 | Tokenization & semantic chunking | [day-01-tokenization.md](day-01-tokenization.md) | `chunk_strategies.py` |
| 2 | Sliding window | [day-02-sliding-window.md](day-02-sliding-window.md) | Overlap sweep |
| 3 | Parent–child | [day-03-parent-child.md](day-03-parent-child.md) | Two-level index design |
| 4 | Evaluation | [day-04-evaluation.md](day-04-evaluation.md) | Compare recall@k |
| 5 | Production pipeline | [day-05-production.md](day-05-production.md) | Config + monitoring hooks |

## Concepts

- **Chunking is retrieval policy** — it is not independent of the embedder and user questions.
- **Context pollution:** overly large chunks lower precision; tiny chunks break semantics.

## Done when

- [ ] Table of 3 strategies with **pros/cons** for your target domain.
- [ ] One experiment: same corpus, two chunk settings, different recall@5.

## Portfolio path

This week’s portfolio artifact should show how your chunking design impacts retrieval:

- One **chunking strategy comparison** table or diagram.
- One **experiment summary** with recall and precision outcomes.
- One **interview story** about why the chosen chunking pattern fits the domain.

If you are reading only, write a summary of the chunking strategies and the metrics you would use to choose one.
