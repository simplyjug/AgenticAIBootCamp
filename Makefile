# Advanced AI Engineering & RAG Systems Bootcamp
# Makefile for build, test, benchmark, and deployment

.PHONY: install install-dev test lint format benchmark run-week1 run-week7 run-week8 run-week9 run-ingestion help

# Default target
help:
	@echo "Advanced AI Engineering & RAG Bootcamp - Available commands:"
	@echo ""
	@echo "  make install        - Install production dependencies"
	@echo "  make install-dev    - Install dev dependencies"
	@echo "  make test           - Run full test suite"
	@echo "  make lint           - Run linters (ruff, mypy)"
	@echo "  make format         - Format code (black, isort)"
	@echo "  make benchmark      - Run benchmark suite"
	@echo "  make run-week1      - Run Week 1 ingestion pipeline"
	@echo "  make run-week7      - Start Week 7 RAG FastAPI app"
	@echo "  make run-week8      - Start Week 8 conversational chatbot"
	@echo "  make run-week9      - Run Week 9 eval script (if entrypoint set)"
	@echo "  make run-ingestion  - Start ingestion microservice"
	@echo "  make docker-up      - Start Docker services"
	@echo "  make docker-down    - Stop Docker services"

# Virtual environment
VENV := .venv
PYTHON := $(VENV)/Scripts/python
PIP := $(VENV)/Scripts/pip

install:
	$(PIP) install -r requirements.txt

install-dev: install
	$(PIP) install -r requirements-dev.txt

# Testing
test:
	$(PYTHON) -m pytest tests/ -v --tb=short -x

test-cov:
	$(PYTHON) -m pytest tests/ -v --cov=src --cov-report=html --cov-report=term-missing

test-week1:
	$(PYTHON) -m pytest tests/week1/ -v --tb=short

# Linting
lint:
	ruff check src/ labs/ tests/
	mypy src/ --ignore-missing-imports

format:
	black src/ labs/ tests/
	isort src/ labs/ tests/

# Benchmarks
benchmark:
	$(PYTHON) benchmarks/run_all.py

benchmark-ingestion:
	$(PYTHON) benchmarks/ingestion_benchmark.py

# Week 1 / Ingestion
run-week1:
	$(PYTHON) -m labs.week1.run_pipeline --pdf datasets/sample.pdf

run-week7:
	$(PYTHON) -m uvicorn labs.week7.rag_service:app --reload --host 0.0.0.0 --port 8000

run-week8:
	$(PYTHON) -m uvicorn labs.week8.conversational_chatbot:app --reload --host 0.0.0.0 --port 8000

run-week9:
	$(PYTHON) -m labs.week9.rag_evaluation

run-ingestion:
	$(PYTHON) -m uvicorn src.ingestion.main:app --reload --host 0.0.0.0 --port 8000

# Docker
docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

docker-build:
	docker-compose build

# CI simulation
ci: lint test
	@echo "CI pipeline passed"
