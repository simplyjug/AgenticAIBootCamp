# Day 3: Load testing & deployment

## Learning objectives

- Use **k6**, **Locust**, or `hey` to load-test `/query` (read-heavy) and `/ingest` (write-heavy) separately.
- Measure **saturation point** and **degradation mode** (queue, 429, backpressure).

## Hands-on

1. Write a small k6 or Locust script hitting your FastAPI with ramping VUs.
2. Capture **p50/p95** latency, error %, and LLM token rate limits hit.
3. Write **Tuning** section: what you’d change first (HPA, cache, model swap).

## Concepts

- **Warm pools** for GPU embedders if applicable — cost vs ready latency.

## Done when

- [ ] Load test script in `capstone/loadtests/`.
- [ ] Graph or table summarizing max sustainable RPS **before** errors dominate.

## Resources

- [k6 docs](https://k6.io/docs/)
