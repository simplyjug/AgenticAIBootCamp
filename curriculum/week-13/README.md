# Week 13: Module 11 — Multi-agent systems

**Time:** ~12–16 hours · **Prerequisites:** Week 12

## Outcomes

- Map **roles** (planner, retriever, writer, critic) to reliable boundaries.
- Compare **message passing** vs **shared state** for agent coordination.
- Evaluate **frameworks** (LangGraph, AutoGen, CrewAI) for your constraints.
- Design **production** multi-agent: idempotency, failure isolation, observability.

## Self-service flow

1. Read **[docs/AGENTIC_AI_ENGINEERING.md](../../docs/AGENTIC_AI_ENGINEERING.md) §4–§7** (multi-agent, failures, observability, testing) — required depth for this week.
2. **[docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-13)**.
3. Study `labs/week13/multi_agent.py` and extend per daily guides.

## Reading-only path

This week covers multi-agent coordination. Reading-only learners should understand role separation, communication patterns, and production concerns.

- Learn how planners, retrievers, writers, and critics divide responsibility.
- Compare shared state vs message passing for coordination.
- Review framework tradeoffs and what production multi-agent needs for observability.
- Study failure isolation, idempotency, and replay/debugging requirements.

Write down one coordination model, one protocol sketch, and one production concern.

## Day-by-day

| Day | Topic | Guide | Lab |
|-----|--------|--------|-----|
| 1 | Architecture | [day-01-architecture.md](day-01-architecture.md) | Diagram |
| 2 | Communication | [day-02-communication.md](day-02-communication.md) | Protocol sketch |
| 3 | Orchestration | [day-03-orchestration.md](day-03-orchestration.md) | Delegation rules |
| 4 | Frameworks | [day-04-frameworks.md](day-04-frameworks.md) | Spike PoC |
| 5 | Production | [day-05-production.md](day-05-production.md) | SLO + tracing |

## Concepts

- **Consensus is expensive** — prefer **single orchestrator** patterns unless domain demands peer agents.
- **Deterministic replay:** log decisions for debugging non-deterministic LLMs.

## Done when

- [ ] Three-agent diagram with data flows and failure arrows.
- [ ] One framework spike **≤300 lines** proving orchestration.
- [ ] Written policy for **human-in-the-loop** escalation.

## Portfolio path

This week’s portfolio artifact should show your multi-agent system thinking:

- One **multi-agent architecture diagram** with roles and data flows.
- One **framework comparison note** with the chosen orchestration pattern.
- One **interview story** about handling failure isolation or replay.

If you are reading only, write a summary of the coordination model and the production guardrails.
