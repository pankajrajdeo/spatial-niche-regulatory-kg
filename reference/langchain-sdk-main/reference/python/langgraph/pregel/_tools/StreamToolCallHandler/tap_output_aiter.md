---
title: "tap_output_aiter"
description: "Pass-through — required by the _StreamingCallbackHandler protocol."
source: "https://reference.langchain.com/python/langgraph/pregel/_tools/StreamToolCallHandler/tap_output_aiter"
category: "reference"
tags: [reference, langgraph, pregel, tools, streamtoolcallhandler, tap_output_aiter]
---

# tap_output_aiter

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_tools/StreamToolCallHandler/tap_output_aiter)

Pass-through — required by the `_StreamingCallbackHandler` protocol.

## Signature

```python
tap_output_aiter(
    self,
    run_id: UUID,
    output: AsyncIterator[T],
) -> AsyncIterator[T]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/_tools.py#L203)
