# Day 1: Feature engineering & text classification

## Learning objectives

- Map a business label set to a **train/val/test** split with **stratification** when needed.
- Train a **baseline** (e.g., TF–IDF + linear) and a **Transformer** head using HuggingFace.
- Log experiments so you can compare **F1** and **calibration** later in the week.

## AI engineering concepts

- **Label schema first:** unclear labels → unclear metrics; fix taxonomy before scaling models.
- **Data leakage:** future information in text (timestamps, filenames) that the model should not use in production.
- **Class imbalance:** accuracy is misleading; use **macro/micro** F1 and per-class recall.

## Watch & read

- [docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-3) (metrics + Hugging Face).
- [Hugging Face — text classification](https://huggingface.co/docs/transformers/main/en/tasks/sequence_classification) (skim the task page).

## Hands-on (order)

1. Open `labs/week3/day01_text_classifier.py` and read the data path it expects; use a small CSV of `text,label` (create under `datasets/` if needed).
2. Run a **baseline** path: hash or TF–IDF + `LogisticRegression` in a notebook or small script in the same folder.
3. Run a **HF** `AutoModelForSequenceClassification` with a tiny model (e.g., `distilbert-base-uncased`) and `Trainer` or `transformers.Trainer` with `eval_strategy="epoch"`.
4. Save **metrics JSON** (precision, recall, F1 per class) next to the run for Day 3.

## Code touchpoint

```text
labs/week3/day01_text_classifier.py
```

Extend the file with a `if __name__ == "__main__":` that prints a one-line summary for CI or local checks.

## Done when

- [ ] You can point to where **random seed** and **split ratios** are defined.
- [ ] Baseline vs HF model metrics are in one table (same test set).
- [ ] You wrote one paragraph on **failure slices** (where both models fail).

## Interview prompts

- How do you detect **train/serve skew** for text classifiers?
- When would you **freeze** BERT layers vs full fine-tune?
