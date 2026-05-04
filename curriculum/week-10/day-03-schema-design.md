# Day 3: Schema design for hybrid vector + metadata retrieval

> **Playbook:** [AI_ENGINEERING_PLAYBOOK.md](../../docs/AI_ENGINEERING_PLAYBOOK.md) §6 RAG · §9 Metadata · §16 failures  
> **Agentic tie-in:** tool `search_docs` should accept **the same** structured filters the index stores — single source of truth.

---

## 1. What “schema” means here

Not only SQL tables — the **contract** between:

1. **Ingestion / enrichment** (what fields exist, types, cardinality)  
2. **Vector index** (which fields are indexed, filterable, or payload-only)  
3. **API** (what clients may query)  
4. **Agents** (tool arguments must mirror filterable fields exactly)

If these diverge, you get silent **filter bugs** — the worst class of RAG failures (“why did customer B see customer A docs?”).

---

## 2. Pydantic-first modeling (recommended pattern)

Define a single `DocumentRecord` used by:

- Ingest pipeline validation  
- DB row serialization  
- Vector DB upsert payload  
- OpenAPI / tool JSON schema generation (derive or mirror manually)

Fields (example set — tune to domain):

| Field | Type | Vector? | Filter? | Notes |
|-------|------|---------|---------|-------|
| `id` | `str` | no | yes | immutable |
| `text` | `str` | source for embed | no | may strip for storage vs embed |
| `embedding` | `list[float]` | yes | no | optional in record pre-embed |
| `tenant_id` | `str` | no | **yes** | hard isolation |
| `acl_principals` | `set[str]` | no | yes | users/groups |
| `created_at` | `datetime` | no | yes | range queries |
| `language` | `str` | no | yes | ISO code |
| `topic_path` | `str` | no | yes | taxonomy leaf |
| `source_uri` | `AnyUrl` | no | optional | provenance |

**Rule:** anything that appears in a **WHERE** clause at query time must be **explicitly** marked filterable in the vector store schema.

---

## 3. Pre-filter vs post-filter (latency story)

- **Pre-filter** reduces candidate set **before** ANN search — can speed or hurt depending on engine + cardinality.
- **Post-filter** retrieves more neighbors then drops — can waste work but simpler.

**Interview:** “I’d read the vendor’s guidance for my cardinality; then **benchmark** p95 with realistic filter hit rates, not toy data.”

---

## 4. JSON Schema & evolution

Ship `document_record.schema.json` versioned:

- Add new fields as **optional** first; backfill job fills them.
- **Never** reuse a field name for a different semantic meaning.

Use compatibility checks in CI: **breaking** schema diff fails build.

---

## 5. Hands-on (portfolio artifact)

1. Create `labs/week10/document_record.py` with Pydantic `DocumentRecord` and `model_json_schema()` export.
2. Write `labs/week10/FILTER_MATRIX.md`: each filterable field → example user query that needs it.
3. Sketch **Weaviate class** or **Milvus collection** field definitions beside the Pydantic model — note mismatches.

---

## 6. Failure modes (design review)

| Bug | Symptom | Prevention |
|-----|---------|------------|
| Filter typo in API | empty retrieval | enum validation + integration tests |
| ACL not attached at upsert | data leak | middleware attaches tenant from auth context |
| Timezone-naive timestamps | off-by-one day filters | store UTC; convert at edge |

---

## 7. Agentic systems alignment

Your `search_knowledge` tool signature should look like:

```json
{
  "query": "string",
  "tenant_id": "string",
  "topic_path": "string | null",
  "after": "ISO-8601 | null"
}
```

The LLM **must not** invent `tenant_id` — inject server-side from session.

---

## 8. Interview question (90-second answer)

**“How do you schema-design for multi-tenant RAG?”**  
Walk through tenant partition strategies (shared index + mandatory filter vs shard per tenant), cite **test** strategy for cross-tenant queries, mention schema versioning.

---

## 9. Done when

- [ ] Pydantic model + exported JSON Schema in repo.
- [ ] Filter matrix doc with ≥6 rows.
- [ ] Explicit note on **where tenant_id is enforced** (API layer vs DB row vs index).
