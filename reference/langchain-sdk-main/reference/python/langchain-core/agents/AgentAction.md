---
title: "AgentAction"
description: "Represents a request to execute an action by an agent."
source: "https://reference.langchain.com/python/langchain-core/agents/AgentAction"
category: "reference"
tags: [reference, langchain-core, agents, agentaction]
---

# AgentAction

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/agents/AgentAction)

Represents a request to execute an action by an agent.

The action consists of the name of the tool to execute and the input to pass
to the tool. The log is used to pass along extra information about the action.

## Signature

```python
AgentAction(
    self,
    tool: str,
    tool_input: str | dict[Any, Any],
    log: str,
    **kwargs: Any = {},
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `tool` | `str` | Yes | The name of the tool to execute. |
| `tool_input` | `str \| dict[Any, Any]` | Yes | The input to pass in to the `Tool`. |
| `log` | `str` | Yes | Additional information to log about the action. |

## Extends

- `Serializable`

## Constructors

```python
__init__(
    self,
    tool: str,
    tool_input: str | dict[Any, Any],
    log: str,
    **kwargs: Any = {},
)
```

| Name | Type |
|------|------|
| `tool` | `str` |
| `tool_input` | `str \| dict[Any, Any]` |
| `log` | `str` |

## Properties

- `tool`
- `tool_input`
- `log`
- `type`
- `messages`

## Methods

- [`is_lc_serializable()`](https://reference.langchain.com/python/langchain-core/agents/AgentAction/is_lc_serializable)
- [`get_lc_namespace()`](https://reference.langchain.com/python/langchain-core/agents/AgentAction/get_lc_namespace)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/agents.py#L44)
