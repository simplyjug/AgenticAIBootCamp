"""
Week 13: Multi-Agent Systems

Implements a simple multi-agent architecture:
- Coordinator agent: receives task, delegates to specialists
- Specialist agents: Researcher (RAG), Analyst (summarize), Writer (draft)
- Message passing: coordinator -> specialist -> coordinator
- Shared context: passed through messages
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, List, Optional


# =============================================================================
# MESSAGE TYPES
# =============================================================================


class AgentRole(str, Enum):
    """Agent specializations."""
    COORDINATOR = "coordinator"
    RESEARCHER = "researcher"
    ANALYST = "analyst"
    WRITER = "writer"


@dataclass
class AgentMessage:
    """Message between agents."""
    from_agent: AgentRole
    to_agent: AgentRole
    content: str
    metadata: dict = field(default_factory=dict)


# =============================================================================
# SPECIALIST AGENTS — Each has a single responsibility
# =============================================================================


class SpecialistAgent:
    """
    Specialist agent with a single capability.
    Receives task, returns result as string.
    """

    def __init__(self, role: AgentRole, handler: Callable[[str], str]):
        self.role = role
        self.handler = handler

    def process(self, task: str) -> str:
        """Execute task and return result."""
        return self.handler(task)


# Stub handlers (replace with real LLM calls)
def researcher_handler(task: str) -> str:
    """Simulates RAG/search. In production: call retriever + generator."""
    return f"[Research results for: {task}]"


def analyst_handler(task: str) -> str:
    """Simulates analysis/summarization."""
    return f"[Analysis: {task[:50]}...]"


def writer_handler(task: str) -> str:
    """Simulates drafting. In production: LLM with instructions."""
    return f"[Draft based on: {task[:50]}...]"


# =============================================================================
# COORDINATOR — Delegates tasks to specialists
# =============================================================================


class CoordinatorAgent:
    """
    Coordinator that:
    1. Receives high-level task
    2. Decides which specialists to call and in what order
    3. Aggregates results
    4. Returns final response

    Simplified: uses fixed pipeline (research -> analyze -> write).
    Advanced: use LLM to decide routing.
    """

    def __init__(self, specialists: dict[AgentRole, SpecialistAgent]):
        self.specialists = specialists

    def run(self, task: str) -> str:
        """
        Execute task by delegating to specialists.
        Pipeline: Researcher -> Analyst -> Writer
        """
        # Step 1: Research
        research_msg = AgentMessage(
            from_agent=AgentRole.COORDINATOR,
            to_agent=AgentRole.RESEARCHER,
            content=task,
        )
        research_result = self.specialists[AgentRole.RESEARCHER].process(task)

        # Step 2: Analyze
        analyze_input = f"Research: {research_result}\nTask: {task}"
        analysis_result = self.specialists[AgentRole.ANALYST].process(analyze_input)

        # Step 3: Write
        write_input = f"Analysis: {analysis_result}\nTask: {task}"
        draft = self.specialists[AgentRole.WRITER].process(write_input)

        return draft


# =============================================================================
# FACTORY — Create full multi-agent system
# =============================================================================


def create_multi_agent_system() -> CoordinatorAgent:
    """Create coordinator with specialists."""
    specialists = {
        AgentRole.RESEARCHER: SpecialistAgent(AgentRole.RESEARCHER, researcher_handler),
        AgentRole.ANALYST: SpecialistAgent(AgentRole.ANALYST, analyst_handler),
        AgentRole.WRITER: SpecialistAgent(AgentRole.WRITER, writer_handler),
    }
    return CoordinatorAgent(specialists)


# =============================================================================
# EXAMPLE
# =============================================================================

if __name__ == "__main__":
    coordinator = create_multi_agent_system()
    result = coordinator.run("What are the main trends in AI?")
    print(result)
