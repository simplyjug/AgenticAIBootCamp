# Day 5: Labeling & active learning

## Learning objectives

- Design **labeling instructions** with edge cases and negative examples.
- Sketch **active learning**: prioritize uncertain samples for human review.

## Hands-on

1. Write a **1-page** labeler guide for one task (e.g., document type).
2. Simulate model **uncertainty** = |0.5 - p| from a dummy classifier; pick top 20 uncertain for review.
3. Compare **time to label** random vs uncertain sampling (rough estimate OK).

## Concepts

- **Label noise** hurts more than less data — invest in instructions first.

## Done when

- [ ] Labeler guide committed under `datasets/labeling/` or `labs/week2/`.
- [ ] Active learning loop diagram.

## Resources

- Humanloop / Label Studio docs — optional tooling
