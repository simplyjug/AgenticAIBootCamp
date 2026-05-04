# Day 4: RAG failure modes & mitigations

## Learning objectives

- Build a **taxonomy**: empty retrieval, wrong retrieval, contradictions, tool misuse, LLM refusal.
- Pair each mode with **detection** (rules/LLM judge) and **mitigation** (fallback answer, human escalation).

## Hands-on

1. Create `labs/week8/failure_modes.md` listing ≥8 failures you’ve seen or simulated.
2. For three of them, write **user-visible** error copy (tone: honest, helpful).
3. Add **unit-style tests** that mock retriever to return empty list — assert API behavior.

## Concepts

- **Confidence scoring:** sum retrieval scores + self-consistency checks — still imperfect.

## Done when

- [ ] Failure matrix committed.
- [ ] At least one **automated** test for empty retrieval path.

## Resources

- Karpathy-style “**hallucination**” talks search on YouTube for intuition
