---
title: "filter_covers"
description: "Whether coverer is a superset of target."
source: "https://reference.langchain.com/python/langgraph-sdk/stream/subscription/filter_covers"
category: "reference"
tags: [reference, langgraph-sdk, stream, subscription, filter_covers]
---

# filter_covers

> **Function** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/stream/subscription/filter_covers)

Whether `coverer` is a superset of `target`.

Direct port of `client/stream/index.ts:filterCovers`. Depth coverage
accounts for namespace-prefix offset: a scoped coverer needs enough depth
to absorb the extra levels of any deeper target namespace prefix.

## Signature

```python
filter_covers(
    coverer: dict[str, Any],
    target: dict[str, Any],
) -> bool
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/stream/subscription.py#L161)
