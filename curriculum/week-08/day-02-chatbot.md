# Day 2: Conversational RAG chatbot

## Learning objectives

- Maintain **session history** with rolling summarization or sliding window of turns.
- Prevent **context explosion** — cap messages and strip old tool traces.

## Hands-on

1. Run `python -m uvicorn labs.week8.conversational_chatbot:app --reload --port 8000`
2. Send 5 sequential chat turns referencing earlier facts (memory test).
3. Implement **history trimming**: keep last N user/assistant pairs + optional summary field.

## Code map

```text
labs/week8/conversational_chatbot.py
```

## Concepts

- **PII in chat logs:** retention TTL and redaction before logging.
- **Session affinity:** sticky routing if state not fully in Redis.

## Done when

- [ ] API accepts `session_id` and returns coherent follow-up answers.
- [ ] Short note on **when** to reset session (user button, inactivity).

## Resources

- [docs/VIDEO_RESOURCES.md](../../docs/VIDEO_RESOURCES.md#week-7-8)
