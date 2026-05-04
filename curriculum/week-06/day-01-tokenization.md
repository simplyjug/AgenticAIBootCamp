# Day 1: Tokenization & semantic chunking

> **Playbook:** [AI_ENGINEERING_PLAYBOOK.md](../../docs/AI_ENGINEERING_PLAYBOOK.md) §5 Chunking · §4 Embeddings  
> **Lab:** `labs/week6/chunk_strategies.py`

---

## 1. Why this day matters for interviews

Interviewers will not ask “what is chunking?” in isolation. They ask: **“How would you improve retrieval quality without changing the LLM?”** The honest answer usually starts with **chunking + embedder + index**, not prompt hacks.

Chunking is a **retrieval policy**: it decides what becomes an atomic unit in the vector index. Bad chunks → wrong neighbors in embedding space → confident wrong answers.

---

## 2. Mental model — tokens vs characters vs “words”

- **Characters** are a poor proxy for LLM cost and context limits (Unicode, CJK).
- **Words** (split on whitespace) are better for humans, still wrong for models.
- **Tokens** are what the **tokenizer** emits — the true currency of context windows and billing.

**tiktoken** (OpenAI-compatible) approximates how many tokens a chunk will consume when you later **stuff** chunks into the model. Your embedder may use a **different** tokenizer (e.g., SentencePiece) — production systems track **both**: `embedder_max_seq` and `generator_max_context`.

---

## 3. Semantic chunking vs naive windows

| Strategy | Retrieval behavior | Failure modes |
|----------|-------------------|---------------|
| Fixed char/window | Stable size; fast | Cuts mid-sentence, splits entities across chunks |
| Sentence / paragraph boundary | Coherent phrases | Very long paragraphs still blow limits |
| **Recursive** (hierarchical separators) | Respects headings, lists | More complex code; order of separators matters |
| **Document-aware** (HTML headings, PDF layout blocks) | Best quality when layout exists | Depends on upstream parser quality |

**Interview line:** “I’d choose **recursive** splitting with a separator hierarchy tuned to our corpus (Markdown vs legal PDF vs HTML), then measure **recall@k** on a frozen query set.”

---

## 4. Reading the lab code

Open `labs/week6/chunk_strategies.py` and trace:

1. `chunk_by_sentences` — good baseline when you have clean plaintext.
2. `chunk_fixed_size` — word-window with **overlap**; overlap is a **recall** knob and a **storage** cost.
3. `chunk_by_tokens` — uses `tiktoken` when installed; falls back to a rough char heuristic — know when fallback is unacceptable (strict budgets).
4. `recursive_chunk` — mirrors “LangChain-style” recursive splitting at a smaller scale.

**Exercise:** Log `len(chunks)`, mean chunk length in tokens, and **max** chunk length for three configs on the same document.

---

## 5. Overlap — intuition and math sketch

If overlap is \(O\) tokens and window is \(W\), redundancy per document scales roughly as \(O/W\). Higher overlap:

- **Increases** chance any given fact appears whole in *some* chunk (good for recall).
- **Increases** index size and duplicate hits (bad for precision and cost).

There is no universal optimum — **only** measured curves on your data.

---

## 6. Link to embeddings (preview)

Chunking changes the **distribution** of strings your embedder sees. If chunks are huge, the embedding may **average** semantics (“bag of topics”). If chunks are tiny, they may be **ambiguous** out of context.

**Coupled optimization (advanced):** freeze embedder, sweep chunk params; then freeze chunker, swap embedder; do **not** change two knobs at once when reporting results.

---

## 7. Production checklist

- [ ] Chunker version in **`chunking.yaml`** (or equivalent) checked into git.
- [ ] `chunk_id` stable across re-runs unless source text or tokenizer version changes.
- [ ] Metrics: chunk length histogram, % empty chunks, tokenizer errors.
- [ ] Backpressure: largest documents routed to async worker queue.

---

## 8. Interview questions (answer out loud)

1. **How do you choose chunk size without labels?**  
   Heuristics + human spot checks first; then weak labels from click logs or search sessions; then full golden set when product has traffic.

2. **Does bigger context window remove chunking?**  
   No — retrieval still must find the right span among millions of docs; long context does not fix search.

3. **Where do parent–child chunks help?**  
   Small **child** for precise retrieval; large **parent** for reader context — especially legal and policy text.

---

## 9. Homework (portfolio-worthy)

1. Implement **one** new splitter (e.g., split on Markdown `##` headings) in `chunk_strategies.py` with tests.
2. Build a **mini table**: tokenizer vs mean tokens per chunk for two strategies.
3. Write 10 bullets in `labs/week6/CHUNKING_NOTES.md` linking failures to mitigations (your own words).

---

## 10. Done when

- [ ] You can explain **why** `chunk_by_tokens` matters for OpenAI-style models.
- [ ] You measured **at least two** strategies on the same file and recorded numbers.
- [ ] You read Playbook **§5** and can quote one failure mode from memory.
