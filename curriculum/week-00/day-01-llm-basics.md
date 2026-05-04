# Day 1: LLM Basics & Prompt Engineering

## Theory: Understanding Large Language Models

Large Language Models (LLMs) are AI systems trained on vast amounts of text data to generate human-like responses. They work by predicting the next word in a sequence based on patterns learned from training data.

### Key Concepts
- **Tokens**: LLMs process text as tokens (words or sub-words). For example, "quantum computing" might be 2-3 tokens.
- **Context Window**: The maximum input length the model can handle (e.g., 4096 tokens for GPT-3.5).
- **Temperature**: Controls randomness in responses (0 = deterministic, 1 = creative).
- **Prompt Engineering**: Crafting inputs to get better outputs without retraining the model.

### Prompt Engineering Techniques
- **Zero-shot**: Ask directly without examples.
- **Few-shot**: Provide examples in the prompt.
- **Chain-of-Thought**: Encourage step-by-step reasoning.
- **Role Prompting**: Assign a role to the model (e.g., "You are a teacher").

### Common Pitfalls
- Vague prompts lead to generic answers.
- Overly long prompts exceed context limits.
- Ignoring model biases or hallucinations.

## Practical: Building Your First LLM Interaction

### Setup
1. Install the OpenAI library: `pip install openai`
2. Get an API key from [OpenAI](https://platform.openai.com/api-keys)
3. Set environment variable: `export OPENAI_API_KEY=your_key_here`

### Hands-on Exercises
1. **Basic Prompt**: Ask the model to explain a simple concept.
2. **Few-shot Example**: Provide examples to improve response quality.
3. **Experiment with Temperature**: Try different values and observe changes.

## Code Examples

### Basic Zero-shot Prompt
```python
import openai
import os

# Set your API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Simple prompt
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Explain quantum computing in simple terms."}
    ],
    max_tokens=150,
    temperature=0.7
)

print("Response:", response.choices[0].message.content)
```

### Few-shot Prompting
```python
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain machine learning: Machine learning is a subset of AI where systems learn from data."},
        {"role": "assistant", "content": "That's correct. Machine learning uses algorithms to find patterns in data."},
        {"role": "user", "content": "Now explain deep learning."}
    ],
    max_tokens=200,
    temperature=0.5
)

print("Few-shot Response:", response.choices[0].message.content)
```

### Experimenting with Temperature
```python
# Low temperature (deterministic)
response_low = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Write a short poem about AI."}],
    temperature=0.1
)

# High temperature (creative)
response_high = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Write a short poem about AI."}],
    temperature=0.9
)

print("Low temp:", response_low.choices[0].message.content)
print("High temp:", response_high.choices[0].message.content)
```

## Resources
- [OpenAI API Documentation](https://platform.openai.com/docs/introduction)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [Anthropic Claude Docs](https://docs.anthropic.com/claude/docs) (alternative to OpenAI)

## Done When
- [ ] You can explain the difference between zero-shot and few-shot prompting.
- [ ] You've run at least 3 different prompts and noted the responses.
- [ ] You understand how temperature affects output creativity.</content>
<parameter name="filePath">c:\Users\jugal\OneDrive\Desktop\AgenticAIBootCamp\curriculum\week-00\day-01-llm-basics.md