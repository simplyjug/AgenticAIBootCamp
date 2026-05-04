"""
Week 1 - Day 1: PDF Processing Fundamentals

Purpose:
- Extract text from PDFs using PyMuPDF (fitz)
- Detect text-based vs scanned PDFs for routing (text extraction vs OCR)
- Production consideration: use pdfplumber for table-heavy docs

Usage:
    pages = extract_text_pymupdf(Path("doc.pdf"))
    pdf_type = detect_pdf_type(pages)  # "text" or "scanned"
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal

# PyMuPDF: fast C backend, best for text extraction. Use pdfplumber for tables.
try:
    import fitz  # PyMuPDF - package name is pymupdf, import as fitz
except ImportError:
    fitz = None


@dataclass
class PageContent:
    """
    Content extracted from a single PDF page.
    page_num: 1-indexed page number
    char_count: used for text vs scanned detection (low = likely scanned)
    images_count: scanned PDFs often have 1 large image per page
    """

    page_num: int
    text: str
    char_count: int
    images_count: int


def extract_text_pymupdf(pdf_path: Path) -> list[PageContent]:
    """
    Extract text from PDF using PyMuPDF.
    For scanned PDFs, text will be empty/minimal - use OCR pipeline instead.
    """
    if fitz is None:
        raise ImportError("PyMuPDF (fitz) is required. Install with: pip install pymupdf")

    doc = fitz.open(pdf_path)
    pages = []
    for i, page in enumerate(doc):
        text = page.get_text()
        images = page.get_images()
        pages.append(
            PageContent(
                page_num=i + 1,
                text=text.strip(),
                char_count=len(text),
                images_count=len(images),
            )
        )
    doc.close()
    return pages


def detect_pdf_type(
    pages: list[PageContent],
    min_chars: int = 50,
) -> Literal["text", "scanned"]:
    """
    Detect if PDF is text-based or scanned based on character density per page.
    Scanned PDFs have near-zero extractable text; text PDFs have hundreds+ chars/page.
    min_chars: threshold for average chars per page (default 50).
    """
    if not pages:
        return "scanned"
    avg_chars = sum(p.char_count for p in pages) / len(pages)
    return "text" if avg_chars >= min_chars else "scanned"


def run_example():
    """Run example extraction (requires sample PDF)."""
    sample_path = Path(__file__).parent.parent.parent / "datasets" / "sample.pdf"
    if not sample_path.exists():
        print("No sample.pdf in datasets/ - create one or use your own path")
        return
    pages = extract_text_pymupdf(sample_path)
    pdf_type = detect_pdf_type(pages)
    print(f"Detected: {pdf_type}, Pages: {len(pages)}, Chars/page avg: {sum(p.char_count for p in pages) / len(pages):.0f}")


if __name__ == "__main__":
    run_example()
