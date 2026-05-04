"""
Week 6: Chunking Strategies

Compares:
- Fixed-size (by chars/tokens)
- Sentence-boundary
- Recursive (by separator hierarchy)
"""
from __future__ import annotations

import re
from typing import List

# Use tiktoken for OpenAI-compatible token count
try:
    import tiktoken
    HAS_TIKTOKEN = True
except ImportError:
    HAS_TIKTOKEN = False


def chunk_by_sentences(text: str, max_sentences: int = 5) -> List[str]:
    """
    Chunk by sentence boundaries. Preserves readability.
    """
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    current = []
    count = 0
    for s in sentences:
        current.append(s)
        count += 1
        if count >= max_sentences:
            chunks.append(" ".join(current))
            current = []
            count = 0
    if current:
        chunks.append(" ".join(current))
    return chunks


def chunk_fixed_size(text: str, chunk_size: int = 512, overlap: int = 50) -> List[str]:
    """
    Fixed-size chunking with overlap.
    Overlap helps avoid losing context at boundaries.
    """
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        if chunk.strip():
            chunks.append(chunk)
        start = end - overlap
    return chunks


def chunk_by_tokens(text: str, max_tokens: int = 256) -> List[str]:
    """
    Chunk by token count (OpenAI tiktoken).
    More accurate for LLM context windows.
    """
    if not HAS_TIKTOKEN:
        # Fallback: ~4 chars per token
        return chunk_fixed_size(text, chunk_size=max_tokens * 4, overlap=0)
    enc = tiktoken.get_encoding("cl100k_base")
    tokens = enc.encode(text)
    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunk_tokens = tokens[i:i + max_tokens]
        chunks.append(enc.decode(chunk_tokens))
    return chunks


def recursive_chunk(text: str, separators: List[str] = None) -> List[str]:
    """
    Recursive splitting: try separators in order.
    First split by \\n\\n, then \\n, then space.
    """
    if separators is None:
        separators = ["\n\n", "\n", ". ", " "]
    if not separators or len(text) < 100:
        return [text] if text.strip() else []
    sep = separators[0]
    parts = text.split(sep)
    results = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        if len(p) > 500:  # Recurse if still too long
            results.extend(recursive_chunk(p, separators[1:]))
        else:
            results.append(p)
    return results
