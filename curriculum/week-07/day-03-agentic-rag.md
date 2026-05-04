# Day 3: Agentic RAG (tools & loops)

## Learning objectives

- Wrap retrieval as a **tool** with schema `search_knowledge(query: str) -> list[Chunk]`.
- Implement a **short ReAct-style loop** (thought → tool → observation) with a **max step** cap.

## Concepts

- **Stop conditions:** no new docs, repeated queries, or confidence threshold.
- **Safety:** tools run server-side; never pass raw user strings into SQL/shell tools.

## Hands-on

1. In a notebook or small script, define tool stubs returning fake chunks.
2. Loop: LLM chooses `tool` or `final_answer` via structured JSON (manual parsing OK for learning).
3. Log **trajectory** for one successful and one **timeout** run.

## Done when

- [ ] Trajectory log committed as `labs/week7/sample_agent_trace.json` (fake data ok).
- [ ] Comparison table: agentic RAG vs linear RAG for latency and quality risks.

## Resources

- [docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-12) (agent overlap)
