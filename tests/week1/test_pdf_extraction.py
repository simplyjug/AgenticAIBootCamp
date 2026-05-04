"""
Unit tests for Week 1 PDF extraction.
"""
from pathlib import Path

import pytest

# Skip if PyMuPDF not installed
pymupdf = pytest.importorskip("fitz", reason="PyMuPDF not installed")

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from labs.week1.day01_basic_pdf import (
    PageContent,
    detect_pdf_type,
    extract_text_pymupdf,
)


def test_extract_returns_list(tmp_path):
    """Extract should return list of PageContent."""
    import fitz
    tmp = tmp_path / "test.pdf"
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((50, 50), "Test content for extraction.")
    doc.save(str(tmp))
    doc.close()
    pages = extract_text_pymupdf(tmp)
    assert isinstance(pages, list)
    assert len(pages) >= 1
    assert all(isinstance(p, PageContent) for p in pages)
    assert pages[0].char_count > 0


def test_detect_pdf_type_text():
    """Text PDF should be detected as 'text'."""
    pages = [
        PageContent(page_num=1, text="A" * 100, char_count=100, images_count=0),
    ]
    assert detect_pdf_type(pages, min_chars=50) == "text"


def test_detect_pdf_type_scanned():
    """Low character count should be 'scanned'."""
    pages = [
        PageContent(page_num=1, text="x", char_count=1, images_count=1),
    ]
    assert detect_pdf_type(pages, min_chars=50) == "scanned"
