"""
Canonical document schema for ingestion pipeline.
Supports PDF, HTML, and multi-modal documents.
"""
from __future__ import annotations

from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, Field


class DocType(str, Enum):
    PDF = "pdf"
    HTML = "html"
    MARKDOWN = "markdown"


class ChunkType(str, Enum):
    PARAGRAPH = "paragraph"
    TABLE = "table"
    LIST = "list"
    TITLE = "title"
    IMAGE = "image"


class ChunkMetadata(BaseModel):
    """Metadata attached to each chunk."""

    page_start: Optional[int] = None
    page_end: Optional[int] = None
    section_title: Optional[str] = None
    section_level: Optional[int] = None
    chunk_type: ChunkType = ChunkType.PARAGRAPH
    extra: dict[str, Any] = Field(default_factory=dict)


class Chunk(BaseModel):
    """A single chunk of document content."""

    id: str
    document_id: str
    parent_id: Optional[str] = None
    section_id: Optional[str] = None
    content: str
    metadata: ChunkMetadata = Field(default_factory=ChunkMetadata)
    token_count: int = 0


class Section(BaseModel):
    """Document section with hierarchy."""

    id: str
    level: int
    title: str
    page_start: Optional[int] = None
    page_end: Optional[int] = None
    children: list[str] = Field(default_factory=list)


class DocumentSource(BaseModel):
    """Source information for the document."""

    type: DocType
    path: Optional[str] = None
    url: Optional[str] = None


class CanonicalDocument(BaseModel):
    """Canonical document schema - output of ingestion pipeline."""

    document_id: str
    content_hash: str
    source: DocumentSource
    metadata: dict[str, Any] = Field(default_factory=dict)
    sections: list[Section] = Field(default_factory=list)
    chunks: list[Chunk] = Field(default_factory=list)
