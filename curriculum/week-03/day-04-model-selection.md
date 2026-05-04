# Day 4: Threshold Tuning & Model Selection

## Learning Objectives

1. **Use** k-fold cross-validation for evaluation
2. **Select** models with cost-sensitive criteria
3. **Version** model artifacts
4. **Tune** thresholds for deployment

---

## 1. Theory

### Model Selection Process

Choosing the best model involves testing on unseen data and considering costs.

**For beginners:** Like picking a car – test drive, check price, reliability.

### 1.1 Cross-Validation

K-fold CV: Split data into K parts, train on K-1, test on 1, repeat.

**Why:** Better than single split, reduces luck.

**Stratified:** Keep class balance in folds.

### 1.2 Cost-Sensitive Selection

Not all errors equal. False positive (spam marked good) vs false negative (good marked spam).

**How:** Assign costs, choose model with lowest total cost.

### 1.3 Threshold Tuning

Adjust decision threshold based on business needs.

**Example:** For medical diagnosis, high recall (catch all sick), even if low precision.

### 1.4 Model Versioning

Save model, config, labels for reproducibility.

**What to save:** Weights, tokenizer, label map, training config.

**Why:** Deploy consistently, audit changes.

### 1.5 Nested CV

For hyperparameter tuning: Outer CV for final eval, inner for tuning.

**Benefit:** Unbiased performance estimate.

---

## 2. Practical: Model Selection

### Setup
Use sklearn for CV: `pip install scikit-learn`

### Hands-on Exercises
1. Run k-fold CV.
2. Tune thresholds.
3. Select best model.
4. Version artifacts.

## Code Examples

### K-Fold Cross-Validation
```python
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import f1_score
import numpy as np

# Sample data
X = np.random.rand(100, 10)  # Features
y = np.random.randint(0, 2, 100)  # Labels

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

scores = []
for train_idx, val_idx in skf.split(X, y):
    X_train, X_val = X[train_idx], X[val_idx]
    y_train, y_val = y[train_idx], y[val_idx]
    
    # Train model (dummy)
    # model.fit(X_train, y_train)
    # preds = model.predict(X_val)
    preds = np.random.randint(0, 2, len(y_val))  # Dummy preds
    
    score = f1_score(y_val, preds)
    scores.append(score)

print(f"CV F1: {np.mean(scores):.3f} ± {np.std(scores):.3f}")
```

### Cost-Sensitive Evaluation
```python
def cost_sensitive_score(y_true, y_pred, fp_cost=1, fn_cost=10):
    fp = ((y_pred == 1) & (y_true == 0)).sum()
    fn = ((y_pred == 0) & (y_true == 1)).sum()
    return fp * fp_cost + fn * fn_cost

# Example
y_true = [0, 0, 1, 1]
y_pred = [0, 1, 1, 0]  # 1 FP, 1 FN

cost = cost_sensitive_score(y_true, y_pred, fp_cost=1, fn_cost=5)
print(f"Total cost: {cost}")
```

### Threshold Tuning
```python
# Probabilities from model
probas = np.random.rand(100)  # Dummy

thresholds = np.arange(0.1, 0.9, 0.1)
best_thresh = 0.5
best_score = 0

for thresh in thresholds:
    preds = (probas > thresh).astype(int)
    score = f1_score(y, preds)  # Or cost-sensitive
    if score > best_score:
        best_score = score
        best_thresh = thresh

print(f"Best threshold: {best_thresh}, Score: {best_score:.3f}")
```

### Saving Artifacts
```python
import json
import pickle

# Label map
label2id = {'negative': 0, 'positive': 1}
with open('artifacts/label2id.json', 'w') as f:
    json.dump(label2id, f)

# Config
config = {'model': 'bert', 'lr': 1e-5, 'epochs': 3}
with open('artifacts/config.json', 'w') as f:
    json.dump(config, f)

# Model (dummy)
model = {'weights': 'dummy'}
with open('artifacts/model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Artifacts saved")
```

### Scorecard
```markdown
| Model | Accuracy | F1 | Cost | Notes |
|-------|----------|----|------|-------|
| Baseline | 0.85 | 0.80 | 50 | Simple |
| BERT | 0.92 | 0.90 | 30 | Better |
```

---

## 3. Homework

Compare models with CV and create deployment artifacts.

---

## 4. Interview Questions

- How to choose between models with similar accuracy?
- What is nested cross-validation?

## Resources
- [Scikit-learn CV](https://scikit-learn.org/stable/modules/cross_validation.html)
- [Hugging Face Trainer](https://huggingface.co/docs/transformers/main_classes/trainer)
