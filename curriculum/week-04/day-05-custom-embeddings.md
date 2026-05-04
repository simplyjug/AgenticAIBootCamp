# Day 5: Custom embeddings & SentenceTransformers

## Learning objectives

- Fine-tune or **contrastively train** embeddings on domain pairs (query, positive doc, negatives).
- Recognize **training objectives**: triplet loss, multiple negatives ranking loss.
- Decide **when not** to fine-tune (data volume too small → overfit).

## Hands-on

1. Use `sentence-transformers` to load `all-MiniLM-L6-v2` (or similar).
2. Create **20–100 synthetic triples** from your domain (even manual) and run a short fine-tune OR show the **loss decreasing** for one epoch (CPU ok).
3. Compare retrieval MRR before/after on a toy query set (≥10 queries).

## Concepts

- **Hard negatives** matter more than more easy negatives.
- **Evaluation leakage:** ensuring negatives are not duplicates of positives.

## Done when

- [ ] Before/after table for MRR or recall@5 on your toy eval.
- [ ] Stop criteria: minimum pairs needed for fine-tune attempt.

## Resources

- [SentenceTransformers training overview](https://www.sbert.net/docs/training/overview.html)
