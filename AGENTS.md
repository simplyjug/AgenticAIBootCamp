# AGENTS.md — guidance for coding agents & automation

This repository is a **curriculum + code** hybrid. When modifying it:

## Priorities

1. **Learner safety** — never add instructions that encourage leaking API keys or scraping without permission.
2. **Reproducibility** — pin versions in examples where drift breaks learners; document optional deps.
3. **Interview value** — changes should help someone **explain tradeoffs** in hiring loops, not only “make it run.”

## Where content lives

- **Long-form concepts** → `docs/AI_ENGINEERING_PLAYBOOK.md`, `docs/AGENTIC_AI_ENGINEERING.md`
- **Week narrative + checklist** → `curriculum/week-NN/README.md`
- **Day tasks** → `curriculum/week-NN/day-*.md`
- **Runnable code** → `labs/`, `src/`, `tests/`

## When adding labs

- Add or extend **tests** when behavior is non-trivial.
- Keep **dependencies** justified in `requirements.txt` or optional install notes.
- Prefer **small** modules over monoliths.

## When editing playbooks

- Preserve **cross-links** between docs.
- Avoid unverifiable claims (“always use X”); prefer **when / why** framing.
