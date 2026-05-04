# Day 1: Multi-agent architecture

## Learning objectives

- Compare **orchestrator–workers**, **peer-to-peer**, and **hierarchical** patterns.
- Assign **clear interfaces**: message schemas (JSON), not loose strings.

## Hands-on

1. Diagram your capstone using ≥3 agents with responsibilities (Retriever, Writer, Critic).
2. Define **message protocol**: fields `from`, `to`, `type`, `payload`, `correlation_id`.
3. List **single points of failure** — how to mitigate.

## Concepts

- **Avoid chatroom chaos:** limit broadcast; prefer star topology for v1.

## Done when

- [ ] Architecture diagram file under `labs/week13/`.
- [ ] Protocol snippet (YAML or JSON schema).

## Resources

- [docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-13)
