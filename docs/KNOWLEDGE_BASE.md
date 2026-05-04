# Knowledge Base: AI Engineering Concepts

This document serves as a reference for key concepts covered in the bootcamp. Think of it as a glossary and FAQ for quick lookups.

## A. Generative AI Fundamentals

### What is an LLM?
A Large Language Model is an AI trained on massive text data to predict and generate human-like text. Examples: GPT, Claude, Llama.

### Prompt Engineering
Crafting inputs to guide LLM outputs. Techniques:
- Zero-shot: Direct ask.
- Few-shot: Provide examples.
- Chain-of-thought: Step-by-step reasoning.

### Fine-Tuning
Adapting a pre-trained model to a specific task with custom data. Use LoRA for efficiency.

### Safety & Alignment
Ensuring models are safe and aligned with human values. Methods: RLHF, guardrails, moderation.

## B. Data Ingestion & Processing

### PDF Types
- Text-based: Extract directly.
- Scanned: Use OCR (e.g., Tesseract).

### Chunking
Splitting documents into smaller pieces for retrieval. Strategies: Fixed size, semantic, hierarchical.

### Embeddings
Vector representations of text. Used for similarity search. Models: Sentence Transformers, OpenAI embeddings.

## C. Retrieval & Search

### Vector Databases
Stores for embeddings. Examples: FAISS, Pinecone, Milvus. Support ANN search.

### RAG (Retrieval-Augmented Generation)
Combine retrieval with generation for accurate answers. Steps: Retrieve relevant docs, generate response.

### Hybrid Search
Combine dense (embeddings) and sparse (BM25) retrieval for better results.

## D. Evaluation & Production

### Metrics
- Retrieval: Recall@k, MRR.
- Generation: Faithfulness, BLEU.

### Production Concerns
- Latency, cost, observability.
- Scaling with Kubernetes, monitoring with Prometheus.

## E. Agentic AI

### Tools & Agents
Agents use tools (APIs) to perform tasks. Patterns: ReAct, tool calling.

### Multi-Agent Systems
Multiple agents coordinating. Frameworks: LangGraph, CrewAI.

### Guardrails
Policies to prevent misuse. Include input/output filters, rate limits.

## FAQs

### Q: When to use fine-tuning vs. prompting?
A: Prompting for quick changes; fine-tuning for domain-specific behavior.

### Q: How to handle hallucinations?
A: Use retrieval (RAG), fact-checking, or lower temperature.

### Q: What's the difference between RAG and fine-tuning?
A: RAG updates knowledge without retraining; fine-tuning changes behavior.

For more details, refer to the weekly curriculum and docs.