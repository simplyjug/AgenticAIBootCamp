# Bootcamp Datasets

## Structure

```
datasets/
├── sample.pdf          # Sample text PDF for Week 1 labs
├── sample_scanned.pdf  # Sample scanned PDF (OCR testing)
├── sample.html         # Sample HTML for web extraction
├── eval/               # Evaluation datasets (Week 9)
│   └── rag_qa_pairs.json
└── benchmarks/         # Benchmark corpora
    └── ...
```

## Obtaining Sample Data

### PDF
- Create a simple PDF from any text document
- For OCR testing: scan a document or use a PDF of an image

### HTML
- Save any web page as HTML (File > Save As)
- Or use `curl -o sample.html https://example.com/article`

### Evaluation (Week 9)
- RAG QA pairs: query + expected relevant chunk IDs + ground truth answer
