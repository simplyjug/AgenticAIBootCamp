"""
Week 2 - Day 1: Data Sourcing & Pipelines

Architecture:
- Web scraping with rate limiting and politeness
- API ingestion with pagination and exponential backoff
- Incremental ingestion with content hashing
"""
from __future__ import annotations

import hashlib
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import AsyncIterator, Iterator

import httpx


# =============================================================================
# DATA MODELS
# =============================================================================


@dataclass
class RawDocument:
    """
    Represents a raw document fetched from any source.
    Used as input for downstream processing (parse, chunk, embed).
    """

    source_id: str  # Unique ID from source (URL, API key, etc.)
    content: bytes | str  # Raw bytes or decoded string
    content_type: str  # e.g., "application/pdf", "text/html"
    metadata: dict  # Source-specific metadata (url, timestamp, etc.)


@dataclass
class FetchResult:
    """Result of a fetch operation with status and optional error."""

    document: RawDocument | None
    success: bool
    error: str | None = None


# =============================================================================
# RATE LIMITER - Ensures we don't exceed source rate limits
# =============================================================================


class RateLimiter:
    """
    Token bucket style rate limiter.
    Allows max `requests_per_second` requests; blocks when exceeded.
    """

    def __init__(self, requests_per_second: float = 1.0):
        self.min_interval = 1.0 / requests_per_second
        self.last_request_time = 0.0

    def wait(self) -> None:
        """Block until next request is allowed."""
        now = time.monotonic()
        elapsed = now - self.last_request_time
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        self.last_request_time = time.monotonic()


# =============================================================================
# API INGESTION - Handles pagination and exponential backoff
# =============================================================================


class APIIngester:
    """
    Generic API ingester with:
    - Exponential backoff on 429/5xx
    - Pagination support
    - Content hashing for deduplication
    """

    def __init__(
        self,
        base_url: str,
        rate_limit: float = 2.0,
        max_retries: int = 3,
        backoff_base: float = 2.0,
    ):
        self.base_url = base_url.rstrip("/")
        self.rate_limiter = RateLimiter(requests_per_second=rate_limit)
        self.max_retries = max_retries
        self.backoff_base = backoff_base

    def _compute_content_hash(self, content: bytes | str) -> str:
        """SHA256 hash for deduplication and change detection."""
        if isinstance(content, str):
            content = content.encode("utf-8")
        return hashlib.sha256(content).hexdigest()

    def fetch_with_retry(self, url: str) -> FetchResult:
        """
        Fetch URL with exponential backoff on failure.
        Retries on 429 (rate limit) and 5xx (server error).
        """
        self.rate_limiter.wait()
        last_error = None

        for attempt in range(self.max_retries):
            try:
                with httpx.Client(timeout=30.0) as client:
                    resp = client.get(url)
                    resp.raise_for_status()
                    content = resp.content
                    content_hash = self._compute_content_hash(content)

                    return FetchResult(
                        document=RawDocument(
                            source_id=url,
                            content=content,
                            content_type=resp.headers.get(
                                "content-type", "application/octet-stream"
                            ),
                            metadata={
                                "url": url,
                                "status_code": resp.status_code,
                                "content_hash": content_hash,
                            },
                        ),
                        success=True,
                    )
            except httpx.HTTPStatusError as e:
                last_error = str(e)
                if e.response.status_code == 429:
                    wait = self.backoff_base**attempt
                    time.sleep(wait)
                elif e.response.status_code >= 500:
                    wait = self.backoff_base**attempt
                    time.sleep(wait)
                else:
                    break
            except Exception as e:
                last_error = str(e)
                break

        return FetchResult(document=None, success=False, error=last_error)

    def fetch_paginated(
        self,
        endpoint: str,
        page_param: str = "page",
        per_page_param: str = "per_page",
        per_page: int = 100,
    ) -> Iterator[RawDocument]:
        """
        Iterate over paginated API results.
        Assumes API returns {items: [...], next_page: N} or similar.
        Override for custom pagination formats.
        """
        page = 1
        while True:
            url = f"{self.base_url}/{endpoint}?{page_param}={page}&{per_page_param}={per_page}"
            result = self.fetch_with_retry(url)
            if not result.success or not result.document:
                break

            # Parse JSON - structure depends on API
            import json
            data = json.loads(
                result.document.content.decode()
                if isinstance(result.document.content, bytes)
                else result.document.content
            )
            items = data.get("items", data.get("data", []))
            if not items:
                break

            for i, item in enumerate(items):
                item_bytes = json.dumps(item).encode()
                yield RawDocument(
                    source_id=f"{result.document.source_id}#{page}#{i}",
                    content=item_bytes,
                    content_type="application/json",
                    metadata={
                        **result.document.metadata,
                        "page": page,
                        "index": i,
                    },
                )

            page += 1
            if not data.get("has_more", True):
                break


# =============================================================================
# EXAMPLE USAGE
# =============================================================================

if __name__ == "__main__":
    # Example: fetch a single URL with rate limiting
    ingester = APIIngester(base_url="https://api.example.com", rate_limit=1.0)
    result = ingester.fetch_with_retry("https://api.example.com/doc/1")
    if result.success and result.document:
        print(f"Fetched: {result.document.source_id}")
        print(f"Content hash: {result.document.metadata.get('content_hash', 'N/A')}")
