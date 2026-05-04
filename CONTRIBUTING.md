# Contributing

Thank you for helping learners and hiring managers see **quality** in this bootcamp. High-signal contributions:

- **Correctness** — fix wrong formulas, broken links, or outdated API names.
- **Depth** — add worked examples, failure-mode stories, or benchmark tables (with methodology).
- **Labs** — small, focused PRs that extend `labs/` with tests and `README` snippets.
- **Evals** — golden-set hygiene, reproducible metrics, no leaked API keys.

## Process

1. **Fork** the repository.
2. Create a branch: `feat/short-description` or `fix/issue-123`.
3. Run **`pytest tests/ -v`** and **`ruff check src/ labs/ tests/`** when you touch Python.
4. Open a PR with: **what** changed, **why**, and how to **verify** it.

## Style

- Match existing tone: precise, interview-useful, minimal fluff.
- Prefer linking to **`docs/AI_ENGINEERING_PLAYBOOK.md`** instead of duplicating long theory in every day file.
- Do not commit **secrets**, real customer data, or huge binaries without LFS and license clarity.

## Code of conduct

Be respectful in issues and PRs. Assume good intent; disagree with technical specifics, not people.
