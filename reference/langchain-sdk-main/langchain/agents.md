---
title: "Agents"
description: "An agent is a model calling tools in a loop until a given task is complete."
source: "https://docs.langchain.com/oss/python/langchain/agents"
category: "docs"
tags: [docs, langchain, agents]
---

# Agents

An agent is a model calling tools in a loop until a given task is complete.

<img src="https://mintcdn.com/langchain-5e9cc07a/jtty0O--UJOKG0nK/oss/images/core_agent_loop.svg?fit=max&auto=format&n=jtty0O--UJOKG0nK&q=85&s=4b4cbb497b6273758a565de1bc90ece0" alt="Core agent loop diagram" width="1060" height="760" data-path="oss/images/core_agent_loop.svg" />

A harness is everything around that loop: the prompt, the tools, and any middleware that shapes the model's behavior.

> [!NOTE]
> **Agent = Model + Harness**
>
> The job of a harness: get the model the right context at the right time for the given task.

[`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent) is a highly configurable harness. At its simplest, you can create one with:

**Google**

```python
from langchain.agents import create_agent

agent = create_agent(model="google_genai:gemini-3.6-flash", tools=tools)
```

**OpenAI**

```python
from langchain.agents import create_agent

agent = create_agent(model="openai:gpt-5.5", tools=tools)
```

**Anthropic**

```python
from langchain.agents import create_agent

agent = create_agent(model="anthropic:claude-sonnet-5", tools=tools)
```

**OpenRouter**

```python
from langchain.agents import create_agent

agent = create_agent(model="openrouter:z-ai/glm-5.2", tools=tools)
```

**Fireworks**

```python
from langchain.agents import create_agent

agent = create_agent(model="fireworks:accounts/fireworks/models/glm-5p2", tools=tools)
```

**Baseten**

```python
from langchain.agents import create_agent

agent = create_agent(model="baseten:zai-org/GLM-5.2", tools=tools)
```

**Ollama**

```python
from langchain.agents import create_agent

agent = create_agent(model="ollama:north-mini-code-1.0", tools=tools)
```

Building on that, you can configure the basics directly with the `model=`, `tools=`, and `system_prompt=` parameters. For more advanced capabilities, extend the harness with [middleware](#configure-the-harness).

> [!TIP]
> [Deep Agents](../deepagents/overview.md) builds on `create_agent` and comes with commonly useful capabilities already assembled, such as planning, file system tools, subagents, and memory. Use `create_agent` when you need to configure the harness yourself.

## Core components

<img src="https://mintcdn.com/langchain-5e9cc07a/jtty0O--UJOKG0nK/oss/images/agent_model_harness.svg?fit=max&auto=format&n=jtty0O--UJOKG0nK&q=85&s=5ac6a7e0343af7cb5ba3ca632e2224af" alt="Agent model and harness components diagram" width="1200" height="760" data-path="oss/images/agent_model_harness.svg" />

### Model

Pass a model identifier string (`"provider:model"`) or an initialized model instance to select the model for your agent. See [Models](models.md) for parameters, provider setup, and dynamic model selection.

**Google**

```python
from langchain.agents import create_agent

agent = create_agent(model="google_genai:gemini-3.6-flash", tools=tools)
```

**OpenAI**

```python
from langchain.agents import create_agent

agent = create_agent(model="openai:gpt-5.5", tools=tools)
```

**Anthropic**

```python
from langchain.agents import create_agent

agent = create_agent(model="anthropic:claude-sonnet-5", tools=tools)
```

**OpenRouter**

```python
from langchain.agents import create_agent

agent = create_agent(model="openrouter:z-ai/glm-5.2", tools=tools)
```

**Fireworks**

```python
from langchain.agents import create_agent

agent = create_agent(model="fireworks:accounts/fireworks/models/glm-5p2", tools=tools)
```

**Baseten**

```python
from langchain.agents import create_agent

agent = create_agent(model="baseten:zai-org/GLM-5.2", tools=tools)
```

**Ollama**

```python
from langchain.agents import create_agent

agent = create_agent(model="ollama:north-mini-code-1.0", tools=tools)
```

### Tools

To provide the agent with tools, pass any Python callable, LangChain tool, or tool dict. See [Tools](tools.md) for tool definition, context access, and dynamic tool selection.

**Google**

```python
from langchain.agents import create_agent
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for information."""
    return f"Results for: {query}"

agent = create_agent(model="google_genai:gemini-3.6-flash", tools=[search])
```

**OpenAI**

```python
from langchain.agents import create_agent
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for information."""
    return f"Results for: {query}"

agent = create_agent(model="openai:gpt-5.5", tools=[search])
```

**Anthropic**

```python
from langchain.agents import create_agent
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for information."""
    return f"Results for: {query}"

agent = create_agent(model="anthropic:claude-sonnet-5", tools=[search])
```

**OpenRouter**

```python
from langchain.agents import create_agent
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for information."""
    return f"Results for: {query}"

agent = create_agent(model="openrouter:z-ai/glm-5.2", tools=[search])
```

**Fireworks**

```python
from langchain.agents import create_agent
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for information."""
    return f"Results for: {query}"

agent = create_agent(model="fireworks:accounts/fireworks/models/glm-5p2", tools=[search])
```

**Baseten**

```python
from langchain.agents import create_agent
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for information."""
    return f"Results for: {query}"

agent = create_agent(model="baseten:zai-org/GLM-5.2", tools=[search])
```

**Ollama**

```python
from langchain.agents import create_agent
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for information."""
    return f"Results for: {query}"

agent = create_agent(model="ollama:north-mini-code-1.0", tools=[search])
```

### System prompt

Shape how the agent approaches tasks. The system prompt parameter accepts a string or `SystemMessage`. For dynamic prompts at runtime, use [middleware](middleware.md).

**Google**

```python
agent = create_agent(
    model="google_genai:gemini-3.6-flash",
    tools=tools,
    system_prompt="You are a helpful assistant. Be concise and accurate.",
)
```

**OpenAI**

```python
agent = create_agent(
    model="openai:gpt-5.5",
    tools=tools,
    system_prompt="You are a helpful assistant. Be concise and accurate.",
)
```

**Anthropic**

```python
agent = create_agent(
    model="anthropic:claude-sonnet-5",
    tools=tools,
    system_prompt="You are a helpful assistant. Be concise and accurate.",
)
```

**OpenRouter**

```python
agent = create_agent(
    model="openrouter:z-ai/glm-5.2",
    tools=tools,
    system_prompt="You are a helpful assistant. Be concise and accurate.",
)
```

**Fireworks**

```python
agent = create_agent(
    model="fireworks:accounts/fireworks/models/glm-5p2",
    tools=tools,
    system_prompt="You are a helpful assistant. Be concise and accurate.",
)
```

**Baseten**

```python
agent = create_agent(
    model="baseten:zai-org/GLM-5.2",
    tools=tools,
    system_prompt="You are a helpful assistant. Be concise and accurate.",
)
```

**Ollama**

```python
agent = create_agent(
    model="ollama:north-mini-code-1.0",
    tools=tools,
    system_prompt="You are a helpful assistant. Be concise and accurate.",
)
```

### Structured output

Return a validated schema from the agent using `response_format=`. See [Structured output](structured-output.md) for strategies and examples.

**Google**

```python
from pydantic import BaseModel
from langchain.agents import create_agent

class Answer(BaseModel):
    summary: str
    confidence: float

agent = create_agent(model="google_genai:gemini-3.6-flash", tools=tools, response_format=Answer)
result = agent.invoke({"messages": [{"role": "user", "content": "Summarize AI trends"}]})
result["structured_response"]  # Answer(summary=..., confidence=...)
```

**OpenAI**

```python
from pydantic import BaseModel
from langchain.agents import create_agent

class Answer(BaseModel):
    summary: str
    confidence: float

agent = create_agent(model="openai:gpt-5.5", tools=tools, response_format=Answer)
result = agent.invoke({"messages": [{"role": "user", "content": "Summarize AI trends"}]})
result["structured_response"]  # Answer(summary=..., confidence=...)
```

**Anthropic**

```python
from pydantic import BaseModel
from langchain.agents import create_agent

class Answer(BaseModel):
    summary: str
    confidence: float

agent = create_agent(model="anthropic:claude-sonnet-5", tools=tools, response_format=Answer)
result = agent.invoke({"messages": [{"role": "user", "content": "Summarize AI trends"}]})
result["structured_response"]  # Answer(summary=..., confidence=...)
```

**OpenRouter**

```python
from pydantic import BaseModel
from langchain.agents import create_agent

class Answer(BaseModel):
    summary: str
    confidence: float

agent = create_agent(model="openrouter:z-ai/glm-5.2", tools=tools, response_format=Answer)
result = agent.invoke({"messages": [{"role": "user", "content": "Summarize AI trends"}]})
result["structured_response"]  # Answer(summary=..., confidence=...)
```

**Fireworks**

```python
from pydantic import BaseModel
from langchain.agents import create_agent

class Answer(BaseModel):
    summary: str
    confidence: float

agent = create_agent(model="fireworks:accounts/fireworks/models/glm-5p2", tools=tools, response_format=Answer)
result = agent.invoke({"messages": [{"role": "user", "content": "Summarize AI trends"}]})
result["structured_response"]  # Answer(summary=..., confidence=...)
```

**Baseten**

```python
from pydantic import BaseModel
from langchain.agents import create_agent

class Answer(BaseModel):
    summary: str
    confidence: float

agent = create_agent(model="baseten:zai-org/GLM-5.2", tools=tools, response_format=Answer)
result = agent.invoke({"messages": [{"role": "user", "content": "Summarize AI trends"}]})
result["structured_response"]  # Answer(summary=..., confidence=...)
```

**Ollama**

```python
from pydantic import BaseModel
from langchain.agents import create_agent

class Answer(BaseModel):
    summary: str
    confidence: float

agent = create_agent(model="ollama:north-mini-code-1.0", tools=tools, response_format=Answer)
result = agent.invoke({"messages": [{"role": "user", "content": "Summarize AI trends"}]})
result["structured_response"]  # Answer(summary=..., confidence=...)
```

### Agent state

Every agent manages its execution context through [`AgentState`](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentState), a typed dictionary that holds the current conversation history and any custom fields your tools and middleware need.

The built-in field is:

| Field      | Type                | Description                                                                                                |
| ---------- | ------------------- | ---------------------------------------------------------------------------------------------------------- |
| `messages` | `list[BaseMessage]` | The full conversation history for the current thread. Append-only: new messages are added, never replaced. |

`AgentState` is also the type signature for every node-style middleware hook (`before_model`, `after_model`, and similar). Hooks receive the current state and can return a dict of updates to merge back into it.

To add custom fields (for example, a `user_id` or a counter), subclass `AgentState` and pass the subclass to `create_agent` via `state_schema=`:

**Google**

```python
from langchain.agents import AgentState, create_agent

class MyState(AgentState):
    user_id: str
    call_count: int

agent = create_agent(
    model="google_genai:gemini-3.6-flash",
    tools=[],
    state_schema=MyState,  # [!code highlight]
)
```

**OpenAI**

```python
from langchain.agents import AgentState, create_agent

class MyState(AgentState):
    user_id: str
    call_count: int

agent = create_agent(
    model="openai:gpt-5.5",
    tools=[],
    state_schema=MyState,  # [!code highlight]
)
```

**Anthropic**

```python
from langchain.agents import AgentState, create_agent

class MyState(AgentState):
    user_id: str
    call_count: int

agent = create_agent(
    model="anthropic:claude-sonnet-5",
    tools=[],
    state_schema=MyState,  # [!code highlight]
)
```

**OpenRouter**

```python
from langchain.agents import AgentState, create_agent

class MyState(AgentState):
    user_id: str
    call_count: int

agent = create_agent(
    model="openrouter:z-ai/glm-5.2",
    tools=[],
    state_schema=MyState,  # [!code highlight]
)
```

**Fireworks**

```python
from langchain.agents import AgentState, create_agent

class MyState(AgentState):
    user_id: str
    call_count: int

agent = create_agent(
    model="fireworks:accounts/fireworks/models/glm-5p2",
    tools=[],
    state_schema=MyState,  # [!code highlight]
)
```

**Baseten**

```python
from langchain.agents import AgentState, create_agent

class MyState(AgentState):
    user_id: str
    call_count: int

agent = create_agent(
    model="baseten:zai-org/GLM-5.2",
    tools=[],
    state_schema=MyState,  # [!code highlight]
)
```

**Ollama**

```python
from langchain.agents import AgentState, create_agent

class MyState(AgentState):
    user_id: str
    call_count: int

agent = create_agent(
    model="ollama:north-mini-code-1.0",
    tools=[],
    state_schema=MyState,  # [!code highlight]
)
```

For full details, examples, and middleware-level state schemas, see [Short-term memory](short-term-memory.md#customizing-agent-memory) and [Custom middleware](middleware/custom.md#state-updates).

## Invocation

> [!TIP]
> Trace each step of this loop, debug tool calls, and evaluate agent outputs with [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langchain-agents). Follow the [tracing quickstart](../langsmith/trace-with-langchain.md) to get set up. We recommend you also set up [LangSmith Engine](../langsmith/engine.md) which monitors your traces, detects issues, and proposes fixes.

You can invoke an agent with a message. Behind the scenes that passes an update to the agent's [`State`](../langgraph/graph-api.md#state). All agents include a [sequence of messages](../langgraph/use-graph-api.md#messagesstate) in their state; to invoke the agent, pass a new message along with a `thread_id` so the agent can persist and resume conversation history:

**Google**

```python
from langchain.agents import create_agent
from langchain_core.utils.uuid import uuid7
from langgraph.checkpoint.memory import InMemorySaver

agent = create_agent(
    model="google_genai:gemini-3.6-flash",
    tools=[],
    checkpointer=InMemorySaver(),
)

config = {"configurable": {"thread_id": str(uuid7())}}

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]},
    config=config,
)

# A follow-up turn on the same conversation: reuse the same thread_id to keep history
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What about tomorrow?"}]},
    config=config,
)
```

**OpenAI**

```python
from langchain.agents import create_agent
from langchain_core.utils.uuid import uuid7
from langgraph.checkpoint.memory import InMemorySaver

agent = create_agent(
    model="openai:gpt-5.5",
    tools=[],
    checkpointer=InMemorySaver(),
)

config = {"configurable": {"thread_id": str(uuid7())}}

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]},
    config=config,
)

# A follow-up turn on the same conversation: reuse the same thread_id to keep history
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What about tomorrow?"}]},
    config=config,
)
```

**Anthropic**

```python
from langchain.agents import create_agent
from langchain_core.utils.uuid import uuid7
from langgraph.checkpoint.memory import InMemorySaver

agent = create_agent(
    model="anthropic:claude-sonnet-5",
    tools=[],
    checkpointer=InMemorySaver(),
)

config = {"configurable": {"thread_id": str(uuid7())}}

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]},
    config=config,
)

# A follow-up turn on the same conversation: reuse the same thread_id to keep history
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What about tomorrow?"}]},
    config=config,
)
```

**OpenRouter**

```python
from langchain.agents import create_agent
from langchain_core.utils.uuid import uuid7
from langgraph.checkpoint.memory import InMemorySaver

agent = create_agent(
    model="openrouter:z-ai/glm-5.2",
    tools=[],
    checkpointer=InMemorySaver(),
)

config = {"configurable": {"thread_id": str(uuid7())}}

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]},
    config=config,
)

# A follow-up turn on the same conversation: reuse the same thread_id to keep history
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What about tomorrow?"}]},
    config=config,
)
```

**Fireworks**

```python
from langchain.agents import create_agent
from langchain_core.utils.uuid import uuid7
from langgraph.checkpoint.memory import InMemorySaver

agent = create_agent(
    model="fireworks:accounts/fireworks/models/glm-5p2",
    tools=[],
    checkpointer=InMemorySaver(),
)

config = {"configurable": {"thread_id": str(uuid7())}}

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]},
    config=config,
)

# A follow-up turn on the same conversation: reuse the same thread_id to keep history
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What about tomorrow?"}]},
    config=config,
)
```

**Baseten**

```python
from langchain.agents import create_agent
from langchain_core.utils.uuid import uuid7
from langgraph.checkpoint.memory import InMemorySaver

agent = create_agent(
    model="baseten:zai-org/GLM-5.2",
    tools=[],
    checkpointer=InMemorySaver(),
)

config = {"configurable": {"thread_id": str(uuid7())}}

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]},
    config=config,
)

# A follow-up turn on the same conversation: reuse the same thread_id to keep history
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What about tomorrow?"}]},
    config=config,
)
```

**Ollama**

```python
from langchain.agents import create_agent
from langchain_core.utils.uuid import uuid7
from langgraph.checkpoint.memory import InMemorySaver

agent = create_agent(
    model="ollama:north-mini-code-1.0",
    tools=[],
    checkpointer=InMemorySaver(),
)

config = {"configurable": {"thread_id": str(uuid7())}}

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]},
    config=config,
)

# A follow-up turn on the same conversation: reuse the same thread_id to keep history
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What about tomorrow?"}]},
    config=config,
)
```

#### [View example trace](https://smith.langchain.com/public/b220516f-9133-4c86-bc5a-073ef63e3f7f/r)
Open a public LangSmith run for this example.

> [!NOTE]
> Persisting conversation history with `thread_id` requires the agent to be configured with a [checkpointer](long-term-memory.md). When deployed on [LangSmith](../langsmith/deployment.md), a checkpointer is provisioned automatically. Locally, pass one explicitly, for example `create_agent(..., checkpointer=InMemorySaver())`.

If you also need to pass per-run configuration (such as a user ID, API keys, or feature flags) to tools and middleware, pass it as `context` alongside `config`. Define the shape of that data with `context_schema` and access it through `runtime.context`:

**Google**

```python
from dataclasses import dataclass

from langchain.agents import create_agent
from langchain_core.utils.uuid import uuid7
from langgraph.checkpoint.memory import InMemorySaver

@dataclass
class Context:
    user_id: str

agent = create_agent(
    model="google_genai:gemini-3.6-flash",
    tools=[],
    context_schema=Context,
    checkpointer=InMemorySaver(),
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]},
    config={"configurable": {"thread_id": str(uuid7())}},
    context=Context(user_id="user-123"),
)
```

**OpenAI**

```python
from dataclasses import dataclass

from langchain.agents import create_agent
from langchain_core.utils.uuid import uuid7
from langgraph.checkpoint.memory import InMemorySaver

@dataclass
class Context:
    user_id: str

agent = create_agent(
    model="openai:gpt-5.5",
    tools=[],
    context_schema=Context,
    checkpointer=InMemorySaver(),
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]},
    config={"configurable": {"thread_id": str(uuid7())}},
    context=Context(user_id="user-123"),
)
```

**Anthropic**

```python
from dataclasses import dataclass

from langchain.agents import create_agent
from langchain_core.utils.uuid import uuid7
from langgraph.checkpoint.memory import InMemorySaver

@dataclass
class Context:
    user_id: str

agent = create_agent(
    model="anthropic:claude-sonnet-5",
    tools=[],
    context_schema=Context,
    checkpointer=InMemorySaver(),
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]},
    config={"configurable": {"thread_id": str(uuid7())}},
    context=Context(user_id="user-123"),
)
```

**OpenRouter**

```python
from dataclasses import dataclass

from langchain.agents import create_agent
from langchain_core.utils.uuid import uuid7
from langgraph.checkpoint.memory import InMemorySaver

@dataclass
class Context:
    user_id: str

agent = create_agent(
    model="openrouter:z-ai/glm-5.2",
    tools=[],
    context_schema=Context,
    checkpointer=InMemorySaver(),
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]},
    config={"configurable": {"thread_id": str(uuid7())}},
    context=Context(user_id="user-123"),
)
```

**Fireworks**

```python
from dataclasses import dataclass

from langchain.agents import create_agent
from langchain_core.utils.uuid import uuid7
from langgraph.checkpoint.memory import InMemorySaver

@dataclass
class Context:
    user_id: str

agent = create_agent(
    model="fireworks:accounts/fireworks/models/glm-5p2",
    tools=[],
    context_schema=Context,
    checkpointer=InMemorySaver(),
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]},
    config={"configurable": {"thread_id": str(uuid7())}},
    context=Context(user_id="user-123"),
)
```

**Baseten**

```python
from dataclasses import dataclass

from langchain.agents import create_agent
from langchain_core.utils.uuid import uuid7
from langgraph.checkpoint.memory import InMemorySaver

@dataclass
class Context:
    user_id: str

agent = create_agent(
    model="baseten:zai-org/GLM-5.2",
    tools=[],
    context_schema=Context,
    checkpointer=InMemorySaver(),
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]},
    config={"configurable": {"thread_id": str(uuid7())}},
    context=Context(user_id="user-123"),
)
```

**Ollama**

```python
from dataclasses import dataclass

from langchain.agents import create_agent
from langchain_core.utils.uuid import uuid7
from langgraph.checkpoint.memory import InMemorySaver

@dataclass
class Context:
    user_id: str

agent = create_agent(
    model="ollama:north-mini-code-1.0",
    tools=[],
    context_schema=Context,
    checkpointer=InMemorySaver(),
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]},
    config={"configurable": {"thread_id": str(uuid7())}},
    context=Context(user_id="user-123"),
)
```

#### [View example trace](https://smith.langchain.com/public/fb33392a-cf5d-4673-a9b2-c58a5abeffd0/r)
Open a public LangSmith run for this example.

`thread_id` scopes the *conversation* (message history, checkpoints), while `context` carries *per-run* data your tools and middleware read at invocation time. Both are commonly passed together. See [tool context](tools.md#context) and [Runtime](runtime.md) for more.

## Streaming

`invoke` returns the final response at the end of a run. If an agent executes multiple tool calls, users often need progress updates before completion. Use streaming to surface intermediate messages and tool activity as they happen.

```python
from langchain.messages import AIMessage, HumanMessage

stream = agent.stream_events(
    {"messages": [{"role": "user", "content": "Search for AI news and summarize the findings"}]},
    version="v3",
)
for snapshot in stream.values:
    # Each snapshot contains the full state at that point
    latest_message = snapshot["messages"][-1]
    if latest_message.content:
        if isinstance(latest_message, HumanMessage):
            print(f"User: {latest_message.content}")
        elif isinstance(latest_message, AIMessage):
            print(f"Agent: {latest_message.content}")
    elif latest_message.tool_calls:
        print(f"Calling tools: {[tc['name'] for tc in latest_message.tool_calls]}")
```

#### [View example trace](https://smith.langchain.com/public/502a2e8a-a9aa-412a-b2e0-ef2ab0290175/r)
Open a public LangSmith run for this example.

> [!TIP]
> For streaming modes, event types, and UI patterns, see [Streaming](streaming.md).

<a id="tool-use-in-the-react-loop"></a>

## Configure the harness

`create_agent` is highly extensible. Middleware is the primitive for customization: each piece handles one concern, hooks into the agent loop at the right moment, and composes freely with any other. Take exactly what your use case needs and skip the rest.

Common patterns are prebuilt as first-class middleware. You can build anything else as [custom middleware](middleware/custom.md).

<img src="https://mintcdn.com/langchain-5e9cc07a/jtty0O--UJOKG0nK/oss/images/agent_harness_capabilities.svg?fit=max&auto=format&n=jtty0O--UJOKG0nK&q=85&s=0ff671d72badd0844826660dfcb04391" alt="Agent harness capabilities by category" width="1500" height="360" data-path="oss/images/agent_harness_capabilities.svg" />

As agents take on complex work, they need support across a few key areas. The middleware ecosystem provides:

#### [Execution environment](#execution-environment)
Tools, filesystem, sandboxes, and code execution

#### [Context management](#context-management)
Summarization, memory, skills, and prompt caching

#### [Planning and delegation](#planning-and-delegation)
Todo lists and subagents for parallel, isolated work

#### [Fault tolerance](#fault-tolerance)
Retries, fallbacks, and call limits

#### [Guardrails](#guardrails)
PII detection and content controls

#### [Steering](#steering)
Human-in-the-loop approval before high-impact actions

> [!TIP]
> `create_deep_agent` pre-assembles this stack for long-running coding and research tasks (filesystem, summarization, subagents, and prompt caching included by default). See [Deep Agents](../deepagents/harness.md) for the full prebuilt harness.

### Execution environment

Agents are especially useful when they can take action rather than just generate text. The execution environment gives the agent a workspace: tools it can call, a filesystem for reading and writing files across turns, and code execution for running scripts or shell commands.

**Google**

```python
from langchain.agents import create_agent
from deepagents.backends import StateBackend
from deepagents.middleware import FilesystemMiddleware

agent = create_agent(
    model="google_genai:gemini-3.6-flash",
    tools=[search],
    middleware=[FilesystemMiddleware(backend=StateBackend())],
)
```

**OpenAI**

```python
from langchain.agents import create_agent
from deepagents.backends import StateBackend
from deepagents.middleware import FilesystemMiddleware

agent = create_agent(
    model="openai:gpt-5.5",
    tools=[search],
    middleware=[FilesystemMiddleware(backend=StateBackend())],
)
```

**Anthropic**

```python
from langchain.agents import create_agent
from deepagents.backends import StateBackend
from deepagents.middleware import FilesystemMiddleware

agent = create_agent(
    model="anthropic:claude-sonnet-5",
    tools=[search],
    middleware=[FilesystemMiddleware(backend=StateBackend())],
)
```

**OpenRouter**

```python
from langchain.agents import create_agent
from deepagents.backends import StateBackend
from deepagents.middleware import FilesystemMiddleware

agent = create_agent(
    model="openrouter:z-ai/glm-5.2",
    tools=[search],
    middleware=[FilesystemMiddleware(backend=StateBackend())],
)
```

**Fireworks**

```python
from langchain.agents import create_agent
from deepagents.backends import StateBackend
from deepagents.middleware import FilesystemMiddleware

agent = create_agent(
    model="fireworks:accounts/fireworks/models/glm-5p2",
    tools=[search],
    middleware=[FilesystemMiddleware(backend=StateBackend())],
)
```

**Baseten**

```python
from langchain.agents import create_agent
from deepagents.backends import StateBackend
from deepagents.middleware import FilesystemMiddleware

agent = create_agent(
    model="baseten:zai-org/GLM-5.2",
    tools=[search],
    middleware=[FilesystemMiddleware(backend=StateBackend())],
)
```

**Ollama**

```python
from langchain.agents import create_agent
from deepagents.backends import StateBackend
from deepagents.middleware import FilesystemMiddleware

agent = create_agent(
    model="ollama:north-mini-code-1.0",
    tools=[search],
    middleware=[FilesystemMiddleware(backend=StateBackend())],
)
```

See [`FilesystemMiddleware`](https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemMiddleware), [Sandboxes](../deepagents/sandboxes.md), [Interpreters](../deepagents/interpreters.md).

> [!NOTE]
> This example imports from the `deepagents` package. Install it with:
>
> **pip**
>
> ```bash
> pip install deepagents
> ```
>
> **uv**
>
> ```bash
> uv add deepagents
> ```

### Context management

Every model call has a fixed context window. As an agent runs, that window fills with accumulating history, tool results, and intermediate steps. Summarization compresses history before overflow hits; memory loads persistent instructions at startup so knowledge carries across sessions; skills surface domain knowledge on demand rather than loading everything upfront.

**Google**

```python
from deepagents.backends import StateBackend
from deepagents.middleware import FilesystemMiddleware, MemoryMiddleware, SkillsMiddleware, SummarizationMiddleware

backend = StateBackend()
model = "google_genai:gemini-3.6-flash"

agent = create_agent(
    model=model,
    tools=[search],
    middleware=[
        FilesystemMiddleware(backend=backend),
        SummarizationMiddleware(model=model, backend=backend),
        MemoryMiddleware(backend=backend, sources=["./AGENTS.md"]),
        SkillsMiddleware(backend=backend, sources=["./skills/"]),
    ],
)
```

**OpenAI**

```python
from deepagents.backends import StateBackend
from deepagents.middleware import FilesystemMiddleware, MemoryMiddleware, SkillsMiddleware, SummarizationMiddleware

backend = StateBackend()
model = "openai:gpt-5.5"

agent = create_agent(
    model=model,
    tools=[search],
    middleware=[
        FilesystemMiddleware(backend=backend),
        SummarizationMiddleware(model=model, backend=backend),
        MemoryMiddleware(backend=backend, sources=["./AGENTS.md"]),
        SkillsMiddleware(backend=backend, sources=["./skills/"]),
    ],
)
```

**Anthropic**

```python
from deepagents.backends import StateBackend
from deepagents.middleware import FilesystemMiddleware, MemoryMiddleware, SkillsMiddleware, SummarizationMiddleware

backend = StateBackend()
model = "anthropic:claude-sonnet-5"

agent = create_agent(
    model=model,
    tools=[search],
    middleware=[
        FilesystemMiddleware(backend=backend),
        SummarizationMiddleware(model=model, backend=backend),
        MemoryMiddleware(backend=backend, sources=["./AGENTS.md"]),
        SkillsMiddleware(backend=backend, sources=["./skills/"]),
    ],
)
```

**OpenRouter**

```python
from deepagents.backends import StateBackend
from deepagents.middleware import FilesystemMiddleware, MemoryMiddleware, SkillsMiddleware, SummarizationMiddleware

backend = StateBackend()
model = "openrouter:z-ai/glm-5.2"

agent = create_agent(
    model=model,
    tools=[search],
    middleware=[
        FilesystemMiddleware(backend=backend),
        SummarizationMiddleware(model=model, backend=backend),
        MemoryMiddleware(backend=backend, sources=["./AGENTS.md"]),
        SkillsMiddleware(backend=backend, sources=["./skills/"]),
    ],
)
```

**Fireworks**

```python
from deepagents.backends import StateBackend
from deepagents.middleware import FilesystemMiddleware, MemoryMiddleware, SkillsMiddleware, SummarizationMiddleware

backend = StateBackend()
model = "fireworks:accounts/fireworks/models/glm-5p2"

agent = create_agent(
    model=model,
    tools=[search],
    middleware=[
        FilesystemMiddleware(backend=backend),
        SummarizationMiddleware(model=model, backend=backend),
        MemoryMiddleware(backend=backend, sources=["./AGENTS.md"]),
        SkillsMiddleware(backend=backend, sources=["./skills/"]),
    ],
)
```

**Baseten**

```python
from deepagents.backends import StateBackend
from deepagents.middleware import FilesystemMiddleware, MemoryMiddleware, SkillsMiddleware, SummarizationMiddleware

backend = StateBackend()
model = "baseten:zai-org/GLM-5.2"

agent = create_agent(
    model=model,
    tools=[search],
    middleware=[
        FilesystemMiddleware(backend=backend),
        SummarizationMiddleware(model=model, backend=backend),
        MemoryMiddleware(backend=backend, sources=["./AGENTS.md"]),
        SkillsMiddleware(backend=backend, sources=["./skills/"]),
    ],
)
```

**Ollama**

```python
from deepagents.backends import StateBackend
from deepagents.middleware import FilesystemMiddleware, MemoryMiddleware, SkillsMiddleware, SummarizationMiddleware

backend = StateBackend()
model = "ollama:north-mini-code-1.0"

agent = create_agent(
    model=model,
    tools=[search],
    middleware=[
        FilesystemMiddleware(backend=backend),
        SummarizationMiddleware(model=model, backend=backend),
        MemoryMiddleware(backend=backend, sources=["./AGENTS.md"]),
        SkillsMiddleware(backend=backend, sources=["./skills/"]),
    ],
)
```

See [`SummarizationMiddleware`](https://reference.langchain.com/python/langchain/agents/middleware/summarization/SummarizationMiddleware), [`MemoryMiddleware`](https://reference.langchain.com/python/deepagents/middleware/memory/MemoryMiddleware), [Skills](multi-agent/skills.md), [Context engineering](../deepagents/context-engineering.md).

> [!NOTE]
> This example imports from the `deepagents` package. Install it with:
>
> **pip**
>
> ```bash
> pip install deepagents
> ```
>
> **uv**
>
> ```bash
> uv add deepagents
> ```

### Planning and delegation

Complex tasks often exceed what one context window can handle. Delegation lets the main agent break work into pieces, hand them to subagents that each run in their own isolated context, and stay focused on coordination rather than execution. Work can run in parallel; the main agent's context stays clean.

**Google**

```python
from deepagents.backends import StateBackend
from deepagents.middleware import FilesystemMiddleware
from deepagents.middleware.subagents import SubAgentMiddleware
from langchain.agents import create_agent
from langchain.agents.middleware import TodoListMiddleware
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for a query and return a short summary."""
    return f"Search results for: {query}"

backend = StateBackend()

agent = create_agent(
    model="google_genai:gemini-3.6-flash",
    tools=[search],
    middleware=[
        FilesystemMiddleware(backend=backend),
        TodoListMiddleware(),
        SubAgentMiddleware(
            backend=backend,
            subagents=[
                {
                    "name": "researcher",
                    "description": "Searches and returns a structured summary.",
                    "system_prompt": "Use the search tool to research the question and summarize key points.",
                    "tools": [search],
                    "model": "anthropic:claude-sonnet-4-6",
                    "middleware": [],
                }
            ],
        ),
    ],
)
```

**OpenAI**

```python
from deepagents.backends import StateBackend
from deepagents.middleware import FilesystemMiddleware
from deepagents.middleware.subagents import SubAgentMiddleware
from langchain.agents import create_agent
from langchain.agents.middleware import TodoListMiddleware
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for a query and return a short summary."""
    return f"Search results for: {query}"

backend = StateBackend()

agent = create_agent(
    model="openai:gpt-5.5",
    tools=[search],
    middleware=[
        FilesystemMiddleware(backend=backend),
        TodoListMiddleware(),
        SubAgentMiddleware(
            backend=backend,
            subagents=[
                {
                    "name": "researcher",
                    "description": "Searches and returns a structured summary.",
                    "system_prompt": "Use the search tool to research the question and summarize key points.",
                    "tools": [search],
                    "model": "anthropic:claude-sonnet-4-6",
                    "middleware": [],
                }
            ],
        ),
    ],
)
```

**Anthropic**

```python
from deepagents.backends import StateBackend
from deepagents.middleware import FilesystemMiddleware
from deepagents.middleware.subagents import SubAgentMiddleware
from langchain.agents import create_agent
from langchain.agents.middleware import TodoListMiddleware
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for a query and return a short summary."""
    return f"Search results for: {query}"

backend = StateBackend()

agent = create_agent(
    model="anthropic:claude-sonnet-5",
    tools=[search],
    middleware=[
        FilesystemMiddleware(backend=backend),
        TodoListMiddleware(),
        SubAgentMiddleware(
            backend=backend,
            subagents=[
                {
                    "name": "researcher",
                    "description": "Searches and returns a structured summary.",
                    "system_prompt": "Use the search tool to research the question and summarize key points.",
                    "tools": [search],
                    "model": "anthropic:claude-sonnet-4-6",
                    "middleware": [],
                }
            ],
        ),
    ],
)
```

**OpenRouter**

```python
from deepagents.backends import StateBackend
from deepagents.middleware import FilesystemMiddleware
from deepagents.middleware.subagents import SubAgentMiddleware
from langchain.agents import create_agent
from langchain.agents.middleware import TodoListMiddleware
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for a query and return a short summary."""
    return f"Search results for: {query}"

backend = StateBackend()

agent = create_agent(
    model="openrouter:z-ai/glm-5.2",
    tools=[search],
    middleware=[
        FilesystemMiddleware(backend=backend),
        TodoListMiddleware(),
        SubAgentMiddleware(
            backend=backend,
            subagents=[
                {
                    "name": "researcher",
                    "description": "Searches and returns a structured summary.",
                    "system_prompt": "Use the search tool to research the question and summarize key points.",
                    "tools": [search],
                    "model": "anthropic:claude-sonnet-4-6",
                    "middleware": [],
                }
            ],
        ),
    ],
)
```

**Fireworks**

```python
from deepagents.backends import StateBackend
from deepagents.middleware import FilesystemMiddleware
from deepagents.middleware.subagents import SubAgentMiddleware
from langchain.agents import create_agent
from langchain.agents.middleware import TodoListMiddleware
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for a query and return a short summary."""
    return f"Search results for: {query}"

backend = StateBackend()

agent = create_agent(
    model="fireworks:accounts/fireworks/models/glm-5p2",
    tools=[search],
    middleware=[
        FilesystemMiddleware(backend=backend),
        TodoListMiddleware(),
        SubAgentMiddleware(
            backend=backend,
            subagents=[
                {
                    "name": "researcher",
                    "description": "Searches and returns a structured summary.",
                    "system_prompt": "Use the search tool to research the question and summarize key points.",
                    "tools": [search],
                    "model": "anthropic:claude-sonnet-4-6",
                    "middleware": [],
                }
            ],
        ),
    ],
)
```

**Baseten**

```python
from deepagents.backends import StateBackend
from deepagents.middleware import FilesystemMiddleware
from deepagents.middleware.subagents import SubAgentMiddleware
from langchain.agents import create_agent
from langchain.agents.middleware import TodoListMiddleware
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for a query and return a short summary."""
    return f"Search results for: {query}"

backend = StateBackend()

agent = create_agent(
    model="baseten:zai-org/GLM-5.2",
    tools=[search],
    middleware=[
        FilesystemMiddleware(backend=backend),
        TodoListMiddleware(),
        SubAgentMiddleware(
            backend=backend,
            subagents=[
                {
                    "name": "researcher",
                    "description": "Searches and returns a structured summary.",
                    "system_prompt": "Use the search tool to research the question and summarize key points.",
                    "tools": [search],
                    "model": "anthropic:claude-sonnet-4-6",
                    "middleware": [],
                }
            ],
        ),
    ],
)
```

**Ollama**

```python
from deepagents.backends import StateBackend
from deepagents.middleware import FilesystemMiddleware
from deepagents.middleware.subagents import SubAgentMiddleware
from langchain.agents import create_agent
from langchain.agents.middleware import TodoListMiddleware
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for a query and return a short summary."""
    return f"Search results for: {query}"

backend = StateBackend()

agent = create_agent(
    model="ollama:north-mini-code-1.0",
    tools=[search],
    middleware=[
        FilesystemMiddleware(backend=backend),
        TodoListMiddleware(),
        SubAgentMiddleware(
            backend=backend,
            subagents=[
                {
                    "name": "researcher",
                    "description": "Searches and returns a structured summary.",
                    "system_prompt": "Use the search tool to research the question and summarize key points.",
                    "tools": [search],
                    "model": "anthropic:claude-sonnet-4-6",
                    "middleware": [],
                }
            ],
        ),
    ],
)
```

See [Subagents](multi-agent/subagents.md).

> [!NOTE]
> This example imports from the `deepagents` package. Install it with:
>
> **pip**
>
> ```bash
> pip install deepagents
> ```
>
> **uv**
>
> ```bash
> uv add deepagents
> ```

### Name your agent

Optionally use an identifier for the agent. This is especially useful when embedding the agent as a subgraph in [multi-agent](multi-agent.md) systems.

**Google**

```python
agent = create_agent(model="google_genai:gemini-3.6-flash", tools=tools, name="research_assistant")
```

**OpenAI**

```python
agent = create_agent(model="openai:gpt-5.5", tools=tools, name="research_assistant")
```

**Anthropic**

```python
agent = create_agent(model="anthropic:claude-sonnet-5", tools=tools, name="research_assistant")
```

**OpenRouter**

```python
agent = create_agent(model="openrouter:z-ai/glm-5.2", tools=tools, name="research_assistant")
```

**Fireworks**

```python
agent = create_agent(model="fireworks:accounts/fireworks/models/glm-5p2", tools=tools, name="research_assistant")
```

**Baseten**

```python
agent = create_agent(model="baseten:zai-org/GLM-5.2", tools=tools, name="research_assistant")
```

**Ollama**

```python
agent = create_agent(model="ollama:north-mini-code-1.0", tools=tools, name="research_assistant")
```

### Fault tolerance

Agents in production encounter failures that rarely appear in development: rate limits, model timeouts, transient API errors. Fault tolerance middleware handles these at the infrastructure level so your tools and business logic don't need try/catch around every call.

**Google**

```python
from langchain.agents import create_agent
from langchain.agents.middleware import ModelRetryMiddleware, ToolRetryMiddleware
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for a query and return a short summary."""
    return f"Search results for: {query}"

agent = create_agent(
    model="google_genai:gemini-3.6-flash",
    tools=[search],
    middleware=[
        ModelRetryMiddleware(max_retries=3),
        ToolRetryMiddleware(max_retries=2),
    ],
)
```

**OpenAI**

```python
from langchain.agents import create_agent
from langchain.agents.middleware import ModelRetryMiddleware, ToolRetryMiddleware
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for a query and return a short summary."""
    return f"Search results for: {query}"

agent = create_agent(
    model="openai:gpt-5.5",
    tools=[search],
    middleware=[
        ModelRetryMiddleware(max_retries=3),
        ToolRetryMiddleware(max_retries=2),
    ],
)
```

**Anthropic**

```python
from langchain.agents import create_agent
from langchain.agents.middleware import ModelRetryMiddleware, ToolRetryMiddleware
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for a query and return a short summary."""
    return f"Search results for: {query}"

agent = create_agent(
    model="anthropic:claude-sonnet-5",
    tools=[search],
    middleware=[
        ModelRetryMiddleware(max_retries=3),
        ToolRetryMiddleware(max_retries=2),
    ],
)
```

**OpenRouter**

```python
from langchain.agents import create_agent
from langchain.agents.middleware import ModelRetryMiddleware, ToolRetryMiddleware
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for a query and return a short summary."""
    return f"Search results for: {query}"

agent = create_agent(
    model="openrouter:z-ai/glm-5.2",
    tools=[search],
    middleware=[
        ModelRetryMiddleware(max_retries=3),
        ToolRetryMiddleware(max_retries=2),
    ],
)
```

**Fireworks**

```python
from langchain.agents import create_agent
from langchain.agents.middleware import ModelRetryMiddleware, ToolRetryMiddleware
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for a query and return a short summary."""
    return f"Search results for: {query}"

agent = create_agent(
    model="fireworks:accounts/fireworks/models/glm-5p2",
    tools=[search],
    middleware=[
        ModelRetryMiddleware(max_retries=3),
        ToolRetryMiddleware(max_retries=2),
    ],
)
```

**Baseten**

```python
from langchain.agents import create_agent
from langchain.agents.middleware import ModelRetryMiddleware, ToolRetryMiddleware
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for a query and return a short summary."""
    return f"Search results for: {query}"

agent = create_agent(
    model="baseten:zai-org/GLM-5.2",
    tools=[search],
    middleware=[
        ModelRetryMiddleware(max_retries=3),
        ToolRetryMiddleware(max_retries=2),
    ],
)
```

**Ollama**

```python
from langchain.agents import create_agent
from langchain.agents.middleware import ModelRetryMiddleware, ToolRetryMiddleware
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for a query and return a short summary."""
    return f"Search results for: {query}"

agent = create_agent(
    model="ollama:north-mini-code-1.0",
    tools=[search],
    middleware=[
        ModelRetryMiddleware(max_retries=3),
        ToolRetryMiddleware(max_retries=2),
    ],
)
```

See [`ModelRetryMiddleware`](https://reference.langchain.com/python/langchain/agents/middleware/model_retry/ModelRetryMiddleware), [`ToolRetryMiddleware`](https://reference.langchain.com/python/langchain/agents/middleware/tool_retry/ToolRetryMiddleware), [Prebuilt middleware](middleware/built-in.md).

### Guardrails

Some policies can't live in a prompt—they need to be enforced deterministically regardless of what the model does. Guardrails intercept data as it flows through the agent loop, applying compliance rules or content policies before tool results reach the model's context.

**Google**

```python
from langchain.agents import create_agent
from langchain.agents.middleware import PIIMiddleware
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for a query and return a short summary."""
    return f"Search results for: {query}"

agent = create_agent(
    model="google_genai:gemini-3.6-flash",
    tools=[search],
    middleware=[PIIMiddleware("email")],
)
```

**OpenAI**

```python
from langchain.agents import create_agent
from langchain.agents.middleware import PIIMiddleware
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for a query and return a short summary."""
    return f"Search results for: {query}"

agent = create_agent(
    model="openai:gpt-5.5",
    tools=[search],
    middleware=[PIIMiddleware("email")],
)
```

**Anthropic**

```python
from langchain.agents import create_agent
from langchain.agents.middleware import PIIMiddleware
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for a query and return a short summary."""
    return f"Search results for: {query}"

agent = create_agent(
    model="anthropic:claude-sonnet-5",
    tools=[search],
    middleware=[PIIMiddleware("email")],
)
```

**OpenRouter**

```python
from langchain.agents import create_agent
from langchain.agents.middleware import PIIMiddleware
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for a query and return a short summary."""
    return f"Search results for: {query}"

agent = create_agent(
    model="openrouter:z-ai/glm-5.2",
    tools=[search],
    middleware=[PIIMiddleware("email")],
)
```

**Fireworks**

```python
from langchain.agents import create_agent
from langchain.agents.middleware import PIIMiddleware
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for a query and return a short summary."""
    return f"Search results for: {query}"

agent = create_agent(
    model="fireworks:accounts/fireworks/models/glm-5p2",
    tools=[search],
    middleware=[PIIMiddleware("email")],
)
```

**Baseten**

```python
from langchain.agents import create_agent
from langchain.agents.middleware import PIIMiddleware
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for a query and return a short summary."""
    return f"Search results for: {query}"

agent = create_agent(
    model="baseten:zai-org/GLM-5.2",
    tools=[search],
    middleware=[PIIMiddleware("email")],
)
```

**Ollama**

```python
from langchain.agents import create_agent
from langchain.agents.middleware import PIIMiddleware
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for a query and return a short summary."""
    return f"Search results for: {query}"

agent = create_agent(
    model="ollama:north-mini-code-1.0",
    tools=[search],
    middleware=[PIIMiddleware("email")],
)
```

See [`PIIMiddleware`](https://reference.langchain.com/python/langchain/agents/middleware/pii/PIIMiddleware), [Prebuilt middleware](middleware/built-in.md).

### Steering

Full autonomy isn't always appropriate. Steering lets you place humans at specific decision points—before destructive writes, expensive API calls, or anything requiring judgment—without restructuring your agent. The agent pauses and waits; a human approves, edits, or rejects; execution continues.

**Google**

```python
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for a query and return a short summary."""
    return f"Search results for: {query}"

agent = create_agent(
    model="google_genai:gemini-3.6-flash",
    tools=[search],
    middleware=[HumanInTheLoopMiddleware(interrupt_on={"write_file": True})],
)
```

**OpenAI**

```python
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for a query and return a short summary."""
    return f"Search results for: {query}"

agent = create_agent(
    model="openai:gpt-5.5",
    tools=[search],
    middleware=[HumanInTheLoopMiddleware(interrupt_on={"write_file": True})],
)
```

**Anthropic**

```python
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for a query and return a short summary."""
    return f"Search results for: {query}"

agent = create_agent(
    model="anthropic:claude-sonnet-5",
    tools=[search],
    middleware=[HumanInTheLoopMiddleware(interrupt_on={"write_file": True})],
)
```

**OpenRouter**

```python
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for a query and return a short summary."""
    return f"Search results for: {query}"

agent = create_agent(
    model="openrouter:z-ai/glm-5.2",
    tools=[search],
    middleware=[HumanInTheLoopMiddleware(interrupt_on={"write_file": True})],
)
```

**Fireworks**

```python
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for a query and return a short summary."""
    return f"Search results for: {query}"

agent = create_agent(
    model="fireworks:accounts/fireworks/models/glm-5p2",
    tools=[search],
    middleware=[HumanInTheLoopMiddleware(interrupt_on={"write_file": True})],
)
```

**Baseten**

```python
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for a query and return a short summary."""
    return f"Search results for: {query}"

agent = create_agent(
    model="baseten:zai-org/GLM-5.2",
    tools=[search],
    middleware=[HumanInTheLoopMiddleware(interrupt_on={"write_file": True})],
)
```

**Ollama**

```python
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for a query and return a short summary."""
    return f"Search results for: {query}"

agent = create_agent(
    model="ollama:north-mini-code-1.0",
    tools=[search],
    middleware=[HumanInTheLoopMiddleware(interrupt_on={"write_file": True})],
)
```

See [`HumanInTheLoopMiddleware`](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/HumanInTheLoopMiddleware), [Human-in-the-loop](human-in-the-loop.md).

### Middleware resources

#### [Middleware overview](middleware/overview.md)
How the middleware stack works and when hooks fire

#### [Prebuilt middleware](middleware/built-in.md)
Full reference with configuration examples

#### [Custom middleware](middleware/custom.md)
Write your own hooks for business logic, PII scrubbing, and more

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/agents.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
