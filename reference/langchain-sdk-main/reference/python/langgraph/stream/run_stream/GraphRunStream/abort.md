---
title: "abort"
description: "Stop the run early."
source: "https://reference.langchain.com/python/langgraph/stream/run_stream/GraphRunStream/abort"
category: "reference"
tags: [reference, langgraph, stream, run_stream, graphrunstream, abort]
---

# abort

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/run_stream/GraphRunStream/abort)

Stop the run early.

Closes the underlying graph iterator (propagating `GeneratorExit`
so in-flight nodes and subgraphs are cancelled), closes the mux,
and marks the stream exhausted. Idempotent.

## Signature

```python
abort(
    self,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/stream/run_stream.py#L148)
