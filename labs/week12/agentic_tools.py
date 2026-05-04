"""
Week 12: Agentic AI — Tool-Using Agents

Implements:
- OpenAI function calling (tools)
- Agent loop: receive query -> decide tool -> execute -> respond
- Example tools: search, calculator, get_weather
- LangChain-style tool abstraction
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, List, Optional

# =============================================================================
# TOOL DEFINITION — OpenAI function format
# =============================================================================


@dataclass
class Tool:
    """
    Tool definition for LLM function calling.
    name: identifier for the tool
    description: natural language description (LLM uses this to decide when to call)
    parameters: JSON schema for arguments
    handler: async or sync function that executes the tool
    """

    name: str
    description: str
    parameters: dict  # JSON Schema
    handler: Callable[..., Any]

    def to_openai_format(self) -> dict:
        """Convert to OpenAI tools API format."""
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": {
                    "type": "object",
                    "properties": self.parameters.get("properties", {}),
                    "required": self.parameters.get("required", []),
                },
            },
        }

    def run(self, **kwargs) -> Any:
        """Execute tool with given arguments."""
        return self.handler(**kwargs)


# =============================================================================
# EXAMPLE TOOLS
# =============================================================================


def search_tool_handler(query: str) -> str:
    """Stub: in production, call your retriever/RAG."""
    return f"[Search results for: {query}]"


def calculator_tool_handler(expression: str) -> str:
    """Safely evaluate math expression."""
    try:
        allowed = set("0123456789+-*/(). ")
        if not all(c in allowed for c in expression):
            return "Error: invalid characters"
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"


# Tool definitions in OpenAI format
SEARCH_TOOL = Tool(
    name="search",
    description="Search the knowledge base for relevant information",
    parameters={
        "properties": {"query": {"type": "string", "description": "Search query"}},
        "required": ["query"],
    },
    handler=search_tool_handler,
)

CALCULATOR_TOOL = Tool(
    name="calculator",
    description="Evaluate a mathematical expression",
    parameters={
        "properties": {
            "expression": {"type": "string", "description": "Math expression, e.g. 2+3*4"}
        },
        "required": ["expression"],
    },
    handler=calculator_tool_handler,
)


# =============================================================================
# AGENT LOOP — ReAct-style: think -> act -> observe -> repeat
# =============================================================================


class ToolAgent:
    """
    Agent that can use tools.
    Uses OpenAI API with tools parameter.
    Loop: send query + tools -> if model wants to call tool, execute and continue.
    """

    def __init__(self, tools: List[Tool], model: str = "gpt-4o-mini", max_iterations: int = 5):
        self.tools = {t.name: t for t in tools}
        self.model = model
        self.max_iterations = max_iterations

    def _execute_tool(self, name: str, arguments: dict) -> str:
        """Execute tool by name with arguments."""
        tool = self.tools.get(name)
        if not tool:
            return f"Unknown tool: {name}"
        try:
            result = tool.run(**arguments)
            return str(result)
        except Exception as e:
            return f"Tool error: {e}"

    def run(self, query: str) -> str:
        """
        Run agent loop: chat with tool calls until done.
        Requires: pip install openai
        """
        import json

        try:
            import openai
        except ImportError:
            return "[Install openai: pip install openai]"

        tools_format = [t.to_openai_format() for t in self.tools.values()]
        messages = [{"role": "user", "content": query}]

        for _ in range(self.max_iterations):
            response = openai.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=tools_format,
                tool_choice="auto",
            )
            choice = response.choices[0]
            if choice.finish_reason == "stop":
                return choice.message.content or ""

            # Model wants to call a tool
            tool_calls = choice.message.tool_calls or []
            for tc in tool_calls:
                name = tc.function.name
                args = json.loads(tc.function.arguments or "{}")
                result = self._execute_tool(name, args)
                messages.append(choice.message)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": result,
                })

        return "[Max iterations reached]"


# =============================================================================
# EXAMPLE
# =============================================================================

if __name__ == "__main__":
    agent = ToolAgent(tools=[SEARCH_TOOL, CALCULATOR_TOOL])
    # response = agent.run("What is 15 * 23?")
    # print(response)
