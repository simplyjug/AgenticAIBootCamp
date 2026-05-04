"""
Week 3 - Day 1: Text Classification with HuggingFace

Fine-tunes a transformer for text classification.
Includes:
- Dataset loading and tokenization
- Training loop with metrics
- Evaluation (Precision, Recall, F1)
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

# HuggingFace imports - install: pip install transformers datasets
try:
    from transformers import (
        AutoModelForSequenceClassification,
        AutoTokenizer,
        Trainer,
        TrainingArguments,
    )
    from datasets import Dataset
    HAS_HF = True
except ImportError:
    HAS_HF = False


@dataclass
class ClassificationExample:
    """Single training example."""
    text: str
    label: int  # 0, 1, 2, ... for multi-class


def train_text_classifier(
    examples: List[ClassificationExample],
    model_name: str = "distilbert-base-uncased",
    num_labels: int = 2,
    output_dir: str = "./output",
    num_epochs: int = 3,
    batch_size: int = 16,
) -> tuple:
    """
    Fine-tune a transformer for sequence classification.

    Returns:
        (model, tokenizer, metrics_dict)
    """
    if not HAS_HF:
        raise ImportError("pip install transformers datasets")

    # Step 1: Prepare dataset
    texts = [ex.text for ex in examples]
    labels = [ex.label for ex in examples]

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    def tokenize_fn(batch):
        """Tokenize a batch of texts."""
        return tokenizer(
            batch["text"],
            truncation=True,
            padding="max_length",
            max_length=128,
            return_tensors=None,
        )

    dataset = Dataset.from_dict({"text": texts, "label": labels})
    tokenized = dataset.map(
        lambda x: tokenize_fn({"text": x["text"]}),
        batched=True,
        remove_columns=["text"],
    )

    # Step 2: Load model
    model = AutoModelForSequenceClassification.from_pretrained(
        model_name,
        num_labels=num_labels,
    )

    # Step 3: Training arguments
    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=num_epochs,
        per_device_train_batch_size=batch_size,
        per_device_eval_batch_size=batch_size,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
        metric_for_best_model="f1",
    )

    # Step 4: Split and train
    split = tokenized.train_test_split(test_size=0.2, seed=42)
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=split["train"],
        eval_dataset=split["test"],
    )
    trainer.train()
    metrics = trainer.evaluate()

    return model, tokenizer, metrics


def predict(
    model,
    tokenizer,
    texts: List[str],
) -> List[int]:
    """Run inference on texts. Returns predicted class IDs."""
    inputs = tokenizer(
        texts,
        truncation=True,
        padding=True,
        return_tensors="pt",
        max_length=128,
    )
    outputs = model(**inputs)
    preds = outputs.logits.argmax(dim=-1)
    return preds.tolist()


# Example usage
if __name__ == "__main__":
    examples = [
        ClassificationExample("This product is great!", 1),
        ClassificationExample("Terrible experience", 0),
        ClassificationExample("Amazing service", 1),
        ClassificationExample("Waste of money", 0),
    ]
    if HAS_HF:
        model, tok, m = train_text_classifier(examples, num_epochs=1)
        print("Metrics:", m)
