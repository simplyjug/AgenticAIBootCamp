# Day 2: Fine-Tuning LLMs

## Theory: When and How to Fine-Tune

Fine-tuning adapts a pre-trained LLM to a specific task or domain by training it further on custom data. This improves performance without building from scratch.

### Key Concepts
- **Pre-training vs. Fine-tuning**: Pre-training learns general language; fine-tuning specializes.
- **LoRA (Low-Rank Adaptation)**: Efficient fine-tuning by updating only small matrices.
- **Data Preparation**: Need high-quality, task-specific examples (e.g., 100-1000 samples).
- **Overfitting**: Too much fine-tuning can make the model too narrow.

### When to Fine-tune
- For domain-specific jargon or styles.
- When prompt engineering isn't enough.
- For tasks like classification or generation in niche areas.

### Tradeoffs
- Cost: Time and compute-intensive.
- Benefits: Better accuracy for specific tasks.
- Alternatives: Retrieval-augmented generation (RAG) for knowledge updates.

## Practical: Fine-Tuning a Model

### Setup
1. Use Hugging Face Transformers: `pip install transformers datasets`
2. Prepare dataset (JSONL format with prompts and completions).
3. Use a small model like GPT-2 for experimentation.

### Hands-on Exercises
1. Prepare a small dataset.
2. Fine-tune using LoRA.
3. Compare before/after responses.

## Code Examples

### Preparing Data
```python
# Example dataset preparation
data = [
    {"prompt": "Summarize this article: [text]", "completion": "Summary here."},
    # More examples...
]

import json
with open("train.jsonl", "w") as f:
    for item in data:
        f.write(json.dumps(item) + "\n")
```

### Fine-Tuning with Hugging Face
```python
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
from datasets import load_dataset

# Load model
model_name = "gpt2"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Load data
dataset = load_dataset("json", data_files="train.jsonl")

# Tokenize
def tokenize_function(examples):
    return tokenizer(examples["prompt"], truncation=True, padding="max_length")

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Training
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=1,
    per_device_train_batch_size=4,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
)

trainer.train()
```

## Resources
- [Hugging Face Fine-Tuning Guide](https://huggingface.co/docs/transformers/training)
- [LoRA Paper](https://arxiv.org/abs/2106.09685)

## Done When
- [ ] You understand when fine-tuning is better than prompting.
- [ ] You've prepared a small dataset and run a fine-tuning script.