# Day 1: Agentic RAG & tool use

## Learning objectives

- Define tools as **JSON Schema** compatible with OpenAI **function calling**.
- Wire **LangChain** or manual loops — understand **tool binding** vs raw prompts.

## Hands-on

1. Open `labs/week12/agentic_tools.py` — extend with a second tool `lookup_policy(topic: str)`.
2. Ensure tools return **structured** payloads (dict), not raw strings when possible.
3. Log **every tool call** with arguments for audit.

## Code map

```text
labs/week12/agentic_tools.py
```

## Concepts

- **Least privilege:** tools expose minimal operations — no arbitrary SQL from LLM text.

## Done when

- [ ] Two tools callable from one agent run (mock backend OK).
- [ ] Audit log format documented.

## Resources

- [docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-12)
- LangChain [tools](https://python.langchain.com/docs/modules/agents/tools/)
