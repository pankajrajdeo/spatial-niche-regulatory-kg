---
title: "create_summarization_tool_middleware"
description: "Create a SummarizationToolMiddleware with model-aware defaults."
source: "https://reference.langchain.com/python/deepagents/middleware/summarization/create_summarization_tool_middleware"
category: "reference"
tags: [reference, deepagents, middleware, summarization, create_summarization_tool_middleware]
---

# create_summarization_tool_middleware

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/summarization/create_summarization_tool_middleware)

Create a `SummarizationToolMiddleware` with model-aware defaults.

Convenience factory: builds a `SummarizationMiddleware` via
[`create_summarization_middleware`][deepagents.middleware.summarization.create_summarization_middleware]
and wraps it in a `SummarizationToolMiddleware`. Saves a step and
accepts a model string.

## What you get

Only the tool layer is registered — the wrapped `SummarizationMiddleware`
is the engine the tool calls into, not a middleware that runs on its
own. The agent gains:

- A `compact_conversation` tool to compact its own context window
- An eligibility gate at ~50% of the auto-summarization trigger so
    the tool refuses to compact too early

## Pairing with auto-summarization

For *automatic* summarization at the trigger threshold, also register
a `SummarizationMiddleware`. `create_deep_agent` adds one by default,
so dropping `create_summarization_tool_middleware(...)` into its
`middleware=[...]` gives you both layers; they share state via the
`_summarization_event` key.

## Signature

```python
create_summarization_tool_middleware(
    model: str | BaseChatModel,
    backend: BackendProtocol,
    *,
    system_prompt: str | None = None,
) -> SummarizationToolMiddleware
```

## Description

**Example:**

Using the default `StateBackend`:

```python
from deepagents import create_deep_agent
from deepagents.backends import StateBackend
from deepagents.middleware.summarization import (
    create_summarization_tool_middleware,
)

model = "openai:gpt-5.5"
agent = create_deep_agent(
    model=model,
    middleware=[
        create_summarization_tool_middleware(model, StateBackend()),
    ],
)
```

Using a custom backend instance (e.g., Daytona Sandbox):

```python
from daytona import Daytona
from deepagents import create_deep_agent
from deepagents.middleware.summarization import (
    create_summarization_tool_middleware,
)
from langchain_daytona import DaytonaSandbox

sandbox = Daytona().create()
backend = DaytonaSandbox(sandbox=sandbox)
model = "openai:gpt-5.5"
agent = create_deep_agent(
    model=model,
    backend=backend,
    middleware=[
        create_summarization_tool_middleware(model, backend),
    ],
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `model` | `str \| BaseChatModel` | Yes | Chat model instance, or a model string (e.g. `"anthropic:claude-sonnet-4-6"`). |
| `backend` | `BackendProtocol` | Yes | Backend instance for persisting conversation history. |
| `system_prompt` | `str \| None` | No | System-prompt fragment nudging the model to call `compact_conversation`. Pass `None` to skip appending the nudge. (default: `None`) |

## Returns

`SummarizationToolMiddleware`

Configured `SummarizationToolMiddleware` instance.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/summarization.py#L1834)
