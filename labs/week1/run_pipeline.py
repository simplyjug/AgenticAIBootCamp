"""
Week 1 - Run Document Ingestion Pipeline
Usage: python -m labs.week1.run_pipeline [--pdf PATH] [--url URL]
"""
from __future__ import annotations

import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Run Week 1 ingestion pipeline")
    parser.add_argument("--pdf", type=Path, help="Path to PDF file")
    parser.add_argument("--url", type=str, help="URL to fetch document")
    args = parser.parse_args()

    if args.pdf:
        from labs.week1.day01_basic_pdf import extract_text_pymupdf, detect_pdf_type  # noqa: E402
        pages = extract_text_pymupdf(args.pdf)
        pdf_type = detect_pdf_type(pages)
        print(f"Processed: {args.pdf}")
        print(f"  Type: {pdf_type}, Pages: {len(pages)}")
        print(f"  Total chars: {sum(p.char_count for p in pages)}")
        return

    if args.url:
        print("URL ingestion: use FastAPI /ingest with source_url")
        print("  curl -X POST http://localhost:8000/ingest -H 'Content-Type: application/json' -d '{\"source_url\": \"" + args.url + "\"}'")
        return

    parser.print_help()


if __name__ == "__main__":
    main()
