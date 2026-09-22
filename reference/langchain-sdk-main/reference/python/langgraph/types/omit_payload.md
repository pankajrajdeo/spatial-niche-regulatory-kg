---
title: "omit_payload"
description: "TracePolicy helper that records an empty payload, dropping the value entirely."
source: "https://reference.langchain.com/python/langgraph/types/omit_payload"
category: "reference"
tags: [reference, langgraph, types, omit_payload]
---

# omit_payload

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/omit_payload)

`TracePolicy` helper that records an empty payload, dropping the value entirely.

Use as `process_inputs` and/or `process_outputs` on a `TracePolicy` to keep a node's
span and its timing while omitting its inputs/outputs from the trace.

## Signature

```python
omit_payload(
    _value: Any,
) -> dict[str, Any]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/types.py#L561)
