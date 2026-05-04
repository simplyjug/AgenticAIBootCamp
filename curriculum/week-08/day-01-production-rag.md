# Day 1: Production RAG service hardening

## Learning objectives

- Add **timeouts** on embedding, retrieval, and LLM calls; return **typed errors** to clients.
- Define **Pydantic** response models with `sources[]` always present (possibly empty).
- Log **trace IDs** per request for support tickets.

## Hands-on

1. Review `labs/week7/rag_service.py` patterns; port improvements into `labs/week8/conversational_chatbot.py` or a shared module.
2. Add `HTTPException` paths for: empty index, provider rate limit, oversize query.
3. Write `curl` examples in a `labs/week8/README_snippets.md` for health + query.

## Concepts

- **Graceful degradation:** keyword-only search if vectors unavailable.
- **Idempotency keys** for paid APIs when clients retry.

## Done when

- [ ] List of **HTTP codes** you use and what they mean.
- [ ] Example structured log line (JSON) with trace_id.

## Resources

- [FastAPI handling errors](https://fastapi.tiangolo.com/tutorial/handling-errors/)
