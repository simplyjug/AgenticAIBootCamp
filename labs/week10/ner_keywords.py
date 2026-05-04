"""
Week 10 — NER + keyword extraction lab stub.

Optional: pip install spacy && python -m spacy download en_core_web_sm
Fallback path uses simple regex + word frequency if spaCy is missing.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from typing import Any

try:
    import spacy

    _nlp = spacy.load("en_core_web_sm")
except Exception:  # pragma: no cover - optional dep
    _nlp = None


def _basic_keywords(text: str, top_k: int = 8) -> list[str]:
    words = re.findall(r"[A-Za-z]+", text.lower())
    stop = {
        "the", "a", "an", "and", "or", "to", "of", "in", "is", "it", "for", "on", "with",
    }
    filt = [w for w in words if w not in stop and len(w) > 2]
    return [w for w, _ in Counter(filt).most_common(top_k)]


def enrich(text: str) -> dict[str, Any]:
    if _nlp is not None:
        doc = _nlp(text[:100000])
        ents = [{"text": e.text, "label": e.label_} for e in doc.ents]
        keywords = _basic_keywords(text)
        return {"entities": ents, "keywords": keywords, "backend": "spacy"}
    return {"entities": [], "keywords": _basic_keywords(text), "backend": "basic"}


def main() -> None:
    sample = (
        "Apple Inc. signed an agreement with WHO in Geneva regarding shipment ETA Q4."
    )
    print(json.dumps(enrich(sample), indent=2))


if __name__ == "__main__":
    main()
