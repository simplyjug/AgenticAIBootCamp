# Day 2: Multi-label & hierarchical classification

## Learning objectives

- Encode **multi-label** targets (one-hot / sigmoid vs softmax).
- Choose metrics: **micro/macro F1**, **Hamming loss**, **subset accuracy**.
- Sketch **hierarchical** labels (tree paths) for routing or retrieval filters later.

## Concepts

- **Sigmoid per label** vs **softmax single class** — different decision boundaries.
- **Threshold tuning:** default 0.5 per label is rarely optimal; sweep on validation data.
- **Hierarchy:** parent errors cascade — sometimes flat multi-label is safer than forced trees.

## Hands-on

1. Convert your Week 3 dataset (or a public multi-label set like Reuters subsets) to **multi-hot** vectors.
2. Train a small model with `BCEWithLogitsLoss` per label or HF multi-label head.
3. Plot **PR curves** per label for top-K frequent labels.
4. Optional: implement **hierarchical** evaluation — precision at each tree depth.

## Done when

- [ ] Table comparing **micro vs macro** F1 with explanation.
- [ ] Written rule for **when to abstain** (no label above threshold).

## Resources

- [docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-3)
