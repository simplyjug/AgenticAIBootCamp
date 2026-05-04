# Day 4: Threshold tuning & model selection

## Learning objectives

- Use **k-fold** or stratified splits without leaking labels across related documents.
- Select models using **cost-sensitive** criteria (FP cost vs FN cost).
- Version **artifacts**: weights, tokenizer, label map (json), training config.

## Concepts

- **Nested CV** when you also tune hyperparameters — avoid optimistic bias.
- **Model registry:** tie run ID → dataset hash → metrics hash for auditability.

## Hands-on

1. Freeze a validation protocol (seed, folds, metric).
2. Compare **at least two** models or hyperparameter sets (e.g., learning rate, max length).
3. Pick a **deploy candidate** using a written scorecard: accuracy is only one row.
4. Export `label2id.json`, `config.json`, and model weights to a folder `artifacts/week3/`.

## Done when

- [ ] Scorecard markdown or spreadsheet screenshot described in text.
- [ ] Clear statement of **stop rule** (when not to ship).

## Resources

- Hugging Face [Trainer](https://huggingface.co/docs/transformers/main_classes/trainer) docs
