# Day 1: Logging, monitoring & observability

## Learning objectives

- Instrument FastAPI with **request latency histogram**, **error rate**, and **token usage** gauges (design-level OK).
- Trace **LLM calls** with OpenTelemetry spans if feasible; else structured logs.

## Hands-on

1. Add middleware logging `trace_id`, `route`, `latency_ms`, `status`.
2. Define **RED** metrics for your RAG service — write Prometheus metric names (even if mocked).
3. Draft **Grafana** dashboard JSON outline (panels list only).

## Concepts

- **Cardinality explosion:** avoid high-cardinality labels (full query text) in metrics.

## Done when

- [ ] Example log line + list of metric names.
- [ ] Alert ideas: p95 latency, error spike, zero retrieval rate.

## Resources

- [docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-11)
- [Google SRE — monitoring distributed systems](https://sre.google/sre-book/monitoring-distributed-systems/) (free online book chapter)
