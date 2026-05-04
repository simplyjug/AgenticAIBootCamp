# Day 5: Multi-tenant vector architecture

## Learning objectives

- Choose **namespace per tenant** vs **shared index + metadata filter** vs **shard per tenant**.
- Define **isolation**: no cross-tenant leakage at API and index layers.

## Hands-on

1. Draw (Excalidraw / diagram) three architectures for 10k tenants, avg 10k vectors each.
2. Write an **API contract**: headers or path for `tenant_id`; validation rules.
3. Threat model: neighbor leakage if embeddings are similar across tenants.

## Concepts

- **Noisy neighbor:** big tenant starves small tenants on shared hardware — rate limits.
- **Compliance:** EU tenant data residency → region pinned indexes.

## Done when

- [ ] Diagram + recommendation for pilot scale vs hyperscale.
- [ ] List of **integration tests** you’d run to prove isolation.

## Resources

- [docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-5)
