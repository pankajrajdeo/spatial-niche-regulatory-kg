---
title: "map_output_values"
description: "Map pending writes (a sequence of tuples (channel, value)) to output chunk."
source: "https://reference.langchain.com/python/langgraph/pregel/_io/map_output_values"
category: "reference"
tags: [reference, langgraph, pregel, io, map_output_values]
---

# map_output_values

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_io/map_output_values)

Map pending writes (a sequence of tuples (channel, value)) to output chunk.

## Signature

```python
map_output_values(
    output_channels: str | Sequence[str],
    pending_writes: Literal[True] | Sequence[tuple[str, Any]],
    channels: Mapping[str, BaseChannel],
) -> Iterator[dict[str, Any] | Any]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/_io.py#L100)
