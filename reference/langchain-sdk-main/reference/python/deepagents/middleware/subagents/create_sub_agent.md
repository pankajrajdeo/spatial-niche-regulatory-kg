---
title: "create_sub_agent"
description: "Create a runnable agent from a raw SubAgent spec."
source: "https://reference.langchain.com/python/deepagents/middleware/subagents/create_sub_agent"
category: "reference"
tags: [reference, deepagents, middleware, subagents, create_sub_agent]
---

# create_sub_agent

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/subagents/create_sub_agent)

Create a runnable agent from a raw `SubAgent` spec.

This is the shared entrypoint for the `create_agent` path used by
raw subagent specs. Pre-compiled `CompiledSubAgent` runnables are already
created by the caller and are handled separately by `SubAgentMiddleware`.

## Signature

```python
create_sub_agent(
    spec: SubAgent,
    *,
    state_schema: type | None = None,
    response_format: ResponseFormat[Any] | type | dict[str, Any] | None = None,
) -> Runnable
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `spec` | `SubAgent` | Yes | Subagent spec to compile. Must specify `model` and `tools`. |
| `state_schema` | `type \| None` | No | Base graph state schema forwarded to `create_agent` for the subagent. (default: `None`) |
| `response_format` | `ResponseFormat[Any] \| type \| dict[str, Any] \| None` | No | Optional response format override for this compiled subagent instance. (default: `None`) |

## Returns

`Runnable`

Runnable agent ready for task-tool invocation.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/subagents.py#L508)
