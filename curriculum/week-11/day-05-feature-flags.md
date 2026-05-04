# Day 5: Feature flags & progressive delivery

## Learning objectives

- Use flags for **router**, **prompt version**, and **new retriever** independently.
- Define **blast radius**: internal-only → beta → GA.

## Hands-on

1. Choose a flag provider (LaunchDarkly, Unleashed, OpenFeature) or **env-based** flags for demo.
2. Implement `if flags.new_reranker: ...` around reranker path with safe default off.
3. Write rollout plan with **kill switch** runbook.

## Concepts

- **Flag debt:** remove stale flags regularly — tech debt ticket template.

## Done when

- [ ] Flag inventory table (name, owner, removal date).
- [ ] Kill switch tested (flip flag off — service healthy).

## Resources

- Martin Fowler — feature toggles (article)
