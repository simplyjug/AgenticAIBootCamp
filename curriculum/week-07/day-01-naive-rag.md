# Day 1: Naive RAG & hybrid RAG

## Learning objectives

- Implement **retrieve → concatenate → generate** with explicit **citations** (chunk IDs).
- Explain **hybrid** retrieval: dense + sparse (BM25) with **RRF** or weighted fusion at high level.
- Run `labs/week7/rag_service.py` as a FastAPI app and issue a sample query.

## Concepts

- **Grounding:** model must cite sources that user can inspect — reduces silent hallucination.
- **Hybrid:** dense captures paraphrase; sparse captures rare tokens (SKUs, legal cites).

## Hands-on

1. `pip install -r requirements.txt` and set `OPENAI_API_KEY` in `.env` (see `.env.example`).
2. Start: `python -m uvicorn labs.week7.rag_service:app --reload --port 8000`
3. POST JSON `{"query":"What is in the knowledge base?","top_k":5}` — trace logs to **retrieval → prompt**.
4. In code, locate `SimpleRetriever` and sketch how you’d add **BM25** alongside FAISS.

## Code map

```text
labs/week7/rag_service.py  — RAGRequest, SimpleRetriever, FastAPI routes
```

## Done when

- [ ] You can draw the request path on a napkin (5 boxes).
- [ ] Written fusion strategy for hybrid (even if not implemented).

## Resources

- [docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-7-8)
- [LangChain RAG Part 1](https://www.youtube.com/watch?v=wd7TZ4w1mSw)
