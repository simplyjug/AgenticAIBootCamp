"""
Week 7: RAG Service — Naive & Hybrid RAG

Complete FastAPI RAG service with:
- Vector retrieval (FAISS or in-memory)
- Optional hybrid (vector + BM25) - extend retrieve() for BM25 fusion
- OpenAI completion
- Structured response (Pydantic)

Naive RAG flow: Query -> Embed -> Retrieve top_k -> Concatenate context -> LLM generate
Hybrid RAG: Same but retrieve from both vector index and BM25; merge with RRF.

Production: Replace SimpleRetriever with Milvus/Pinecone/Weaviate client.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

# Optional dependencies
try:
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel
    import openai
    import numpy as np
    import faiss
    HAS_DEPS = True
except ImportError:
    HAS_DEPS = False


# =============================================================================
# REQUEST / RESPONSE MODELS
# =============================================================================


class RAGRequest(BaseModel):
    """Incoming query for RAG."""
    query: str
    top_k: int = 5
    use_hybrid: bool = False


class RetrievedChunk(BaseModel):
    """Single retrieved chunk with score."""
    content: str
    score: float
    metadata: dict = {}


class RAGResponse(BaseModel):
    """RAG response with answer and sources."""
    answer: str
    sources: List[RetrievedChunk]
    model: str = "gpt-4o-mini"


# =============================================================================
# RETRIEVER — Vector + optional keyword
# =============================================================================


@dataclass
class Chunk:
    """Stored chunk with embedding and metadata."""
    id: str
    content: str
    embedding: List[float]
    metadata: dict


class SimpleRetriever:
    """
    In-memory retriever using FAISS.
    For production, replace with Milvus/Pinecone/Weaviate.
    """

    def __init__(self, dim: int = 384):
        self.dim = dim
        self.index = faiss.IndexFlatIP(dim)  # Inner product (cosine for normalized)
        self.chunks: List[Chunk] = []
        self._embed_model = None

    def _embed(self, texts: List[str]) -> np.ndarray:
        """Embed texts. Uses sentence-transformers if available."""
        try:
            from sentence_transformers import SentenceTransformer
            if self._embed_model is None:
                self._embed_model = SentenceTransformer("all-MiniLM-L6-v2")
            embs = self._embed_model.encode(texts, normalize_embeddings=True)
            return embs.astype(np.float32)
        except ImportError:
            # Fallback: random vectors for testing
            return np.random.randn(len(texts), self.dim).astype(np.float32) / np.sqrt(self.dim)

    def add_chunks(self, chunks: List[Chunk]) -> None:
        """Add chunks to index."""
        for c in chunks:
            self.chunks.append(c)
        if chunks:
            embs = np.array([c.embedding for c in chunks], dtype=np.float32)
            faiss.normalize_L2(embs)
            self.index.add(embs)

    def search(self, query: str, top_k: int = 5) -> List[tuple[Chunk, float]]:
        """Retrieve top_k chunks by vector similarity."""
        q_emb = self._embed([query])
        faiss.normalize_L2(q_emb)
        scores, indices = self.index.search(q_emb, min(top_k, len(self.chunks)))
        results = []
        for i, idx in enumerate(indices[0]):
            if idx >= 0 and idx < len(self.chunks):
                results.append((self.chunks[idx], float(scores[0][i])))
        return results


# =============================================================================
# RAG PIPELINE
# =============================================================================


class RAGPipeline:
    """
    End-to-end RAG: retrieve → format context → generate.
    """

    def __init__(
        self,
        retriever: SimpleRetriever,
        model: str = "gpt-4o-mini",
        max_context_tokens: int = 2000,
    ):
        self.retriever = retriever
        self.model = model
        self.max_context_tokens = max_context_tokens

    def _format_context(self, chunks: List[tuple[Chunk, float]]) -> str:
        """Format retrieved chunks into context string for LLM."""
        parts = []
        for i, (chunk, score) in enumerate(chunks, 1):
            parts.append(f"[{i}] {chunk.content}")
        return "\n\n".join(parts)

    def _build_prompt(self, query: str, context: str) -> str:
        """Build RAG prompt with context and query."""
        return f"""Use the following context to answer the question. If the context doesn't contain the answer, say so.

Context:
{context}

Question: {query}

Answer:"""

    def run(
        self,
        query: str,
        top_k: int = 5,
    ) -> RAGResponse:
        """
        Run RAG pipeline: retrieve → generate.
        """
        # Step 1: Retrieve
        retrieved = self.retriever.search(query, top_k=top_k)
        if not retrieved:
            return RAGResponse(
                answer="No relevant context found.",
                sources=[],
                model=self.model,
            )

        # Step 2: Format context
        context = self._format_context(retrieved)

        # Step 3: Generate (requires OpenAI API key)
        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "user", "content": self._build_prompt(query, context)}
                ],
                max_tokens=500,
            )
            answer = response.choices[0].message.content
        except Exception as e:
            answer = f"[Generation error: {e}]"

        sources = [
            RetrievedChunk(content=c.content, score=s, metadata=c.metadata)
            for c, s in retrieved
        ]

        return RAGResponse(answer=answer, sources=sources, model=self.model)


# =============================================================================
# FASTAPI APP
# =============================================================================


def create_app(retriever: Optional[SimpleRetriever] = None) -> "FastAPI":
    """Create FastAPI app with RAG endpoint."""
    if not HAS_DEPS:
        raise ImportError("Install: fastapi uvicorn openai faiss-cpu numpy")

    app = FastAPI(title="RAG Service")
    pipeline = RAGPipeline(retriever=retriever or SimpleRetriever())

    @app.post("/query", response_model=RAGResponse)
    async def query(req: RAGRequest):
        return pipeline.run(query=req.query, top_k=req.top_k)

    return app


if __name__ == "__main__":
    app = create_app()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
