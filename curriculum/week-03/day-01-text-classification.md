# Day 1: Feature Engineering & Text Classification

## Learning Objectives

1. **Map** business labels to train/val/test splits with stratification
2. **Train** baseline and Transformer models for text classification
3. **Log** experiments for comparison
4. **Handle** class imbalance and data leakage

---

## 1. Theory

### What is Text Classification?

Text classification assigns categories to text, like sorting emails into "spam" or "not spam".

**For beginners:** It's like teaching a computer to read and label documents, just like you categorize news articles.

### 1.1 Feature Engineering

Features are what the model learns from. For text:
- **TF-IDF:** Counts word importance (common words less important)
- **Embeddings:** Turn words into numbers (vectors)

**Why important:** Good features = better model.

### 1.2 Baseline Models

Start simple: TF-IDF + Logistic Regression.

**Why:** Quick to train, easy to understand. Compare advanced models to this.

### 1.3 Transformer Models

Use pre-trained models like BERT from Hugging Face.

**How:** Fine-tune on your data. Better accuracy but slower.

### 1.4 Train/Val/Test Splits

- **Train:** Teach the model
- **Val:** Tune settings
- **Test:** Final check

**Stratification:** Keep class balance in each split.

### 1.5 Common Issues

- **Data leakage:** Model sees future info (e.g., dates)
- **Imbalance:** Some classes rare – use F1, not accuracy

---

## 2. Practical: Building a Classifier

### Setup
Install transformers, sklearn: `pip install transformers scikit-learn`

### Hands-on Exercises
1. Prepare data splits.
2. Train baseline.
3. Train Transformer.
4. Compare metrics.

## Code Examples

### Data Preparation
```python
import pandas as pd
from sklearn.model_selection import train_test_split

# Sample data
data = pd.DataFrame({
    'text': ['I love this', 'This is bad', 'Neutral'],
    'label': [1, 0, 1]  # 1=positive, 0=negative
})

# Stratified split
train, test = train_test_split(data, test_size=0.2, stratify=data['label'], random_state=42)
val, test = train_test_split(test, test_size=0.5, stratify=test['label'], random_state=42)

print(f"Train: {len(train)}, Val: {len(val)}, Test: {len(test)}")
```

### Baseline: TF-IDF + Logistic
```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Features
vectorizer = TfidfVectorizer(max_features=1000)
X_train = vectorizer.fit_transform(train['text'])
X_test = vectorizer.transform(test['text'])

# Model
model = LogisticRegression(random_state=42)
model.fit(X_train, train['label'])

# Predict
preds = model.predict(X_test)
print(classification_report(test['label'], preds))
```

### Transformer with Hugging Face
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments

tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')
model = AutoModelForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=2)

# Tokenize
def tokenize_function(examples):
    return tokenizer(examples['text'], padding='max_length', truncation=True)

train_enc = tokenize_function(train.to_dict('records'))
# Similar for val

# Training
training_args = TrainingArguments(
    output_dir='./results',
    evaluation_strategy='epoch',
    per_device_train_batch_size=8,
    num_train_epochs=1,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_enc,  # Need Dataset object
    eval_dataset=val_enc,
)

trainer.train()
```

### Logging Metrics
```python
import json

# After training
metrics = trainer.evaluate()
with open('metrics.json', 'w') as f:
    json.dump(metrics, f)
```

---

## 3. Homework

Train classifiers on a larger dataset and analyze failures.

---

## 4. Interview Questions

- How to detect train/serve skew?
- When to freeze BERT layers?

## Resources
- [Hugging Face Text Classification](https://huggingface.co/docs/transformers/tasks/sequence_classification)
- [Scikit-learn Docs](https://scikit-learn.org/)

## Done When
- [ ] Baseline and Transformer metrics compared.
- [ ] One paragraph on failure analysis.
