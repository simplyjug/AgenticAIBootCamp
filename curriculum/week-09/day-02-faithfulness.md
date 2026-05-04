# Day 2: Faithfulness & groundedness

## Learning objectives

- Define **faithfulness** (supported by context) vs **correctness** (true in the world).
- Build a small **LLM-as-judge** prompt with **chain-of-thought** disabled for scoring stability (optional policy).

## Hands-on

1. For 10 RAG answers, add `judge(context, answer) -> {0,1}` rubric in plain language.
2. Compute **agreement** between two prompt variants or between LLM and human on 5 samples.
3. Document **known limitations** of LLM judges (position bias, verbosity bias).

## Concepts

- **Reference-free** metrics are attractive but fragile — always spot-check.

## Done when

- [ ] Rubric + 10 scored examples (can be toy).
- [ ] One paragraph on **when** you would not trust auto faithfulness scores.

## Resources

- Search “**G-Eval**” or “**RAGAS**” papers for survey reading (no paywall required for abstracts)
