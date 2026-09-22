---
title: "AsyncSubAgent"
description: "Specification for an async subagent running on a remote Agent Protocol server."
source: "https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgent"
category: "reference"
tags: [reference, deepagents, middleware, async_subagents, asyncsubagent]
---

# AsyncSubAgent

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgent)

Specification for an async subagent running on a remote [Agent Protocol](https://github.com/langchain-ai/agent-protocol) server.

Async subagents connect to any Agent Protocol-compliant server via the
LangGraph SDK. They run as background tasks that the main agent can
monitor and update.

Compatible with LangGraph Platform / LangSmith Deployment (managed) and
self-hosted servers.

Authentication for LangGraph Platform / LangSmith Deployment is handled
automatically by the SDK via environment variables (`LANGGRAPH_API_KEY`,
`LANGSMITH_API_KEY`, or `LANGCHAIN_API_KEY`). For self-hosted servers,
pass custom auth via `headers`.

!!! note "Async invocation required for local ASGI transport"

    Omitting `url` uses in-process ASGI transport for a local server. This
    transport is available only through an async parent-agent entrypoint,
    such as `ainvoke`. The synchronous `invoke` path requires a URL for a
    reachable Agent Protocol server.

## Signature

```python
AsyncSubAgent()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    name: str,
    description: str,
    graph_id: str,
    url: NotRequired[str],
    headers: NotRequired[dict[str, str]],
)
```

| Name | Type |
|------|------|
| `name` | `str` |
| `description` | `str` |
| `graph_id` | `str` |
| `url` | `NotRequired[str]` |
| `headers` | `NotRequired[dict[str, str]]` |

## Properties

- `name`
- `description`
- `graph_id`
- `url`
- `headers`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/async_subagents.py#L34)
