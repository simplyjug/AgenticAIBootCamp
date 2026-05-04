# Day 2: Dimensionality reduction & drift signals

## Learning objectives

- Run **PCA/UMAP** on embeddings for sanity checks (clusters, outliers).
- Define **embedding drift**: centroid movement + nearest-neighbor overlap metrics at high level.
- Document actions when drift crosses a threshold (re-index, retrain embedder).

## Concepts

- **Covariate shift** in retrieval: query distribution changes faster than document corpus.
- **Visualization caveats:** UMAP is non-linear; use for exploration, not prod metrics alone.

## Hands-on

1. Sample ~5k vectors from your corpus (or synthetic Gaussian mixtures).
2. Fit PCA to **50D→2D** for visualization; optionally UMAP if installed.
3. Write **drift checklist**: what you’d compare weekly (cosine to centroid, KL on norms).

## Done when

- [ ] One figure (PNG) or description of two **time slices** and how they differ.
- [ ] Two mitigations: cheap vs expensive.

## Resources

- [StatQuest — PCA](https://www.youtube.com/watch?v=FgakZw6y1OU)
