# Day 3: Multi-agent RAG & orchestration

## Learning objectives

- Delegate retrieval vs synthesis to **specialists**; orchestrator merges.
- Define **when to stop**: consensus, max rounds, or critic approval.

## Hands-on

1. Role-play traces: Orchestrator asks Retriever for chunks → Writer drafts → Critic requests revision once.
2. Encode **stop condition** in code comments or small state machine.
3. Estimate **cost** vs single-agent RAG for same task (token counts rough).

## Concepts

- **Over-orchestration:** more agents ≠ better — latency and error compound.

## Done when

- [ ] Cost/latency comparison paragraph.
- [ ] Clear stopping criteria list.

## Resources

- LangGraph / CrewAI docs — skim patterns
