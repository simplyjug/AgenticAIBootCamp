# Day 2: Multi-hop reasoning & graph-friendly RAG

## Learning objectives

- Tell **single-hop** vs **multi-hop** queries apart; pick strategies (iterative retrieval, sub-queries).
- Sketch **graph RAG** at architecture level: entities/edges + retrieval over subgraphs.

## Concepts

- **Decomposition:** LLM proposes sub-questions; retriever runs each; composer merges.
- **Cost:** multi-hop multiplies LLM + retrieval calls — cache intermediate results.

## Hands-on

1. Write 5 **multi-hop** questions about a small corpus (your PDF split into chunks).
2. Implement **manual** 2-step retrieval in a notebook: answer Q1 from chunk A, feed answer into query for Q2.
3. Compare token/latency vs single-shot RAG on same questions (rough timing OK).

## Done when

- [ ] Pseudo-code for `multihop_answer(query, max_steps=3)`.
- [ ] One failure mode: **compounding hallucination** across hops — mitigation.

## Resources

- LangChain playlist episodes on **query transformation** ([playlist](https://www.youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyVJiQ23ZztA0x))
