# Day 1: NER & keyword extraction for retrieval metadata

> **Playbook:** [AI_ENGINEERING_PLAYBOOK.md](../../docs/AI_ENGINEERING_PLAYBOOK.md) §9 Metadata  
> **Lab:** `labs/week10/ner_keywords.py`

---

## 1. Interview framing

**Question:** “How do you make RAG better without a bigger model?”  
**Strong answer:** “Structured **metadata** for filtering + hybrid retrieval — entities and keywords are cheap signals that disambiguate SKUs, laws, and product lines.”

NER (named entity recognition) and keyword extractors turn **unstructured** text into **facets** your UI and retriever can trust — when quality is monitored.

---

## 2. NER approaches (tradeoffs)

| Approach | When to use | Pitfalls |
|----------|-------------|----------|
| **spaCy / CRF-style** small models | High throughput, predictable CPU | Domain shift (finance vs news) |
| **Transformer token classification** | Higher accuracy with enough labels | GPU/latency cost at ingest |
| **LLM extraction** | Schema-flexible, great zero-shot | Cost + variance; needs validation |

**Production default:** start with a **small deterministic** pipeline + **spot-check**; graduate to HF model when error rate measured on gold entities exceeds threshold.

---

## 3. Keywords: classical vs neural

- **TF–IDF / YAKE / RAKE** — cheap, explainable; good for glossaries.
- **KeyBERT** (embedding similarity to candidate phrases) — better semantic “topics” but heavier.

Use keywords for **BM25 sidecar** in hybrid retrieval and for **human facets** in UI.

---

## 4. Running the lab

```bash
python labs/week10/ner_keywords.py
# Optional high quality:
pip install spacy
python -m spacy download en_core_web_sm
python labs/week10/ner_keywords.py
```

Extend the script to output **JSON lines** suitable for ingestion:

```json
{"doc_id": "d1", "entities": [{"text": "WHO", "label": "ORG"}], "keywords": ["shipment", "agreement"]}
```

---

## 5. Quality & governance

- **PII entities** (`PERSON`, `GPE` in some corpora) — decide redaction before indexing.
- **Confidence thresholds** — drop low-confidence spans from filters (avoid false negatives in legal search).
- **Version** models: `ner_model=v2` stored per document for replay.

---

## 6. Interview drills

1. **Why not LLM-extract everything at ingest?**  
2. **How do you prevent NER drift after deploy?**  
3. **What metadata is unsafe to expose in the client?**

Write 5-sentence answers in your notes.

---

## 7. Done when

- [ ] Script outputs structured JSON for ≥3 sample strings.
- [ ] List of **which entity types** you would index vs display-only.
- [ ] Read Playbook **§9** and link one idea to your output schema.
