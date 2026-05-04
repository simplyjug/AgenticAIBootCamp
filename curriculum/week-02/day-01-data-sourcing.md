# Day 1: Data Sourcing & Pipelines

## Learning Objectives

1. **Design** web scraping architecture with rate limiting and politeness
2. **Implement** API ingestion pipelines with pagination and backoff
3. **Handle** incremental ingestion and change detection
4. **Architect** data pipeline for scale (batch vs streaming)

---

## 1. Theory

### 1.1 Data Sources for RAG

| Source | Challenges | Strategy |
|--------|------------|----------|
| **Web** | Dynamic content, rate limits | Crawler + Playwright fallback |
| **APIs** | Pagination, auth, rate limits | Exponential backoff, token refresh |
| **Databases** | Schema, incremental | CDC or timestamp-based delta |
| **File stores** | Formats, large files | Async workers, format detection |
| **Streaming** | Ordering, exactly-once | Kafka/Redis Streams |

### 1.2 Pipeline Architecture Patterns

- **Batch**: Scheduled jobs; process N documents per run
- **Streaming**: Event-driven; process as events arrive
- **Hybrid**: Batch for bulk; stream for updates

---

## 2. Coding Lab

See `labs/week2/day01_data_sourcing.py` for full implementation with detailed comments.

---

## 3. Homework

Implement sitemap discovery and parallel fetch with connection pooling.

---

## 4. Interview Questions

- How do you handle rate limits across multiple API keys?
- Design a pipeline for ingesting 10M documents from 100 sources.
