# Day 5: Context compression & prompt optimization

## Learning objectives

- Apply **map-reduce** style summarization of chunks when context exceeds model limits.
- Use **structured prompting**: system rules + retrieved XML-ish blocks with IDs.

## Concepts

- **Stuffing vs summarizing:** stuffing is faithful but long; summarization drops facts — pick per risk appetite.
- **Lost-in-the-middle:** models attend poorly to middle of long contexts — reorder important chunks to edges (research-backed heuristic).

## Hands-on

1. Take 15 retrieved chunks; implement **greedy max-token packer** into `max_context=3000` tokens (estimate chars/4).
2. Add **per-chunk summary** layer for overflow chunks only — compare output length.
3. Document **prompt template** version in git (`prompts/rag_v1.txt`).

## Done when

- [ ] `prompts/rag_v1.txt` checked in with placeholders `{context}`, `{question}`.
- [ ] Risk note for summarization in **regulated** answers.

## Resources

- OpenAI [prompt engineering guide](https://platform.openai.com/docs/guides/prompt-engineering)
