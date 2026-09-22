---
title: "finalize"
description: "Called when the run ends normally (sync lane)."
source: "https://reference.langchain.com/python/langgraph/stream/_types/StreamTransformer/finalize"
category: "reference"
tags: [reference, langgraph, stream, types, streamtransformer, finalize]
---

# finalize

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/_types/StreamTransformer/finalize)

Called when the run ends normally (sync lane).

Override to close StreamChannels, resolve promises, or perform
other teardown. StreamChannel instances in the projection dict
are auto-closed by the mux.

## Signature

```python
finalize(
    self,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/stream/_types.py#L186)
