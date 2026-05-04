"""
Week 10 — Canonical document record for ingest → index → API → tools.

Run: python -m labs.week10.document_record
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional

from pydantic import AnyUrl, BaseModel, Field


class DocumentRecord(BaseModel):
    """Single document/chunk row shape — extend fields per product."""

    id: str
    text: str = Field(..., description="Text embedded and/or shown to LLM")
    tenant_id: str
    acl_principals: frozenset[str] = Field(default_factory=frozenset)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    language: str = "en"
    topic_path: Optional[str] = None
    source_uri: Optional[AnyUrl] = None

    model_config = {"frozen": False}


def main() -> None:
    ex = DocumentRecord(
        id="doc-1",
        text="Sample policy text.",
        tenant_id="tenant-a",
        acl_principals=frozenset({"user:123", "group:hr"}),
        topic_path="hr.policy.leave",
    )
    print(ex.model_dump_json(indent=2))
    schema = DocumentRecord.model_json_schema()
    print("schema title:", schema.get("title"))


if __name__ == "__main__":
    main()
