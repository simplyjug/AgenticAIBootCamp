# Week 11: Module 9 — Production engineering

**Time:** ~12–18 hours (Docker-heavy) · **Prerequisites:** Weeks 7–10

## Outcomes

- Add **observability**: structured logs, metrics, traces for LLM apps.
- Practice **versioned prompts/models**, safe **deployments**, **Docker/Kubernetes** basics.
- Optimize **cost vs latency**, use **feature flags** for progressive rollout.

## Self-service flow

1. **[docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-11)**.
2. Bring up infra via [SETUP.md](../../SETUP.md) / docker-compose when applicable.
3. Days **1–5** — capture screenshots or YAML snippets for your portfolio.

## Day-by-day

| Day | Topic | Guide |
|-----|--------|--------|
| 1 | Monitoring | [day-01-monitoring.md](day-01-monitoring.md) |
| 2 | Versioning | [day-02-versioning.md](day-02-versioning.md) |
| 3 | Docker & Kubernetes | [day-03-docker-k8s.md](day-03-docker-k8s.md) |
| 4 | Scaling & cost | [day-04-scaling.md](day-04-scaling.md) |
| 5 | Feature flags | [day-05-feature-flags.md](day-05-feature-flags.md) |

## Concepts

- **RED metrics:** rate, errors, duration — adapted for streaming LLM responses.
- **Canary & rollback:** model/router changes are production incidents waiting to happen.

## Done when

- [ ] Dashboard or metric export showing generation latency & error codes.
- [ ] Dockerfile builds (`docker build .`) or compose stack starts.
- [ ] Written rollout plan for a **prompt change** (who approves, how to revert).
