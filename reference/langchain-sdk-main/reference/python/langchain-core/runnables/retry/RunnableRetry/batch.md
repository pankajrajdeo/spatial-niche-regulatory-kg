---
title: "batch"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/runnables/retry/RunnableRetry/batch"
category: "reference"
tags: [reference, langchain-core, runnables, retry, runnableretry, batch]
---

# batch

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/retry/RunnableRetry/batch)

## Signature

```python
batch(
    self,
    inputs: list[Input],
    config: RunnableConfig | list[RunnableConfig] | None = None,
    *,
    return_exceptions: bool = False,
    **kwargs: Any = {},
) -> list[Output]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/retry.py#L290)
