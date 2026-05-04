# Week 1: Module 0 — Document processing & multimodal ingestion

**Time:** ~10–14 hours · **Prerequisites:** Python, basic CLI, optional Docker for later stack

## What you will be able to do

- Classify **text vs scanned** PDFs and pick extractors (PyMuPDF, pdfplumber, OCR).
- Build an **ingestion path** for HTML and controlled crawling.
- Describe how **image + text** documents map to a **hybrid** RAG index.
- Sketch **async ingestion**, quality checks, and storage boundaries.

## Self-service flow

1. Read **[docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-1)** (20–40 min).
2. Work **Day 1 → Day 6** in order (see table below). Do not skip the hands-on blocks.
3. Run tests touching Week 1: `pytest tests/week1/ -v` (if present) or the Week 1 pipeline command.
4. Check the **Done when** list at the bottom.

## Week at a glance

```mermaid
graph LR
    A[Day 1: PDF] --> B[Day 2: Advanced PDF]
    B --> C[Day 3: HTML & crawl]
    C --> D[Day 4: Multimodal]
    D --> E[Day 5: Schema & chunking]
    E --> F[Day 6: Pipeline & quality]
```

## Day-by-day

| Day | Topic | Guide | Code / command |
|-----|--------|--------|----------------|
| 1 | PDF fundamentals | [day-01-pdf-fundamentals.md](day-01-pdf-fundamentals.md) | `labs/week1/day01_basic_pdf.py`, `run_pipeline.py` |
| 2 | Advanced PDF, tables, OCR | [day-02-advanced-pdf.md](day-02-advanced-pdf.md) | Extend `run_pipeline` with fallbacks |
| 3 | HTML & crawling | [day-03-html-crawling.md](day-03-html-crawling.md) | New script or `src/ingestion` |
| 4 | Multimodal | [day-04-multimodal.md](day-04-multimodal.md) | Design + optional CLIP/SigLIP experiment |
| 5 | Schema & chunking | [day-05-schema-chunking.md](day-05-schema-chunking.md) | JSON schema + chunk strategy |
| 6 | Pipeline & quality | [day-06-pipeline-quality.md](day-06-pipeline-quality.md) | Async job + quality score |

**Ingestion API (optional this week):** `python -m uvicorn src.ingestion.main:app --reload --port 8000` after wiring routes (see [SETUP.md](../../SETUP.md)).

## New AI / data engineering concepts

- **Dual-path PDF:** structure-based text vs raster **OCR** with different SLAs and costs.
- **Document IR:** reading order, headers/footers, and layout blocks as first-class objects.
- **Multimodal RAG:** align text chunks with image embeddings for hybrid retrieval.

## Done when

- [ ] You can explain when PyMuPDF vs pdfplumber vs OCR wins.
- [ ] You produced structured output (JSON or DB rows) from at least one PDF and one HTML source.
- [ ] You documented **failure modes** (empty extract, bad encoding, huge scans) and mitigations.
- [ ] `pytest tests/week1/ -v` passes (or your pipeline runs end-to-end on `datasets/sample.pdf`).

## Resources

- **Videos / links:** [docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md) (Week 1 section).
- **Project setup:** [START_HERE.md](../../START_HERE.md), [SETUP.md](../../SETUP.md).
