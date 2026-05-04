# Day 5: Evaluation datasets & benchmarking harness

## Learning objectives

- Version datasets with **git-lfs** or manifest hashes (`datasets-lock.json`).
- Wire **CI smoke eval**: tiny subset runs on each PR (cheap).

## Hands-on

1. Package `golden_set.jsonl` + hash SHA256 in manifest.
2. Extend `labs/week9/rag_evaluation.py` to load manifest path via CLI flag.
3. Add **pytest** that runs metrics on synthetic data (no API calls) OR marked `@pytest.mark.integration`.

## Concepts

- **Data contamination:** eval questions accidentally in training corpora — track sources.

## Done when

- [ ] `pytest` passes locally with new test.
- [ ] README section “How we prevent eval leakage” (bullet list).

## Resources

- [Hugging Face — dataset cards](https://huggingface.co/docs/hub/datasets-cards)
