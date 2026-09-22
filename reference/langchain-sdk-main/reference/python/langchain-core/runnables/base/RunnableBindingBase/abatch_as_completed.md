---
title: "abatch_as_completed"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/abatch_as_completed"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnablebindingbase, abatch_as_completed]
---

# abatch_as_completed

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/abatch_as_completed)

## Signature

```python
abatch_as_completed(
    self,
    inputs: Sequence[Input],
    config: RunnableConfig | Sequence[RunnableConfig] | None = None,
    *,
    return_exceptions: bool = False,
    **kwargs: Any | None = {},
) -> AsyncIterator[tuple[int, Output | Exception]]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L6151)
