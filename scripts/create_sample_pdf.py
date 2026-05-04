"""Create sample.pdf for Week 1 labs if not present."""
from pathlib import Path

try:
    import fitz
except ImportError:
    print("PyMuPDF required: pip install pymupdf")
    exit(1)

out = Path(__file__).parent.parent / "datasets" / "sample.pdf"
out.parent.mkdir(parents=True, exist_ok=True)
if out.exists():
    print(f"{out} already exists")
    exit(0)
doc = fitz.open()
page = doc.new_page()
page.insert_text((50, 50), "Advanced AI Engineering & RAG Systems Bootcamp - Sample Document")
page.insert_text((50, 80), "This is a sample PDF for testing the ingestion pipeline.")
page.insert_text((50, 110), "It contains multiple lines of text for extraction exercises.")
doc.save(str(out))
doc.close()
print(f"Created {out}")
