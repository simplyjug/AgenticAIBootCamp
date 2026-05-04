# Day 3: Safety & Alignment in LLMs

## Theory: Why Safety Matters

LLMs can generate harmful, biased, or incorrect content. Safety and alignment ensure models behave ethically and reliably.

### Key Concepts
- **Alignment**: Making the model follow human values and instructions.
- **Guardrails**: Filters to prevent harmful outputs.
- **Hallucinations**: When the model generates false information confidently.
- **Bias**: Unfair treatment of groups based on training data.

### Techniques
- **RLHF (Reinforcement Learning from Human Feedback)**: Train on human preferences.
- **Constitutional AI**: Use principles to guide responses.
- **Input/Output Filtering**: Check prompts and responses for safety.

### Challenges
- Balancing safety with creativity.
- Handling edge cases and adversarial inputs.
- Measuring and improving alignment.

## Practical: Implementing Basic Guardrails

### Setup
1. Use libraries like `transformers` or API filters.
2. Define safety rules (e.g., no hate speech).

### Hands-on Exercises
1. Test a model with unsafe prompts.
2. Add filters to block harmful content.

## Code Examples

### Basic Safety Check
```python
def is_safe(prompt):
    unsafe_words = ["hate", "violence", "illegal"]
    return not any(word in prompt.lower() for word in unsafe_words)

# Example
prompt = "How to make explosives?"
if not is_safe(prompt):
    print("Blocked: Unsafe prompt")
else:
    # Call LLM
    pass
```

### Using OpenAI Moderation
```python
import openai

response = openai.Moderation.create(
    input="Some potentially harmful text"
)
if response.results[0].flagged:
    print("Content flagged")
else:
    print("Safe")
```

## Resources
- [OpenAI Safety Guide](https://platform.openai.com/docs/guides/safety-best-practices)
- [Anthropic Alignment Research](https://www.anthropic.com/research)

## Done When
- [ ] You can explain RLHF and its role in alignment.
- [ ] You've implemented a basic safety filter.