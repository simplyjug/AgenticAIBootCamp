# Week 12: Module 10 — Agentic AI, tools & guardrails

**Time:** ~12–16 hours · **Prerequisites:** Weeks 7–11 · **API keys** as needed

## Outcomes

- Compose **tool-using agents** (function calling, retrieval tools).
- Compare planning patterns (**ReAct**, plan-and-execute) at engineering depth.
- Implement **guardrails**, **security** basics (injection, exfiltration), **red-team** passes.

## Self-service flow

1. Read **[docs/AGENTIC_AI_ENGINEERING.md](../../docs/AGENTIC_AI_ENGINEERING.md)** end-to-end — this is the **canonical depth** for agentic patterns (tools, loops, failures, observability).
2. **[docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-12)** for video pointers.
3. Lab entrypoint: `labs/week12/agentic_tools.py` — follow days **1–5** to extend patterns.

## Day-by-day

| Day | Topic | Guide | Lab |
|-----|--------|--------|-----|
| 1 | Agentic tools | [day-01-agentic-tools.md](day-01-agentic-tools.md) | `agentic_tools.py` |
| 2 | Planning & reasoning | [day-02-planning.md](day-02-planning.md) | Flowcharts + code |
| 3 | Guardrails | [day-03-guardrails.md](day-03-guardrails.md) | Policy layer |
| 4 | Security & privacy | [day-04-security.md](day-04-security.md) | Threat model |
| 5 | Red teaming | [day-05-redteaming.md](day-05-redteaming.md) | Test cases |

## Concepts

- **Tool surface area:** every tool is an API you must authN/Z and validate.
- **Policy engines:** separate business rules from model creativity.

## Done when

- [ ] Agent that calls **at least two tools** with explicit schemas.
- [ ] List of 10 **adversarial** inputs you tested.
- [ ] One-page **threat model** (assets, adversaries, mitigations).
