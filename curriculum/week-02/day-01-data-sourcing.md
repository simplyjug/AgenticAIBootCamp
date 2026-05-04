# Day 1: Data Sourcing & Pipelines

## Learning Objectives

1. **Design** web scraping architecture with rate limiting and politeness
2. **Implement** API ingestion pipelines with pagination and backoff
3. **Handle** incremental ingestion and change detection
4. **Architect** data pipeline for scale (batch vs streaming)

---

## 1. Theory

### 1.1 What is Data Sourcing?

Data sourcing is collecting data from various sources to build your knowledge base for AI models. For a new graduate, think of it as gathering ingredients for a recipe – you need the right quality and quantity.

### 1.2 Data Sources for RAG

RAG (Retrieval-Augmented Generation) needs diverse, up-to-date data. Here's a beginner-friendly breakdown:

| Source | What It Is | Challenges | Strategy |
|--------|------------|------------|----------|
| **Web** | Websites, blogs, articles | Pages change, sites block scrapers | Use polite crawlers, respect robots.txt |
| **APIs** | Services like Twitter API, news APIs | Limits on requests, need keys | Handle errors, use backoff |
| **Databases** | Company databases, SQL/NoSQL | Access permissions, large data | Query efficiently, avoid overloading |
| **File stores** | PDFs, docs on cloud storage | Different formats, large files | Detect format, process in chunks |
| **Streaming** | Real-time data like social media feeds | Data comes fast, hard to store | Use queues like Kafka |

### 1.3 Pipeline Architecture Patterns

Pipelines move data from source to storage. For beginners:

- **Batch**: Like baking cookies in batches – process a group at once, scheduled (e.g., daily).
- **Streaming**: Like a conveyor belt – process data as it arrives, real-time.
- **Hybrid**: Mix both – batch for big loads, stream for updates.

**Why important?** Wrong architecture can crash your system or miss data.

---

## 2. Practical: Building a Simple Data Pipeline

### Setup
1. Install requests: `pip install requests`
2. Use a free API like JSONPlaceholder for testing.

### Hands-on Exercises
1. Fetch data from an API.
2. Handle pagination.
3. Add error handling.

## Code Examples

### Basic API Fetch
```python
import requests

# Simple API call
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)
```

### With Pagination
```python
import time

def fetch_all_posts():
    posts = []
    page = 1
    while True:
        response = requests.get(f"https://jsonplaceholder.typicode.com/posts?_page={page}&_limit=10")
        if response.status_code != 200 or not response.json():
            break
        posts.extend(response.json())
        page += 1
        time.sleep(1)  # Be polite
    return posts

posts = fetch_all_posts()
print(f"Fetched {len(posts)} posts")
```

### Error Handling
```python
try:
    response = requests.get("https://badurl.com", timeout=5)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
```

---

## 3. Homework

Implement sitemap discovery and parallel fetch with connection pooling.

---

## 4. Interview Questions

- How do you handle rate limits across multiple API keys?
- Design a pipeline for ingesting 10M documents from 100 sources.

## Resources
- [Requests Library Docs](https://requests.readthedocs.io/)
- [Web Scraping Ethics](https://blog.apify.com/web-scraping-ethics/)

## Done When
- [ ] You can explain batch vs streaming.
- [ ] You've fetched data from an API with error handling.
