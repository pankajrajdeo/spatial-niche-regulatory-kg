---
title: "astream"
description: "Default implementation of astream, which calls ainvoke."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/astream"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnable, astream]
---

# astream

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/astream)

Default implementation of `astream`, which calls `ainvoke`.

Subclasses must override this method if they support streaming output.

## Signature

```python
astream(
    self,
    input: Input,
    config: RunnableConfig | None = None,
    **kwargs: Any | None = {},
) -> AsyncIterator[Output]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input` | `Input` | Yes | The input to the `Runnable`. |
| `config` | `RunnableConfig \| None` | No | The config to use for the `Runnable`. (default: `None`) |
| `**kwargs` | `Any \| None` | No | Additional keyword arguments to pass to the `Runnable`. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L1215)
