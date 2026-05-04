# Day 2: Multi-label & Hierarchical Classification

## Learning Objectives

1. **Encode** multi-label targets with one-hot vectors
2. **Choose** appropriate metrics for multi-label tasks
3. **Tune** thresholds for prediction
4. **Design** hierarchical classification systems

---

## 1. Theory

### What is Multi-label Classification?

One text can have multiple labels. Like a news article tagged "Politics" and "Economy".

**For beginners:** Unlike single-label (one category), multi-label allows multiple tags per item.

### 1.1 Encoding Labels

- **One-hot:** Each label is 0 or 1
- **Multi-hot:** Vector of 0s and 1s for all labels

**Example:** Labels: [Sports, Politics, Tech]
Article: Sports + Tech → [1, 0, 1]

### 1.2 Loss Functions

- **Sigmoid:** Each label independent (0-1 probability)
- **Softmax:** One label only (probabilities sum to 1)

**For multi-label:** Use sigmoid per label.

### 1.3 Metrics

- **Hamming loss:** Fraction of wrong labels
- **Subset accuracy:** All labels correct (strict)
- **Micro F1:** Average over all labels
- **Macro F1:** Average per label

**Why:** Accuracy doesn't work for multi-label.

### 1.4 Threshold Tuning

Default 0.5 not always best. Tune per label on validation.

**How:** Try thresholds 0.3, 0.5, 0.7; pick best F1.

### 1.5 Hierarchical Classification

Labels in a tree: Animal > Mammal > Cat.

**Benefit:** Structured predictions, easier routing.

**Challenge:** Errors propagate up/down.

---

## 2. Practical: Multi-label Classifier

### Setup
Install sklearn, torch: `pip install scikit-learn torch`

### Hands-on Exercises
1. Prepare multi-label data.
2. Train with BCE loss.
3. Tune thresholds.
4. Evaluate metrics.

## Code Examples

### Data Preparation
```python
import pandas as pd
import numpy as np

# Sample multi-label data
data = pd.DataFrame({
    'text': ['AI in sports', 'Politics and tech', 'Just sports'],
    'labels': [[1,0,1], [0,1,1], [1,0,0]]  # Sports, Politics, Tech
})

# Convert to multi-hot
from sklearn.preprocessing import MultiLabelBinarizer

mlb = MultiLabelBinarizer()
y = mlb.fit_transform(data['labels'])

print("Classes:", mlb.classes_)
print("Multi-hot:\n", y)
```

### Training with PyTorch
```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

# Simple model
class MultiLabelModel(nn.Module):
    def __init__(self, vocab_size, num_labels):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, 50)
        self.fc = nn.Linear(50, num_labels)
        self.sigmoid = nn.Sigmoid()
    
    def forward(self, x):
        x = self.embedding(x).mean(dim=1)  # Simple average
        return self.sigmoid(self.fc(x))

model = MultiLabelModel(vocab_size=1000, num_labels=3)
criterion = nn.BCELoss()  # Binary cross-entropy
optimizer = torch.optim.Adam(model.parameters())

# Dummy data
X = torch.randint(0, 1000, (10, 20))  # 10 samples, 20 words
y = torch.rand(10, 3)  # Random labels

# Train loop
for epoch in range(5):
    optimizer.zero_grad()
    outputs = model(X)
    loss = criterion(outputs, y)
    loss.backward()
    optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")
```

### Threshold Tuning
```python
from sklearn.metrics import f1_score

# Predictions (probabilities)
preds_proba = model(X).detach().numpy()

# Try thresholds
thresholds = [0.3, 0.5, 0.7]
for thresh in thresholds:
    preds = (preds_proba > thresh).astype(int)
    f1 = f1_score(y.numpy(), preds, average='macro')
    print(f"Threshold {thresh}: Macro F1 {f1:.3f}")
```

### Metrics
```python
from sklearn.metrics import hamming_loss, accuracy_score

# Assuming binary predictions
hamming = hamming_loss(y.numpy(), preds)
subset_acc = accuracy_score(y.numpy(), preds)  # All correct

print(f"Hamming Loss: {hamming:.3f}")
print(f"Subset Accuracy: {subset_acc:.3f}")
```

---

## 3. Homework

Train on a real multi-label dataset and compare hierarchical vs flat.

---

## 4. Interview Questions

- How to handle imbalanced multi-label data?
- When to use hierarchical classification?

## Resources
- [Multi-label Classification Guide](https://scikit-learn.org/stable/modules/multiclass.html)
- [PyTorch BCE Loss](https://pytorch.org/docs/stable/generated/torch.nn.BCELoss.html)

## Done When
- [ ] Micro vs macro F1 compared.
- [ ] Threshold tuning done.
