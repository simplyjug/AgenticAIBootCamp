# Day 3: Guardrails & safety

## Learning objectives

- Add **input rails** (PII, jailbreak patterns) and **output rails** (toxicity, secrets).
- Prefer **policy-as-code** over prompt-only “don’t be evil.”

## Hands-on

1. Integrate a lightweight checker (regex + optional NeMo/Guardrails AI) before LLM call.
2. Define **safe fallback response** for blocked inputs.
3. Unit-test rails with **10** adversarial strings (non-toxic simulated jailbreak patterns).

## Concepts

- **Defense in depth:** rails + tool permissions + human review for high-risk actions.

## Done when

- [ ] Blocked vs allowed examples documented.
- [ ] Tests for rails (pytest).

## Resources

- [NVIDIA NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) — skim docs
