# Day 4: Metadata Enrichment & Taxonomy

## Learning Objectives

1. **Build** a controlled vocabulary for consistent tagging
2. **Enrich** documents with metadata for better retrieval
3. **Design** taxonomy structure for scalability
4. **Connect** tags to downstream filters

---

## 1. Theory

### What is Metadata and Taxonomy?

Metadata is extra information about your data – like tags, dates, authors. Taxonomy is a organized system of categories.

**For beginners:** Think of a library book. Metadata is title, author, publish date. Taxonomy is the Dewey Decimal system organizing books by subject.

### 1.1 Why Metadata Matters

Without metadata, searching is hard. With it, you can filter "AI articles from 2023" easily.

**Benefits:**
- Faster search
- Better AI training (models learn from context)
- Easier management

### 1.2 Controlled Vocabulary

Don't let anyone add any tag. Use a fixed list to avoid chaos.

**Example taxonomy:**
- Technology > AI > Machine Learning > Supervised Learning

**Rules:**
- Hierarchical (parent-child)
- No duplicates
- Stable IDs (don't change names)

### 1.3 Enrichment Process

Add metadata automatically or manually.

**Automatic:** Extract from text (e.g., dates, entities)
**Manual:** Human labeling for quality

### 1.4 Downstream Use

Tags help in retrieval. In Week 10, you'll use them to filter search results.

---

## 2. Practical: Building Taxonomy

### Setup
Use YAML for taxonomy: `pip install pyyaml`

### Hands-on Exercises
1. Create a taxonomy file.
2. Tag sample documents.
3. Query with tags.

## Code Examples

### Taxonomy Structure
```yaml
# taxonomy.yaml
domains:
  technology:
    ai:
      - machine_learning
      - deep_learning
    web:
      - frontend
      - backend
```

### Loading and Using
```python
import yaml

with open('taxonomy.yaml') as f:
    tax = yaml.safe_load(f)

# Check if tag exists
def validate_tag(tag):
    # Simple check
    return tag in ['machine_learning', 'deep_learning']  # etc.

print(validate_tag('machine_learning'))  # True
```

### Enriching Documents
```python
documents = [
    {"text": "Neural networks are cool", "tags": ["deep_learning"]},
    {"text": "HTML and CSS", "tags": ["frontend"]}
]

# Add metadata
for doc in documents:
    doc['word_count'] = len(doc['text'].split())
    doc['has_ai'] = 'ai' in doc.get('tags', [])

print(documents)
```

### Filtering
```python
ai_docs = [d for d in documents if 'deep_learning' in d.get('tags', [])]
print(f"AI docs: {len(ai_docs)}")
```

---

## 3. Homework

Build taxonomy for a news dataset and enrich 100 articles.

---

## 4. Interview Questions

- How to handle taxonomy evolution without breaking old data?
- Design metadata for multi-language documents.

## Resources
- [SKOS Primer](https://www.w3.org/TR/skos-primer/)
- [Taxonomy Design Guide](https://www.ontotext.com/knowledgehub/fundamentals/taxonomy-ontology/)

## Done When
- [ ] You can explain why controlled vocabulary matters.
- [ ] You've created a simple taxonomy and tagged documents.
