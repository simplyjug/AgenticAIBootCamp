"""
Document Ingestion Microservice - FastAPI
Week 1 - Day 6: Production ingestion API
"""
from __future__ import annotations

import hashlib
import uuid
from typing import Optional

from fastapi import BackgroundTasks, FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Document Ingestion Service",
    description="Production document ingestion for RAG pipeline",
    version="0.1.0",
)


class IngestRequest(BaseModel):
    """Request body for document ingestion."""

    source_url: Optional[str] = None
    document_base64: Optional[str] = None


class IngestResponse(BaseModel):
    """Response after queuing ingestion job."""

    job_id: str
    content_hash: str
    status: str


# In-memory job store (replace with Redis/DB in production)
_jobs: dict[str, dict] = {}


def _get_content_hash(source_url: Optional[str], document_base64: Optional[str]) -> str:
    if source_url:
        return hashlib.sha256(source_url.encode()).hexdigest()
    if document_base64:
        return hashlib.sha256(document_base64.encode()).hexdigest()
    raise ValueError("No content to hash")


@app.post("/ingest", response_model=IngestResponse)
async def ingest(request: IngestRequest, background_tasks: BackgroundTasks):
    """
    Queue a document for ingestion.
    Provide either source_url (to fetch) or document_base64 (direct upload).
    """
    if not request.source_url and not request.document_base64:
        raise HTTPException(400, "Provide source_url or document_base64")

    content_hash = _get_content_hash(request.source_url, request.document_base64)
    job_id = str(uuid.uuid4())

    _jobs[job_id] = {
        "status": "queued",
        "content_hash": content_hash,
        "progress": 0.0,
    }

    # In production: celery_app.ingest_document_task.delay(...)
    background_tasks.add_task(_process_document, job_id, request)

    return IngestResponse(
        job_id=job_id,
        content_hash=content_hash,
        status="queued",
    )


def _process_document(job_id: str, request: IngestRequest):
    """Placeholder for actual processing (parse -> chunk -> embed)."""
    _jobs[job_id]["status"] = "processing"
    _jobs[job_id]["progress"] = 0.5
    # Simulate completion
    _jobs[job_id]["status"] = "completed"
    _jobs[job_id]["progress"] = 1.0


@app.get("/status/{job_id}")
async def status(job_id: str):
    """Get ingestion job status."""
    if job_id not in _jobs:
        raise HTTPException(404, f"Job {job_id} not found")
    return _jobs[job_id]


@app.get("/health")
async def health():
    """Health check for load balancers."""
    return {"status": "ok"}
