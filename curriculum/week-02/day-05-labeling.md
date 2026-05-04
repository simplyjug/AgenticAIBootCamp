# Day 5: Labeling & Active Learning

## Learning Objectives

1. **Design** clear labeling instructions with examples
2. **Implement** active learning to prioritize uncertain samples
3. **Measure** labeling efficiency
4. **Handle** label noise and quality

---

## 1. Theory

### What is Labeling?

Labeling assigns categories or values to data for training AI models.

**For beginners:** Like sorting photos into "cats" or "dogs" folders so the computer can learn.

### 1.1 Labeling Instructions

Good instructions prevent mistakes. Include:
- **Definition:** What is a "positive" example?
- **Examples:** 3 good, 3 bad
- **Edge cases:** Ambiguous situations

**Why important:** Bad labels = bad AI.

### 1.2 Active Learning

Instead of labeling everything randomly, label the hardest examples first.

**How:** Train a model, find samples it's unsure about, label those.

**Benefit:** Get better model faster with fewer labels.

### 1.3 Label Noise

Wrong labels confuse the model. Worse than having less data.

**Causes:** Tired labelers, unclear instructions.

**Solutions:** Double-check, use multiple labelers.

---

## 2. Practical: Labeling Workflow

### Setup
Use pandas for data: `pip install pandas`

### Hands-on Exercises
1. Write labeling guide.
2. Simulate active learning.
3. Compare strategies.

## Code Examples

### Labeling Guide Template
```
Task: Classify sentiment (positive/negative)

Definition: Positive = expresses approval or happiness.

Examples:
Positive: "I love this product!"
Negative: "This is terrible."

Edge cases:
- Sarcasm: "Oh great, another delay" → Negative
- Neutral: "It's okay" → Skip or neutral category
```

### Simulating Uncertainty
```python
import numpy as np

# Dummy model predictions (probabilities)
predictions = np.random.rand(100, 2)  # 100 samples, 2 classes

# Uncertainty = distance from 0.5 (most uncertain when close to 0.5)
uncertainties = np.abs(predictions[:, 0] - 0.5)

# Sort by uncertainty (highest first)
uncertain_indices = np.argsort(uncertainties)[::-1]

# Top 20 uncertain
top_uncertain = uncertain_indices[:20]
print(f"Label these first: {top_uncertain}")
```

### Active Learning Loop
```python
# Simple simulation
labeled = []
unlabeled = list(range(100))

for round in range(5):
    # Train dummy model (random for sim)
    model_preds = np.random.rand(len(unlabeled), 2)
    
    # Get uncertainties
    uncert = np.abs(model_preds[:, 0] - 0.5)
    
    # Label top 10 uncertain
    to_label = np.argsort(uncert)[-10:]
    labeled.extend([unlabeled[i] for i in to_label])
    
    # Remove from unlabeled
    unlabeled = [u for i, u in enumerate(unlabeled) if i not in to_label]
    
    print(f"Round {round+1}: Labeled {len(labeled)} total")
```

### Quality Check
```python
# Simulate label agreement
labels1 = np.random.randint(0, 2, 50)
labels2 = labels1.copy()
# Add some noise
noise_idx = np.random.choice(50, 5, replace=False)
labels2[noise_idx] = 1 - labels2[noise_idx]

agreement = np.mean(labels1 == labels2)
print(f"Labeler agreement: {agreement:.2f}")
```

---

## 3. Homework

Create labeling guide for a dataset and implement active learning simulation.

---

## 4. Interview Questions

- How to scale labeling for 1M samples?
- What if labelers disagree?

## Resources
- [Active Learning Survey](https://arxiv.org/abs/1910.09128)
- [Label Studio](https://labelstud.io/)

## Done When
- [ ] You can explain active learning benefits.
- [ ] You've simulated an active learning loop.
