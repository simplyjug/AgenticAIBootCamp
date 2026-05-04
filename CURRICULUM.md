# Complete 14-Week Curriculum Outline

## Generative AI & Agentic AI Engineering Bootcamp
(Including Document Processing, RAG, Conversational Chatbots, Agentic Patterns & Multi-Agent Systems)

> **Interview depth track:** read [**docs/AI_ENGINEERING_PLAYBOOK.md**](docs/AI_ENGINEERING_PLAYBOOK.md) alongside this outline, then [**docs/AGENTIC_AI_ENGINEERING.md**](docs/AGENTIC_AI_ENGINEERING.md) before Weeks 12–13. [**docs/INTERVIEW_COMPANION.md**](docs/INTERVIEW_COMPANION.md) is your oral-exam cram sheet.

This curriculum is designed as a professional training program rather than a casual tutorial. Each week has:

- explicit outcomes,
- clear deliverables,
- portfolio-facing artifacts,
- interview and production notes.

Use this as a self-paced professional bootcamp: read the guide, execute the lab, and capture one story per week.

---

## Week 0: Foundations of Generative AI

| Day | Topic | Key Deliverables |
|-----|-------|------------------|
| **Day 1** | LLM Basics & Prompt Engineering | API calls, zero-shot/few-shot, temperature tuning |
| **Day 2** | Fine-Tuning LLMs | LoRA, data prep, evaluation metrics |
| **Day 3** | Safety & Alignment | RLHF, guardrails, bias detection |
| **Day 4** | Model Deployment & Optimization | vLLM, quantization, cost monitoring |
| **Day 5** | Multimodal Generative Models | DALL-E, CLIP, image generation |
| **Day 6** | Ethics & Responsible AI | Fairness, transparency, regulations |

---

## Week 1: Module 0 — Document Processing & Multimodal Ingestion

| Day | Topic | Key Deliverables |
|-----|-------|------------------|
| **Day 1** | PDF Processing Fundamentals | Text vs scanned PDF pipeline, PyMuPDF, pdfplumber |
| **Day 2** | Advanced PDF: Tables, Layout, OCR | LayoutParser, Tesseract, Unstructured, table extraction |
| **Day 3** | HTML Processing & Web Crawling | BeautifulSoup, trafilatura, Playwright, crawler architecture |
| **Day 4** | Multi-Modal Documents | CLIP, SigLIP, image embeddings, hybrid indexing |
| **Day 5** | Document Schema & Chunking | Canonical JSON schema, section-aware chunking, Postgres design |
| **Day 6** | Ingestion Pipeline & Quality | Async pipeline (Celery), quality scoring, monitoring |

---

## Week 2: Module 1 — Data Curation Engineering

| Day | Topic | Key Deliverables |
|-----|-------|------------------|
| **Day 1** | Data Sourcing & Pipelines | Web scraping architecture, API ingestion |
| **Day 2** | Deduplication (MinHash, LSH, SimHash) | Dedup pipeline code, embedding-based clustering |
| **Day 3** | Semantic Dedup & Noise Reduction | Label quality measurement, dataset audit |
| **Day 4** | Metadata Enrichment & Taxonomy | Taxonomy design, metadata enrichment pipeline |
| **Day 5** | Labeling & Active Learning | Weak supervision, active learning loops |
| **Day 6** | Data Governance & Versioning | Dataset versioning, lineage, governance |

---

## Week 3: Module 2 — Classification Systems Engineering

| Day | Topic | Key Deliverables |
|-----|-------|------------------|
| **Day 1** | Feature Engineering & Text Classification | PyTorch classifier, HuggingFace fine-tuning |
| **Day 2** | Multi-Label & Hierarchical Classification | Evaluation metrics, confusion matrix |
| **Day 3** | Evaluation & Calibration | Precision, Recall, F1, ROC-AUC, PR-AUC |
| **Day 4** | Threshold Tuning & Model Selection | Cross-validation, bias detection |
| **Day 5** | Evaluation Dashboard | Visualization, production classifiers |

---

## Week 4: Module 3 — Embeddings Deep Dive

| Day | Topic | Key Deliverables |
|-----|-------|------------------|
| **Day 1** | Embedding Math & Similarity | Cosine, dot product, normalization |
| **Day 2** | Dimensionality Reduction & Drift | PCA, UMAP, drift detection |
| **Day 3** | Quantization & Compression | Index comparison benchmark |
| **Day 4** | ANN Search (HNSW, IVF, PQ) | FAISS index build, latency vs recall |
| **Day 5** | Custom Embeddings | SentenceTransformers, fine-tuning |

---

## Week 5: Module 4 — Vector Databases Deep Dive

| Day | Topic | Key Deliverables |
|-----|-------|------------------|
| **Day 1** | FAISS Internals & Production | Production config, benchmark harness |
| **Day 2** | Milvus & Pinecone Architecture | Query latency, load testing |
| **Day 3** | Weaviate & Metadata Filtering | Schema design, hybrid search |
| **Day 4** | Index Tuning & Rebuilding | Fragmentation, sharding |
| **Day 5** | Multi-Tenant Architecture | Production config files |

---

## Week 6: Module 5 — Chunking Science

| Day | Topic | Key Deliverables |
|-----|-------|------------------|
| **Day 1** | Tokenization & Semantic Chunking | Chunk strategy comparison tool |
| **Day 2** | Sliding Window & Overlap Tuning | Retrieval recall comparison |
| **Day 3** | Parent-Child & Adaptive Chunking | Recursive splitting strategies |
| **Day 4** | Chunk Evaluation Metrics | Comparative evaluation framework |
| **Day 5** | Production Chunking Pipeline | Optimized for retrieval quality |

---

## Week 7: Module 6 — RAG Architecture (Part 1)

| Day | Topic | Key Deliverables |
|-----|-------|------------------|
| **Day 1** | Naive RAG & Hybrid RAG | Complete RAG service (FastAPI) |
| **Day 2** | Multi-Hop & Graph RAG | Retriever + generator separation |
| **Day 3** | Agentic RAG | Re-ranking module, metadata-aware retrieval |
| **Day 4** | Query Rewriting & Reranking | Caching layer, async processing |
| **Day 5** | Context Compression & Prompt Optimization | Failure modes, production patterns |

---

## Week 8: Module 6 — RAG Architecture (Part 2) + Conversational Chatbot

| Day | Topic | Key Deliverables |
|-----|-------|------------------|
| **Day 1** | Production RAG Service | Full FastAPI service, error handling |
| **Day 2** | Conversational RAG Chatbot | Multi-turn memory, chat history, session management |
| **Day 3** | Caching & Performance | Redis caching, request coalescing |
| **Day 4** | RAG Failure Modes & Mitigations | Troubleshooting guide |
| **Day 5** | Advanced Retrieval & Chat UI | ColBERT, streaming responses, chat frontend |

---

## Week 9: Module 7 — RAG Evaluation & Metrics

| Day | Topic | Key Deliverables |
|-----|-------|------------------|
| **Day 1** | Retrieval Metrics | Recall@k, MRR, nDCG, automatic eval script |
| **Day 2** | Faithfulness & Groundedness | Hallucination rate, LLM-as-judge |
| **Day 3** | Human Evaluation Pipeline | Offline vs online eval |
| **Day 4** | A/B Testing Framework | Score aggregation dashboard |
| **Day 5** | Evaluation Dataset & Benchmarking | Production eval pipeline |

---

## Week 10: Module 8 — Metadata Enrichment

| Day | Topic | Key Deliverables |
|-----|-------|------------------|
| **Day 1** | NER & Keyword Extraction | NLP enrichment pipeline |
| **Day 2** | Topic Modeling & Taxonomy | Metadata scoring, enriched search |
| **Day 3** | Schema Design | Structured + unstructured hybrid |
| **Day 4** | Production Enrichment Pipeline | Incremental enrichment |
| **Day 5** | Metadata for Retrieval | Filter optimization |

---

## Week 11: Module 9 — Production Engineering

| Day | Topic | Key Deliverables |
|-----|-------|------------------|
| **Day 1** | Logging, Monitoring, Observability | Prometheus, Grafana dashboards |
| **Day 2** | Versioning & Deployment | Prompt versioning, canary deployment |
| **Day 3** | Docker & Kubernetes | Dockerfile, K8s YAML, docker-compose |
| **Day 4** | Cost Optimization & Scaling | GPU vs CPU, horizontal scaling |
| **Day 5** | Feature Flags & Production Patterns | Complete deployment pipeline |

---

## Week 12: Module 10 — Agentic AI, Tools & Guardrails

| Day | Topic | Key Deliverables |
|-----|-------|------------------|
| **Day 1** | Agentic RAG & Tool Use | LangChain/LlamaIndex agents, function calling |
| **Day 2** | Planning & Reasoning | ReAct, Plan-and-Execute, Chain-of-Thought |
| **Day 3** | Guardrails & Safety | NeMo Guardrails, input/output validation |
| **Day 4** | Security & Data Privacy | PII redaction, injection prevention |
| **Day 5** | Red Teaming & Bias | Adversarial testing, bias detection |

---

## Week 13: Module 11 — Multi-Agent Systems (NEW)

| Day | Topic | Key Deliverables |
|-----|-------|------------------|
| **Day 1** | Multi-Agent Architecture | Coordinator, specialist agents, messaging |
| **Day 2** | Agent Communication & Protocols | Shared memory, message passing, consensus |
| **Day 3** | Multi-Agent RAG & Orchestration | Delegation, hierarchical agents |
| **Day 4** | Multi-Agent Frameworks | AutoGen, CrewAI, LangGraph |
| **Day 5** | Production Multi-Agent System | Failure handling, scaling, observability |

---

## Week 14: Capstone & Final Review

| Day | Topic | Key Deliverables |
|-----|-------|------------------|
| **Day 1-2** | Capstone Project | Architecture design, multi-tenant RAG chatbot |
| **Day 3** | Capstone Implementation | RBAC, evaluation pipeline |
| **Day 4** | Load Testing & Deployment | 1M+ document scaling |
| **Day 5** | Demo & Interview Prep | Comprehensive Q&A, optimization checklist |

---

## Capstone Project: Enterprise RAG Chatbot

**Requirements:**
- Multi-tenant support
- Role-based access control (RBAC)
- Metadata filtering
- Evaluation pipeline
- Monitoring dashboard
- Load testing (1M+ documents)
- Production deployment (Docker + K8s)

---

## Architectural Decision Framework (Applied Throughout)

For every major design decision:
1. **Compare 3 approaches** — Document alternatives
2. **Scalability analysis** — Throughput, latency, resource usage
3. **Cost analysis** — Compute, storage, API costs
4. **Failure modes** — Degradation, recovery, fallbacks
5. **Benchmarking methodology** — Reproducible evaluation
