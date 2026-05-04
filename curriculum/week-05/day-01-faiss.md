# Day 1: FAISS internals & production

## Learning objectives

- Distinguish `IndexFlat*`, `IndexIVF*`, `IndexHNSW*` and select for your QPS/recall target.
- **Persist** indices to disk; reload in a worker; document **version** in object storage.
- Run a **benchmark harness** (see `labs/week5/faiss_production.py` if present; else create a 50-line script).

## Hands-on

1. Create or open `labs/week5/faiss_production.py` (add if missing) that:
   - loads random vectors
   - builds an index
   - serializes to `/tmp` or `artifacts/`
   - runs query loop and prints p50/p95 latency
2. Document **one failure**: corrupt file, dim mismatch — how you’d detect in prod.

## Concepts

- **Index lifetime:** build on batch job; hot-swap with double-buffer or blue/green.
- **Threading:** FAISS search threads vs Python GIL — know your deployment.

## Done when

- [ ] Benchmark numbers committed or pasted in a `week5-results.md` in your fork.
- [ ] Checklist for **rebuilding** the index (who, when, how long).

## Resources

- [docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-5)
