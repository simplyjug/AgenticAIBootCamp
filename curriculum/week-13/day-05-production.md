# Day 5: Production multi-agent systems

## Learning objectives

- Add **tracing** across agents (shared trace_id), **timeouts** per agent, **circuit breakers**.
- Plan **human escalation** when agents disagree beyond threshold.

## Hands-on

1. List **SLO** per stage (retrieve <200ms p95, generate <3s p95, etc.) — aspirational OK.
2. Write **on-call runbook** for “agent loop exceeded max steps.”
3. Optional: integrate OpenTelemetry exporter stub.

## Concepts

- **Poison turns:** one bad message shouldn’t corrupt state — immutable event log helps.

## Done when

- [ ] Runbook markdown + SLO table.
- [ ] Failure injection idea (chaos) for one dependency.

## Resources

- Google SRE — **error budgets** chapter
