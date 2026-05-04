# Day 2: Agent communication & protocols

## Learning objectives

- Implement **shared state** (Redis/Postgres) vs **message passing** only — tradeoffs.
- Handle **idempotent** message processing with dedupe keys.

## Hands-on

1. Extend `labs/week13/multi_agent.py` with a `Mailbox` class (in-memory dict OK).
2. Simulate **race**: two agents write same key — use versioning or compare-and-swap pattern description.
3. Log message DAG for one run.

## Concepts

- **Backpressure:** slow critic agent must not unbounded-queue requests.

## Done when

- [ ] Sequence diagram (ASCII ok) of one multi-turn coordination.
- [ ] Dedupe strategy written.

## Resources

- Message-passing vs actor model primers — optional reading
