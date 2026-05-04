# Agentic AI engineering — patterns, pitfalls, interview framing

This document complements the [AI engineering playbook](AI_ENGINEERING_PLAYBOOK.md). It is written for engineers who will **ship** tool-using LLMs, not only prompt them. Labs: `labs/week12/`, `labs/week13/`, `curriculum/week-12/`, `week-13/`.

---

## 1. What “agentic” actually means in production

**Agentic** = the model **chooses control flow**: which tools to call, in what order, when to stop, and when to ask for clarification. That is fundamentally different from a **fixed** RAG chain where the developer hard-codes retrieve → generate.

| Property | Fixed chain | Agentic |
|----------|-------------|---------|
| Control flow | Developer graph | Model + policy |
| Testability | Higher | Lower unless you invest |
| Latency tail | Predictable | Heavy tail (loops) |
| Failure blast radius | Bounded | Tools expand surface |
| Cost | Easier to cap | Needs budgets & kill switches |

**Interview line:** “We treat every tool as a microservice with authZ, input validation, and structured output — the LLM is a router/planner, not magic.”

---

## 2. Tool design (the real product)

### 2.1 Schema first

Tools should expose **typed** arguments (JSON Schema / OpenAI function definitions):

- Prefer **enums** and **bounded strings** over free text when possible.
- Add **`max_results`**, **`time_range`**, **`tenant_id`** as explicit parameters — never infer tenant from model hidden state alone.
- Return **structured JSON** from tools, not markdown blobs, so downstream code can validate.

### 2.2 Least privilege

Each tool receives **only** the credentials needed for that operation. Avoid “god tool” that can read the whole database because the model asked nicely.

### 2.3 Idempotency & side effects

Classify tools:

- **Read-only** (search, calculator) — cacheable, safe to retry.
- **Write** (create ticket, send email) — require **idempotency keys**, human approval, or both.

**Interview line:** “Writes go through an approval queue or idempotent API; reads can be retried with backoff.”

---

## 3. Core patterns (know names + tradeoffs)

### 3.1 ReAct-style loop (reason + act)

Interleave **thought** (optional in prod — often internal), **action** (tool call), **observation** (tool result). Stop when the model emits **final answer** or max steps reached.

**Strengths:** Flexible, good for exploratory tasks.  
**Weaknesses:** Verbose traces, harder to test, easy to **rabbit-hole** on useless tools.

**Production mitigations:** max steps, per-tool timeouts, duplicate-call detection, forced summarization of observations before next step.

### 3.2 Plan-and-execute

Model first emits a **plan** (ordered steps), then executor runs steps with **cheaper** models or deterministic code where possible.

**Strengths:** Easier to log and audit; can parallelize independent steps.  
**Weaknesses:** Plans go stale if world changes mid-flight — need **replan triggers**.

### 3.3 Router / specialist (orchestrator–workers)

A **router** classifies intent and delegates to specialist chains (billing vs HR vs code).

**Strengths:** Isolates prompts and tools per domain; simpler eval per slice.  
**Weaknesses:** Router errors are expensive — calibrate router with its own eval set.

### 3.4 Reflexion / self-critique (use carefully)

Model proposes answer → critic model (or same) lists issues → revise.

**Strengths:** Can improve quality on hard reasoning.  
**Weaknesses:** **2–3× cost**; can “agree with itself” — still add programmatic checks.

### 3.5 Graph / state-machine agents (LangGraph-style)

Nodes = deterministic functions or LLM calls; edges = conditions. Gives **replay**, **breakpoints**, and **human-in-the-loop** on specific nodes.

**Interview line:** “We use a graph for anything that touches money or PII; free-form ReAct only for read-only research.”

---

## 4. Multi-agent systems (when they help)

**Good reasons:**

- True **specialist** skills (coder vs reviewer vs retriever) with different prompts and tools.
- **Parallelism** for independent subtasks with merge step.

**Bad reasons:**

- “More agents = smarter” — usually increases coordination bugs and cost.

**Topologies:**

- **Star** — central orchestrator (best default for v1).
- **Pipeline** — A → B → C (good for extract → verify → summarize).
- **Debate / ensemble** — costly; only if measured win on benchmark.

**Consensus:** expensive; prefer **single orchestrator + critic** over peer-to-peer gossip unless domain demands it.

---

## 5. Failure modes (memorize for interviews)

| Failure | Symptom | Mitigation |
|---------|---------|------------|
| Tool hallucination | Calls nonexistent tool | Strict schema validation; server returns 400 with hint |
| Argument hallucination | Wrong types / out of range | JSON schema + repair loop max 1 |
| Runaway loop | 20 useless calls | max steps; duplicate detection; cumulative cost cap |
| Prompt injection via RAG | Doc text says “ignore rules” | System prompt isolation; cite-only generation; output rails |
| Exfiltration | Tool sends data outward | egress allowlist; DLP on tool outputs |
| Non-determinism | Different trace each time | log prompts + tool I/O + model version; golden replay for tools only |
| Long tail latency | p99 explodes | async tools; parallelize; shed load |

---

## 6. Observability for agents

Log **per step** (not only final answer):

- `trace_id`, `step_idx`, `tool_name`, `args_redacted`, `latency_ms`, `status`, `tokens_in/out`

Metrics:

- Tool error rate, **steps per resolved task**, cost per task, % escalations to human.

Tracing: OpenTelemetry spans around each tool + LLM call — links to existing APM.

---

## 7. Testing strategy (what “good” looks like)

1. **Unit tests** for each tool with golden inputs (no LLM).
2. **Contract tests** for tool JSON schema round-trip.
3. **Trajectory tests** — recorded replay of successful runs; detect regressions when prompt changes.
4. **Adversarial suite** — injection strings, oversized args, unicode edge cases.
5. **Shadow mode** — new agent policy runs in parallel without user impact; compare outcomes.

---

## 8. NVIDIA / infra angle (brief)

For GPU-heavy deployments:

- **Batch embedding** jobs on GPU; **online** query path may stay CPU + ANN for cost.
- **TensorRT-LLM / Triton** style serving: continuous batching, KV cache reuse — know the **vocabulary** even if you use managed APIs day-to-day.
- **Quantization** tradeoffs (INT8/FP8) for throughput vs accuracy — tie to your eval harness.

---

## 9. Anthropic / safety-forward angle (brief)

- **Constitutional** or layered policies: separate **policy model** or rules engine from task model when stakes are high.
- **Computer use** style agents: extreme least-privilege OS accounts, sandboxed filesystem, no raw shell from LLM text.
- **Claude-style** long context: still need **retrieval** — context window does not remove indexing discipline.

---

## 10. Checklist: “is our agent shippable?”

- [ ] Every tool has owner, SLO, and rollback.
- [ ] Max steps + max cost per user request enforced.
- [ ] PII redaction on logs; secrets never in prompts.
- [ ] Human escalation path defined with SLA.
- [ ] Eval set includes **tool-required** and **no-tool** questions.
- [ ] Runbook for “agent stuck” and “tool outage.”

Next: [INTERVIEW_COMPANION.md](INTERVIEW_COMPANION.md) and hands-on `labs/week12/agentic_tools.py`.
