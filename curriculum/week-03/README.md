# Week 3: Module 2 — Classification systems engineering

**Time:** ~10–12 hours · **Prerequisites:** Weeks 1–2 (clean text and labels)

## Outcomes

- Train / fine-tune **text classifiers** (baseline → Transformer).
- Handle **multi-label** and calibration for production thresholds.
- Build an **evaluation narrative** (metrics + dashboards).

## Self-service flow

1. **[docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-3)** — metrics & Hugging Face channel.
2. Follow days **1–5**; primary lab: `labs/week3/day01_text_classifier.py`.

## Reading-only path

This week covers classification, evaluation, and calibration. If you are reading only:

- Focus on the classifier architecture and the difference between binary, multi-class, and multi-label setups.
- Learn why calibration matters and how to tune thresholds for production.
- Understand the evaluation metrics and the role of dashboards in debugging model behavior.
- Think in terms of what you would measure and why.

Write down one model comparison, one evaluation chart, and one production decision rule.

## Day-by-day

| Day | Topic | Guide | Lab |
|-----|--------|--------|-----|
| 1 | Text classification | [day-01-text-classification.md](day-01-text-classification.md) | `labs/week3/day01_text_classifier.py` |
| 2 | Multi-label | [day-02-multilabel.md](day-02-multilabel.md) | Extend classifier |
| 3 | Evaluation | [day-03-evaluation.md](day-03-evaluation.md) | Metrics notebook |
| 4 | Model selection | [day-04-model-selection.md](day-04-model-selection.md) | CV + threshold sweep |
| 5 | Dashboard | [day-05-dashboard.md](day-05-dashboard.md) | Streamlit or HTML report |

## Concepts

- **Calibration** vs raw softmax scores for threshold decisions.
- **Slice analysis:** performance by region, language, or topic bucket.

## Done when

- [ ] Baseline + HF model compared on the same split.
- [ ] Precision/recall/F1 reported with **class imbalance** called out.
- [ ] One visualization (confusion matrix or PR curve) checked into `labs/` or `reports/`.

## Portfolio path

This week’s portfolio artifact should be a result-focused note or chart:

- One **model comparison summary** with chosen metric rationale.
- One **evaluation visualization** (confusion matrix, PR curve, or calibration plot).
- One **interview story** on how you selected the production threshold or handled imbalance.

If you are reading only, write a summary of the classification strategy, the key metric, and the deployment decision.
