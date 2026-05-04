"""
Week 8 - Day 2: Conversational RAG Chatbot

Implements:
- Multi-turn conversation memory (stores last N messages per session)
- Session management (session_id -> conversation history). Use Redis in production.
- RAG with conversation context:
  - Retrieval: enrich query with recent turns ("tell me more" -> use prior context)
  - Generation: pass full history + retrieved context to LLM
- OpenAI Chat Completions API with messages format (system, user, assistant)

Key design: get_query_with_context() builds retrieval query from last N turns
so that "what about X?" or "explain that" can find relevant chunks.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional

# =============================================================================
# MESSAGE MODELS — OpenAI-compatible message format
# =============================================================================


@dataclass
class Message:
    """Single message in conversation (role + content)."""
    role: str  # "user", "assistant", "system"
    content: str


@dataclass
class Conversation:
    """
    In-memory conversation storage.
    Keeps last max_messages for context window management.
    """

    session_id: str
    messages: List[Message] = field(default_factory=list)
    max_messages: int = 20  # Store last 10 turns (user+assistant pairs)

    def add(self, role: str, content: str) -> None:
        """Add message and trim if over limit."""
        self.messages.append(Message(role=role, content=content))
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]

    def to_openai_messages(self) -> List[dict]:
        """Convert to OpenAI messages format."""
        return [{"role": m.role, "content": m.content} for m in self.messages]

    def get_query_with_context(self, new_query: str, last_n_turns: int = 3) -> str:
        """
        Build enriched query for retrieval by including recent conversation.
        Helps retrieval find relevant chunks when user says "tell me more" or "what about X?"
        """
        if last_n_turns <= 0:
            return new_query
        recent = self.messages[-(last_n_turns * 2):]  # user + assistant pairs
        context_parts = []
        for m in recent:
            prefix = "User" if m.role == "user" else "Assistant"
            context_parts.append(f"{prefix}: {m.content}")
        context_str = "\n".join(context_parts)
        return f"Previous conversation:\n{context_str}\n\nCurrent question: {new_query}"


# =============================================================================
# SESSION MANAGER — Stores conversations by session_id
# =============================================================================


class SessionManager:
    """
    Manages conversation sessions.
    In production: use Redis with TTL (e.g., 1 hour).
    """

    def __init__(self):
        self.sessions: dict[str, Conversation] = {}

    def get_or_create(self, session_id: str) -> Conversation:
        """Get existing conversation or create new one."""
        if session_id not in self.sessions:
            self.sessions[session_id] = Conversation(session_id=session_id)
        return self.sessions[session_id]

    def clear(self, session_id: str) -> None:
        """Clear conversation for session."""
        if session_id in self.sessions:
            self.sessions[session_id].messages.clear()


# =============================================================================
# CONVERSATIONAL RAG CHATBOT
# =============================================================================


class ConversationalRAGChatbot:
    """
    Chatbot that:
    1. Maintains conversation history per session
    2. Enriches query with recent context for retrieval
    3. Retrieves relevant chunks
    4. Generates response with full conversation history
    """

    def __init__(
        self,
        retriever,  # Any retriever with .search(query, top_k)
        session_manager: Optional[SessionManager] = None,
        system_prompt: str = "You are a helpful assistant. Use the context to answer.",
        retrieval_context_turns: int = 2,
    ):
        self.retriever = retriever
        self.session_manager = session_manager or SessionManager()
        self.system_prompt = system_prompt
        self.retrieval_context_turns = retrieval_context_turns

    def _build_rag_context(self, chunks: List[tuple]) -> str:
        """Format retrieved chunks as context for LLM."""
        parts = []
        for i, (chunk, score) in enumerate(chunks, 1):
            parts.append(f"[{i}] {chunk.content}")
        return "\n\n".join(parts)

    def _build_messages_for_llm(
        self,
        conversation: Conversation,
        new_query: str,
        retrieved_context: str,
    ) -> List[dict]:
        """
        Build messages for OpenAI API:
        - System: instructions + retrieved context
        - History: last N turns
        - User: new query
        """
        system_content = f"{self.system_prompt}\n\nRelevant context:\n{retrieved_context}"
        messages = [{"role": "system", "content": system_content}]

        for m in conversation.messages:
            if m.role != "system":  # Don't duplicate system
                messages.append({"role": m.role, "content": m.content})

        messages.append({"role": "user", "content": new_query})
        return messages

    def chat(
        self,
        session_id: str,
        user_message: str,
        top_k: int = 5,
    ) -> str:
        """
        Process user message and return assistant response.
        Uses conversation history for context-aware retrieval and generation.
        """
        conv = self.session_manager.get_or_create(session_id)
        conv.add("user", user_message)

        # Enriched query for retrieval (includes recent conversation)
        retrieval_query = conv.get_query_with_context(
            user_message,
            last_n_turns=self.retrieval_context_turns,
        )

        # Retrieve
        retrieved = self.retriever.search(retrieval_query, top_k=top_k)
        context_str = self._build_rag_context(retrieved) if retrieved else "No relevant context."

        # Build messages for LLM
        messages = self._build_messages_for_llm(conv, user_message, context_str)

        # Generate (replace with actual OpenAI call)
        try:
            import openai
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                max_tokens=500,
            )
            assistant_message = response.choices[0].message.content
        except Exception as e:
            assistant_message = f"[Error: {e}]"

        conv.add("assistant", assistant_message)
        return assistant_message


# =============================================================================
# EXAMPLE USAGE
# =============================================================================

if __name__ == "__main__":
    # Minimal retriever stub
    class StubRetriever:
        def search(self, query: str, top_k: int = 5):
            return [(type("Chunk", (), {"content": "Sample context."})(), 0.9)]

    bot = ConversationalRAGChatbot(retriever=StubRetriever())
    r1 = bot.chat("session-1", "What is machine learning?")
    r2 = bot.chat("session-1", "Can you tell me more?")  # Uses context from previous turn
    print("Turn 1:", r1[:50], "...")
    print("Turn 2:", r2[:50], "...")
