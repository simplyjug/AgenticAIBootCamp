# Day 4: Cost optimization & scaling

## Learning objectives

- Estimate **$/1M tokens** and **$/1k queries** for your stack (rough spreadsheet).
- Choose **horizontal scaling** vs **bigger nodes** for retrieval + LLM tiers.

## Hands-on

1. Build a **cost model** CSV: components (embeddings API, LLM, vector DB, VMs).
2. Identify **top 3** cost drivers — propose mitigations (cache, smaller model, batching).
3. Sketch **autoscaling** metric (queue depth vs CPU).

## Concepts

- **Batch inference** for embeddings offline vs online query path.

## Done when

- [ ] Spreadsheet or markdown table with assumptions explicit.
- [ ] One **cost guardrail** you’d enforce in CI/CD (max tokens per request).

## Resources

- Major cloud pricing pages — skim for units
