---
title: "collect_runs"
description: "Collect all run traces in context."
source: "https://reference.langchain.com/python/langchain-core/tracers/context/collect_runs"
category: "reference"
tags: [reference, langchain-core, tracers, context, collect_runs]
---

# collect_runs

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/context/collect_runs)

Collect all run traces in context.

## Signature

```python
collect_runs() -> Generator[RunCollectorCallbackHandler, None, None]
```

## Description

**Example:**

>>> with collect_runs() as runs_cb:
chain.invoke("foo")
run_id = runs_cb.traced_runs[0].id

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tracers/context.py#L85)
