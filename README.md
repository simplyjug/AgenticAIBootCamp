<div align="center">

# Generative AI & Agentic AI Bootcamp

### A serious, end-to-end curriculum for **AI engineers** who ship — ingestion, embeddings, vector search, RAG, evaluation, production, **generative models**, **agentic patterns**, and multi-agent systems.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![CI: GitHub Actions](https://img.shields.io/badge/CI-GitHub_Actions-2088FF?logo=githubactions&logoColor=white)](.github/workflows/ci.yml)

**Clone → study → build → talk about it in interviews** (OpenAI, Anthropic, NVIDIA-class applied roles).

[Start here](START_HERE.md) · [AI Engineering Playbook](docs/AI_ENGINEERING_PLAYBOOK.md) · [Generative AI Engineering](docs/GENERATIVE_AI_ENGINEERING.md) · [Agentic AI Engineering](docs/AGENTIC_AI_ENGINEERING.md) · [Interview companion](docs/INTERVIEW_COMPANION.md) · [Career & portfolio](docs/CAREER_PORTFOLIO.md) · [Video resources](docs/VIDEO_RESOURCES.md)

</div>

---

## Why this repo exists

Most “LLM courses” stop at prompts. **Top AI engineering roles** expect you to own:

- **Data & ingestion quality** (bad PDFs, ACLs, drift)
- **Retrieval science** (chunking, hybrid search, reranking, ANN tradeoffs)
- **Evaluation** (golden sets, faithfulness, online A/B discipline)
- **Production** (latency tails, cost, observability, safe rollback)
- **Agentic systems** (tools as APIs, loops with budgets, multi-agent when justified — not hype)

This bootcamp is a **structured path** plus **deep playbooks** so you can refresh the entire stack before interviews and point recruiters at **real code** under `labs/`.

---

## Who this is for

- Software / ML engineers moving into **LLM platform**, **RAG**, **agents**, or **AI product** teams  
- Anyone who wants a **single Git clone** that covers the **full modern AI stack** with interview-level depth  
- Builders preparing for **system design** + **coding** + **safety** loops at frontier labs  

**Prerequisites:** strong Python, basic ML, HTTP/APIs, willingness to read docs and run Docker for some modules.

---

## Documentation map (read in this order for interviews)

| Document | Purpose |
|----------|---------|
| [**docs/DOCUMENTATION_INDEX.md**](docs/DOCUMENTATION_INDEX.md) | **Hub** — every major doc linked in one place |
| [**START_HERE.md**](START_HERE.md) | Environment, workflow, commands |
| [**docs/AI_ENGINEERING_PLAYBOOK.md**](docs/AI_ENGINEERING_PLAYBOOK.md) | **Dense** end-to-end concepts + failure taxonomies + question bank |
| [**docs/GENERATIVE_AI_ENGINEERING.md**](docs/GENERATIVE_AI_ENGINEERING.md) | Prompt engineering, fine-tuning, safety, deployment |
| [**docs/AGENTIC_AI_ENGINEERING.md**](docs/AGENTIC_AI_ENGINEERING.md) | Tool design, loops, multi-agent, observability, **patterns** |
| [**docs/INTERVIEW_COMPANION.md**](docs/INTERVIEW_COMPANION.md) | Oral exam structure, system design skeletons, rapid-fire |
| [**docs/CAREER_PORTFOLIO.md**](docs/CAREER_PORTFOLIO.md) | How to **fork**, extend, and present this as *your* portfolio |
| [**CURRICULUM.md**](CURRICULUM.md) | 14-week outline (calendar-style) |
| [**docs/VIDEO_RESOURCES.md**](docs/VIDEO_RESOURCES.md) | Curated YouTube + official docs |
| [**GITHUB_PUSH.md**](GITHUB_PUSH.md) | **Publish to GitHub** (auth + first push) |

---

## Quick start

```bash
git clone https://github.com/<you>/AgenticAIBootCamp.git
cd AgenticAIBootCamp

python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux

pip install -r requirements.txt
pip install -r requirements-dev.txt
copy .env.example .env          # then add OPENAI_API_KEY for LLM weeks

pytest tests/ -v
```

**Labs you should be able to demo:**

```bash
# Week 1 — PDF / pipeline
python -m labs.week1.run_pipeline --pdf datasets/sample.pdf

# Week 5 — FAISS persistence + benchmark
python -m labs.week5.faiss_production

# Week 7 — RAG API
python -m uvicorn labs.week7.rag_service:app --reload --port 8000

# Week 8 — Conversational RAG
python -m uvicorn labs.week8.conversational_chatbot:app --reload --port 8000

# Week 9 — Retrieval metrics demo
python -m labs.week9.rag_evaluation
```

On Unix with `make`: `make install`, `make test`, `make run-week7`, etc.

---

## Repository structure

| Path | Contents |
|------|----------|
| `docs/` | **Playbooks**, interview prep, videos, career guide |
| `curriculum/week-01` … `week-14` | Week + **day** guides (hands-on + interview hooks) |
| `labs/` | Runnable code (RAG, eval, chunking, agents, …) |
| `src/` | Shared services (e.g. ingestion) |
| `handbook/` | MkDocs sources (snippets into `docs/` + curriculum) |
| `.github/workflows/` | CI + optional **GitHub Pages** deploy |

---

## Curriculum at a glance

| Block | Topics |
|-------|--------|
| **0–2** | Documents, curation, dedup, governance |
| **3–4** | Classification, embeddings, ANN |
| **5–6** | Vector DBs, **chunking as retrieval policy** |
| **7–8** | **RAG**, hybrid, chat, caching, failure modes |
| **9** | **Evaluation** (recall@k, faithfulness, A/B) |
| **10** | Metadata, enrichment, schema for hybrid filters |
| **11** | Production: observability, deploy, cost, flags |
| **12** | **Agentic AI**: tools, planning, guardrails, security, red team |
| **13** | **Multi-agent** coordination & frameworks |
| **14** | **Capstone** + interview sprint |

---

## Optional documentation site (MkDocs)

```bash
pip install mkdocs mkdocs-material pymdown-extensions
mkdocs serve
```

See [**DEPLOY.md**](DEPLOY.md) for **GitHub Pages** and [**GITHUB_PUSH.md**](GITHUB_PUSH.md) to publish your fork.

---

## Certification

Complete the bootcamp and earn a **Generative AI & Agentic AI Engineer Certification** from [AIDeeva.com](https://aideeva.com). 

To get certified:
1. Finish all weeks and labs.
2. Submit your completion details via [this form](https://forms.gle/example) (replace with actual form link).
3. Receive your certificate via email.

---

---

## License

[**MIT**](LICENSE) — use commercially, fork freely, attribute appreciated.

---

## Maintainer note — replace placeholders

After you fork, replace `YOUR_GITHUB_USERNAME` in this README (badge + links) and in `mkdocs.yml` (`site_url`, `repo_url`). See [GITHUB_PUSH.md](GITHUB_PUSH.md).
