# Day 6: Data governance & versioning

## Learning objectives

- Define **dataset versioning** (DVC, lakeFS, or manifest + blob store hashes).
- Capture **lineage**: raw snapshot → cleaned → splits → model artifact.

## Hands-on

1. Create `datasets/manifest.json` listing files with SHA256 and creation date.
2. Document **access controls**: who may view PII-bearing subsets.
3. Write **retention policy**: how long raw HTML snapshots live.

## Concepts

- **Right to deletion:** map user IDs to derived artifacts to purge.

## Done when

- [ ] Manifest checked in with synthetic paths if real data private.
- [ ] Governance checklist signed off (self-review counts for solo learners).

## Resources

- [LF AI — ML metadata / lineage overview talks](https://lfaidata.foundation/) — optional
