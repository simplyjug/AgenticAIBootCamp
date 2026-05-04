# Week 9: Module 7 — RAG evaluation & metrics

**Time:** ~10–14 hours · **Prerequisites:** Weeks 7–8

## Outcomes

- Measure **retrieval** (Recall@k, MRR, nDCG) on labeled query sets.
- Score **faithfulness** / groundedness with automated judges (know limits).
- Stand up **human eval**, **A/B** hooks, and a repeatable **eval dataset** workflow.

## Self-service flow

1. **[docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-9)**.
2. Lab: `labs/week9/rag_evaluation.py` — follow day guides to extend metrics.

## Reading-only path

This week teaches evaluation of RAG systems. Reading-only learners should focus on the metrics, judge limitations, and experiment design.

- Learn retrieval metrics and why they matter for search quality.
- Understand faithfulness scoring and the limits of automated judges.
- Study human evaluation and A/B design as the gold standard.
- Think through how to version and reuse evaluation datasets.

Summarize one metric comparison, one judge limitation, and one experiment plan.

## Day-by-day

| Day | Topic | Guide | Lab |
|-----|--------|--------|-----|
| 1 | Retrieval metrics | [day-01-retrieval-metrics.md](day-01-retrieval-metrics.md) | `rag_evaluation.py` |
| 2 | Faithfulness | [day-02-faithfulness.md](day-02-faithfulness.md) | LLM judge harness |
| 3 | Human eval | [day-03-human-eval.md](day-03-human-eval.md) | Rubric + sheet |
| 4 | A/B testing | [day-04-ab-testing.md](day-04-ab-testing.md) | Experiment design |
| 5 | Eval datasets | [day-05-eval-dataset.md](day-05-eval-dataset.md) | Versioned JSONL |

## Concepts

- **Evaluation drives iteration** — without frozen sets, you optimize vibes.
- **Judge drift:** LLM judges need spot-checks by humans.

## Done when

- [ ] Small **golden set** (≥50 queries) checked in or documented location.
- [ ] Table comparing two retrieval configs on the same set.
- [ ] Short ethics note on automated judges + PII.

## Portfolio path

This week’s portfolio artifact should show your evaluation discipline:

- One **evaluation summary** with metrics and dataset design.
- One **comparative table** of retrieval configs.
- One **interview story** about the ethical or PII tradeoff in automatic judging.

If you are reading only, write a summary of the evaluation workflow and the limitations of automated metrics.
