# Day 4: A/B testing for RAG

## Learning objectives

- Define **unit of randomization** (user vs session) and **primary metric** (CSAT, task success, latency).
- Plan **power**: how long to run for MDE (minimum detectable effect).

## Hands-on

1. Write **experiment spec**: hypothesis, variants A/B, guardrails (p95 latency < X).
2. Mock assign users to A/B in code with **hash** of `user_id` for sticky assignment.
3. Document **early stopping** rules to avoid peeking bias (even if you only simulate).

## Concepts

- **Simpson’s paradox** in RAG: global win can be loss in a slice — monitor slices.

## Done when

- [ ] Experiment design doc (2 pages max) in `evaluation/ab_week9.md`.
- [ ] Ethical note on exposing half users to worse system — mitigation.

## Resources

- Spotify / Uber engineering blogs on experimentation — optional reading
