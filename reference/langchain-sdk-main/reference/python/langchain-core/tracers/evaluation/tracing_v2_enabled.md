---
title: "tracing_v2_enabled"
description: "Instruct LangChain to log all runs in context to LangSmith."
source: "https://reference.langchain.com/python/langchain-core/tracers/evaluation/tracing_v2_enabled"
category: "reference"
tags: [reference, langchain-core, tracers, evaluation, tracing_v2_enabled]
---

# tracing_v2_enabled

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/context/tracing_v2_enabled)

Instruct LangChain to log all runs in context to LangSmith.

## Signature

```python
tracing_v2_enabled(
    project_name: str | None = None,
    *,
    example_id: str | UUID | None = None,
    tags: list[str] | None = None,
    client: LangSmithClient | None = None,
) -> Generator[LangChainTracer, None, None]
```

## Description

**Example:**

>>> with tracing_v2_enabled():
...     # LangChain code will automatically be traced

You can use this to fetch the LangSmith run URL:

>>> with tracing_v2_enabled() as cb:
...     chain.invoke("foo")
...     run_url = cb.get_run_url()

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `project_name` | `str \| None` | No | The name of the project.  Defaults to `'default'`. (default: `None`) |
| `example_id` | `str \| UUID \| None` | No | The ID of the example. (default: `None`) |
| `tags` | `list[str] \| None` | No | The tags to add to the run. (default: `None`) |
| `client` | `LangSmithClient \| None` | No | The client of the langsmith. (default: `None`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tracers/context.py#L39)
