# Week 8: Module 6 — RAG (part 2) & conversational chatbot

**Time:** ~12–16 hours · **Prerequisites:** Week 7

## Outcomes

- Harden a **production-shaped RAG service** (errors, timeouts, schemas).
- Build **multi-turn** chat with history and session discipline.
- Add **caching**, characterize **failure modes**, explore **advanced retrieval** (e.g., ColBERT-style ideas at architecture level).

## Self-service flow

1. **[docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-7-8)**.
2. Run chatbot API:
   ```bash
   python -m uvicorn labs.week8.conversational_chatbot:app --reload --port 8000
   ```
3. Days **1–5** — extend labs with Redis optional ([SETUP.md](../../SETUP.md)).

## Day-by-day

| Day | Topic | Guide | Code |
|-----|--------|--------|------|
| 1 | Production RAG | [day-01-production-rag.md](day-01-production-rag.md) | Harden `rag_service` patterns |
| 2 | Conversational bot | [day-02-chatbot.md](day-02-chatbot.md) | `conversational_chatbot.py` |
| 3 | Caching | [day-03-caching.md](day-03-caching.md) | Redis memo |
| 4 | Failure modes | [day-04-failure-modes.md](day-04-failure-modes.md) | Runbook |
| 5 | Advanced retrieval | [day-05-advanced-retrieval.md](day-05-advanced-retrieval.md) | Reading + experiment plan |

## Concepts

- **Session memory:** what to store raw vs summarized; privacy TTL.
- **Cache stampede:** coalescing identical queries under load.

## Done when

- [ ] Chat endpoint works with **history** object (messages in/out).
- [ ] Documented cache keys and invalidation strategy.
- [ ] One postmortem-style note on a simulated outage (timeouts, empty retrieval).
