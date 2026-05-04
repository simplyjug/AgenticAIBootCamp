# Day 4: Model Deployment & Optimization

## Theory: Deploying LLMs in Production

Deploying LLMs involves serving them efficiently, handling requests, and optimizing for cost and latency.

### Key Concepts
- **Inference**: Running the model to generate responses.
- **Serving Frameworks**: Tools like vLLM, TGI for fast inference.
- **Optimization**: Quantization (reducing model size), batching requests.
- **Scaling**: Handling multiple users with load balancing.

### Challenges
- High compute costs.
- Latency for long responses.
- Monitoring usage and errors.

## Practical: Deploying a Simple Model

### Setup
1. Install vLLM: `pip install vllm`
2. Use a small model for testing.

### Hands-on Exercises
1. Serve a model locally.
2. Test with API calls.

## Code Examples

### Basic vLLM Server
```python
from vllm import LLM, SamplingParams

# Load model
llm = LLM(model="microsoft/DialoGPT-small")

# Generate
prompt = "Hello, how are you?"
sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=50)
outputs = llm.generate([prompt], sampling_params)

print(outputs[0].outputs[0].text)
```

## Resources
- [vLLM Docs](https://vllm.readthedocs.io/)

## Done When
- [ ] You can explain quantization benefits.
- [ ] You've deployed and queried a model.