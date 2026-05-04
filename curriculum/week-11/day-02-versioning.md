# Day 2: Prompt & model versioning

## Learning objectives

- Store prompts as **files** with semver (`prompts/rag/v1.2.txt`) or DB with migrations.
- Tie **deploy** to specific **model name + revision** (`gpt-4o-mini-2024-07-18`).

## Hands-on

1. Create `prompts/` folder with versioned prompt + changelog entry.
2. Write release checklist: bump prompt → run golden eval → deploy canary.
3. Simulate rollback: pointer file `prompts/current.txt` → prior symlink pattern.

## Concepts

- **Fallback model:** cheaper backup when primary provider errors — policy for quality drop.

## Done when

- [ ] Changelog snippet for one prompt edit.
- [ ] Rollback steps tested mentally or on paper.

## Resources

- OpenAI [model snapshots](https://platform.openai.com/docs/models)
