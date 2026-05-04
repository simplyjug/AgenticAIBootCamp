# Day 5: Advanced retrieval & ColBERT-style intuition

## Learning objectives

- Explain **late interaction** models (ColBERT / multi-vector) vs single-vector bi-encoders — **latency tradeoffs**.
- Outline **routing**: send FAQs to canned responses; hard queries to agentic path.

## Hands-on

1. Read one ColBERT / late-interaction blog or paper abstract; summarize in 5 bullets for your team.
2. Design a **router** function `route(query) -> {rag_naive, rag_hybrid, agent}` with mock rules (regex + LLM optional).
3. Optional: stream tokens from OpenAI API for UX — list SSE considerations.

## Concepts

- **Cost-aware routing** saves $ at scale — measure misroute rate.

## Done when

- [ ] Diagram of router + two retrieval backends.
- [ ] Note on when **streaming** hurts observability (partial citations).

## Resources

- [Stanford ColBERT / late interaction overviews](https://www.google.com/search?q=ColBERT+late+interaction+retrieval) — pick one reputable article
