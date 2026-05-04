"""
Week 9: RAG Evaluation

Implements:
- Retrieval metrics: Recall@k, MRR
- Faithfulness (LLM-as-judge): is answer supported by context?
- Automatic evaluation script
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Set


# =============================================================================
# RETRIEVAL METRICS
# =============================================================================


def recall_at_k(retrieved_ids: List[str], relevant_ids: Set[str], k: int) -> float:
    """
    Recall@k = |relevant ∩ retrieved[:k]| / |relevant|
    Proportion of relevant items found in top-k.
    """
    if not relevant_ids:
        return 1.0
    top_k = set(retrieved_ids[:k])
    return len(top_k & relevant_ids) / len(relevant_ids)


def mrr(retrieved_ids: List[str], relevant_ids: Set[str]) -> float:
    """
    Mean Reciprocal Rank: 1 / rank of first relevant item.
    For multiple queries: average of 1/rank for each.
    """
    for i, rid in enumerate(retrieved_ids):
        if rid in relevant_ids:
            return 1.0 / (i + 1)
    return 0.0


def ndcg_at_k(retrieved_ids: List[str], relevant_ids: Set[str], k: int) -> float:
    """
    Normalized Discounted Cumulative Gain.
    Rewards relevant items at top of list.
    DCG = sum(rel_i / log2(rank_i + 1))
    """
    import math
    dcg = 0.0
    for i, rid in enumerate(retrieved_ids[:k]):
        if rid in relevant_ids:
            dcg += 1.0 / math.log2(i + 2)
    # Ideal DCG (all relevant first)
    n_relevant = min(k, len(relevant_ids))
    idcg = sum(1.0 / math.log2(i + 2) for i in range(n_relevant))
    return dcg / idcg if idcg > 0 else 0.0


# =============================================================================
# FAITHFULNESS (LLM-as-Judge)
# =============================================================================


FAITHFULNESS_PROMPT = """Given the context and the answer, determine if the answer is fully supported by the context.
Respond with ONLY one word: YES or NO.

Context:
{context}

Answer:
{answer}

Supported (YES/NO):"""


def check_faithfulness_llm(context: str, answer: str) -> bool:
    """
    Use LLM to judge if answer is grounded in context.
    Returns True if faithful (supported by context).
    """
    try:
        import openai
        prompt = FAITHFULNESS_PROMPT.format(context=context, answer=answer)
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=5,
        )
        text = response.choices[0].message.content.strip().upper()
        return "YES" in text
    except Exception:
        return False


# =============================================================================
# EVALUATION SUITE
# =============================================================================


@dataclass
class EvalExample:
    """Single evaluation example."""
    query: str
    relevant_chunk_ids: Set[str]
    ground_truth_answer: str  # Optional, for answer quality


@dataclass
class EvalResult:
    """Aggregated evaluation result."""
    recall_at_5: float
    recall_at_10: float
    mrr: float
    faithfulness_rate: float
    n: int


def evaluate_rag(
    examples: List[EvalExample],
    retrieve_fn,  # (query) -> List[(chunk_id, score)]
    generate_fn,  # (query, context) -> str
    check_faithfulness: bool = True,
) -> EvalResult:
    """
    Run full RAG evaluation.
    """
    recalls_5, recalls_10, mrrs, faithful = [], [], [], []

    for ex in examples:
        retrieved = retrieve_fn(ex.query)
        retrieved_ids = [r[0] for r in retrieved]
        recalls_5.append(recall_at_k(retrieved_ids, ex.relevant_chunk_ids, 5))
        recalls_10.append(recall_at_k(retrieved_ids, ex.relevant_chunk_ids, 10))
        mrrs.append(mrr(retrieved_ids, ex.relevant_chunk_ids))

        if check_faithfulness and retrieved:
            # retrieved is List[tuple]: (chunk_obj, score) - use chunk content
            context = "\n".join([
                getattr(r[0], "content", str(r[0])) if hasattr(r[0], "content") else str(r)
                for r in retrieved[:5]
            ])
            answer = generate_fn(ex.query, context)
            faithful.append(1 if check_faithfulness_llm(context, answer) else 0)

    n = len(examples)
    return EvalResult(
        recall_at_5=sum(recalls_5) / n if n else 0,
        recall_at_10=sum(recalls_10) / n if n else 0,
        mrr=sum(mrrs) / n if n else 0,
        faithfulness_rate=sum(faithful) / len(faithful) if faithful else 0,
        n=n,
    )


if __name__ == "__main__":
    print("Week 9 metrics demo (toy retrieval order)")
    rel = {"a", "b"}
    retrieved = ["x", "a", "y", "b", "z"]
    print("recall@2", recall_at_k(retrieved, rel, 2))
    print("mrr", mrr(retrieved, rel))
    print("ndcg@5", ndcg_at_k(retrieved, rel, 5))
