# Day 3: Evaluation & Calibration

## Learning Objectives

1. **Tie** classifier outputs to business decisions
2. **Build** calibration for reliable probabilities
3. **Perform** error analysis on slices
4. **Optimize** metrics for deployment

---

## 1. Theory

### Why Evaluation Matters

Evaluation tells you if your model is good enough for real use.

**For beginners:** Like grading a test – you check scores, not just memorize.

### 1.1 Business Decisions

- **Precision:** When you predict positive, how often right? (Avoid false alarms)
- **Recall:** How many positives did you catch? (Don't miss important ones)

**Tradeoff:** High precision = fewer false positives, but might miss some. High recall = catch more, but more false positives.

### 1.2 Calibration

Calibration means probabilities are accurate. If model says 80% chance, it should be right 80% of time.

**Why:** For decisions like "auto-approve if >90% confident".

**Check:** Reliability diagrams – plot predicted vs actual.

### 1.3 Slice Analysis

Don't just look at overall metrics. Check by groups: language, topic, etc.

**Example:** Model good on English, bad on Spanish.

**Benefit:** Find weak spots.

### 1.4 Error Analysis

Look at mistakes: Why did it fail?

**Types:**
- False positive: Wrongly predicted positive
- False negative: Missed positive

**How:** Group errors, find patterns.

---

## 2. Practical: Evaluating Classifiers

### Setup
Install sklearn, matplotlib: `pip install scikit-learn matplotlib`

### Hands-on Exercises
1. Compute ROC/PR curves.
2. Check calibration.
3. Analyze errors by slices.

## Code Examples

### ROC and PR Curves
```python
from sklearn.metrics import roc_curve, auc, precision_recall_curve
import matplotlib.pyplot as plt

# Binary classification
y_true = [0, 0, 1, 1]
y_scores = [0.1, 0.4, 0.35, 0.8]  # Probabilities

# ROC
fpr, tpr, _ = roc_curve(y_true, y_scores)
roc_auc = auc(fpr, tpr)

# PR
precision, recall, _ = precision_recall_curve(y_true, y_scores)
pr_auc = auc(recall, precision)

plt.figure()
plt.plot(fpr, tpr, label=f'ROC AUC = {roc_auc:.2f}')
plt.plot(recall, precision, label=f'PR AUC = {pr_auc:.2f}')
plt.legend()
plt.show()
```

### Calibration Check
```python
from sklearn.calibration import calibration_curve

# Get calibration curve
prob_true, prob_pred = calibration_curve(y_true, y_scores, n_bins=5)

plt.plot(prob_pred, prob_true, marker='o')
plt.plot([0, 1], [0, 1], linestyle='--')  # Perfect calibration
plt.xlabel('Predicted probability')
plt.ylabel('Empirical probability')
plt.title('Calibration Curve')
plt.show()
```

### Temperature Scaling
```python
import torch
import torch.nn as nn

# Simple temperature scaling
class TempScaledModel(nn.Module):
    def __init__(self, model, temperature=1.0):
        super().__init__()
        self.model = model
        self.temperature = nn.Parameter(torch.tensor(temperature))
    
    def forward(self, x):
        logits = self.model(x)
        return logits / self.temperature

# Train temperature on validation set
# (Simplified - in practice, optimize temperature)
```

### Slice Analysis
```python
import pandas as pd

# Sample data with slices
data = pd.DataFrame({
    'text': ['English text', 'Spanish text', 'English text'],
    'language': ['en', 'es', 'en'],
    'true': [1, 0, 1],
    'pred': [1, 1, 0]
})

# Metrics by slice
for lang in data['language'].unique():
    subset = data[data['language'] == lang]
    acc = (subset['true'] == subset['pred']).mean()
    print(f"{lang} accuracy: {acc:.2f}")
```

### Error Analysis
```python
# False positives and negatives
fp = data[(data['true'] == 0) & (data['pred'] == 1)]
fn = data[(data['true'] == 1) & (data['pred'] == 0)]

print("False Positives:")
print(fp.head())
print("\nFalse Negatives:")
print(fn.head())
```

---

## 3. Homework

Perform full evaluation on your classifier and recommend deployment.

---

## 4. Interview Questions

- How to choose between precision and recall?
- What is model calibration and why care?

## Resources
- [Calibration in Deep Learning](https://arxiv.org/abs/1706.04599)
- [Scikit-learn Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html)

## Done When
- [ ] Slice metrics table created.
- [ ] Launch recommendation written.
