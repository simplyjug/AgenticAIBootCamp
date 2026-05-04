# Day 3: Evaluation & calibration

## Learning objectives

- Tie classifier outputs to **business decisions** (precision vs recall tradeoffs).
- Build **calibration** intuition (reliability diagrams; optional Platt/temperature scaling).
- Produce an **error analysis** notebook: confusion clusters, not only aggregates.

## Concepts

- **Calibration:** predicted probabilities match empirical frequencies — matters when thresholds trigger automation.
- **Slice analysis:** geography, language, product line — aggregate metrics hide defects.

## Hands-on

1. From Day 1–2 artifacts, load validation predictions + probabilities.
2. Compute **ROC-AUC** / **PR-AUC** where applicable; for multi-label, per-label PR-AUC.
3. Bucket examples into **false positives** / **false negatives** with 5 exemplars each (no customer PII).
4. Optional: apply **temperature scaling** on logits and re-check ECE (expected calibration error).

## Done when

- [ ] One figure or markdown table of **slice metrics**.
- [ ] Short recommendation: which metric you optimize for launch **and why**.

## Resources

- [StatQuest — Precision, Recall, F1](https://www.youtube.com/watch?v=8rr1tbLdSiQ) (review)
