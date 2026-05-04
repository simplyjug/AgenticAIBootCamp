# Day 5: Evaluation dashboard

## Learning objectives

- Surface **live-ish** monitoring for a classifier: traffic, latency, drift triggers (design level).
- Build a simple **dashboard**: Streamlit, Gradio, or static HTML from CSV metrics.

## Concepts

- **Offline dashboards** (this day) vs **online** monitoring (Week 11) — different SLAs.
- **Human-readable** dashboards win interviews — show confusion + slice drill-down.

## Hands-on

1. Aggregate metrics from Days 1–4 into one `metrics_summary.json` or CSV.
2. Build a **minimal** dashboard that shows:
   - overall F1
   - per-class bar chart
   - link or expandable section for error samples (sanitized)
3. If time: add a **“what-if”** threshold slider for one label (Streamlit `st.slider`).

## Done when

- [ ] Screenshot or hosted URL (optional) + instructions to run (`streamlit run ...`).
- [ ] Three bullets on what you would **alert** on in production.

## Resources

- [Streamlit docs](https://docs.streamlit.io/) if you choose Streamlit
