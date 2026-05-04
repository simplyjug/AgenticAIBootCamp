# Day 5: Evaluation Dashboard

## Learning Objectives

1. **Build** a dashboard for model evaluation
2. **Monitor** classifier performance
3. **Design** alerts for production issues
4. **Create** interactive visualizations

---

## 1. Theory

### Why Dashboards Matter

Dashboards show model health at a glance. Like a car's dashboard – check speed, fuel, warnings.

**For beginners:** Visualize metrics instead of raw numbers.

### 1.1 Offline vs Online Monitoring

- **Offline:** Batch evaluation on historical data
- **Online:** Real-time monitoring of live predictions

**This day:** Offline dashboards.

### 1.2 Key Metrics to Show

- Overall accuracy/F1
- Per-class performance
- Error samples
- Slice analysis

### 1.3 Alerts

What to watch: Sudden drops in accuracy, high error rates, drift.

**Example:** Alert if F1 < 0.8 for a week.

### 1.4 Tools

- **Streamlit:** Easy Python web apps
- **Gradio:** Quick ML demos
- **Plotly/Dash:** Advanced charts

---

## 2. Practical: Building a Dashboard

### Setup
Install streamlit: `pip install streamlit matplotlib`

### Hands-on Exercises
1. Aggregate metrics.
2. Create dashboard.
3. Add interactivity.

## Code Examples

### Metrics Aggregation
```python
import json

# From previous days
metrics = {
    'overall_f1': 0.85,
    'per_class': {'class0': 0.80, 'class1': 0.90},
    'errors': ['sample1', 'sample2']
}

with open('metrics_summary.json', 'w') as f:
    json.dump(metrics, f)
```

### Simple Streamlit Dashboard
```python
import streamlit as st
import json
import matplotlib.pyplot as plt

# Load metrics
with open('metrics_summary.json') as f:
    metrics = json.load(f)

st.title("Model Evaluation Dashboard")

# Overall F1
st.metric("Overall F1", metrics['overall_f1'])

# Per-class chart
fig, ax = plt.subplots()
classes = list(metrics['per_class'].keys())
scores = list(metrics['per_class'].values())
ax.bar(classes, scores)
ax.set_ylabel('F1 Score')
st.pyplot(fig)

# Errors
st.subheader("Error Samples")
for error in metrics['errors']:
    st.write(error)

# Threshold slider
threshold = st.slider("Threshold", 0.0, 1.0, 0.5)
st.write(f"Selected threshold: {threshold}")
```

### Running the Dashboard
```bash
streamlit run dashboard.py
```

### Alerts Design
- Alert if overall F1 < 0.8
- Alert if any class F1 < 0.7
- Alert on high latency (>1s)

---

## 3. Homework

Add more charts and deploy dashboard.

---

## 4. Interview Questions

- How to monitor ML models in production?
- What metrics to prioritize in a dashboard?

## Resources
- [Streamlit Docs](https://docs.streamlit.io/)
- [Gradio](https://gradio.app/)

## Done When
- [ ] Dashboard shows key metrics.
- [ ] Three alert ideas listed.
