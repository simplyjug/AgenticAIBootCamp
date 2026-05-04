# Day 2: Planning & reasoning (ReAct, plan-and-execute)

## Learning objectives

- Compare **ReAct** (interleaved thought/action) vs **plan-then-execute** (full plan upfront).
- Add **step caps** and **budget** for tokens per trajectory.

## Hands-on

1. Implement **plan-and-execute** on paper for “research company X using web + doc search tools” (5 steps).
2. Simulate **failure**: step 3 tool errors — how does replanning work?
3. Write **policy**: max 8 steps; escalate to human on repeated failures.

## Concepts

- **Non-determinism:** same prompt → different trajectories — log seeds when debugging.

## Done when

- [ ] Side-by-side comparison table for two patterns.
- [ ] Escalation policy text suitable for compliance review.

## Resources

- Search “**ReAct paper**” + read abstract and Figure 1
