# Week 3: Module 2 — Classification systems engineering

**Time:** ~10–12 hours · **Prerequisites:** Weeks 1–2 (clean text and labels)

## Outcomes

- Train / fine-tune **text classifiers** (baseline → Transformer).
- Handle **multi-label** and calibration for production thresholds.
- Build an **evaluation narrative** (metrics + dashboards).

## Self-service flow

1. **[docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-3)** — metrics & Hugging Face channel.
2. Follow days **1–5**; primary lab: `labs/week3/day01_text_classifier.py`.

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
