# Setup Instructions

## Prerequisites

- Python 3.11+
- Docker & Docker Compose (for full stack)
- Git

## Quick Setup

```bash
# Clone the repository
cd AgenticAIBootCamp

# Create virtual environment
python -m venv .venv

# Activate (Windows PowerShell)
.venv\Scripts\Activate.ps1

# Activate (Linux/Mac)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Run tests
pytest tests/ -v

# Start ingestion service
uvicorn src.ingestion.main:app --reload
```

## Docker Setup (Full Stack)

```bash
docker-compose up -d
# Starts: Postgres, Redis, Elasticsearch, Milvus, Prometheus, Grafana
```

## Week 1 Labs

```bash
# Run PDF extraction (requires sample PDF in datasets/)
python labs/week1/run_pipeline.py --pdf datasets/sample.pdf

# Or run ingestion API and POST to /ingest
uvicorn src.ingestion.main:app --reload --port 8000
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| DATABASE_URL | PostgreSQL connection | postgresql://bootcamp:bootcamp_secret@localhost:5432/rag_bootcamp |
| REDIS_URL | Redis connection | redis://localhost:6379/0 |
| OPENAI_API_KEY | OpenAI API key | (required for RAG) |

Copy `.env.example` to `.env` in the project root for local overrides (never commit `.env`).
