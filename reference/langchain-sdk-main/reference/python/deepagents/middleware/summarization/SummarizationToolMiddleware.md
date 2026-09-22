---
title: "SummarizationToolMiddleware"
description: "Middleware that provides a compact_conversation tool for manual compaction."
source: "https://reference.langchain.com/python/deepagents/middleware/summarization/SummarizationToolMiddleware"
category: "reference"
tags: [reference, deepagents, middleware, summarization, summarizationtoolmiddleware]
---

# SummarizationToolMiddleware

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/summarization/SummarizationToolMiddleware)

Middleware that provides a `compact_conversation` tool for manual compaction.

This middleware composes with a `SummarizationMiddleware` instance, reusing
its summarization engine (model, backend, trigger thresholds) to let the
agent compact its own context window.

This middleware never compacts automatically. Compaction only occurs when
`compact_conversation` is called as a normal tool call (by the model or by
an explicit user action, e.g. as implemented in the deepagents-code CLI).

To avoid compacting too early, compact tool execution is gated by
`_is_eligible_for_compaction`, which requires reported usage to reach about
50% of the configured auto-summarization trigger.

The tool and auto-summarization share the same `_summarization_event` state
key, so they interoperate correctly.

For a simpler setup, use `create_summarization_tool_middleware` which
handles both steps.

## Signature

```python
SummarizationToolMiddleware(
    self,
    summarization: _DeepAgentsSummarizationMiddleware,
    *,
    system_prompt: str | None = None,
)
```

## Description

**Example:**

```python
from deepagents.middleware.summarization import (
    SummarizationMiddleware,
    SummarizationToolMiddleware,
)

summ = SummarizationMiddleware(model="gpt-5.5", backend=backend)
tool_mw = SummarizationToolMiddleware(summ)

agent = create_deep_agent(middleware=[summ, tool_mw])
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `summarization` | `_DeepAgentsSummarizationMiddleware` | Yes | The `SummarizationMiddleware` instance whose summarization engine this tool will delegate to. |
| `system_prompt` | `str \| None` | No | System-prompt fragment nudging the model to call `compact_conversation`. Pass `None` to skip appending the nudge entirely (the tool remains registered and callable but the model is unlikely to discover it without an external mention). (default: `None`) |

## Extends

- `AgentMiddleware`

## Constructors

```python
__init__(
    self,
    summarization: _DeepAgentsSummarizationMiddleware,
    *,
    system_prompt: str | None = None,
) -> None
```

| Name | Type |
|------|------|
| `summarization` | `_DeepAgentsSummarizationMiddleware` |
| `system_prompt` | `str \| None` |

## Properties

- `trace_policy`
- `state_schema`
- `system_prompt`
- `tools`

## Methods

- [`wrap_model_call()`](https://reference.langchain.com/python/deepagents/middleware/summarization/SummarizationToolMiddleware/wrap_model_call)
- [`awrap_model_call()`](https://reference.langchain.com/python/deepagents/middleware/summarization/SummarizationToolMiddleware/awrap_model_call)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/summarization.py#L1924)
