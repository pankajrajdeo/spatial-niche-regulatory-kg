---
title: "branches"
description: "A list of (condition, Runnable) pairs."
source: "https://reference.langchain.com/python/langchain-core/runnables/branch/RunnableBranch/branches"
category: "reference"
tags: [reference, langchain-core, runnables, branch, runnablebranch, branches]
---

# branches

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/branch/RunnableBranch/branches)

A list of `(condition, Runnable)` pairs.

## Signature

```python
branches: Sequence[tuple[Runnable[Input, bool], Runnable[Input, Output]]]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/branch.py#L70)
