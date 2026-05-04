# Week 7: Module 6 — RAG architecture (part 1)

**Time:** ~12–16 hours · **Prerequisites:** Weeks 4–6 · **API key** for OpenAI (or compatible)

## Outcomes

- Ship a **naive RAG** path: embed → retrieve → generate with citations.
- Add **hybrid** retrieval (dense + sparse) and **reranking** hooks.
- Sketch **agentic RAG** (tooling, iterative retrieval) and **context compression**.

## Self-service flow

1. Read **[docs/AI_ENGINEERING_PLAYBOOK.md](../../docs/AI_ENGINEERING_PLAYBOOK.md) §6–§8** (RAG + eval mindset) before coding.
2. **[docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-7-8)** — LangChain RAG playlist.
2. Run the service:
   ```bash
   pip install -r requirements.txt
   set OPENAI_API_KEY=...   # Windows cmd
   python -m uvicorn labs.week7.rag_service:app --reload --port 8000
   ```
3. Complete days **1–5** and extend `labs/week7/rag_service.py` where guided.

## Reading-only path

This week is the first RAG implementation phase. Reading-only learners should focus on retrieval grounding, hybrid search, and the agentic context for retrieval-based answers.

- Learn the naive RAG pipeline and how hybrid retrieval improves relevance.
- Understand multi-hop retrieval and when it is worth the added complexity.
- Study tool loop architecture for agentic RAG.
- Review reranking and context compression as quality / cost controls.

Note one grounding strategy, one latency budget tradeoff, and one tool error handling pattern.

## Day-by-day

| Day | Topic | Guide | Code |
|-----|--------|--------|------|
| 1 | Naive & hybrid RAG | [day-01-naive-rag.md](day-01-naive-rag.md) | `labs/week7/rag_service.py` |
| 2 | Multi-hop | [day-02-multihop.md](day-02-multihop.md) | Planner sketch |
| 3 | Agentic RAG | [day-03-agentic-rag.md](day-03-agentic-rag.md) | Tool loop |
| 4 | Reranking | [day-04-reranking.md](day-04-reranking.md) | Cross-encoder / API |
| 5 | Context compression | [day-05-context-compression.md](day-05-context-compression.md) | Prompt trim |

## Concepts

- **Grounding:** every user-visible claim should trace to retrieved IDs.
- **Latency budget:** retrieval, rerank, and LLM must fit your SLO.

## Done when

- [ ] `/query` (or equivalent) returns **answer + sources** from your index.
- [ ] Written tradeoff: single-shot vs **multi-hop** for your domain.
- [ ] Failure modes list (empty retrieval, duplicate chunks, tool errors).

## Portfolio path

This week’s portfolio artifact should illustrate your RAG architecture and decisions:

- One **RAG system diagram** with retrieval, generation, and grounding flow.
- One **tradeoff note** comparing single-shot and multi-hop strategies.
- One **interview story** describing a retrieval failure mode and your mitigation.

If you are reading only, write a note that explains the RAG pipeline and the source grounding approach.
