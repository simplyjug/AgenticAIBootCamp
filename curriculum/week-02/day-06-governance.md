# Day 6: Data Governance & Versioning

## Learning Objectives

1. **Implement** dataset versioning for reproducibility
2. **Track** data lineage from raw to model
3. **Define** access controls and retention policies
4. **Handle** data deletion requests

---

## 1. Theory

### What is Data Governance?

Data governance is rules and processes for managing data quality, security, and compliance.

**For beginners:** Like a library's rules – who can borrow books, how long to keep them, how to track changes.

### 1.1 Dataset Versioning

Versioning tracks changes to data, like Git for code.

**Why:** Reproduce experiments, rollback bad changes.

**Tools:** DVC (Data Version Control), lakeFS, or simple hashes.

### 1.2 Data Lineage

Lineage tracks data's journey: raw data → cleaned → trained model.

**Example:** Raw web scrape → deduplicated → embedded → model.

**Benefit:** Debug issues, ensure compliance.

### 1.3 Access Controls

Control who sees what data.

**Levels:** Public, internal, confidential (PII).

**Implementation:** Permissions, encryption.

### 1.4 Retention and Deletion

How long to keep data, how to delete when requested (GDPR).

**Policy:** Raw data 1 year, processed forever (anonymized).

---

## 2. Practical: Governance Setup

### Setup
Use hashlib for hashes: built-in.

### Hands-on Exercises
1. Create manifest with hashes.
2. Track lineage.
3. Define policies.

## Code Examples

### Dataset Manifest
```python
import json
import hashlib
from datetime import datetime

def hash_file(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

# Sample files
files = ['data/raw.txt', 'data/cleaned.txt']

manifest = {
    'version': '1.0',
    'created': datetime.now().isoformat(),
    'files': {}
}

for f in files:
    manifest['files'][f] = {
        'hash': hash_file(f),
        'size': 123  # os.path.getsize(f)
    }

with open('datasets/manifest.json', 'w') as f:
    json.dump(manifest, f, indent=2)

print("Manifest created")
```

### Lineage Tracking
```python
# Simple lineage dict
lineage = {
    'raw_data': {'source': 'web_scrape', 'date': '2023-01-01'},
    'cleaned': {'from': 'raw_data', 'steps': ['dedup', 'filter']},
    'embeddings': {'from': 'cleaned', 'model': 'bert-base'},
    'model': {'from': 'embeddings', 'type': 'classifier'}
}

# Save
with open('datasets/lineage.json', 'w') as f:
    json.dump(lineage, f, indent=2)
```

### Access Control
```python
# Simple role-based
roles = {
    'public': ['read_public'],
    'researcher': ['read_public', 'read_internal'],
    'admin': ['read_public', 'read_internal', 'read_pii']
}

def has_access(user_role, data_type):
    return data_type in roles.get(user_role, [])

print(has_access('researcher', 'read_internal'))  # True
```

### Retention Policy
```python
from datetime import datetime, timedelta

policy = {
    'raw_data': timedelta(days=365),
    'processed': timedelta(days=365*5),
    'models': None  # Keep forever
}

def should_delete(data_type, created_date):
    if policy[data_type] is None:
        return False
    return datetime.now() - created_date > policy[data_type]

created = datetime(2022, 1, 1)
print(should_delete('raw_data', created))  # True if old
```

---

## 3. Homework

Implement versioning for a small dataset and document governance rules.

---

## 4. Interview Questions

- How to handle data deletion in trained models?
- Design governance for international compliance.

## Resources
- [DVC Docs](https://dvc.org/)
- [LF AI Data Governance](https://lfaidata.foundation/)

## Done When
- [ ] You can explain data lineage importance.
- [ ] You've created a dataset manifest.
