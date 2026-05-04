# Day 3: Caching & performance

## Learning objectives

- Cache **embeddings** for repeated queries; **cache answers** only when safe (idempotent, no time-sensitive facts).
- Use **Redis** optional from [SETUP.md](../../SETUP.md); fallback dict LRU for local dev.

## Hands-on

1. Pick a cache key: `hash(normalize(query))` document decision on normalization (lowercase? locale?).
2. Implement **TTL** (e.g., 300s) for answer cache; **bypass** for admin users.
3. Simulate **thundering herd** with 20 parallel identical requests — optional locking sketch.

## Concepts

- **Semantic cache:** cache by embedding similarity — risky but powerful (must validate thresholds).

## Done when

- [ ] Table: what is cached | TTL | invalidation rule.
- [ ] One scenario where cache **must** be bypassed.

## Resources

- Redis [documentation](https://redis.io/docs/)
