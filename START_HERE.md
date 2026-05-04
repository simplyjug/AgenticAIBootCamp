# Start here — self-service bootcamp guide

This repository is designed so you can complete it **without an instructor**: clone once, set up your environment, then follow **one week at a time** using `curriculum/week-XX/README.md` and the linked day guides.

**If you are preparing for interviews** (OpenAI, Anthropic, NVIDIA-class applied AI), read these **in parallel** — they are denser than the week guides on purpose:

- [**docs/AI_ENGINEERING_PLAYBOOK.md**](docs/AI_ENGINEERING_PLAYBOOK.md) — full-stack concepts, failure taxonomies, question bank  
- [**docs/AGENTIC_AI_ENGINEERING.md**](docs/AGENTIC_AI_ENGINEERING.md) — tool design, loops, multi-agent, observability  
- [**docs/INTERVIEW_COMPANION.md**](docs/INTERVIEW_COMPANION.md) — how to answer under time pressure  
- [**docs/CAREER_PORTFOLIO.md**](docs/CAREER_PORTFOLIO.md) — how to **fork** and present this as your portfolio  

## What you will build

Across 14 weeks you move from **document ingestion** → **data curation & classification** → **embeddings & vector search** → **RAG services & chat** → **evaluation & metadata** → **production operations** → **agentic & multi-agent systems** → **capstone**. Labs live under `labs/`; shared app code under `src/`.

## Prerequisites

- **Python 3.11+** (3.12 OK)
- **Git**
- **Docker Desktop** (optional but recommended from Week 5 onward for vector DBs and Week 11 for compose-based stacks)
- An **OpenAI API key** (or compatible endpoint) for LLM weeks — export as `OPENAI_API_KEY` when you reach RAG/agent labs

## One-time setup (Windows PowerShell)

```powershell
cd AgenticAIBootCamp
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

Copy [`.env.example`](.env.example) to `.env` when you add API keys. See [SETUP.md](SETUP.md) for service URLs.

## One-time setup (macOS / Linux)

```bash
cd AgenticAIBootCamp
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## How to study each week

1. Open **[docs/VIDEO_RESOURCES.md](docs/VIDEO_RESOURCES.md)** for that week’s **YouTube / official docs** (watch *before* deep-diving when a topic is new).
2. Read **`curriculum/week-NN/README.md`** for outcomes, time estimate, and the **weekly checklist**.
3. Each day, open the linked **`day-*.md`** file in the same folder. Complete **Hands-on** and **Done when** before moving on.
4. Run tests when you change code: `pytest tests/ -v` (or week-scoped tests if present).
5. At week end, tick **Done when** in the week README.

## Quick commands

| Goal | Command |
|------|---------|
| Install deps | `pip install -r requirements.txt` and `pip install -r requirements-dev.txt` |
| Week 1 pipeline | `python -m labs.week1.run_pipeline --pdf datasets/sample.pdf` (place a PDF in `datasets/` or use the sample generator in `scripts/create_sample_pdf.py`) |
| Week 7 RAG API | `python -m uvicorn labs.week7.rag_service:app --reload --port 8000` (after deps installed) |
| Week 8 chatbot API | `python -m uvicorn labs.week8.conversational_chatbot:app --reload --port 8000` |
| Tests | `pytest tests/ -v` |
| Lint (with dev deps) | `ruff check src/ labs/ tests/` |

On Unix systems with `make`, see [Makefile](Makefile) for `make install`, `make test`, etc. On Windows, use the Python commands above directly.

## GitHub usage

- **Fork** this repo to your account, then **clone your fork**.
- Push branches and open PRs against your fork for practice.
- Enable **Actions** in your fork to run CI (see [.github/workflows/ci.yml](.github/workflows/ci.yml)).
- Optional documentation site: see [DEPLOY.md](DEPLOY.md) for **MkDocs + GitHub Pages**.

## If you get stuck

1. Re-read the day’s **Failure modes** / **Troubleshooting** section.
2. Run the smallest command that reproduces the issue (often `pytest` or the FastAPI app with `--reload`).
3. Check [SETUP.md](SETUP.md) for services (`DATABASE_URL`, `REDIS_URL`, Docker).

## Suggested pace

- **8–12 hours per week** for working professionals (read + labs + short video playlist).
- **Full-time learners** can target **2–3 weeks per calendar week** for the first modules if prerequisites are strong.

Next step: open **[curriculum/week-01/README.md](curriculum/week-01/README.md)** and **[docs/VIDEO_RESOURCES.md](docs/VIDEO_RESOURCES.md)**.
