---
title: "NemotronProgressBudgetMiddleware"
description: "Stop Ultra3-specific tool loops before they consume runaway context."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/NemotronProgressBudgetMiddleware"
category: "reference"
tags: [reference, deepagents, profiles, harness, nvidia_nemotron_3_ultra, nemotronprogressbudgetmiddleware]
---

# NemotronProgressBudgetMiddleware

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/NemotronProgressBudgetMiddleware)

Stop Ultra3-specific tool loops before they consume runaway context.

## Signature

```python
NemotronProgressBudgetMiddleware(
    self,
    *,
    max_model_calls: int = _MAX_MODEL_CALLS,
    max_tool_results: int = _MAX_TOOL_RESULTS,
    max_repeated_tool_calls: int = _MAX_REPEATED_TOOL_CALLS,
)
```

## Extends

- `AgentMiddleware`

## Constructors

```python
__init__(
    self,
    *,
    max_model_calls: int = _MAX_MODEL_CALLS,
    max_tool_results: int = _MAX_TOOL_RESULTS,
    max_repeated_tool_calls: int = _MAX_REPEATED_TOOL_CALLS,
) -> None
```

| Name | Type |
|------|------|
| `max_model_calls` | `int` |
| `max_tool_results` | `int` |
| `max_repeated_tool_calls` | `int` |

## Properties

- `name`
- `max_model_calls`
- `max_tool_results`
- `max_repeated_tool_calls`

## Methods

- [`wrap_model_call()`](https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/NemotronProgressBudgetMiddleware/wrap_model_call)
- [`awrap_model_call()`](https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/NemotronProgressBudgetMiddleware/awrap_model_call)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/harness/_nvidia_nemotron_3_ultra.py#L1021)
