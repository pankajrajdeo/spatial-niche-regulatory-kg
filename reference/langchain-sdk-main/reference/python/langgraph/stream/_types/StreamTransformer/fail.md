---
title: "fail"
description: "Called when the run ends with an error (sync lane)."
source: "https://reference.langchain.com/python/langgraph/stream/_types/StreamTransformer/fail"
category: "reference"
tags: [reference, langgraph, stream, types, streamtransformer, fail]
---

# fail

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/_types/StreamTransformer/fail)

Called when the run ends with an error (sync lane).

Override to fail StreamChannels, reject promises, or perform
other teardown. StreamChannel instances in the projection dict
are auto-failed by the mux.

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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/stream/_types.py#L205)
