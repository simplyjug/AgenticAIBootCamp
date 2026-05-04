# Day 1: LLM Basics & Prompt Engineering

## Objectives
- Understand LLM APIs (OpenAI, Anthropic).
- Learn prompt engineering techniques.

## Hands-on
- Install openai library.
- Write scripts for different prompting strategies.

## Code
```python
import openai

# Example prompt
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Explain quantum computing simply."}]
)
print(response.choices[0].message.content)
```

## Resources
- [Prompt Engineering Guide](https://www.promptingguide.ai/)</content>
<parameter name="filePath">c:\Users\jugal\OneDrive\Desktop\AgenticAIBootCamp\curriculum\week-00\day-01-llm-basics.md