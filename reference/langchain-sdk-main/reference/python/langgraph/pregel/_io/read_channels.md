---
title: "read_channels"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langgraph/pregel/_io/read_channels"
category: "reference"
tags: [reference, langgraph, pregel, io, read_channels]
---

# read_channels

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_io/read_channels)

## Signature

```python
read_channels(
    channels: Mapping[str, BaseChannel],
    select: Sequence[str] | str,
    *,
    skip_empty: bool = True,
) -> dict[str, Any] | Any
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/_io.py#L38)
