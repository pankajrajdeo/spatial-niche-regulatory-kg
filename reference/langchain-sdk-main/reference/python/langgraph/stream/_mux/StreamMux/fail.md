---
title: "fail"
description: "Fail all transformers, projections, and the main log."
source: "https://reference.langchain.com/python/langgraph/stream/_mux/StreamMux/fail"
category: "reference"
tags: [reference, langgraph, stream, mux, streammux, fail]
---

# fail

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/_mux/StreamMux/fail)

Fail all transformers, projections, and the main log.

StreamChannels discovered in transformer projections are
auto-failed — transformers don't need to fail them manually.
If any transformer's `fail()` raises, the remaining
transformers, projections, and the main log are still failed.

## Signature

```python
fail(
    self,
    err: BaseException,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `err` | `BaseException` | Yes | The exception that ended the run. |

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/stream/_mux.py#L326)
